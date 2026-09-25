# -*- coding: utf-8 -*-
"""
refresh_sector_data.py
======================
Refresh the stale fundamentals in ``US_Sector_Data.xlsm`` (3,195 large-cap US
stocks; snapshot ~mid-2021) to CURRENT values from Yahoo Finance via yfinance.

Design goals (this is a multi-hour run for ~3,195 tickers):
  * Resume cache (JSON checkpoint) — survives interruptions / rate-limiting.
  * Per-ticker retries with backoff; rate-limit detection pauses all workers.
  * Small thread pool to cut wall-time while staying under Yahoo's limits.
  * Errors logged to refresh_errors.csv; original rows left intact on failure.
  * Writes back in-place to a NEW dated .xlsm (VBA preserved via keep_vba).

Usage:
    py refresh_sector_data.py            # full run (resumes from cache)
    py refresh_sector_data.py --test 12  # quick smoke test on first 12 tickers
"""
from __future__ import annotations

import os
import sys
import json
import time
import csv
import threading
import argparse
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

import openpyxl
import yfinance as yf

# Silence yfinance's chatty per-request error logging (404s for delisted tickers
# etc.) — we capture errors ourselves in fetch_one and log them to CSV.
import logging
logging.getLogger("yfinance").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
try:
    yf_logging = yf.logging if hasattr(yf, "logging") else None
    if yf_logging:
        yf_logging.getLogger().setLevel(logging.CRITICAL)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
# 2026-08-12: the original template moved to "18. Portfolio Management\"; the freshest ticker
# panel is the last refreshed output itself, so refresh FROM it (output is a NEW dated file,
# the source is never modified)
SRC = os.path.join(HERE, "38. US_Sector_Data_Updated_2026-07-03.xlsm")
if not os.path.exists(SRC):
    SRC = os.path.join(HERE, "18. Portfolio Management", "US_Sector_Data.xlsm")
TODAY = datetime.now().strftime("%Y-%m-%d")
DST = os.path.join(HERE, f"US_Sector_Data_Updated_{TODAY}.xlsm")
CACHE = os.path.join(HERE, "sector_refresh_cache.json")
ERRORS = os.path.join(HERE, "refresh_errors.csv")

# Concurrency / resilience knobs
WORKERS = 6
RETRIES = 3
BACKOFF = 2.0          # seconds, doubled each retry
CACHE_EVERY = 50       # persist cache every N completed tickers
RATE_PAUSE = 60        # seconds to sleep when a 429/999 storm is detected

# Column index map (1-based) — verified against the screener header row.
COL = {
    "ticker": 1, "mcap": 7, "rev_fy1": 9, "rev_g1": 11,
    "eps_fy1": 14, "eps_fy2": 15, "eg1": 17,
    "pe_fy1": 20, "pe_fy2": 21, "peg_fy1": 23,
    "de": 26, "margin": 27, "divy": 28,
    "surp_fqm3": 29, "surp_fqm2": 30, "surp_fqm1": 31, "surp_fq0": 32,
    "next_eps": 35,
}
ASOF_COL = 36  # first empty column (AJ area) for the As-Of date stamp

# ----------------------------------------------------------------------------
# Cache helpers
# ----------------------------------------------------------------------------
_cache_lock = threading.Lock()


