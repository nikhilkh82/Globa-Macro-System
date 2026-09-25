---
title: Macro Curve-Trade Strategy
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Macrosynergy curve-trade notebook on US FRED 1992–2026: macro composite → DV01-neutral 2s10s flattener — an honest null: Pearson IC 0.076 is crisis-tail-driven; rank IC 0.053 and crisis-excluded IC ≈ 0, sign-hit 50%."
tags: [global-macro, strategy, rates, yield-curve, flattener, macro-signals, quantamental, null-result, backtest]
data_vintage: "LIVE (US FRED 1992-02→2026-09; engine re-run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Macro Curve-Trade Strategy

**Do macro signals predict the yield curve?** A faithful recreation of the Macrosynergy *"Curve trades with macroeconomic signals"* notebook on free US FRED data: a composite of point-in-time macro factors predicting a DV01-weighted 2s10s flattener. Built 2026-06-22.

> **Honest answer: barely, and not tradably.** The apparent edge is crisis-tail-driven; on a rank-correlation / crisis-excluded basis it is indistinguishable from zero. This is a **disciplined null result** — the value is the *regime read*, not a timing signal. Research/education only.

## Provenance — what we adapted
The source is a Macrosynergy quantamental notebook (JPMaQS, paid DataQuery, multi-country panel). As with our other Macrosynergy-notebook recreations, we keep the *methodology* and run it on free data: macro factors → point-in-time z-scores → "conceptual parity" composite → a DV01-weighted curve target → IC + PnL value-checks. US-only (FRED), monthly, 1992→2026.

## How it works
- **Factors (FRED), each oriented so + = flattening pressure, point-in-time expanding-z (≥24m):** excess CPI (YoY − 2%), activity overheating (INDPRO YoY), labour tightness (−UNRATE + payrolls YoY), economic confidence (UMich), real policy rate (FEDFUNDS − CPI YoY), money/QE (−M2 YoY).
- **Signal:** equal-weight mean of available factor z's ("conceptual parity"). High → late-cycle/restrictive → expect **flattening**; low → easing/QE → **steepening**.
- **Target:** **DV01-neutral** 2s10s **flattener** return = `(−A₁₀·Δy10 + A₂·Δy2)/100`, where `A(T,y) = (1−e^{−yT})/y` and **each leg uses its own annuity** (A₁₀ for the 10y, A₂ for the 2y). *Audit-corrected 2026-06-23: the original used A₁₀ on both legs, over-weighting the 2y leg ~4.5× — see [[the-dv01-both-legs-flattener-bug]]. This build was already a null; the fix lowered the IC and the conclusion is unchanged.*
  - **Leg-convention check, 2026-09-24.** `curvemacro_latest.json` does **not** carry a leg-convention flag — it publishes only the realised flattener series (`flat_fwd`) and the `robust`/`pnl` blocks computed from it, so the convention cannot be read off the payload. It was therefore re-checked in the builder that wrote it: `tools/curve_macro.py` computes `A10 = annuity(y10ₚ,10)` and `A2 = annuity(y2ₚ,2)` separately and forms `flat = (−A10·Δy10 + A2·Δy2)/100` — **both legs DV01-weighted, each on its own annuity.** Every curve figure below is on that basis.
