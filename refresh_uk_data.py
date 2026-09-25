# -*- coding: utf-8 -*-
"""
refresh_uk_data.py
==================
Fetch current UK macro series for the UK Endogenous Driver Analysis workbook.

Sources (all free, no API key):
  * ONS  timeseries JSON  -> CPI, Core CPI, PPI, unemployment, debt/GDP, deficit, earnings
  * FRED fredgraph.csv    -> 10Y gilt, Bank Rate, consumer confidence, M4, unemployment (xcheck)

Writes a clean JSON cache (uk_data_cache.json) of monthly time-series that the
workbook builder consumes.  Re-run any time to refresh; idempotent.

Usage:  py refresh_uk_data.py
"""
from __future__ import annotations

import os
import ssl
import json
import time
import urllib.request
import csv
import io
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "uk_data_cache.json")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

MONTHS = {"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,
          "SEP":9,"OCT":10,"NOV":11,"DEC":12,"Q1":3,"Q2":6,"Q3":9,"Q4":12}


def _get(url, retries=2, timeout=45):
    """HTTP GET. Tries urllib, then falls back to curl (FRED resets Python
    urllib from some networks but works fine over curl)."""
    # try urllib first (quick)
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
                return r.read().decode("utf-8")
        except Exception as e:
            last = e
            print(f"    (urllib fail {i+1}/{retries}: {type(e).__name__}) -> curl", flush=True)
            time.sleep(1)
    # fallback: curl
    import subprocess
    for i in range(3):
        try:
            out = subprocess.run(
                ["curl", "-sL", "--max-time", "40", "-A", UA, url],
                capture_output=True, text=True, timeout=50)
            if out.returncode == 0 and out.stdout and not out.stdout.lstrip().startswith("<"):
                return out.stdout
            print(f"    (curl fail {i+1}/3: rc={out.returncode})", flush=True)
        except Exception as e:
            print(f"    (curl fail {i+1}/3: {type(e).__name__})", flush=True)
        time.sleep(2)
    raise last


def parse_ons_date(s):
    """'2026 MAY' -> '2026-05-01' ; '2025' -> '2025-01-01' (annual)."""
    s = s.strip().upper()
    parts = s.split()
    if len(parts) == 2 and parts[1] in MONTHS:
        y, m = int(parts[0]), MONTHS[parts[1]]
        return f"{y}-{m:02d}-01"
    if len(parts) == 1 and parts[0].isdigit():
        return f"{parts[0]}-01-01"
    return None


def fetch_ons(cdid, dataset, taxonomy, label):
    url = f"https://www.ons.gov.uk/{taxonomy}/timeseries/{cdid.lower()}/{dataset}/data"
    d = json.loads(_get(url))
    pts = []
    for bucket in ("months", "quarters"):
        for e in d.get(bucket, []):
            iso = parse_ons_date(e["date"])
            try:
                v = float(e["value"])
            except (TypeError, ValueError):
                continue
            if iso:
                pts.append((iso, v))
    # de-dup + sort ascending by date
    seen = {}
    for iso, v in pts:
        seen[iso] = v
    pts = sorted(seen.items())
    print(f"  ONS {cdid:5s} {label:28s} {len(pts):4d} pts  latest={pts[-1] if pts else None}")
    return pts


def fetch_fred(sid, label):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
    txt = _get(url)
    rows = list(csv.reader(io.StringIO(txt)))
    pts = []
    for r in rows[1:]:
        if len(r) >= 2 and r[1] != ".":
            try:
                pts.append((r[0], float(r[1])))
            except ValueError:
                pass
    print(f"  FRED {sid:14s} {label:24s} {len(pts):4d} pts  latest={pts[-1] if pts else None}")
    return pts


# ---------------------------------------------------------------------------
# Series definitions
# ---------------------------------------------------------------------------
def fetch_all():
    # start from existing cache so re-runs only fill gaps
    if os.path.exists(CACHE):
        try:
            with open(CACHE, encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:
            cache = {}
    else:
        cache = {}
    cache["_meta"] = {"fetched": datetime.now().isoformat(timespec="seconds")}

    def _persist():
        with open(CACHE, "w", encoding="utf-8") as f:
            json.dump(cache, f)

    def safe(key, fn, *args):
        if cache.get(key):  # already have it — skip
            print(f"  (cached) {key}", flush=True)
            return
        try:
            cache[key] = fn(*args)
            _persist()     # durable progress after every successful fetch
        except Exception as e:
            print(f"  !! FAILED {key}: {type(e).__name__}: {e}", flush=True)
            cache[key] = cache.get(key, [])
            _persist()

    # --- ONS ---
    print("ONS series:", flush=True)
    safe("cpi_rate",      fetch_ons, "D7G7", "mm23", "economy/inflationandpriceindices", "CPI rate %")
    safe("cpi_index",     fetch_ons, "D7BT", "mm23", "economy/inflationandpriceindices", "CPI index")
    safe("corecpi_rate",  fetch_ons, "DKO8", "mm23", "economy/inflationandpriceindices", "Core CPI rate %")
    safe("ppi_output",    fetch_ons, "GB7S", "ppi",  "economy/inflationandpriceindices", "PPI output idx")
    safe("ppi_input",     fetch_ons, "GHIK", "ppi",  "economy/inflationandpriceindices", "PPI input idx")
    safe("unemp",         fetch_ons, "MGSX", "lms",  "employmentandlabourmarket/peoplenotinwork/unemployment", "Unemployment %")
    safe("earnings",      fetch_ons, "KAC2", "emp",  "employmentandlabourmarket/peopleinwork/earningsandworkinghours", "AWE earnings %")
    safe("debt_gdp",      fetch_ons, "A3PW", "pusf", "economy/governmentpublicsectorandtaxes/publicsectorfinance", "Debt/GDP % (Maastricht)")
    safe("debt_gdp_psnd", fetch_ons, "HF6X", "pusf", "economy/governmentpublicsectorandtaxes/publicsectorfinance", "PSND % GDP")
    safe("deficit",       fetch_ons, "J5II", "pusf", "economy/governmentpublicsectorandtaxes/publicsectorfinance", "PS borrowing £m")

    # --- FRED ---
    print("\nFRED series:", flush=True)
    safe("gilt10y",       fetch_fred, "IRLTLT01GBM156N", "10Y gilt yield %")
    safe("bank_rate",     fetch_fred, "IRSTCI01GBM156N", "Bank Rate %")
    safe("consumer_conf", fetch_fred, "CSCICP02GBM460S", "Consumer confidence")
    safe("m4",            fetch_fred, "MANMM101GBM189S", "Broad money £")

    ok = sum(1 for k, v in cache.items() if k != "_meta" and v)
    print(f"\n✓ Cached {ok}/{len(cache)-1} series → {os.path.basename(CACHE)}", flush=True)
    return cache


if __name__ == "__main__":
    print("Fetching UK macro series ...\n")
    fetch_all()
