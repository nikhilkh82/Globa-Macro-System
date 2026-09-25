"""Macro Pulse — cross-asset vol-adjusted z-score monitor.

Spec: `brain/09 - Synthesis/Macro Pulse — Cross-Asset Z-Score Monitor (June 2026).md`.

z_t = r_t / std(r_{t-window .. t-1}) — trailing realised vol, no look-ahead. The dominant
variable is the instrument with the largest |z| today. The study asks the question the
monitor alone can't: does a |z| >= 2 shock predict the next `horizon` days?
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

INSTRUMENTS = {  # name: (yahoo symbol, macro driver)
    "US10Y": ("^TNX", "Growth / Rates"),
    "US3M": ("^IRX", "Fed expectations"),
    "DXY": ("DX-Y.NYB", "Global liquidity"),
    "Oil": ("CL=F", "Fear / real yields"),
    "SPY": ("SPY", "Risk appetite"),
    "QQQ": ("QQQ", "Growth / liquidity"),
    "VIX": ("^VIX", "Fear"),
}

# (label, source, direction, target): direction +1 means z >= +thresh, -1 means z <= -thresh, 0 means |z|.
SIGNALS = [
    ("SPY abnormal down", "SPY", -1, "SPY"),
    ("SPY abnormal up", "SPY", +1, "SPY"),
    ("QQQ abnormal down", "QQQ", -1, "QQQ"),
    ("VIX fear spike", "VIX", +1, "SPY"),
    ("DXY surge", "DXY", +1, "SPY"),
    ("US10Y rate shock", "US10Y", +1, "SPY"),
    ("Oil abnormal move", "Oil", 0, "Oil"),
]

REGIME_READ = {
    ("US10Y", 1): "Rates up / growth-or-inflation", ("US10Y", -1): "Rates down / growth scare",
    ("US3M", 1): "Hawkish repricing", ("US3M", -1): "Dovish repricing",
    ("DXY", 1): "USD strength / tightening liquidity", ("DXY", -1): "USD weakness / easing liquidity",
    ("Oil", 1): "Energy shock / inflation risk", ("Oil", -1): "Energy unwind / demand scare",
    ("SPY", 1): "Risk-on", ("SPY", -1): "Risk-off",
    ("QQQ", 1): "Growth / liquidity bid", ("QQQ", -1): "Growth de-rating",
    ("VIX", 1): "Fear spike", ("VIX", -1): "Vol crush / complacency",
}


@dataclass
class Config:
    window: int = 60
    z_thresh: float = 2.0
    horizon: int = 10


def zscores(closes: pd.DataFrame, cfg: Config = Config()) -> pd.DataFrame:
    r = closes.pct_change(fill_method=None)
    sd = r.rolling(cfg.window, min_periods=cfg.window).std(ddof=1).shift(1)
    return r / sd


def board(closes: pd.DataFrame, cfg: Config = Config()) -> tuple[list[dict], dict]:
    z = zscores(closes, cfg)
    last = z.dropna(how="all").index[-1]
    rows = []
    for name in closes.columns:
        s = closes[name].dropna()
        rows.append({
            "instrument": name,
            "driver": INSTRUMENTS.get(name, ("", ""))[1],
            "z": round(float(z.at[last, name]), 2) if pd.notna(z.at[last, name]) else None,
            "chg_1d": round(float(s.iloc[-1] / s.iloc[-2] - 1), 4) if len(s) > 1 else None,
            "chg_1w": round(float(s.iloc[-1] / s.iloc[-6] - 1), 4) if len(s) > 5 else None,
            "close": round(float(s.iloc[-1]), 2),
        })
    rows.sort(key=lambda r: -abs(r["z"] or 0))
    top = rows[0]
    sign = 1 if (top["z"] or 0) >= 0 else -1
    dominant = {"date": last.strftime("%Y-%m-%d"), "instrument": top["instrument"], "z": top["z"],
                "regime": REGIME_READ.get((top["instrument"], sign), "—")}
    return rows, dominant


def study(closes: pd.DataFrame, cfg: Config = Config()) -> list[dict]:
    z = zscores(closes, cfg)
    fwd = closes.shift(-cfg.horizon) / closes - 1
    out = []
    for label, src, direction, tgt in SIGNALS:
        if src not in z or tgt not in fwd:
            continue
        zs = z[src]
        hit = (zs >= cfg.z_thresh) if direction > 0 else (zs <= -cfg.z_thresh) if direction < 0 else (zs.abs() >= cfg.z_thresh)
        f = fwd[tgt].dropna()
        cond = f[hit.reindex(f.index).fillna(False)]
        n = int(len(cond))
        if n < 2:
            out.append({"signal": label, "target": tgt, "n": n})
            continue
        base = float(f.mean())
        mean = float(cond.mean())
        t = float((mean - base) / (cond.std(ddof=1) / np.sqrt(n))) if cond.std(ddof=1) > 0 else float("nan")
        out.append({"signal": label, "target": tgt, "n": n, "fwd": round(mean, 5),
                    "edge_pp": round((mean - base) * 100, 2), "t": round(t, 2),
                    "hit": round(float((cond > 0).mean()), 3)})
    return out


def dominant_frequency(closes: pd.DataFrame, cfg: Config = Config()) -> dict[str, int]:
    z = zscores(closes, cfg).abs().dropna(how="all")
    return z.idxmax(axis=1).value_counts().astype(int).to_dict()
