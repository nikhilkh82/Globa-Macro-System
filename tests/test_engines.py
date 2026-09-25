import numpy as np
import pandas as pd
import pytest

from gms.engine import metrics, pulse, regime


def monthly_macro(cpi_yoy: float, growth_yoy: float, months: int = 60) -> pd.DataFrame:
    idx = pd.date_range("2015-01-01", periods=months, freq="MS")
    t = np.arange(months) / 12
    return pd.DataFrame({
        "INDPRO": 100 * (1 + growth_yoy / 200) ** t,
        "PAYEMS": 150_000 * (1 + growth_yoy / 200) ** t,
        "CPIAUCSL": 250 * (1 + cpi_yoy / 100) ** t,
    }, index=idx)


@pytest.mark.parametrize("cpi,growth,expected", [
    (2.0, 3.0, "Goldilocks"), (4.0, 3.0, "Reflation"), (4.0, -3.0, "Stagflation"), (1.0, -3.0, "Deflation"),
])
def test_classify_quadrants(cpi, growth, expected):
    cls = regime.classify(monthly_macro(cpi, growth))
    assert cls["regime"].iloc[-1] == expected
    assert cls["inflation"].iloc[-1] == pytest.approx(cpi, abs=1e-6)


def test_publication_lag_shifts_regime_forward():
    macro = monthly_macro(2.0, 3.0, months=36)
    macro.loc["2017-06-01":, "CPIAUCSL"] *= 1.05  # inflation jumps in the Jun-2017 print
    cls = regime.classify(macro)
    labels = regime.regime_for_return_months(cls, pd.date_range("2017-05-01", "2017-09-01", freq="MS"))
    assert list(labels) == ["Goldilocks", "Goldilocks", "Goldilocks", "Reflation", "Reflation"]


def synthetic_markets(months: int = 120, seed: int = 7):
    rng = np.random.default_rng(seed)
    days = pd.bdate_range("2012-01-02", periods=months * 21)
    prices = pd.DataFrame({a: 100 * np.exp(np.cumsum(rng.normal(0.0003, 0.01, len(days)))) for a in regime.ASSETS}, index=days)
    vix = pd.Series(np.where(np.arange(len(days)) % 500 >= 440, 30.0, 15.0), index=days)
    cash = pd.Series(2.0, index=pd.date_range("2010-01-01", days[-1], freq="MS"))
    macro = monthly_macro(4.0, 3.0, months=months + 36).set_index(pd.date_range("2009-01-01", periods=months + 36, freq="MS"))
    return macro, prices, vix, cash


def test_backtest_runs_walk_forward_and_matches_vol():
    macro, prices, vix, cash = synthetic_markets()
    res = regime.backtest(macro, prices, vix, cash)
    assert res.current["regime"] == "Reflation"
    assert res.current["weights"] == {"SPY": 0.3, "DBC": 0.3, "GLD": 0.2, "HYG": 0.2}  # VIX 15 at the end (2519 % 500 = 19): overlay off
    for name in ["Macro regime allocation", "Static blend (no switching)", "60/40 (SPY/IEF)", "Equal-weight menu"]:
        assert res.table[name]["vol"] == pytest.approx(0.10, abs=0.035)
    assert res.legs.index.max() <= prices.index[-1]


def test_vix_overlay_moves_half_of_risk_assets_to_cash():
    w = regime._weights_frame(pd.Series(["Reflation"], index=[pd.Timestamp("2020-03-01")]), regime.PLAYBOOK)
    out = regime.apply_overlay(w, pd.Series([35.0], index=w.index))
    row = out.iloc[0]
    assert row["SPY"] == pytest.approx(0.15) and row["HYG"] == pytest.approx(0.10) and row["DBC"] == pytest.approx(0.15)
    assert row["GLD"] == pytest.approx(0.20) and row["CASH"] == pytest.approx(0.40)
    assert row.sum() == pytest.approx(1.0)


def test_pulse_zscore_is_causal_and_finds_dominant():
    rng = np.random.default_rng(1)
    idx = pd.bdate_range("2020-01-01", periods=300)
    closes = pd.DataFrame({k: 100 * np.exp(np.cumsum(rng.normal(0, 0.01, 300))) for k in pulse.INSTRUMENTS}, index=idx)
    before = pulse.zscores(closes).iloc[:-1]
    closes.iloc[-1, closes.columns.get_loc("US10Y")] = closes["US10Y"].iloc[-2] * 1.06  # +6% day, ~6σ
    z = pulse.zscores(closes)
    pd.testing.assert_frame_equal(z.iloc[:-1], before)  # a new bar never rewrites history
    rows, dom = pulse.board(closes)
    assert dom["instrument"] == "US10Y" and dom["z"] > 4 and dom["regime"] == "Rates up / growth-or-inflation"
    assert rows[0]["instrument"] == "US10Y"


def test_pulse_study_reports_every_signal():
    rng = np.random.default_rng(2)
    idx = pd.bdate_range("2010-01-01", periods=2000)
    closes = pd.DataFrame({k: 100 * np.exp(np.cumsum(rng.standard_t(3, 2000) * 0.01)) for k in pulse.INSTRUMENTS}, index=idx)
    out = pulse.study(closes)
    assert [s["signal"] for s in out] == [s[0] for s in pulse.SIGNALS]
    assert all(s["n"] > 10 for s in out)


def test_metrics_drawdown_and_cagr():
    r = pd.Series([0.1, -0.5, 0.2] + [0.0] * 9)
    assert metrics.max_drawdown(r) == pytest.approx(-0.5)
    assert metrics.summarize(r)["cagr"] == pytest.approx(1.1 * 0.5 * 1.2 - 1)