- **Strictly causal:** factor z uses only data ≤ t; a **1-month publication lag** means the signal acting at month-end *i* uses macro through *i−1* (CPI/payrolls/IP/M2 for month *i* aren't released until *i+1*); the position earns the *i→i+1* curve move; vol-scaling uses a trailing (expanding) flattener vol.

## Outputs (`Curve Macro/`)
- **`Curve Macro Dashboard.html`** — light theme, Chart.js inlined: naive PnL vs always-flattener, the signal-vs-forward-return scatter, current factor z-scores, and a **robustness / honesty table**.
- **`Curve Macro Note <date>.md`** + **`curvemacro_latest.json`**.
Tools: `tools/curve_macro.py` · `curve_macro_report.py` · `build_curve_macro.py`. Reuses `tools/fred.py`.

## Result — 1992-02 → 2026-09 (n=415 monthly)  *(DV01-neutral, audit-corrected)*
| Check | Value | t-stat | Read |
|---|---|---|---|
| Pearson IC (full sample) | **+0.076** | 1.56 | not significant |
| **Rank (Spearman) IC** | **+0.053** | **1.08** | **≈ 0 — not significant** |
| Pearson IC — excl. 2008-09 | +0.065 | — | not significant |
| Pearson IC — excl. 2008-09 & 2020 | **+0.059** | **1.15** | not significant |
| Pearson IC — excl. 2008-09, 2020 & 2021 | **+0.025** | — | **collapses to ~0** |
| Sign-hit (directional) | 50% | — | coin flip |
| Top-10 months' share of IC | **61%** | — | crisis-concentrated |

*Metrics re-verified 2026-09-24 against `Curve Macro/curvemacro_latest.json` (as_of 2026-09-24, generated 16:14); the 2026-09-08 figures — rank IC 0.052 / t 1.07, top-10 share 62%, always-flattener Sharpe 0.08 — are superseded. The `ex-2008-09` and `ex-3-crises` rows are new to this page (`robust.ic_ex_gfc` = +0.065, `robust.ic_ex_3crises` = +0.025); the always-flattener figure was already carried and now reads `bench_flat.sharpe` = 0.07. The window (1992-02 → 2026-09, n=415) did not move: the last macro-complete month is unchanged. The audit verdicts below are unchanged and still refer to the original adversarial review.*

**Naive PnL Sharpe decays as crises are removed:** full **0.18** → ex-GFC **0.20** → ex-(GFC+2020) **0.17** → ex-(+2021) **0.08**, converging on the static always-flattener benchmark at **0.07** (`bench_flat.sharpe` — the *benchmark* leg, run at the same vol scale, not a variant of the strategy). The strategy is essentially *long the flattener into a few large crisis flattening episodes* — not a broad month-to-month edge. *(The earlier buggy build read IC 0.12 / PnL 0.31; the DV01 fix lowered both — but it was a null then and is a null now.)*

## Verdict
- **Macro identifies the curve *regime* (which macro state favours flatteners vs steepeners), but provides no reliable, tradable monthly curve-timing edge** at single-country scale. The Pearson IC is inflated by crisis tails; the rank IC and crisis-excluded IC are ~0; directional accuracy is ~50%.
- This matches the **source's own framing**: the per-country signal is weak and relies on a **multi-country panel** to reach significance — which we can't replicate on free FRED data (no 2Y curve for most countries). Best used as a regime lens inside a broader process, not a standalone timer.
- Fits the Brain's recurring theme: rigorous out-of-sample / robustness testing dissolves an IC that looked tradable. Honest disclosure beats a dressed-up backtest. See [[ML Macro-Direction Model]], [[LangAlpha Strategy System]] for the same lesson.
- **2026-06-23:** this build shared the DV01-both-legs flattener bug found in [[Macro Demand-Based Rates System]] and [[Treasury Macro-Trend System]]; rebuilt DV01-neutral. Because it was already a null, the **conclusion is unchanged** (the IC merely eased from 0.12 to 0.076). See [[the-dv01-both-legs-flattener-bug]].

## Caveats
- US-only; the source uses a multi-country JPMaQS panel (breadth is where the significance comes from).
- The flattener target is the **curve-move / price** component — excludes carry/roll (disclosed).
- Revised (not vintage) FRED data; 1-month lag approximates true release lags; `excess_cpi` and `real_rate` both use CPI (mild collinearity in the equal-weight composite).
- Adversarially audited (2-lens workflow): the audit's load-bearing diagnostics (rank IC 0.06, ex-2-crises IC 0.084, top-10 = 63%) were reproduced and are now reported in-product; the framing was corrected from "modest predictive power" to this honest null.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[Treasury Macro-Trend System]] · [[Macro Demand-Based Rates System]] · [[Managed-Futures Trend System]] · [[ML Macro-Direction Model]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