def load_cache():
    if os.path.exists(CACHE):
        try:
            with open(CACHE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    tmp = CACHE + ".tmp"
    with _cache_lock:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(cache, f)
        os.replace(tmp, CACHE)


# ----------------------------------------------------------------------------
# Per-ticker fetch
# ----------------------------------------------------------------------------
def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fetch_one(ticker):
    """Return a dict of refreshed fields for ticker, or {'__error__': reason}."""
    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            t = yf.Ticker(ticker)
            info = t.info or {}
            # A ticker is effectively dead if no price AND no market cap
            if not info and not t.history(period="5d").empty is False:
                if not info:
                    return {"__error__": "no info returned (delisted/invalid)"}
            out = {
                "mcap": _num(info.get("marketCap")),
                "rev_fy1": _num(info.get("totalRevenue")),
                "rev_g1": _num(info.get("revenueGrowth")),
                "eps_fy1": _num(info.get("trailingEps")),
                "eps_fy2": _num(info.get("forwardEps")),
                "eg1": _num(info.get("earningsGrowth")),
                "pe_fy1": _num(info.get("trailingPE")),
                "pe_fy2": _num(info.get("forwardPE")),
                "peg_fy1": _num(info.get("pegRatio")),
                "de": _num(info.get("debtToEquity")),
                "margin": _num(info.get("profitMargins")),
                "divy": _num(info.get("dividendYield")),
            }
            # Next EPS report date (epoch → ISO date)
            ets = info.get("earningsTimestampStart") or info.get("earningsTimestamp")
            if ets:
                try:
                    out["next_eps"] = datetime.fromtimestamp(int(ets), tz=timezone.utc).date().isoformat()
                except Exception:
                    out["next_eps"] = None
            else:
                out["next_eps"] = None

            # Earnings surprises (4 most recent quarters → FQ0, FQ-1, FQ-2, FQ-3)
            try:
                eh = t.earnings_history
                if eh is not None and "surprisePercent" in eh.columns and len(eh):
                    sp = list(eh["surprisePercent"].iloc[:4][::-1])  # oldest→newest
                    # align to FQ-3,FQ-2,FQ-1,FQ0
                    for i, key in enumerate(["surp_fqm3", "surp_fqm2", "surp_fqm1", "surp_fq0"]):
                        out[key] = _num(sp[i]) if i < len(sp) else None
                else:
                    for key in ("surp_fqm3", "surp_fqm2", "surp_fqm1", "surp_fq0"):
                        out[key] = None
            except Exception:
                for key in ("surp_fqm3", "surp_fqm2", "surp_fqm1", "surp_fq0"):
                    out[key] = None

            # If absolutely nothing useful came back, treat as failure
            if all(v is None for k, v in out.items() if not k.startswith("surp")):
                return {"__error__": "all key fields null"}
            return out

        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            # crude rate-limit detection
            msg = str(e).lower()
            if "429" in msg or "999" in msg or "too many" in msg:
                time.sleep(RATE_PAUSE)
            else:
                time.sleep(BACKOFF * attempt)
    return {"__error__": last_err or "unknown"}


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def read_tickers(limit=None):
    wb = openpyxl.load_workbook(SRC, data_only=False, keep_vba=True)
    ws = wb.active
    tickers = []
    r = 2
    while True:
        v = ws.cell(row=r, column=1).value
        if v is None:
            break
        tickers.append((r, str(v).strip()))
        r += 1
        if limit and len(tickers) >= limit:
            break
    wb.close()
    return tickers


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", type=int, default=0, metavar="N",
                    help="smoke-test on the first N tickers only")
    ap.add_argument("--workers", type=int, default=WORKERS)
    args = ap.parse_args()

    print("Reading tickers from", os.path.basename(SRC))
    tickers = read_tickers(limit=args.test or None)
    total = len(tickers)
    print(f"  {total} tickers to refresh  |  workers={args.workers}")

    cache = load_cache()
    print(f"  resume cache: {len(cache)} tickers already done")

    # Phase 1: fetch (with resume)
    todo = [(row, tk) for row, tk in tickers if tk not in cache or "__error__" in cache[tk]]
    print(f"  to fetch now: {len(todo)}")
    done = len(cache)
    errors = []
    completed_since_save = 0
    start = time.time()

    def task(tk):
        return tk, fetch_one(tk)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(task, tk): tk for _, tk in todo}
        for fut in as_completed(futures):
            tk, res = fut.result()
            cache[tk] = res
            done += 1
            completed_since_save += 1
            if "__error__" in res:
                errors.append((tk, res["__error__"]))
            if completed_since_save >= CACHE_EVERY:
                save_cache(cache)
                completed_since_save = 0
                el = time.time() - start
                rate = (done - len(cache) + len(cache)) / max(el, 1)
                pct = done / total * 100
                print(f"  {done}/{total} ({pct:.1f}%)  errors={len(errors)}  "
                      f"elapsed={el/60:.1f}m  ({tk})", flush=True)

    save_cache(cache)
    print(f"\nFetch complete: {done}/{total} done, {len(errors)} errors, "
          f"{(time.time()-start)/60:.1f}m")

    # write error log
    if errors:
        with open(ERRORS, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ticker", "reason"])
            w.writerows(errors)
        print(f"  errors logged → {os.path.basename(ERRORS)}")

    # Phase 2: write back to a new dated .xlsm
    print("\nWriting refreshed workbook ...")
    write_back(cache, tickers)
    print("✓ Done →", os.path.basename(DST))

    # Coverage stats
    coverage(cache)


def write_back(cache, tickers):
    wb = openpyxl.load_workbook(SRC, data_only=False, keep_vba=True)
    ws = wb.active
    # As-Of header
    ws.cell(row=1, column=ASOF_COL, value="As-Of (Yahoo Finance)")
    note_col = ASOF_COL + 1
    ws.cell(row=1, column=note_col, value="Source: Yahoo Finance via yfinance")

    fields = ["mcap", "rev_fy1", "rev_g1", "eps_fy1", "eps_fy2", "eg1",
              "pe_fy1", "pe_fy2", "peg_fy1", "de", "margin", "divy",
              "surp_fqm3", "surp_fqm2", "surp_fqm1", "surp_fq0", "next_eps"]
    written = 0
    for row, tk in tickers:
        rec = cache.get(tk)
        if not rec or "__error__" in rec:
            continue
        for fld in fields:
            if fld in rec and rec[fld] is not None:
                ws.cell(row=row, column=COL[fld], value=rec[fld])
        # next_eps as a real date
        if rec.get("next_eps"):
            try:
                d = datetime.fromisoformat(rec["next_eps"]).date()
                ws.cell(row=row, column=COL["next_eps"], value=d)
            except Exception:
                pass
        ws.cell(row=row, column=ASOF_COL, value=TODAY)
        written += 1
    print(f"  {written} rows updated")
    wb.save(DST)


def coverage(cache):
    fields = ["mcap", "rev_fy1", "rev_g1", "eps_fy1", "eps_fy2", "eg1",
              "pe_fy1", "pe_fy2", "peg_fy1", "de", "margin", "divy",
              "surp_fq0", "next_eps"]
    good = {f: 0 for f in fields}
    err = 0
    for rec in cache.values():
        if "__error__" in rec:
            err += 1
            continue
        for f in fields:
            if rec.get(f) is not None:
                good[f] += 1
    n = len(cache)
    print(f"\n=== Coverage (of {n} fetched) ===")
    for f in fields:
        print(f"  {f:10s} {good[f]:5d}  ({good[f]/max(n,1)*100:.0f}%)")
    print(f"  errors:     {err}")


if __name__ == "__main__":
    main()
