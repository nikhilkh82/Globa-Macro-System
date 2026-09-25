---
title: Managed-Futures Trend System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Multi-lookback TSMOM (3/6/12m, long and short) across equities/rates/commodities/FX, 15% vol target, FRED 2000–2026 — Sharpe 0.54 (< 60/40) but −0.23 S&P correlation and +2.69% in worst-decile equity months."
tags: [global-macro, strategy, managed-futures, trend-following, tsmom, cta, crisis-alpha, backtest]
data_vintage: "LIVE (FRED 2000-03→2026-08) + ^GSPC splice — engine re-run 2026-09-24 16:21"
sources: 1
updated: 2026-09-24
---

# Managed-Futures Trend System

A **time-series-momentum (CTA / managed-futures) strategy** — diversified trend following across equities, rates, commodities and FX, vol-targeted — ported from the [systematic-trend-following](../../raw/11.%20Strategies/systematic-trend-following-with-managed-futures-main/) framework to live FRED data. Its defining property is **crisis alpha**: it tends to make money exactly when equities fall hardest. Built 2026-06-22.

> Research/education only — not investment advice.

## Provenance — what we adapted
The source (`tf-trend`) is a professional managed-futures backtesting scaffold: multi-lookback TSMOM signals, EWMA-vol targeting to a constant portfolio vol, a diversified futures universe with sector caps, cost/roll models, and walk-forward tooling — but it runs on **synthetic** data. The faithful adaptation keeps the *methodology and config* (lookbacks 3/6/12, 15% vol target, sector caps 40%, gross ≤ 2.5×) and runs it on **live free data with long history**, so the **2008 GFC and 2020** are in-sample for the crisis-alpha test.

## How it works
- **Universe (8, 4 sectors):** S&P 500, Nasdaq (Equities) · US 10Y & 2Y bonds, as *synthetic total returns* from yields, `r = carry − duration·Δy` (Rates) · WTI, Copper (Commodities; copper substitutes gold, which has no long free FRED price) · EUR/USD, JPY-long (FX). S&P history spliced from `^GSPC.csv` (1990–2018) + live FRED `SP500`.
- **Signal:** multi-lookback **time-series momentum** — the average sign of the 3/6/12-month return per instrument (long if up-trending, **short if down-trending** — both sides, the CTA hallmark).
- **Sizing:** trend × inverse-EWMA-vol, scaled to a **15% ex-ante portfolio-vol target**, sector-capped at 40%, gross ≤ 2.5×.
- **Causal, monthly:** signal and vol use only data ≤ t; the position earns month t→t+1's return; 15bps × turnover cost; the run ends at the last **completed** month.

