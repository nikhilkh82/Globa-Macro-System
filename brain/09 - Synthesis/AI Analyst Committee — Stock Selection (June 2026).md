---
title: AI Analyst Committee — Stock Selection (June 2026)
category: synthesis
type: strategy-system
data_asof: 2026-09-24
summary: "Free-data reconstruction of the ai-hedge-fund committee as a 7-factor L/S over 67 US large-caps, 2001-01→2026-09: long book 10.7%/yr, Sharpe 0.83, MaxDD −40.9% vs SPY 7.1%/0.53, audited genuine; L/S ~flat."
tags: [global-macro, ai-hedge-fund, stock-selection, factor, long-short, committee, backtest, equities]
data_vintage: "LIVE — free Yahoo monthly OHLCV 2001-01→2026-09 (309 months, the final 2026-09 bar month-to-date at the 2026-09-24 pull) + Yahoo fundamentals pulled 2026-09-24"
sources: "Adapted from the open-source ai-hedge-fund (virattt) — multi-analyst architecture, free-data reconstruction"
updated: 2026-09-25
---

# AI Analyst Committee — Stock Selection (June 2026)

**What it is & why it matters** — A **single-stock long/short equity** strategy: a *free-data, backtested reconstruction* of the open-source [`ai-hedge-fund`](https://github.com/virattt/ai-hedge-fund) **multi-analyst committee**. It adds the one thing the rest of this project lacks — **bottom-up security selection** — to a system that is otherwise top-down (the [[Trading System - Backtest (June 2026)|systematic trading system]] trades indices/FX/commodities; the [[Analyst System — Live Cockpit (June 2026)|cockpit]] reads the macro regime). The original needs paid fundamentals + LLM keys; this version uses **only free Yahoo data** and replaces the LLM-persona prose with **transparent, deterministic factor-personas** — so it is auditable, reproducible, and **fabrication-free**. Artifacts in project-root `ai analyst committee/` (interactive dashboard), built by `tools/build_ai_committee.py` + `build_ai_committee_dashboard.py`.

## The committee → free-data mapping
The original runs ~17 analysts (13 investor personas + 4 quant agents) → risk manager → portfolio manager. We reproduce that **architecture** with members computable on free data, flagging what is backtestable vs current-only:

| Committee member | Inspired by | Free-data factor | Backtested? |
|---|---|---|---|
| **Momentum** | Lynch / Wood | 12-1 month price momentum | ✅ yes |
| **Trend** | Druckenmiller | price vs its 12-month average | ✅ yes |
| **Breakout** | Fisher / Lynch | proximity to the 12-month high | ✅ yes |
| **LowVol** | Buffett / Munger | inverse trailing 12-month volatility | ✅ yes |
| **MeanRev** | Burry | contrarian — negative recent 1-month return | ✅ yes |
| **TailRisk** | Taleb | return skew (antifragile convexity) | ✅ yes |
| **MacroFit** | Druckenmiller (macro) | cyclical vs defensive, tilted by the engine's risk-on regime flag | ✅ yes |
| Buffett · Graham/Burry · Lynch · Wood | the 4 fundamental personas | ROE/margins/debt, P/B-P/E-EV/EBITDA, PEG-growth, revenue/earnings growth | ⚠️ current-only |

Each member emits a cross-sectional **z-score** per month; the **portfolio manager** combines them confidence-weighted into a composite; the **risk manager** sizes positions inverse-to-volatility. The four **named fundamental personas** (Buffett, Graham/Burry, Lynch, Wood) need *point-in-time* paid data to backtest, so they run on **current** Yahoo fundamentals as a live overlay only — clearly marked, never in the track record.

## Method (honest, no look-ahead)
- **Universe:** 67 liquid US large-caps across all 11 sectors (`meta.n_univ` 67); free Yahoo **monthly OHLCV, 2001-01 → 2026-09** (`meta.start` 2001-01-31 → `meta.end` 2026-09-30, **309 monthly observations**).
- **Signal → book:** 7 factor-personas → per-month cross-sectional z → weighted composite → **top tercile long / bottom tercile short**, inverse-vol weighted. **Position formed at month *t* earns the return of month *t+1*** (no look-ahead). Monthly rebalance, benchmarked vs **SPY**.
- **Value check:** each member's **Information Coefficient** (mean monthly rank-correlation of its signal with next-month return) + IC-IR — the transparent test of who actually predicts.

## Results — 2001-01 → 2026-09 (309 months)
| Book | CAGR | Vol | Sharpe | Max DD | Hit rate (mo) | vs SPY |
|---|---|---|---|---|---|---|
| **Committee — long book** | **10.7%** | 13.4% | **0.83** | −40.9% | 64.7% | beats SPY |
| Committee — long/short (neutral) | 0.3% | 7.9% | 0.07 | −31.8% | 53.7% | ~flat |
| SPY buy & hold | 7.1% | 15.1% | 0.53 | −52.2% | 62.5% | — |

*Metrics refreshed **2026-09-24** from the rebuilt engine output (`ai_committee_latest.json`, `meta.asof` 2026-09-24, `perf.*`, 309 months through 2026-09) — this supersedes the 2026-09-08 refresh, which had superseded the original June-2026 figures. On the extended window the long book's CAGR/Sharpe eased **10.9% → 10.7% / 0.84 → 0.83**; the drawdown, the market-neutral book and the SPY benchmark are unchanged. **The final September bar is month-to-date:** prices were pulled 2026-09-24 (`ai_committee_prices.pkl`, written 2026-09-24 16:50, monthly index ending at the 2026-09-30 label), so the 309th observation is a stub and the 2026-09 book below is formed on an incomplete month — negligible for the headline figures, but the window is not 309 *complete* months. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- The **long book beats the market** — higher return, higher Sharpe (0.83 vs 0.53), and a **shallower drawdown** (−40.9% vs −52.2%) — a genuine selection edge. It also wins more months (64.7% vs 62.5%) at **lower volatility** (13.4% vs 15.1%).
- **Momentum is the engine** (IC +0.025, IC-IR **+1.69** — the only statistically strong member); Trend (IC +0.010, IC-IR +0.68) and TailRisk (+0.006, +0.63) add a little. **Three of the seven members now have a negative IC** on the longer window: **LowVol is the worst** (IC −0.031, IC-IR **−1.91**, solo Sharpe −0.57) — the low-volatility anomaly does *not* operate *within* mega-caps — with **Breakout** (−0.009, −0.61) and **MacroFit** (−0.007, −0.40) also mildly counter-productive. MeanRev is ≈ 0 (+0.002). The weights are unchanged and **not** re-fit to these ICs, so the composite is deliberately carrying three detractors rather than being optimised on its own backtest.

**Current book — formation month 2026-09, run 2026-09-24** (`scorecard`, `asof_month` 2026-09): of the 67 names, **22 LONG / 23 SHORT** (the rest neutral). The composite's top longs are **MU +0.95, AMD +0.73, INTC +0.73, CSCO +0.63, TGT +0.51** — a semis/hardware-led, momentum-driven long book. The bottom of the book is **NKE −0.84, ORCL −0.74, WMT −0.60, MCD −0.53, PG −0.51** — staples and lagging mega-caps. This is a signal snapshot, not a position record.

## Honest read
- The edge lives in the **long book and security selection**, not in shorting: the **market-neutral long/short is roughly flat** because the universe is current S&P constituents (**survivorship bias**) in a 26-year bull — shorting quality survivors loses. This is disclosed, not hidden.
- **The excess over SPY is front-loaded.** The adversarial audit found nearly all lifetime *relative* alpha was earned in **2001–2008** (dot-com + GFC); the relative edge has been roughly flat-to-negative since ~2022. The **absolute** Sharpe is robust, though (5-year rolling long-book Sharpe never negative, median ~1.0). The dashboard shows the cumulative-excess-vs-SPY curve so this is visible, not buried.
- The **fundamental personas are a current snapshot**, not a backtested signal; free data has no clean point-in-time fundamentals. The snapshot behind them (`ai_committee_fundamentals.json`) was re-pulled **2026-09-24** and covers all **67** names (ROE, margins, revenue/earnings growth, debt/equity, P/E, P/B, PEG, EV/EBITDA, beta, market cap, FCF; 66 of 67 carry a P/E). It has no `as_of` field of its own — its vintage is the pull date, which is why it is never folded into the track record.
- **Transaction costs are excluded**; tercile turnover is moderate. Treat the Sharpe as a gross, in-sample-universe upper bound.
- **The `meta.regime` label is a constant, not a read.** The payload reports `"regime": "Reflation (risk-on)"`, but that string is hard-coded in `build_ai_committee.py` — it is *not* re-derived each run and must not be quoted as a live regime call. Use [[Macro Regime - Live (June 2026)]] for that. The MacroFit member's own cyclical-vs-defensive tilt is computed from prices and is unaffected; it just happens to be one of the members with a negative IC (−0.007).

> **Adversarially audited (2026-06-21): GENUINE — cleared to publish.** Two independent audits + a lead verifier reproduced the load-bearing facts. **No look-ahead** — book PnL is `(weights.shift(1)*ret).sum()`, so the signal through end of month *t* earns the month *t+1* return; the leaking contemporaneous variant scores Sharpe **1.29** vs the published **0.84**, confirming the shift is real. The IC target (`ret.shift(-1)`) is evaluation-only. Headline (Sharpe 0.84 / 11.0% / −40.9%, 306 months) and member ICs reproduce exactly. Survivorship bias and transaction-cost exclusion are disclosed; worst issue severity: minor (the front-loaded-alpha caveat above).

## What's faithful / what's approximated vs the original
Faithful: the **committee-of-analysts architecture**, the per-stock bullish/bearish + confidence vote, the risk-manager sizing and portfolio-manager aggregation, and the investor-persona *spirit* (momentum=Druckenmiller, contrarian=Burry, antifragility=Taleb, quality=Buffett, deep-value=Graham, GARP=Lynch, disruption=Wood). Dropped/approximated: the **LLM-generated narratives** (replaced by deterministic factors — no fabrication) and the **paid point-in-time fundamentals** (price/macro factors backtested; fundamentals current-only).

## See also
- The live committee scorecard + performance: open `ai analyst committee/AI Analyst Committee Dashboard.html` (it carries its own *built 2026-09-24* stamp and renders the payloads above; the file itself was last written 2026-09-25, re-rendering the same 2026-09-24 payload).
- Sibling systematic strategy: [[Trading System - Backtest (June 2026)]] (top-down cross-asset). Macro regime feeding the MacroFit member: [[Macro Regime - Live (June 2026)]]. Sizing/stops discipline: [[Risk Management]]. Method lineage: [[The Global Macros Framework]].

*Educational; not investment advice. Every figure is computed from free data and reproducible — no fabricated performance.*
