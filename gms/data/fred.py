"""FRED series. Uses the keyed JSON API when `FRED_API_KEY` is set, else the public fredgraph CSV."""

from __future__ import annotations

import io
import os

import pandas as pd
import requests

from gms.data.cache import cached

API = "https://api.stlouisfed.org/fred/series/observations"
CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv"
TIMEOUT = 30


def _fetch(series_id: str, start: str) -> pd.Series:
    key = os.environ.get("FRED_API_KEY")
    if key:
        r = requests.get(API, params={"series_id": series_id, "api_key": key, "file_type": "json",
                                      "observation_start": start}, timeout=TIMEOUT)
        r.raise_for_status()
        obs = r.json()["observations"]
        s = pd.Series({pd.Timestamp(o["date"]): o["value"] for o in obs})
    else:
        r = requests.get(CSV, params={"id": series_id, "cosd": start}, timeout=TIMEOUT)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        s = pd.Series(df.iloc[:, 1].values, index=pd.to_datetime(df.iloc[:, 0]))
    return pd.to_numeric(s, errors="coerce").dropna().sort_index().rename(series_id)


def series(series_id: str, start: str = "1990-01-01", max_age_hours: float = 12.0) -> pd.Series:
    return cached("fred", series_id, lambda: _fetch(series_id, start), max_age_hours)


def frame(ids: list[str], start: str = "1990-01-01") -> pd.DataFrame:
    return pd.concat([series(i, start) for i in ids], axis=1)
