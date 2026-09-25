"""Tiny CSV cache so repeated runs don't re-pull, and a failed pull can fall back to the last good copy."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Callable

import pandas as pd

from gms import paths


def cached(kind: str, key: str, fetch: Callable[[], pd.Series], max_age_hours: float = 12.0) -> pd.Series:
    path = paths.CACHE / kind / f"{key.replace('^', '_').replace('=', '_')}.csv"
    fresh = path.exists() and (time.time() - path.stat().st_mtime) < max_age_hours * 3600
    if fresh:
        return _read(path, key)
    try:
        s = fetch()
    except Exception:
        if path.exists():  # stale beats nothing; the caller's data_asof tells the truth
            return _read(path, key)
        raise
    path.parent.mkdir(parents=True, exist_ok=True)
    s.rename(key).to_csv(path, index_label="date")
    return s


def _read(path: Path, key: str) -> pd.Series:
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df.iloc[:, 0].rename(key).dropna()
