---
title: Credit ML Classification System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Macro-factor ML ensemble (NB/Logistic/KNN/RF majority vote) timing US HY credit 2012–2026 — a clean ML null: 61% accuracy ≈ the 65% long-credit base rate; long-flat ML (0.56) only ties buy-and-hold (0.60)."
tags: [global-macro, strategy, credit, high-yield, machine-learning, ensemble, base-rate, null-result, backtest]
data_vintage: "LIVE (HYG/IEF + FRED macro, 2012-05→2026-08; engine re-run 2026-09-24, figures unchanged)"
sources: 1
updated: 2026-09-24
---

# Classifying Credit Markets with Macro Factors

A free-data port of the Macrosynergy **"Classifying credit markets with macro factors"** notebook: use macro factors to classify the next-month direction of US high-yield credit, via an **ensemble of scikit-learn classifiers** (Gaussian Naive Bayes, Logistic Regression, KNN, Random Forest) combined by **majority vote**. Built 2026-06-23.

> **A clean ML null with a base-rate lesson:** the macro-ML adds no directional edge over simply holding credit — and only the *short leg* (forfeiting the carry) actively loses. Research/education only.

## Provenance — what we adapted
The source builds per-country credit factors and runs pooled-panel ML classifiers (NB / LR / KNN / RF) with majority voting for a global credit signal (paid JPMaQS). We rebuilt the core on **free US data** as a time-series classifier: the same 4-model ensemble + majority vote, on a duration-hedged HY-credit target and 6 free macro factors.

## How it works
- **Target:** duration-hedged HY credit excess return = **HYG total return − 0.45×IEF** (HY minus a duration-matched Treasury, isolating the credit/spread component). Going long = long credit risk.
- **6 macro factors (FRED, point-in-time expanding-z, lagged 1m, + = credit-supportive):** business sentiment (UMich), house-price trend (Case-Shiller YoY), real rate (−(10y − CPI YoY)), bank-lending tightening (−SLOOS `DRTSCILM`), private credit growth (C&I loans YoY), credit-spread widening (−Baa-spread 3m change).
- **ML ensemble:** GaussianNB + LogisticRegression + KNN(7) + RandomForest(120, depth 4), each in a StandardScaler pipeline, **trained walk-forward** on the expanding history of (factors → sign of next-month credit), majority vote (≥2 of 4 = long). Compared as long/short and **long-flat** (never short). Vol-targeted 8%.

## Outputs (`Credit ML/`)
- **`Credit ML Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (buy & hold vs ML long-flat vs ML long/short vs simple-macro), a performance table, and the current macro-factor reads.
- **`Credit ML Note <date>.md`** + **`creditml_latest.json`**.
Tools: `tools/credit_ml.py` · `credit_ml_report.py` · `build_credit_ml.py`.

## Result — 2012-05 → 2026-08 (n=171, vol-target 8%)
| Strategy | Sharpe | CAGR | Realised vol | MaxDD |
|---|---|---|---|---|
| ML ensemble — long/short | 0.28 | 2.29% | 9.9% | −39.0% |
| ML ensemble — long-flat (never short) | 0.56 | 5.06% | 9.7% | −32.4% |
| Simple macro composite | −0.21 | −2.56% | 9.9% | −55.4% |
| **Buy & hold HY credit** | **0.60** | **3.89%** | 6.8% | **−15.8%** |

*Why realised vol sits above the 8% heading: the target is applied **causally, through a trailing estimate** — `tools/credit_ml.py` sizes each month at `sc = min(3.0, (TARGET_VOL/sqrt(12))/sd)` with `TARGET_VOL = 0.08` and `sd` the std of the **last 12 months** of realised strategy returns — so a trailing, 3×-capped scaler only catches rising vol with a lag, and the three signal books land at 9.7–9.9%. Buy & hold is the unscaled benchmark (never vol-targeted), hence 6.8%.*

*Re-verified 2026-09-24 against `Credit ML/creditml_latest.json` (as_of 2026-09-24, generated 16:13): the 2026-09-24 re-run reproduced the 2026-09-08 figures **exactly** — same window (2012-05 → 2026-08), same n=171, same Sharpes — because the panel is monthly and August is still the last complete month. CAGR and realised vol are new columns on this page (`perf_*.cagr` / `perf_*.vol`); the remaining MaxDDs, previously left blank, are now read from the payload. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Directional accuracy 61% — statistically *indistinguishable* from the 65% long-credit base rate** (one-sided binomial p 0.851; the ~4pt gap is ≈1.1 SE on n=171). No timing skill over the fact that credit excess returns are positive most months (the risk premium).
- **The long/short book badly trails buy-and-hold (0.28 vs 0.60) — but that's the short leg, not the signal.** A **long-flat** version (never short) earns **0.56 — essentially a tie** with buy-and-hold. Shorting credit against a 65%-positive base rate forfeits the carry; the macro signal itself neither helps nor (kept long-only) hurts.
- **And that tie is a tie on Sharpe only — the path is much worse.** Long-flat ML does out-earn buy & hold on raw CAGR (5.06% vs 3.89%), but only by running more risk: 9.7% realised vol against buy & hold's 6.8%, which is exactly why its Sharpe (0.56) merely *ties* 0.60 — and it pays for that with a −32.4% drawdown versus −15.8%. Risk-scaled, the extra leverage is given straight back.

## Verdict
- **The macro-ML adds no directional timing edge over simply being long credit.** Credit's positive risk premium means the bar is *being long* (buy & hold Sharpe 0.60); the ensemble's accuracy is indistinguishable from that base rate, and a long-flat ML just ties it. Only the short leg (which gives up carry) actively loses.
- Consistent with the Brain's recurring lesson ([[ML Macro-Direction Model]], [[FX Signals System (Common Sense vs ML)]]): on a noisy single market with a high base rate, ML classifiers don't beat the passive premium. The macro factors are a useful **risk read** (the current environment), not a directional edge.

## Audit
Adversarially audited (2-lens: ML hygiene + base-rate honesty) → **no look-ahead** (training strictly on history before t, scaler fit inside the walk-forward, factors lagged, RF seed fixed — all verified). 2 LOW framing fixes, both applied: (1) added a **long-flat ML variant** — the fair "does macro improve on *being long*" test — which revealed the long/short underperformance was the *short-leg packaging* (long-flat ≈ ties buy-and-hold), not a negative signal; (2) corrected "accuracy *below* base rate" to **"indistinguishable from"** (60% vs 62% is ≈0.5 SE; the one-sided test only shows it isn't *above*). The core null held; the framing is now precise.

## Caveats
- Duration hedge (0.45) is an approximation (imperfect); US HY only; vol-targeted 8%; revised (not vintage) FRED data; SLOOS forward-filled from quarterly; 1-month macro lag. **Free-data note:** the SLOOS lending survey (`DRTSCILM`) is quarterly; HY OAS (`BAMLH0A0HYM2`) truncates so the Baa spread (`BAA10Y`) is used for the credit factor.

## Related
[[ML Macro-Direction Model]] · [[FX Signals System (Common Sense vs ML)]] · [[Macro Curve-Trade Strategy]] · [[Macro-Aware Risk Parity System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
