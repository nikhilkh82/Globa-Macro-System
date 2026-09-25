---
title: ML Macro-Direction Model
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Walk-forward classification of S&P next-month direction from 13 macro/rates/sentiment features vs passive — no genuine skill: no accuracy is meaningfully above the 63.5% always-up base rate; the 'edge' is time in cash."
tags: [global-macro, strategy, machine-learning, classification, backtest, calibration, needs-re-audit]
data_vintage: "LIVE (FRED 1990→2026-08) + source ^GSPC splice; engine re-run 2026-09-24 16:20"
sources: 1
updated: 2026-09-24
---

# ML Macro-Direction Model

A supervised-ML system that predicts **S&P 500 next-month direction** from macro + rates + sentiment features, benchmarking SVM / Decision Tree / Naive Bayes / Logistic / Random Forest against passive buy-and-hold — a strictly **walk-forward (no-look-ahead)** recreation of the [ML-macro-market capstone](../../raw/11.%20Strategies/ML-macro-market-master/) on live, free, long-history data. Built 2026-06-22.

> Research/education only — not investment advice.

## Provenance — what we adapted
The source ([ML-macro-market](../../raw/11.%20Strategies/ML-macro-market-master/)) is a data-science capstone framed by **Buffett's 10-year bet** (hedge funds couldn't beat passive indexing): can supervised ML on macro/sentiment features predict the market and beat passive? Its finding: **SVM/Decision Tree came close but couldn't beat passive**; LEI + rates carried most feature weight; Decision Tree overfit. Its data ends 2018 and several inputs are proprietary (Conference Board LEI, CBOE put/call, NAAIM/AAII surveys). We rebuilt the **methodology** on live data (refreshable through 2026), using FRED sentiment/risk proxies for the proprietary surveys.

## How it works
- **Target** — sign of next-month S&P 500 return. S&P history is spliced from the source's `^GSPC.csv` (1990–2018) + live FRED `SP500` (2018→2026).
- **Features (13, monthly, point-in-time; FRED pulled from 1990, usable sample after transforms 1991-03→2026-08)** — *Leading:* yield-curve `T10Y3M`, building-permits YoY, jobless-claims 3m change. *Rates:* 10Y level & 3m change, 3M T-bill. *Sentiment/risk:* VIX level & change, U-Mich consumer sentiment (proxying the source's put/call & investor surveys). *Macro:* INDPRO/M2/CPI YoY. *Price:* S&P 6-month momentum.
- **Walk-forward, no look-ahead** — at month *t* each model (sklearn `Pipeline(StandardScaler, clf)`) trains only on months `< t`; the scaler is fit on the training window only; the prediction earns month *t→t+1*'s return. Publication-lagged macro prints (permits, INDPRO, M2, CPI, the T-bill average) are shifted back one month so only data actually released by end-of-*t* is used.
- **Honest evaluation** — strategy = long if predict-up, else **earn the T-bill** (not 0); compared to passive on Sharpe/CAGR/MaxDD **plus** the metrics that expose artifacts: each model's **directional accuracy vs the up-month base rate** (binomial *z*), its **time-in-market**, and a **random-timer null** (its Sharpe percentile vs no-skill timers at the same exposure). `beats_passive` is set **only** if a model's accuracy is significantly above the base rate *and* its Sharpe clears the no-skill null.

## Outputs (`ML Macro Model/`)
- **`ML Macro Model Dashboard.html`** — light theme, Chart.js inlined: accuracy-by-model (vs base rate), feature importance by category, strategy-vs-passive equity curves, top features, the bake-off table.
- **`ML Macro Model Note <date>.md`** + **`mlmacro_<date>.json`** (dated snapshots) beside **`mlmacro_latest.json`**, which is the payload this page documents.
Tools: `tools/ml_macro.py` (engine) · `ml_macro_report.py` · `build_ml_macro.py` (one command). Reuses `tools/fred.py`; needs `scikit-learn`.

## Result — live, sample 1991-03 → 2026-08; held out 2001-03 → 2026-08 (304 OOS months)
*Metrics refreshed 2026-09-24 from the re-run engine (`mlmacro_latest.json`, `generated` 2026-09-24 16:20). **Nothing drifted today:** the re-run reproduces the **2026-09-08** payload — `mlmacro_2026-09-08.json` carries the same `window` [1991-03, 2026-08], `n_months` 424, `oos_months` 304, `base_rate` 63.5 and the same `models[]` statistics as the table below, differing only in `as_of` / `generated` and 4th-decimal `cat_imp` / `feat_imp` rounding. The move away from the 2026-06-22 figures (sample to 2026-05, 301 OOS months) therefore happened at the **2026-09-08** run, which this page was not updated for; today's refresh is where it is being written down. The verdict is unchanged and preserved word-for-word — the engine's own gates still read `beats_passive: false` and `skilled_models: []`.*

*Window, stated precisely (a correction to the June heading, which quoted the sample span as if it were the held-out span): `window` is the feature sample **1991-03 → 2026-08** (`n_months` 424) and `min_train` is **120 months**, so the first scored month is 2001-03 and the evaluated out-of-sample period is **2001-03 → 2026-08**, `oos_months` **304** (`labels[0]`/`labels[-1]` confirm both ends). June's run held out 2001-03 → 2026-05, 301 months — the same start, three months shorter.*

**No model shows genuine directional skill — it cannot beat passive.** No model's directional accuracy is meaningfully above the **63.5% "always-up" base rate** (binomial *z* from −2.98 to +0.12; SVM's "best" 63.8% sits 0.3pt over the base rate and is statistically identical to always-up). The highest-Sharpe model (Decision Tree, 0.69 vs passive 0.56) is at the **95th percentile of no-skill random timers** at the same exposure — i.e. within best-of-5 selection luck — and its accuracy (60.9%) is *below* the base rate. Its apparent Sharpe "edge" over passive is **time spent in cash, not directional alpha**: it is in the market only 78.9% of months and realizes 11.7% vol against passive's 15.0%. Feature importance (Random Forest, in-sample) is close to flat across categories — Macro 25% / Sentiment 23% / Leading 22% / Rates 21% / Price 10% — with 6-month price momentum the single largest feature (`spx_mom6`, 10.3%) and the yield curve the *smallest* (`curve`, 6.5%). **This reproduces the capstone's and Buffett's conclusion.**

