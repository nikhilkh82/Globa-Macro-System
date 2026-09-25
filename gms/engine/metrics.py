"""Performance metrics shared by the engines."""

from __future__ import annotations

import numpy as np
import pandas as pd


def max_drawdown(returns: pd.Series) -> float:
    wealth = (1 + returns.fillna(0)).cumprod()
    return float((wealth / wealth.cummax() - 1).min())


def summarize(returns: pd.Series, cash: pd.Series | None = None, periods: int = 12) -> dict:
    r = returns.dropna()
    if r.empty:
        return {"sharpe": float("nan"), "cagr": float("nan"), "vol": float("nan"), "maxdd": float("nan"), "n": 0}
    excess = r - (cash.reindex(r.index).fillna(0) if cash is not None else 0)
    vol = float(r.std(ddof=1) * np.sqrt(periods))
    ex_sd = float(excess.std(ddof=1))
    sharpe = float(excess.mean() / ex_sd * np.sqrt(periods)) if ex_sd > 0 else float("nan")
    years = len(r) / periods
    cagr = float((1 + r).prod() ** (1 / years) - 1) if years > 0 else float("nan")
    return {"sharpe": sharpe, "cagr": cagr, "vol": vol, "maxdd": max_drawdown(r), "n": int(len(r))}
