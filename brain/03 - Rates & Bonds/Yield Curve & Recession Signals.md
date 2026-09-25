---
title: Yield Curve & Recession Signals
category: rates
type: domain
data_asof: 2026-07-25
summary: "Curve slope (10yr-3mo, 10yr-2yr) as a recession predictor and its lead/lag with the S&P 500; live 10Y−3M +0.71pp (2026-07-25), and the desk’s OOS logit scores 32% worse than the base rate."
tags: [global-macro, yield-curve, recession, inversion, 10yr-3mo, leading-indicator]
data_vintage: "2000–2017 (10yr-3mo & S&P history to 2014; curve data to 2015)"
sources: 2
updated: 2026-07-25
---

# Yield Curve & Recession Signals

**What it is & why it matters** — The slope of the government bond curve — long-yield minus short-yield — is a well-documented predictor of recessions, albeit with uncertain forecasting times (and, on the desk's own out-of-sample test, materially worse-calibrated than its reputation — see Live counterparts below). Per the Global Macros bond methodology, the expectations hypothesis says today's curve embeds the market's view of future short rates and inflation: a *normal* upward slope implies expansionary policy and rising future rates, while an *inverted* curve (short > long) reveals the opposite and is "a well-documented predictor of recessions, albeit with uncertain forecasting times." This page tracks the two canonical spreads — **10yr-3mo** and **10yr-2yr** — and their lead/lag relationship with the S&P 500. It builds directly on the curves in [[Government Bond Yields]].

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `us_yield_curve_2017.xlsx` — *Yield Curve Analysis* | Full daily UST tenor matrix (1mo→30yr) used to compute the curve shape | **2000-01-03 → 2015-12-21** (~4,000 daily) | 2 line charts: full curve (%Yield) and multi-tenor overlay |
| `us_yield_curve_2017.xlsx` — *10yr-3mo vs S&P500* | The 10yr-3mo slope plotted against the S&P 500 (and JNK) | **2000-01-03 → 2014-12-08** (~3,900 daily) | 2 line charts overlaying slope vs S&P500 |
| `us_yield_curve_2017.xlsx` — *Summary Tables* | Curve + bond-ETF 1wk/1mo/6mo change snapshot; recent tenor table | Snapshot dated **2017-11-17**; tenor table 2014 | — |
| `us_yield_curve_2017.xlsx` — *US Fixed Income ETFs* | Treasury/credit ETF prices (SHY, IEI, IEF, TLH, TLT, LQD, HYG, JNK, TIP) | 2000-01 → **2014-12-08** weekly | "US Treasury ETFs" |

## Charts & key trends
**10yr-3mo slope, 2000 → Dec 2014** (the headline recession signal):
- Range **-0.95 to +3.85 percentage points**, mean **+1.95pp** — i.e. the curve was upward-sloping (positive) most of the period.
- The **minimum of -0.95pp** marks the deep **2006–2007 inversion** that preceded the Global Financial Crisis — the textbook "inverted curve → recession" episode.
- By the end of the series (late 2014) the slope sat richly positive at **~+2.2pp** (recent readings 2.19 → 2.29 → 2.23), consistent with a mid-expansion, zero-bound front end and a steep curve.
- **Mechanism**: an inversion appears when the short end (3mo) is dragged up by tight monetary policy while the long end (10yr) reflects weaker future growth/inflation. The curve then re-steepens *after* the recession begins as the central bank cuts.

**S&P 500 alongside the slope (to Dec 2014)** — S&P range in the overlay **683.4 (2009 GFC trough) → 2,075**, mean ~1,280. The pairing is the core teaching point: the curve inverted in 2006–07 *ahead* of the 2008 equity collapse, then the post-crisis re-steepening accompanied the long bull market. The JNK high-yield ETF series (range **15.99 → 40.61**) is overlaid as a credit/risk-appetite cross-check — high-yield prices crater into recessions as the curve inverts.

**Curve levels over the cycle (Yield Curve Analysis, 2000→2015)** — The whole curve collapsed across the period: 3mo from **~5.45%** (2000) to **~0.21%** (2015); 10yr from **~6.97%** to **~2.62%**; 30yr from **~6.71%** to **~2.90%**. The min on the 3mo column reaches **-0.013%** (the brief 2015 negative-bill print). This is the secular fall in rates that flattened the achievable slope over time.

**10yr-2yr (the alternative slope)** — The methodology PDF flags the **2yr-10yr** spread as the other standard slope definition; on the 2021 snapshot in [[Government Bond Yields]] it was a healthy ~**+0.81pp** (10yr 0.93% − 2yr 0.12%) — steep and non-recessionary, in keeping with the easy-policy regime of that vintage.

## How it's used in the strategy
- **Regime classification**: A positive/steepening curve = "risk-on / expansion" lean (favour cyclicals, credit, equities); a flattening-toward-inversion curve = de-risk, raise the recession probability in [[Macro Regime Snapshot]].
- **Equity timing overlay**: Because the inversion *leads* equity peaks (often by 6–18 months, with the "uncertain forecasting time" the PDF warns about), the slope is used as a slow, strategic warning rather than a precise entry/exit — pairs with [[Bull & Bear Markets]] and [[VIX & Implied Volatility]].
- **Credit confirmation**: Inversions that coincide with widening high-yield spreads / falling JNK-HYG are treated as higher-conviction recession signals — see [[Corporate Bond Yields & Credit]].
- **Cross-asset**: Slope feeds the rate-differential and growth-expectation legs used in [[FX Endogenous-Exogenous Framework]] and complements the [[Leading Indicators]] / [[Coincident Indicators]] work and [[Yield Curve & Recession Signals]]-adjacent [[GDP & Growth]] tracking.

**Live counterparts:** [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] runs this signal live — 10Y−3M **+0.71pp** (asof 2026-07-25) with an NY-Fed-style logit putting the 12-month recession probability at **9%**. That model is published **with its honest negative**: over 282 expanding-window out-of-sample predictions (2002–2026) its Brier score was **0.087 vs a 0.066 base rate — 32% WORSE than simply predicting the base rate**, because the 2022–24 inversion was a multi-year false alarm. [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] adds the structural-break evidence: the curve→Δunemployment relation itself **breaks at 2011-06** (sup-F 12.0). Treat the slope as one input among several, sized accordingly — not as a calibrated probability.

## See also
- [[Government Bond Yields]]
- [[Corporate Bond Yields & Credit]]
- [[Leading Indicators]]
- [[GDP & Growth]]
- [[Bull & Bear Markets]]
- [[VIX & Implied Volatility]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Glossary]]