| Model | Accuracy | *z* vs base | Sharpe | CAGR | Vol | MaxDD | In-market | Null %ile |
|---|---|---|---|---|---|---|---|---|
| Decision Tree | 60.9% | −0.95 | 0.69 | 7.7% | 11.7% | −35.0% | 78.9% | 95.0 |
| Naive Bayes | 55.3% | −2.98 | 0.68 | 6.5% | 10.1% | −33.2% | 61.5% | 92.8 |
| SVM (RBF) | 63.8% | +0.12 | 0.64 | 8.1% | 13.8% | −54.7% | 91.1% | 94.1 |
| Logistic | 59.2% | −1.55 | 0.62 | 7.1% | 12.2% | −30.0% | 78.6% | 84.8 |
| Random Forest | 62.2% | −0.48 | 0.62 | 7.6% | 13.4% | −47.6% | 86.8% | 85.6 |
| **Passive (buy & hold)** | 63.5% *(base rate)* | — | **0.56** | **7.5%** | **15.0%** | **−52.6%** | 100% | — |

*Read from `mlmacro_latest.json` (`models[].acc / acc_z / sharpe / cagr / vol / maxdd / time_in / null_pct`, `passive`, `base_rate`). "Null %ile" is the model's Sharpe percentile against no-skill random timers at the same market exposure; cash months earn the T-bill, not 0%.*

> **Flagged for re-audit (2026-09-24) — one supporting statistic drifted with the three extra months that arrived at the 2026-09-08 run (today's re-run reproduced that payload unchanged), and one was wrong when it was written; the verdict itself did not flip.**
> 1. The June write-up's "every model's accuracy is **at or below** the 63.8% base rate" was **false at birth, not overtaken by drift**: `mlmacro_2026-06-22.json` itself has SVM at **64.1%** against June's own **63.8%** base rate — 0.3pt *above*. Today reads 63.8% against a 63.5% base rate: the same 0.3pt gap, the same relation. At *z* +0.12 it is statistically indistinguishable from always-up either way, so no skill is implied — but the sentence was wrong when written and is reworded here rather than left standing.
> 2. On the like-for-like CAGR metric, **3 of 5 models now edge past passive's 7.5%** (Decision Tree 7.7%, SVM 8.1%, Random Forest 7.6%), where the June write-up said "4 of 5 models match or trail passive". Re-reading `mlmacro_2026-06-22.json` directly, June was already 2 of 5 *above* passive (Decision Tree 8.0%, SVM 8.2%) with Random Forest exactly matching at 7.5% — so that sentence overstated the gap even then, and the drift since is Random Forest crossing from 7.5% to 7.6%.
>
> Neither model clears the engine's skill gate (accuracy significantly above base rate **and** Sharpe beyond the no-skill null), so the published null stands as written. This CAGR comparison goes back for **re-audit**, not absorption.
>
> **Also flagged, same date — a boundary case, not a drift:** Decision Tree's `null_pct` of **95.0** sits *at or over* the "≥95 = beyond luck" line that the engine's own note legend draws (`ML Macro Model Note 2026-09-24.md`), while the paragraph above reads the same 95.0 as "within best-of-5 selection luck". `beats_passive` stays false either way, because the accuracy gate fails independently (60.9%, *z* −0.95). The framing predates this refresh — June's `null_pct` was 98.0, also ≥95 — so it is sent for **adjudication** as written rather than softened here.

*Correction, same date:* the June text described feature importance as leaning on "the rate/curve and momentum features". Momentum does lead, but re-reading both payloads' `feat_imp` / `cat_imp`, Rates has been the second-*lowest* category and `curve` the lowest single feature in **both** runs (June: Rates 20.7%, `curve` 6.2%). The description above is corrected to match the data; this is a mis-description at birth, not a change in the data.

## Caveats
- Walk-forward but uses **revised** (not vintage) FRED data, so real-time figures differed slightly; no transaction costs.
- VIX & consumer sentiment proxy the source's proprietary put/call & investor-survey inputs.
- Feature importance is in-sample (interpretation, not a prediction claim).
- Adversarially audited (3-lens workflow) → **12 defects fixed before publishing**, most importantly the original "beats passive" verdict, which was a volatility/time-in-market artifact (cash modeled as 0% and an un-risk-matched Sharpe comparison). See the [[log]].

## Related
[[Trading System - Backtest (June 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[Analyst System — Live Cockpit (June 2026)]] · [[The Global Macros Framework]]
