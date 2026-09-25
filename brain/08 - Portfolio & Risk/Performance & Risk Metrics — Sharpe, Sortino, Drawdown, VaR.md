---
title: "Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR"
category: portfolio-risk
type: live-read
data_asof: 2026-09-19
summary: "Gliner Ch 2's measurement half plus the platform's scorecard (17 audited systems: 5 POSITIVE, 8 NULL, 1 MARGINAL, 2 CORRECTED, 1 SUPPORT); a Sharpe alone earns nothing — Macro Regime Allocation's 0.69 is still NULL."
tags: ["risk", "sharpe", "sortino", "drawdown", "var", "metrics", "gliner"]
updated: 2026-09-19
data_vintage: "strategy verdicts from scorecard_latest.json (17 audited backtests, held as constants in tools/synthesis_scorecard.py; the payload's as_of is a rebuild stamp — 2026-09-19 on the copy read today) · book figures from macrocot_latest.json (2026-09-19 engine run on CFTC positions as of 2026-09-15)"
sources: 4
---

# Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR

Gliner Ch 2's measurement half. The formulas are standard; what matters is **which one answers which question**, and what this platform's own numbers look like when measured honestly.

## The metrics

**Sharpe ratio** — excess return per unit of total volatility.
```
Sharpe = (Rp − Rf) / σp
```
Penalises upside and downside volatility equally. Its weakness for macro: a strategy with rare large gains and steady small losses (long options, trend) looks worse than it trades.

**Sortino ratio** — excess return per unit of *downside* volatility.
```
Sortino = (Rp − Rf) / σ_downside
```
Only deviations below the target enter the denominator. Better for the asymmetric return profiles global macro deliberately seeks.

**Drawdown** — peak-to-trough decline; the honest measure of what an investor actually endures. Max drawdown and time-to-recovery matter more than either ratio for capital retention, which the book identifies as global macro's *primary* aim.

**Value at Risk (VaR)** — the loss threshold not expected to be exceeded at a given confidence over a horizon (e.g. 95%/1-day). Its known failure: it says nothing about the size of the loss *beyond* the threshold, which is precisely the macro tail. Pair with stress tests.

**Risk utilisation** — how much of the risk budget is deployed. Low utilisation with good returns is skill; full utilisation with the same returns is leverage.

## This platform's measured record

From the Strategy Scorecard (`Synthesis/scorecard_latest.json`, re-read 2026-09-19). The table below reproduces that payload line for line: 17 systems tested with honest verdicts, 5 POSITIVE / 8 NULL / 1 MARGINAL / 2 CORRECTED plus 1 SUPPORT.

**Read the payload's date carefully.** Its `as_of` field is a *rebuild stamp*, not an observation date — `tools/synthesis_scorecard.py` writes `datetime.now()` into it on every run, and the copy read today is stamped **2026-09-19** (earlier passes this cycle recorded it as 2026-09-16 and 2026-09-08 — each that day's rebuild, not a data vintage). None of the numbers below was measured on either date: the Sharpes and verdicts are constants held in that builder — the audited output of each system's own backtest — re-emitted unchanged on each rebuild. Read the table as a ledger of audit results, not as a market read taken today.

| Verdict | Systems |
|---|---|
| **POSITIVE** | Managed Futures (CTA) 0.55 · Hedge-Fund Replication 0.65 · Macro-Aware Risk Parity 0.69 · FX Signals (carry) 0.40 · FX Carry-Valuation 0.31 |
| **MARGINAL** | Treasury Macro-Trend 0.50 |
| **CORRECTED** | Demand-Based Rates · Sectoral Macro-Trend 0.43 |
| **SUPPORT** | AI Hedge-Fund Committee |
| **NULL** | ML Macro-Direction · Curve Macro 0.18 · Macro Regime Allocation 0.69 · Robust Equity Trend 0.32 · Macro Sector Rotation 0.01 · Credit ML 0.57 · Information State Changes −0.09 · Surprises→Commodities −0.29 |

Two disciplines are visible in that table and both are worth preserving:

1. **A Sharpe number alone does not earn a POSITIVE verdict.** Macro Regime Allocation shows 0.69 — the same as Risk Parity — yet is marked NULL, because the metric did not survive the significance/robustness test. Ranking by Sharpe would have promoted a system the evidence does not support.
2. **Negative results are kept, not deleted.** Information State Changes (−0.09) and Surprises→Commodities (−0.29) remain in the ledger. That is what stops the lab from becoming a record of survivors only.

## What this platform does not compute

Stated plainly rather than implied:

- **No portfolio-level VaR.** Per-trade risk is sized and gross risk is reported (currently **3.0% of the illustrative account across 3 TAKEs** — $3,000 on the $100,000 account, all three at HIGH conviction (USD/JPY short, WTI Crude long, Dow Jones long); 2026-09-19 engine run on CFTC positions as of 2026-09-15; it was 2.6% across 3 TAKEs on 2026-09-16 and 4.4% across 6 TAKEs on 2026-08-12), but there is no covariance-based VaR number. Gross risk is a *sum of stop distances*, not a portfolio risk estimate: it assumes nothing about how the three positions co-move.
- **No stress-testing engine.** No scenario shocks (rates +100bp, equities −20%, USD +5%).
- **No Sortino** anywhere in the stack — every reported ratio is a Sharpe.
- **No live drawdown tracking** on the paper book; drawdowns exist only inside individual backtests.

Those four are the honest gap between Gliner Ch 2 and this platform's risk layer. The sizing half is implemented ([[Position Sizing, Unit Size & Volatility Adjustment]]); the portfolio-measurement half is partial.

Related: [[Risk Management]] · [[Position Sizing, Unit Size & Volatility Adjustment]] · [[Cross-System Synthesis — What Works]] · [[Distribution of Returns]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
