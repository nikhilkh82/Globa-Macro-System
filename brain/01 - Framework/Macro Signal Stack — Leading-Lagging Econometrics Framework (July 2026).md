---
title: Macro Signal Stack — Leading→Lagging Econometrics Framework
category: framework
type: live-read
data_asof: 2026-09-19
summary: "Point-in-time signal-stack doctrine (z-signals, ADF+KPSS, lead-lag stability, curve logit, 5 regimes) built live from free FRED; the 2026-09-19 read is Goldilocks +0.53 (Aug-2026 data), 8% curve recession probability"
tags: [global-macro, leading-indicators, econometrics, signal-stack, regimes, yield-curve, nfci, cli, point-in-time]
data_vintage: "LIVE through Sep-2026 on the daily/weekly market series (month-to-date means); ISM ends Jul-2026 and Global PMI Jun-2026; INDPRO, permits, CLI, CPI and UNRATE Aug-2026 — latest-vintage FRED, not true PIT vintages"
sources: 1
updated: 2026-09-19
---

# Macro Signal Stack — Leading→Lagging Econometrics Framework

Filed from the VP-level research brief *"Using Time-Series Econometrics on Global Macro Leading Indicators to Forecast Lagging Indicators and Build Cross-Asset Trading Frameworks"* (July 2026). **Implemented live** as the [Macro Signal Stack dashboard](<../../Signal Stack/Macro Signal Stack.html>) (`tools/signal_stack_data.py` → `tools/build_signal_stack.py`, free FRED/DBnomics/workbook data only).

## The framework in one paragraph

The edge is not one model — it is a disciplined, **point-in-time macro signal stack**: leading indicators (PMIs, yield-curve spreads, credit spreads, NFCI-type financial-conditions indexes, global liquidity, OECD CLI) transformed into standardized information states, **diagnosed before trusted** (stationarity via ADF *and* KPSS, cointegration, Granger causality, structural/regime stability), then mapped to asset exposures only with market-implied confirmation (credit, vol, rates, USD) and regime awareness. Signal = z(Δ LeadingIndicator, point-in-time) × expected asset sign. Horizons must match: PMI momentum and credit impulses work at 1–3m; curve, CLI (4–8m documented lead) and credit/leverage at 3–12m. The key constraint is **data integrity**: revised data ≠ what was knowable (Orphanides); backtests on overwritten vintages carry hindsight bias.

## What we implemented (and honest deviations)

| Framework prescription | Our implementation | Honest deviation |
|---|---|---|
| PIT information-state signals | Expanding-window z per month, no lookahead within series, 12 indicator signals | **Latest-vintage FRED, not ALFRED vintages** — historical strips are approximations; live read unaffected. Disclosed on the dashboard |
| Diagnostics before modeling | ADF (H0 unit root) + KPSS (H0 stationary) per signal, MIXED flagged; half-sample lead-lag stability with ⚠ flags | Johansen cointegration & Bai-Perron not implemented (single-series signals; VECM layer not built) |
| NY-Fed curve model | Logit of USREC(t+12) on 10Y−3M, 524 monthly obs (1982-01→2025-08, the last month with a known 12m-ahead NBER outcome), expanding-window OOS scoring | **Honest negative published**: OOS Brier 0.087 vs base-rate 0.065 (−33%) over 2002–2026 (284 expanding-refit 12m-ahead predictions) — the 2022–24 inversion was a multi-year false alarm. Accuracy 89% at the 50% threshold. Current read: **8%** (spread +0.88pp, 2026-09; asof 2026-09-19, unchanged from the 2026-09-16 read — the fit is still 524 obs and the OOS record still 284 predictions at Brier 0.087 vs 0.065) *Superseded 2026-09-11: 535 monthly obs, base-rate 0.066 (−32%), current read 9% at spread +0.71pp (as of Jul-2026).* |
| Regime classification | Rule-based scores on the deck's 5 regimes (Goldilocks/Reflation/Stagflation/Hard landing/Liquidity shock) from growth/inflation-momentum/credit/vol/NFCI composites; 24m dominant-regime strip | Scores, **not probabilities** (no Markov-switching fit); asset priors stated as framework priors, **not backtested** |
| VAR/VECM, Kalman, ML ensemble | The Workbook Explorer's Desk Analyst covers the univariate/ADL layer (ARI, Theta, Holt-Winters, ensembles, ADL Granger-in-forecast with nested held-out evaluation) | ~~Full VAR/VECM/state-space layers not built~~ → **BUILT 2026-07-19** as the [Econometrics Lab](<../../Econometrics Lab/Econometrics Lab.html>) (see below); ML layer remains open |

