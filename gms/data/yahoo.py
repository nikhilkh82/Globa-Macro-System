"""Daily closes from Yahoo's public chart endpoint (adjusted close where available)."""

from __future__ import annotations

import pandas as pd
import requests

from gms.data.cache import cached

URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
HEADERS = {"User-Agent": "Mozilla/5.0 (global-macro-system)"}


def _fetch(symbol: str, start: str) -> pd.Series:
    p1 = int(pd.Timestamp(start).timestamp())
    p2 = int(pd.Timestamp.now(tz="UTC").timestamp())
    r = requests.get(URL.format(symbol=symbol), headers=HEADERS, timeout=30,
                     params={"period1": p1, "period2": p2, "interval": "1d", "events": "div,split"})
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]
    idx = pd.to_datetime(res["timestamp"], unit="s").normalize()
    ind = res["indicators"]
    close = (ind.get("adjclose") or [{}])[0].get("adjclose") or ind["quote"][0]["close"]
    s = pd.Series(close, index=idx, dtype="float64").dropna()
    return s[~s.index.duplicated(keep="last")].rename(symbol)


def closes(symbol: str, start: str = "2000-01-01", max_age_hours: float = 12.0) -> pd.Series:
    return cached("yahoo", symbol, lambda: _fetch(symbol, start), max_age_hours)


def frame(symbols: list[str], start: str = "2000-01-01") -> pd.DataFrame:
    return pd.concat([closes(s, start) for s in symbols], axis=1).sort_index()
