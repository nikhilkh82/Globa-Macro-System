"""Macro Regime Allocation Engine.

Spec: `brain/15 - Strategy Systems/Macro Regime Allocation Engine.md`.

- Regime from FRED, point-in-time with a 2-month publication lag:
  growth  = INDPRO YoY + PAYEMS YoY  (> 0 -> up)
  inflation = CPIAUCSL YoY           (> 3% -> high)
  -> Goldilocks (up, low) / Reflation (up, high) / Stagflation (down, high) / Deflation (down, low)
- Predefined playbook (macro theory, not fitted), with a VIX > 20 overlay that moves
  half the risk-asset (SPY/HYG/DBC) weight to cash.
- Walk-forward monthly: regime from macro <= t-lag, portfolio earns month t.
- Every leg (regime, static blend, 60/40, equal-weight) gets the same causal vol target
  and the same VIX overlay, so the switching effect is isolated.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from gms.engine.metrics import summarize

MACRO_IDS = ["INDPRO", "PAYEMS", "CPIAUCSL"]
CASH_ID = "TB3MS"  # 3-month T-bill, % annualised, monthly
ASSETS = ["SPY", "TLT", "IEF", "DBC", "GLD", "HYG"]
RISK_ASSETS = {"SPY", "HYG", "DBC"}
REGIMES = ["Goldilocks", "Reflation", "Stagflation", "Deflation"]

# Reflation weights are the vault's recorded live allocation. The other three follow the
# vault's playbook text (Goldilocks: equities+credit+bonds; Stagflation: gold+commodities+cash;
# Deflation: long bonds+gold) with round, unfitted weights.
PLAYBOOK: dict[str, dict[str, float]] = {
    "Goldilocks": {"SPY": 0.40, "HYG": 0.30, "IEF": 0.30},
    "Reflation": {"SPY": 0.30, "DBC": 0.30, "GLD": 0.20, "HYG": 0.20},
    "Stagflation": {"GLD": 0.40, "DBC": 0.30, "CASH": 0.30},
    "Deflation": {"TLT": 0.60, "GLD": 0.40},
}


@dataclass
class Config:
    inflation_high: float = 3.0
    lag_months: int = 2
    vix_trigger: float = 20.0
    vol_target: float = 0.10
    vol_window: int = 12
    max_leverage: float = 2.0


@dataclass
class Result:
    regimes: pd.Series
    growth: pd.Series
    inflation: pd.Series
    legs: pd.DataFrame
    table: dict[str, dict]
    current: dict = field(default_factory=dict)


def yoy(s: pd.Series) -> pd.Series:
    return (s / s.shift(12) - 1) * 100


def classify(macro: pd.DataFrame, cfg: Config = Config()) -> pd.DataFrame:
    """Monthly macro (INDPRO, PAYEMS, CPIAUCSL levels) -> growth, inflation, regime by macro month."""
    m = macro.resample("MS").last()
    growth = yoy(m["INDPRO"]) + yoy(m["PAYEMS"])
    infl = yoy(m["CPIAUCSL"])
    ok = growth.notna() & infl.notna()
    up = growth > 0
    high = infl > cfg.inflation_high
    regime = pd.Series(np.select([up & ~high, up & high, ~up & high], REGIMES[:3], REGIMES[3]), index=m.index)
    return pd.DataFrame({"growth": growth, "inflation": infl, "regime": regime.where(ok)})[ok]


def regime_for_return_months(cls: pd.DataFrame, months: pd.DatetimeIndex, cfg: Config = Config()) -> pd.Series:
    """Regime used in return month t = classification of macro month t - lag."""
    shifted = cls["regime"].copy()
    shifted.index = shifted.index + pd.DateOffset(months=cfg.lag_months)
    return shifted.reindex(months)


def _weights_frame(labels: pd.Series, table: dict[str, dict[str, float]]) -> pd.DataFrame:
    cols = ASSETS + ["CASH"]
    rows = [pd.Series(table.get(lbl, {}), dtype=float).reindex(cols).fillna(0.0) if isinstance(lbl, str)
            else pd.Series(np.nan, index=cols) for lbl in labels]
    return pd.DataFrame(rows, index=labels.index)


def apply_overlay(weights: pd.DataFrame, vix_prev: pd.Series, cfg: Config = Config()) -> pd.DataFrame:
    w = weights.copy()
    hot = (vix_prev.reindex(w.index) > cfg.vix_trigger).fillna(False)
    for a in RISK_ASSETS & set(w.columns):
        moved = w.loc[hot, a] * 0.5
        w.loc[hot, a] -= moved
        w.loc[hot, "CASH"] += moved
    return w


def vol_target(raw: pd.Series, cash: pd.Series, cfg: Config = Config()) -> pd.Series:
    """Scale by target / trailing realised vol known before month t; the unlevered remainder earns cash."""
    trailing = raw.rolling(cfg.vol_window, min_periods=cfg.vol_window).std(ddof=1).shift(1) * np.sqrt(12)
    lev = (cfg.vol_target / trailing).clip(upper=cfg.max_leverage)
    return (lev * raw + (1 - lev) * cash).where(lev.notna())


def leg_returns(weights: pd.DataFrame, rets: pd.DataFrame) -> pd.Series:
    r = rets.reindex(weights.index)
    return (weights * r[weights.columns]).sum(axis=1, min_count=1).where(weights.notna().all(axis=1))


def backtest(macro: pd.DataFrame, prices: pd.DataFrame, vix: pd.Series, cash_rate: pd.Series,
             cfg: Config = Config()) -> Result:
    """macro: monthly FRED levels; prices: daily/monthly closes for ASSETS; vix: daily/monthly VIX;
    cash_rate: TB3MS in % annualised."""
    px = prices[ASSETS].resample("MS").last()  # label t = month t's last close
    rets = px.pct_change(fill_method=None)  # label t = return earned during month t
    # Rate and VIX as known at the start of month t (i.e. month t-1's print / close).
    rets["CASH"] = (cash_rate.resample("MS").last() / 100 / 12).shift(1).reindex(rets.index).ffill()
    vix_m = vix.resample("MS").last().shift(1).reindex(rets.index)
    month_end = rets.index[-1] + pd.offsets.MonthEnd(0)
    if prices.index[-1] < month_end - pd.Timedelta(days=3):
        rets = rets.iloc[:-1]  # drop the partial current month

    cls = classify(macro, cfg)
    labels = regime_for_return_months(cls, rets.index, cfg).dropna()
    rets = rets.loc[labels.index]

    static = {a: np.mean([PLAYBOOK[r].get(a, 0.0) for r in REGIMES]) for a in ASSETS + ["CASH"]}
    legs_w = {
        "Macro regime allocation": _weights_frame(labels, PLAYBOOK),
        "Static blend (no switching)": _weights_frame(labels.map(lambda _: "S"), {"S": static}),
        "60/40 (SPY/IEF)": _weights_frame(labels.map(lambda _: "B"), {"B": {"SPY": 0.6, "IEF": 0.4}}),
        "Equal-weight menu": _weights_frame(labels.map(lambda _: "E"), {"E": {a: 1 / len(ASSETS) for a in ASSETS}}),
    }
    legs = pd.DataFrame({
        name: vol_target(leg_returns(apply_overlay(w, vix_m, cfg), rets), rets["CASH"], cfg)
        for name, w in legs_w.items()
    })
    legs["All-equity (SPY, raw)"] = rets["SPY"]
    legs = legs.dropna()
    table = {name: summarize(legs[name], rets["CASH"]) for name in legs}

    last_macro = cls.index[-1]
    current_regime = str(cls["regime"].iloc[-1])
    current_vix = float(vix.dropna().iloc[-1]) if not vix.dropna().empty else float("nan")
    cw = pd.Series(PLAYBOOK[current_regime], dtype=float).reindex(ASSETS + ["CASH"]).fillna(0.0)
    if current_vix > cfg.vix_trigger:
        for a in RISK_ASSETS:
            cw["CASH"] += cw[a] * 0.5
            cw[a] *= 0.5
    current = {
        "regime": current_regime,
        "macro_month": last_macro.strftime("%Y-%m"),
        "growth": round(float(cls["growth"].iloc[-1]), 2),
        "inflation": round(float(cls["inflation"].iloc[-1]), 2),
        "vix": round(current_vix, 2),
        "vix_overlay_on": bool(current_vix > cfg.vix_trigger),
        "weights": {k: round(float(v), 4) for k, v in cw.items() if v > 0},
        "switching_edge_sharpe": round(table["Macro regime allocation"]["sharpe"] - table["Static blend (no switching)"]["sharpe"], 3),
    }
    return Result(regimes=labels, growth=cls["growth"], inflation=cls["inflation"], legs=legs, table=table, current=current)