## Update 2026-07-19 — the multivariate layer is built (Econometrics Lab)

The full research report (`raw/2.8/Framework/Time-Series Econometrics on Global Macro Leading Indicators -- Research Report.docx`, filed 19-Jul-2026) specified the §13 roadmap; the [Econometrics Lab dashboard](<../../Econometrics Lab/Econometrics Lab.html>) (`tools/econlab_data.py` → `tools/build_econlab.py`) now implements it: bivariate **Johansen + Engle-Granger + VECM** on the four named pairs, **Hamilton 2-state Markov-switching** regime probabilities (EM-estimated) on the growth composite, **VAR(2)** of the leading block with Cholesky IRFs/FEVD/stability, **Kalman** local-level r* proxy and INDPRO cycle, and an automated **sup-F break scan**.

**Headline honest results (Jul-2026 vintage, latest-vintage data; post-audit numbers):** all four framework cointegration candidates **FAIL** the joint Johansen+EG test on the full sample — AUD/iron-ore (trace 7.5), USD-CAD/WTI (8.3), gold/inverse-real-yield (11.9, EG ADF +2.11, spread +2.77σ), EUR/10Y-differential (12.8). The sup-F break scan explains why, and the **subsample re-tests recover the one genuine relation: EUR/USD vs the US–DE 10Y differential is COINTEGRATED post-2003** (trace 21.2, EG ADF −3.90; the early synthetic-euro years contaminated the full sample). Gold/real-yield broke at **2022-06** (sup-F 373, the central-bank-buying decoupling) and is not cointegrated in either era once calendar-gap-safe diffs are used; CAD/WTI shows only weak partial evidence post-2015. Per the framework's own rule, correlated-but-not-cointegrated spreads are **not tradeable**. Markov filter: P(low-growth) = 1% now (regime means −0.77z/+0.23z, durations 21m/31m). VAR stable (spectral radius 0.92, Gelfand estimator). Kalman r* proxy +0.32%.