## Outputs (`Managed Futures/`)
- **`Managed Futures Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 vs S&P & 60/40, the **crisis-alpha** bar, current positioning, a benchmark table, and sector P&L attribution.
- **`Managed Futures Note <date>.md`** + **`mfutures_latest.json`**.
Tools: `tools/mfutures.py` (engine) · `mfutures_report.py` · `build_mfutures.py` (one command). Reuses `tools/fred.py`.

## Result — 2000-03 → 2026-08 (monthly, net of cost)
| Strategy | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| **Managed-Futures (TSMOM)** | **+0.54** | 5.4% | 10.9% | −29.0% |
| S&P 500 (buy & hold) | +0.51 | 6.7% | 15.2% | −52.6% |
| 60/40 | +0.68 | 5.9% | 9.1% | −31.1% |
| Equal-weight long-only | +0.61 | 5.1% | 8.9% | −31.3% |

*Vintage: engine **re-run 2026-09-24 16:21** (`mfutures_latest.json`, `as_of` 2026-09-24). The run ends at the last **completed** month, still **2026-08** (`mf.n` = 318), so no new return months entered the sample and the window did not move — but **the figures still shift slightly run-to-run**, because the engine re-pulls revised FRED data and the live `SP500` splice. An unmoved window is therefore not a reason to assume unmoved numbers. **Changed this pass** (against `Managed Futures Note 2026-09-08.md`): MF MaxDD **−29.1% → −29.0%** and the crisis mean **+2.68% → +2.69%**. **Unchanged:** MF Sharpe 0.54, CAGR 5.4%, Vol 10.9%, and the whole S&P and 60/40 rows. Added this pass: the benchmark CAGR/Vol/MaxDD cells, previously blank, from `sp` / `s6040` / `ew` — the equal-weight row now reads 5.1% / **8.9%** / **−31.3%**, themselves revised from 8.8% / −31.1% on 2026-09-08. (Supersedes the earlier "metrics refreshed 2026-09-08" provenance note; the June-2026 figures remain superseded.) The audit verdicts below are unchanged and still refer to the original adversarial review.*

**The value is diversification, not standalone return.** Standalone, the CTA is a modest Sharpe (0.54, below 60/40's 0.68) — typical for trend following. But it has **−0.23 correlation to the S&P** (`corr_sp`), and in the **worst-decile equity months** (avg S&P **−8.19%**, n=31) it averaged **+2.69%** (median **+2.87%**; positive in **68%** of them) — genuine **crisis alpha**. It's an equity-drawdown hedge / portfolio diversifier that sits *alongside*, not instead of, a long book. *(`crisis.worst_eq_avg` / `.mf_in_worst` / `.mf_median` / `.pos_share`. The crisis mean **moved** +2.68% → +2.69% on this run — a **data** change from the revised re-pull, not a re-rounding: the 2026-09-08 note printed +2.68% at this same precision. Separately, this page previously wrote the S&P average as −8.2% and the positive share as "~⅔"; those two are re-rounding fixes only, now at the payload's own precision.)*

**The drawdown case, now that the benchmark cells are filled:** the CTA's **−29.0%** MaxDD is the shallowest in the table — better than 60/40 (−31.1%), equal-weight long-only (−31.3%) and far better than the S&P's **−52.6%** — on 10.9% vol (above 60/40's 9.1% and equal-weight's 8.9%, well below the S&P's 15.2%). It earns a lower Sharpe than 60/40 on barely half the S&P's drawdown, which is the whole argument for holding it.

## Live positioning — 2026-09-24
*Signal as of the 2026-09-24 16:21 run (`positions[]`, weights = % portfolio notional after vol-scaling; the signal uses data ≤ 2026-08 and earns 2026-08→09).*

| Instrument | Sector | Weight | Direction |
|---|---|---|---|
| Copper | Commodities | +37.4% | LONG |
| US 2Y bond | Rates | +36.7% | LONG |
| JPY (long) | FX | −28.5% | SHORT |
| S&P 500 | Equities | +24.0% | LONG |
| Nasdaq | Equities | +16.0% | LONG |
| EUR/USD | FX | −11.5% | SHORT |
| US 10Y bond | Rates | −3.3% | SHORT |
| WTI crude | Commodities | +2.6% | LONG |

- **The book is risk-on with a long-front-end tilt:** long both equity indices, long copper as the largest single position, short both FX crosses (i.e. long USD), and — the notable pair — **long the 2Y (+36.7%) against a small short in the 10Y (−3.3%)**, a de-facto **steepener** expressed through two separate trend signals rather than as a curve trade.
- **That sits awkwardly against the front-end repricing** (`tools/macro_pack.json`, read 2026-09-24): the Fed hiked 2026-09-16, fed funds 3.88% (09-22), 2Y 4.71% and 10Y 4.96% (09-22), 2s10s +0.26pp (09-23). A trend signal fitted on data through 2026-08 is long the instrument the hike repriced most; this is the ordinary lag of a monthly trend system after a policy turn, not a view.
- **Sector P&L attribution, cumulative over 2000-03→2026-08** (`sector_attr[].contrib`, cumulative percentage points of summed monthly contribution): Commodities **+73.4**, Equities **+72.9**, FX **+21.4**, Rates **+21.2**. Commodities and equities have carried the book **roughly equally** (+73.4 vs +72.9); rates and FX are the minor contributors at about a third of that each. **⚠️ Flagged 2026-09-24:** [[Robust Equity Trend System]] describes this CTA as one "where rates/commodities/FX trend carried the book" — the attribution says otherwise, since equity trend is the joint-largest contributor here. That cross-page claim is flagged on both pages for correction at the next audit; no verdict on either page depends on it.

## Caveats
- The crisis-alpha statistic is **descriptive / ex-post** (the worst months are identified with hindsight over the full sample) — a diversification property, **not** a realizable market-timing edge.
- Realized vol (10.9%) runs below the 15% target because the zero-correlation ex-ante scaling is conservative (trend signs diversify).
- Free-data proxies: synthetic bond total returns from yields; **copper substitutes gold** for free long history; revised (not vintage) data; monthly cadence.
- Adversarially audited (2-lens workflow) → **6 LOW-severity items fixed** (a forward-availability filter in sizing; the partial current month; crisis-stat framing) — none changed the headline numbers; the fixes nudged Sharpe 0.54→0.55.

## Related
[[Trading System - Backtest (June 2026)]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[LangAlpha Strategy System]] · [[Analyst System — Live Cockpit (June 2026)]] · [[The Global Macros Framework]]