A 9-agent adversarial math review (2026-07-19) confirmed and fixed 6 defects before these numbers were finalized: wrong-scale sup-F critical value (F-form vs Wald-form — now 5.86), power-iteration spectral radius diverging on complex eigenvalue pairs (→ Gelfand estimator), calendar-gap contamination of diffs (gold feed has missing months → adjacency-masked estimators; this moved gold's EG ADF from +0.74 to +2.01), a mislabeled curve→unemployment break regression, a positional chart-payload lookup, and an unflushed open recession band.

## Live read — 2026-09-19 (current)

*Source: `Signal Stack/signal_stack.json` asof 2026-09-19 (rebuilt 14:53), rendered by the dashboard (built 2026-09-19, 14:56). Supersedes the 2026-09-16 read below, which stays as the dated record. Daily and weekly series are monthly means, so the 2026-09 points are month-to-date. INDPRO, CPI, UNRATE, permits and the CLI now run through 2026-08, so the regime engine's latest scored month moves to Aug-2026. ISM still ends 2026-07 (and Global PMI, which is not a regime input, 2026-06), so the Aug growth composite uses only INDPRO YoY and CLI Δ3m.*

- **Regime: Goldilocks, score +0.53** (latest scored month 2026-08; Jul-2026 re-scores unchanged at +0.25) → framework prior: long equities & credit beta — *prior, not advice*. Other scores: Reflation −0.34, Stagflation −0.41, Hard landing −0.45, Liquidity shock −0.66. Most of the jump is mechanical. The credit term (HY OAS z −1.04) enters the engine for the first time in Aug-2026, because FRED's ICE OAS history starts 2023-09 and the engine's 36-month expanding z first returns a value that month (Jul scored the term as zero). It adds about +0.19 to the score. The inflation-momentum term adds about +0.06: the z of the 3-month change in CPI YoY is −0.97 for Aug (−0.57 for Jul), as headline CPI YoY is 3.35% in Aug against 4.17% in May. Lower VIX adds about +0.05 (engine z −0.57 Aug vs −0.32 Jul), and the thinner growth composite (no ISM) takes away about 0.02. The same credit entry explains most of Hard landing's fall to −0.45 (about −0.26 of the −0.30 move; lower VIX adds −0.07 and the weaker growth composite gives back +0.03). The Aug growth inputs are INDPRO YoY z −0.20 and CLI Δ3m z +0.34. Supporting states (signal-table z now): credit tight (HY OAS z −1.04), vol contained (VIX z −0.46), conditions loose (NFCI z −0.56), ISM level z +0.39 (Jul). The 24m strip now prints Jul and Aug 2026 as Goldilocks after Apr–Jun Reflation (2025-10 is still absent because the CPI month was never published)
- **What the engine does not yet see.** Both major central banks tightened in the same week that the energy shock re-intensified. The Fed made its first hike of the cycle, to 3.75–4.00% (effective 2026-09-17), and the ECB raised its deposit rate to 2.50% (effective 2026-09-16), as WTI rose to $107.02 and Brent to $130.80 (15 Sep) with August PPI at +9.85% y/y. The engine's only inflation input is headline CPI momentum (Aug +3.35% y/y, 3m annualised +0.18%). Core CPI is still only +2.45% y/y; its 3-month pace turned up to 1.97% from 1.64% in July (still below 2% and below the 2.45% y/y), and core PCE remains 3.34% (Jul). The Aug Goldilocks score rests about equally on tight credit (+0.19) and the soft CPI-momentum term (+0.19), with low vol adding +0.13 and the thin growth composite +0.02. The CPI-momentum term is the input most exposed to energy pass-through. Read it as the Aug-2026 state, not as a call through the hike. Demand is firm, not fading (retail sales +1.24% m/m and payrolls +162k in Aug, claims 196k in the week of 12 Sep), but the engine's own growth composite is thin: +0.07 in Aug (INDPRO YoY z −0.20, CLI Δ3m z +0.34, no ISM), down from +0.17 in Jul
- **Curve recession probability 8%** (10Y−3M +0.88pp, 2026-09 month-to-date; the daily spread was +0.87 on 18 Sep), unchanged from 8% at +0.88pp on 2026-09-16. The fit is still 524 obs and the OOS caveat is unchanged: Brier 0.087 vs base-rate 0.065, 33% worse over 284 predictions; accuracy 89%. The curve flattened in the week of the hike (10Y−2Y +0.33 on 15 Sep → +0.25 on 18 Sep: a bear-flattening on 16 Sep, 2Y +7bp and 10Y +1bp, then a parallel 7bp rally on hike day, 17 Sep, with 2s10s unchanged), but the 10Y−3M input the model reads, the month-to-date mean, is still +0.88pp at two decimals
- **NFCI −0.56** (2026-09 month-to-date, unchanged; −0.55 at 2026-08) · **HY OAS 2.69%** (2026-09 month-to-date mean, 2.68% at the last read; the daily print was 2.70 on 17 Sep) · **VIX 16.08** (Sep-2026 month-to-date average, up from 15.865; the 15 and 16 Sep prints (17.20, 17.71) lifted the mean, and VIX was back to 15.44 on 17 Sep). Equities and credit absorbed the hike
- Diagnostics unchanged from the 2026-09-16 read: **3 MIXED stationarity verdicts** (10Y−3M level, HY OAS level, NFCI) and **2 fragile lead-lag flags** on 2 signals (Global PMI→UNRATE +18m; HY OAS 3m change→INDPRO +18m). The HY OAS 3m change→UNRATE best lead is +15m (r −0.63) and stays stable. The flagged leads stay untradeable

## Live read — 2026-09-16 (superseded by the 2026-09-19 read above)

*Source: `Signal Stack/signal_stack.json` asof 2026-09-16 (rebuilt 09:21), rendered by the dashboard (built 2026-09-16, 09:53). Supersedes the 2026-09-11 read below, which stays as the dated record. Daily and weekly series are monthly means, so the 2026-09 points are month-to-date; ISM and INDPRO still end 2026-07, so the regime engine's latest scored month is Jul-2026.*

- **Regime: Goldilocks, score +0.25** (latest scored month 2026-07; +0.22 at the last read) → framework prior: long equities & credit beta — *prior, not advice*. Other scores: Hard landing −0.16, Reflation −0.18, Stagflation −0.34, Liquidity shock −0.55. Supporting states: credit tight (HY OAS z −1.07), vol contained (VIX z −0.49), conditions loose (NFCI z −0.56), ISM level z +0.39. The 24m strip still prints Apr–Jun 2026 as Reflation, so Jul-2026 remains the first Goldilocks month since Feb-2026 (the strip is recomputed on latest-vintage data at every build; 2025-10 is absent because the CPI month was never published)
- **Curve recession probability 8%** (10Y−3M +0.88pp, 2026-09 month-to-date), unchanged from 8% at +0.87pp on 2026-09-11. The OOS caveat still holds and is unchanged: Brier 0.087 vs base-rate 0.065, 33% worse over 284 predictions; accuracy 89%
- **NFCI −0.56** (2026-09 month-to-date, looser than average, from −0.55 at 2026-08) · **HY OAS 2.68%** (2026-09, tight; 2.67% at the last read) · **VIX 15.87** (Sep-2026 month-to-date average 15.865, up from 15.235)
- Diagnostics now surface **3 MIXED stationarity verdicts** (10Y−3M level, **HY OAS level — newly MIXED this build**, NFCI) and **2 fragile lead-lag flags** on 2 signals (Global PMI→UNRATE +18m; HY OAS 3m change→INDPRO +18m), against 2 MIXED and 3 flags in the 2026-09-11 read — the HY OAS 3m change→UNRATE lead lost its ⚠ this build. Those leads stay flagged untradeable

## Live read — 2026-09-11 (superseded by the 2026-09-16 read above)

*Source: `Signal Stack/signal_stack.json` asof 2026-09-11, rendered by the dashboard (built 2026-09-10). Supersedes the Jul-2026 read below, which stays as the dated record. Daily and weekly series are monthly means, so the 2026-09 points are month-to-date.*

- **Regime: Goldilocks, score +0.22** (latest scored month 2026-07) → framework prior: long equities & credit beta — *prior, not advice*. Other scores: Hard landing −0.12, Reflation −0.23, Stagflation −0.29, Liquidity shock −0.55. Supporting states: credit tight (HY OAS z −1.09), vol contained (VIX z −0.57), conditions loose (NFCI z −0.56), ISM level z +0.39. In this vintage the 24m strip shows Apr–Jun 2026 as Reflation, so Jul-2026 is the first Goldilocks month since Feb-2026 (the strip is recomputed on latest-vintage data at every build)
- **Curve recession probability 8%** (10Y−3M +0.87pp, 2026-09), down from 9% at +0.71pp. The OOS caveat still holds: Brier 0.087 vs base-rate 0.065, 33% worse over 284 predictions; accuracy 89%
- **NFCI −0.55** (2026-08, looser than average) · **HY OAS 2.67%** (2026-09, tight) · **VIX 15.2** (Sep-2026 month-to-date average 15.235)
- Diagnostics now surface **2 MIXED stationarity verdicts** (10Y−3M level, NFCI) and **3 fragile lead-lag flags** on 2 signals (Global PMI→UNRATE; HY OAS 3m change→INDPRO and →UNRATE), down from 4 and 5 in the Jul-2026 read. Those leads stay flagged untradeable

## Current reads (Jul-2026 vintage)

- **Regime: Goldilocks** (growth composite positive, inflation momentum negative, credit tight-spreads, vol contained) → framework prior: long equities & credit beta — *prior, not advice*
- **Curve recession probability 9%** (10Y−3M +0.71pp) — with the OOS caveat above
- **NFCI −0.54** (looser than average) · **HY OAS 2.71%** (tight) · **VIX 16.7**
- Diagnostics surfaced 4 MIXED stationarity verdicts and 5 fragile lead-lag relationships (sign flips across half-samples) — those leads are flagged untradeable

## Data sources (all free)

FRED: NFCI/ANFCI, T10Y3M, T10Y2Y, ICE BofA HY/IG OAS (provider-limited ~3y history — shallow z, disclosed), VIX, broad USD, WALCL, USREC, INDPRO, UNRATE, CPI, PAYEMS, PERMIT, OECD CLI (USALOLITOAASTSAM; DBnomics fallback wired). Workbooks: ISM, Global PMI. Raw pulls vintage-dated under `Signal Stack/raw/<date>/`, never overwritten.

## Related

[[The Global Macros Framework]] · [[Leading Indicators]] · [[Lagging Indicators]] · [[Endo-Exo Toolkit & Workflow]] · [[Macro Regime - Live (June 2026)]] · [[Bonus Indicators (New Set)]] · the 2026 Workbook Explorer's Desk Analyst (econometric tournaments & ADL leading→lagging engine)
