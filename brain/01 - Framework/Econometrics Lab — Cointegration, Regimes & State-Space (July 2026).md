---
title: Econometrics Lab — Cointegration, Regimes & State-Space
category: framework
type: live-read
data_asof: 2026-09-19
summary: "Multivariate layer (Johansen/VECM, Markov-switching, VAR, Kalman, sup-F): at the 2026-09-19 build all four pairs still FAIL cointegration on the full sample; only EUR/USD vs US−DE 10Y post-2003 passes both tests"
tags: [global-macro, econometrics, cointegration, johansen, vecm, markov-switching, var, kalman, structural-breaks, honest-negative]
data_vintage: "LIVE through Sep-2026 (in-progress month) on the market pairs (WTI/CAD, gold), Aug-2026 on EUR/US−DE and Jul-2026 on AUD–iron ore (workbook-27 cap); INDPRO cycle and r* proxy end Aug-2026; growth composite and VAR end Jul-2026 (ISM-capped) — latest-vintage FRED/Yahoo, not ALFRED PIT vintages"
sources: 1
updated: 2026-09-19
---

# Econometrics Lab — Cointegration, Regimes & State-Space

The **multivariate layer** of the desk's signal pipeline, built 2026-07-19 from the §13 roadmap of the research report *"Time-Series Econometrics on Global Macro Leading Indicators"* (`raw/2. Macro Indicators/2.8 …/Framework/`). Live dashboard: [Econometrics Lab](<../../Econometrics Lab/Econometrics Lab.html>) · builders `tools/econlab_data.py` → `tools/build_econlab.py` · on the hourly auto-refresh chain since 2026-07-25.

Where [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] handles **univariate** point-in-time signals and the Explorer's Desk Analyst handles **forecast tournaments and ADL lead-lag**, this page covers what neither could: relationships *between* non-stationary series, regime probabilities, latent states, and dated parameter breaks.

## What it computes (all hand-rolled — no third-party numerics)

| Technique | Question it answers | Implementation |
|---|---|---|
| **Johansen trace + Engle-Granger + VECM** | Are these two non-stationary series *cointegrated* — i.e. is the spread tradeable? | Bivariate trace test (analytic 2×2 eigenvalues), EG residual-ADF cross-check, error-correction speed α with t-stat and half-life. **Both tests must reject** for a COINTEGRATED verdict |
| **Hamilton 2-state Markov switching** | Which regime are we in, *with what probability*? | EM: forward filter + Kim smoother, means and variances switch, on the growth composite (ISM, INDPRO YoY, CLI Δ3m expanding-z) |
| **VAR(2) + IRF + FEVD** | Joint dynamics of the leading block; what shock drives what? | Per-equation OLS, Cholesky orthogonalisation, MA recursion, variance decomposition, companion-matrix stability |
| **Kalman local-level filters** | What is the latent state under the noise? | Neutral-real-rate **proxy** (trend of Fed funds − CPI YoY) and the INDPRO cycle — end-of-sample-safe, unlike two-sided filters |
| **Andrews sup-F break scan** | Did this relationship break, and *when*? | Single-unknown-break scan, 15% trimming, F-form statistic vs the 5% critical value **5.86** |

## Live read — 2026-09-19 (current)

*Source: `Econometrics Lab/econlab.json` **asof 2026-09-19** (file rebuilt 2026-09-19 14:53) → dashboard **built 2026-09-19** (14:56); the regime / VAR / INDPRO-cycle blocks read `Signal Stack/signal_stack.json` (also rebuilt 2026-09-19 14:53); the r* proxy pairs `econlab.json`'s Fed funds with the Signal Stack CPI. Supersedes the 2026-09-16 read below, which stays as the dated record. Pair samples are the same length as last build: they end 2026-09 (USD/CAD–WTI, gold — the in-progress month: WTI and the 10Y real yield as month-to-date averages, gold as the latest close), 2026-08 (EUR/USD–US−DE, capped by the OECD German 10Y) and 2026-07 (AUD–iron ore, capped by the workbook-27 iron-ore series). In the Signal Stack feed INDPRO now runs to 2026-08, but the growth composite still ends 2026-07 because the ISM series has no August month yet; the real-rate input ends 2026-08.*

**Verdicts unchanged — all four framework pairs still FAIL cointegration on the full sample** (Johansen trace 5% crit 15.49 / 3.84; EG residual-ADF 5% crit −3.34; both tests must reject for COINTEGRATED):

| Pair · sample | Johansen trace r=0 / r≤1 | EG residual ADF | Spread now | Verdict | Change vs 2026-09-16 |
|---|---|---|---|---|---|
| AUD/USD vs iron ore (logs) · 1992-01→2026-07, n=415 | 7.5 / 1.1 | −2.21 | −0.91σ | NOT cointegrated | unchanged (no new iron-ore month) |
| USD/CAD vs WTI (logs) · 1986-01→2026-09, n=489 | 7.6 / 2.3 | −1.29 | +1.70σ | NOT cointegrated | trace 7.7 / 2.4 → 7.6 / 2.3; EG ADF −1.31 → −1.29; spread +1.66σ → +1.70σ |
| Gold (log) vs inverse 10Y real yield · 2003-01→2026-09, n=244 | 14.0 / 3.3 | **+2.53** | **+2.83σ** | NOT cointegrated (stretched, but no equilibrium to revert to) | trace 13.4 / 3.1 → 14.0 / 3.3; EG ADF +2.42 → +2.53; spread +2.80σ → +2.83σ |
| EUR/USD (log) vs US−DE 10Y differential · 1999-01→2026-08, n=332 | 12.8 / 4.9 | −1.95 | +0.06σ | NOT cointegrated on the full sample | unchanged (German 10Y still ends 2026-08) |

**What moved, and why:** only the two pairs with an in-progress September month changed. The September WTI average (daily prints through 15 Sep, when WTI closed at $107.02) is now $97.46, against $83.90 for August (`econlab.json`), while USD/CAD's September average is unchanged since the last build (1.38, H.10 still ends 11 Sep; 1.39 in August), when the relation expects higher oil to strengthen CAD, so the USD/CAD–WTI spread widened. The September 10Y real-yield average (through 17 Sep, when the 10Y TIPS was +2.61%) is 2.52%, against 2.40% for August, while gold's September close ($4,424.90, `econlab.json`) is only 1.3% below August's ($4,481.50), a smaller fall than the higher real yield implies, so the gold spread widened. Neither widening is a trade signal: both pairs are still NOT cointegrated.

**Subsample re-tests at each pair's levels-relation break** (short windows, low power — indicative, not green lights):

- **EUR/USD vs US−DE 10Y — still the one COINTEGRATED relation:** break 2003-05 (sup-F 367); post-break (n=280) trace **21.4**, EG ADF **−3.93**, both rejecting. Pre-break (n=52) not cointegrated. Every figure is unchanged, because no new month entered this pair.
- **USD/CAD vs WTI — post-break only "weak/partial":** break 2015-06 (sup-F **158**, prior 159); post-break (n=136) trace **20.8** (prior 21.1) rejects, but EG ADF −2.50 (unchanged) does not clear −3.34. The both-tests rule is still not met, so this is *not* a COINTEGRATED verdict. Pre-break (n=353): trace 7.0, EG ADF −1.67, unchanged.
- **AUD/USD vs iron ore:** break 2015-02 (sup-F 207); neither side cointegrated — pre-break (n=277) trace 9.4 / EG −2.66, post-break (n=138) trace 14.9 / EG −2.50. Every figure unchanged.
- **Gold vs inverse real yield:** break 2022-06 (sup-F **409**, prior 408); pre-break (n=199) trace 9.5 / EG −1.88, not cointegrated; the post-break window is under 48 months, too short to test. The full-sample trace rose back toward 15.49 without crossing it (13.4 → 14.0), and the EG ADF moved further *positive* (+2.42 → +2.53). As in the 2026-09-11 build, the two tests are moving apart; the verdict is unchanged. *Superseded 2026-09-19: the "(now 2.11 after refresh)" gold EG ADF quoted in the 2026-07-19 review section below is now **+2.53**; the 2026-09-16 section's +2.42 is the prior build.*

**Break scan** (sup-F, F-form, 5% crit 5.86) — all four lead-lag relations still BREAK, at unchanged dates:

- inverse real yield → log gold (0m): **408.5 @ 2022-06** (n=244; prior 408.0)
- ISM level → INDPRO YoY (+3m): 84.7 @ 2003-08 (n=788; prior 84.5, n=787 — the August INDPRO month adds one observation)
- CLI Δ3m → INDPRO YoY (+6m): 67.4 @ 2000-07 (n=788; prior 67.1, n=787)
- Curve 10Y−3M → ΔUNRATE next 12m: 12.0 @ 2011-06 (n=523; unchanged)

**Regime, dynamics, latent states:** Markov **P(low-growth) = 1%** (smoothed 0.007 at the 2026-07 end-point). This is unchanged because the composite did not extend; regime means −0.77z / +0.23z, expected durations 21m / 31m and persistence 0.95 / 0.97 are also unchanged. VAR(2) on the leading block **stable** (535 obs, companion spectral radius 0.924, both unchanged); in the 12m FEVD, NFCI shocks still explain 14% of ISM Δ3m and 24% of CLI Δ3m variance. Kalman **r\* proxy +0.31%** vs realized real rate **+0.28%** (2026-08, both unchanged); INDPRO cycle **+1.2%** above its Kalman trend, now read at 2026-08 (prior +1.3% at 2026-07).

**Policy context (not yet in the model):** the Fed made its first hike of the cycle, 25bp to 3.75–4.00% effective 2026-09-17 (EFFR 3.88% on 17 Sep), and the ECB raised its deposit rate to 2.50% effective 2026-09-16. The Kalman real rate does not include the Fed hike yet, because its input ends 2026-08 (August Fed funds 3.63% less CPI +3.35% y/y) until September CPI is published. The Markov composite also predates the hike. A 1% low-growth probability matches the firm demand data (August payrolls +162k, retail sales +1.24% m/m, claims 196k in the week of 12 Sep).

**Net:** no headline conclusion changes. Every full-sample verdict is still NOT cointegrated, and EUR/USD vs US−DE 10Y post-2003 is still the only relation passing both tests (figures identical). The gold spread is slightly more stretched (+2.83σ) and still has no equilibrium behind it; USD/CAD vs WTI is wider (+1.70σ) but just as untradeable.

## Live read — 2026-09-16 (superseded by the 2026-09-19 read above)

*Source: `Econometrics Lab/econlab.json` **asof 2026-09-16** (file rebuilt 2026-09-16 09:21) → dashboard **built 2026-09-16** (09:53). Supersedes the 2026-09-11 read below, which stays as the dated record. Pair samples now end 2026-09 (USD/CAD–WTI, gold), 2026-08 (EUR/USD–US−DE, where the OECD German 10Y now runs two months further than at the last read) and 2026-07 (AUD–iron ore, capped by the workbook-27 iron-ore series); the regime / VAR / Kalman blocks read the Signal Stack feed, whose growth composite now ends 2026-07 and whose real-rate input ends 2026-08.*

**Verdicts unchanged — all four framework pairs still FAIL cointegration on the full sample** (Johansen trace 5% crit 15.49 / 3.84; EG residual-ADF 5% crit −3.34; both tests must reject for COINTEGRATED):

| Pair · sample | Johansen trace r=0 / r≤1 | EG residual ADF | Spread now | Verdict | Change vs 2026-09-11 |
|---|---|---|---|---|---|
| AUD/USD vs iron ore (logs) · 1992-01→2026-07, n=415 | 7.5 / 1.1 | −2.21 | −0.91σ | NOT cointegrated | unchanged |
| USD/CAD vs WTI (logs) · 1986-01→2026-09, n=489 | 7.7 / 2.4 | −1.31 | +1.66σ | NOT cointegrated | trace 7.8 → 7.7; EG ADF −1.32 → −1.31; spread +1.65σ → +1.66σ |
| Gold (log) vs inverse 10Y real yield · 2003-01→2026-09, n=244 | 13.4 / 3.1 | **+2.42** | **+2.80σ** | NOT cointegrated (stretched, but no equilibrium to revert to) | trace 13.8 → 13.4; EG ADF +2.48 → +2.42; spread +2.82σ → +2.80σ |
| EUR/USD (log) vs US−DE 10Y differential · 1999-01→2026-08, n=332 | 12.8 / 4.9 | −1.95 | +0.06σ | NOT cointegrated on the full sample | sample +2m (n=330 → 332); trace r≤1 5.0 → 4.9; spread +0.01σ → +0.06σ |

**Subsample re-tests at each pair's levels-relation break** (short windows, low power — indicative, not green lights):

- **EUR/USD vs US−DE 10Y — still the one COINTEGRATED relation:** break 2003-05 (sup-F **367**, prior 365); post-break (n=280, prior 278) trace **21.4** (prior 21.2), EG ADF **−3.93** (prior −3.90), both rejecting. Pre-break (n=52) not cointegrated. The two extra months of German 10Y data moved the estimates without touching the verdict.
- **USD/CAD vs WTI — post-break only "weak/partial":** break 2015-06 (sup-F 159, unchanged); post-break (n=136) trace **21.1** (prior 21.2) rejects but EG ADF −2.50 (prior −2.49) does not clear −3.34, so the both-tests rule is still not met and this is *not* a COINTEGRATED verdict. Pre-break (n=353): trace 7.0, EG ADF −1.67 — unchanged.
- **AUD/USD vs iron ore:** break 2015-02 (sup-F 207); neither side cointegrated — pre-break (n=277) trace 9.4 / EG −2.66, post-break (n=138) trace 14.9 / EG −2.50. Every figure unchanged; the iron-ore leg has no new month.
- **Gold vs inverse real yield:** break 2022-06 (sup-F 408); pre-break (n=199) trace 9.5 / EG −1.88, not cointegrated; post-break window <48m, too short to test. This build the full-sample trace eased back (13.8 → 13.4) and the EG ADF eased with it (+2.48 → +2.42) — still far above the −3.34 rejection region, so the two tests remain apart and the verdict is unchanged. *Superseded 2026-09-16: the "(now 2.11 after refresh)" gold EG ADF quoted in the 2026-07-19 review section below is now **+2.42**; the 2026-09-11 section's +2.48 is the prior build.*

**Break scan** (sup-F, F-form, 5% crit 5.86) — all four lead-lag relations still BREAK, at unchanged dates:

- inverse real yield → log gold (0m): **408.0 @ 2022-06** (n=244; prior 407.6)
- ISM level → INDPRO YoY (+3m): 84.5 @ 2003-08 (n=787; unchanged)
- CLI Δ3m → INDPRO YoY (+6m): 67.1 @ 2000-07 (n=787; prior 67.3)
- Curve 10Y−3M → ΔUNRATE next 12m: 12.0 @ 2011-06 (n=523; unchanged)

**Regime, dynamics, latent states:** Markov **P(low-growth) = 1%** (smoothed 0.007 at the 2026-07 end-point, against 0.012 at the 2026-06 end-point last build; regime means −0.77z / +0.23z; expected durations 21m / 31m, persistence 0.95 / 0.97 — all unchanged). VAR(2) on the leading block **stable** (**535 obs**, prior 534; companion spectral radius 0.924, unchanged); in the 12m FEVD, NFCI shocks still explain 14% of ISM Δ3m and 24% of CLI Δ3m variance. Kalman **r\* proxy +0.31%** (prior +0.32%) vs realized real rate **+0.28%** (prior +0.32%), now read at 2026-08; INDPRO cycle **+1.3%** above its Kalman trend (2026-07, unchanged).

**Net:** no headline conclusion changes — every full-sample verdict is still NOT cointegrated, EUR/USD vs US−DE 10Y post-2003 remains the only relation passing both tests (and passes it slightly more clearly on the longer sample), and the gold spread stays stretched (+2.80σ) with still no equilibrium behind it.

## Live read — 2026-09-11 (superseded by the 2026-09-16 read above)

*Source: `Econometrics Lab/econlab.json` **asof 2026-09-11** (file rebuilt 2026-09-10 13:11) → dashboard **built 2026-09-10**. Supersedes the 2026-07-25 headline read below, which stays as the dated record. Pair samples now end 2026-09 (USD/CAD–WTI, gold), 2026-07 (AUD–iron ore) and 2026-06 (EUR/USD–US−DE, capped by the OECD German 10Y); the regime / VAR / Kalman blocks read the Signal Stack feed, whose growth composite ends 2026-06.*

**Verdicts unchanged — all four framework pairs still FAIL cointegration on the full sample** (Johansen trace 5% crit 15.49 / 3.84; EG residual-ADF 5% crit −3.34; both tests must reject for COINTEGRATED):

| Pair · sample | Johansen trace r=0 / r≤1 | EG residual ADF | Spread now | Verdict | Change vs 2026-07-25 |
|---|---|---|---|---|---|
| AUD/USD vs iron ore (logs) · 1992-01→2026-07, n=415 | 7.5 / 1.1 | −2.21 | −0.91σ | NOT cointegrated | EG ADF −2.24 → −2.21 |
| USD/CAD vs WTI (logs) · 1986-01→2026-09, n=489 | 7.8 / 2.4 | −1.32 | +1.65σ | NOT cointegrated | trace 8.3 → 7.8 |
| Gold (log) vs inverse 10Y real yield · 2003-01→2026-09, n=244 | 13.8 / 3.0 | **+2.48** | **+2.82σ** | NOT cointegrated (stretched, but no equilibrium to revert to) | trace 11.9 → 13.8; EG ADF +2.11 → +2.48; spread +2.77σ → +2.82σ |
| EUR/USD (log) vs US−DE 10Y differential · 1999-01→2026-06, n=330 | 12.8 / 5.0 | −1.95 | +0.01σ | NOT cointegrated on the full sample | unchanged |

**Subsample re-tests at each pair's levels-relation break** (short windows, low power — indicative, not green lights):

- **EUR/USD vs US−DE 10Y — still the one COINTEGRATED relation:** break 2003-05 (sup-F 365); post-break (n=278) trace **21.2**, EG ADF **−3.90**, both rejecting — unchanged. Pre-break (n=52) not cointegrated.
- **USD/CAD vs WTI — post-break only "weak/partial":** break 2015-06 (sup-F 159); post-break (n=136) trace 21.2 rejects but EG ADF −2.49 does not clear −3.34, so the both-tests rule is not met and this is *not* a COINTEGRATED verdict. Pre-break (n=353): trace 7.0, EG ADF −1.67.
- **AUD/USD vs iron ore:** break 2015-02 (sup-F 207); neither side cointegrated — pre-break (n=277) trace 9.4 / EG −2.66, post-break (n=138) trace 14.9 / EG −2.50.
- **Gold vs inverse real yield:** break 2022-06 (sup-F 408); pre-break (n=199) trace 9.5 / EG −1.88, not cointegrated; post-break window <48m, too short to test. The full-sample trace drifted up toward (not through) 15.49 while the EG ADF drifted further *positive* — the two tests are moving apart; verdict unchanged. *Superseded 2026-09-11: the "(now 2.11 after refresh)" gold EG ADF quoted in the 2026-07-19 review section below is now +2.48.*

**Break scan** (sup-F, F-form, 5% crit 5.86) — all four lead-lag relations still BREAK, at unchanged dates:

- inverse real yield → log gold (0m): **407.6 @ 2022-06** (n=244; prior 373.2)
- ISM level → INDPRO YoY (+3m): 84.5 @ 2003-08 (n=787; unchanged)
- CLI Δ3m → INDPRO YoY (+6m): 67.3 @ 2000-07 (n=787; prior 67.1)
- Curve 10Y−3M → ΔUNRATE next 12m: 12.0 @ 2011-06 (n=523; unchanged)

**Regime, dynamics, latent states — unchanged:** Markov **P(low-growth) = 1%** (smoothed 0.012 at the 2026-06 end-point; regime means −0.77z / +0.23z; expected durations 21m / 31m, persistence 0.95 / 0.97). VAR(2) on the leading block **stable** (534 obs, companion spectral radius 0.924); in the 12m FEVD, NFCI shocks explain 14% of ISM Δ3m and 24% of CLI Δ3m variance. Kalman **r\* proxy +0.32%** vs realized real rate +0.32% (2026-07); INDPRO cycle **+1.3%** above its Kalman trend (2026-07).

**Net:** no headline conclusion changes — every full-sample verdict is still NOT cointegrated, EUR/USD vs US−DE 10Y post-2003 remains the only relation passing both tests, and the gold spread is more stretched (+2.82σ) with still no equilibrium behind it.

## Headline results (asof 2026-07-25 — honest negatives included)

**All four framework cointegration candidates FAIL on the full sample.** Per the framework's own rule, correlated-but-not-cointegrated spreads are **not tradeable**, whatever the narrative:

| Pair | Johansen trace (r=0) | EG residual ADF | Verdict |
|---|---|---|---|
| AUD/USD vs iron ore (logs) | 7.5 | −2.24 | NOT cointegrated |
| USD/CAD vs WTI (logs) | 8.3 | −1.32 | NOT cointegrated |
| Gold vs inverse 10Y real yield | 11.9 | **+2.11** | NOT cointegrated (spread +2.77σ — stretched, but no equilibrium to revert to) |
| EUR/USD vs US−DE 10Y differential | 12.8 | −1.95 | NOT cointegrated on the full sample |

**The one relation that survives honest re-testing:** subsample re-tests (run wherever the break scan dates a break in the levels relation) recover **EUR/USD vs the US−DE 10Y differential as COINTEGRATED post-2003** — trace **21.2**, EG ADF **−3.90**, both rejecting. The pre-2003 synthetic-euro years were contaminating the full-sample test. Low-power caveats are displayed on the dashboard; this is an indicative finding, not a green light.

**The break scan explains the failures** (sup-F, F-form, 5% crit 5.86):

- inverse real yield → log gold: **373.2 @ 2022-06** — the central-bank-buying decoupling; gold is not cointegrated with real yields in *either* era once calendar-gap-safe diffs are used
- ISM level → INDPRO YoY (+3m): 84.5 @ 2003-08
- CLI Δ3m → INDPRO YoY (+6m): 67.1 @ 2000-07
- Curve 10Y−3M → ΔUNRATE next 12m: 12.0 @ 2011-06

**Regime, dynamics, latent states:** Markov filter puts **P(low-growth) = 1%** (regime means −0.77z / +0.23z, expected durations 21m / 31m) — the probabilistic upgrade to the rule-based 5-regime scorecard, validated visually against NBER bands. VAR(2) on the leading block is **stable** (T=534, spectral radius 0.924 by Gelfand estimator). Kalman **r\* proxy +0.32%** — a univariate trend proxy, deliberately *not* Laubach-Williams.

## The 2026-07-19 adversarial math review

A 9-agent review confirmed and fixed **6 defects before any number was published**:

1. **Wrong-scale sup-F critical value** — the F-form statistic was compared against the Wald-form threshold (11.79 instead of 5.86), making a "5%" test actually ~1% and hiding real breaks
2. **Spectral radius could be arbitrary** — plain power iteration never converges on complex dominant eigenvalue pairs; replaced with a Gelfand estimator (validated against exact eigenvalues)
3. **Calendar-gap contamination** — the Yahoo gold feed was missing 43 months, 38 of them inside the gold-pair sample, so 16% of its "monthly" innovations spanned 2–3 months. All diff-based estimators now mask non-adjacent months; this moved gold's EG ADF from +0.74 to +2.01 (now 2.11 after refresh)
4. A **mislabeled break regression** (curve→unemployment tested the 12–24m-ahead change under a 0–12m label)
5. A **positional chart lookup** that would silently mislabel a chart on a feed outage
6. An **unflushed open recession band**

## Limits, honestly stated

- **Latest-vintage data, not ALFRED PIT vintages** — the standing data-integrity gap across the whole stack; historical statistics carry that discount
- Bivariate Johansen only (no k>2 systems); **Bai-Perron multi-break** sequential testing not yet built (single-break sup-F only)
- Kalman layer is local-level; a full Laubach-Williams r\* system and a mixed-frequency GDP nowcast remain open
- Subsample verdicts have **low power** by construction — short windows, wide critical regions

## Related

[[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] · [[The Global Macros Framework]] · [[Yield Curve & Recession Signals]] · [[USD & G10 FX]] · [[FX Endogenous-Exogenous Framework]] · [[Cyclical Commodities]] · [[Macro Regime - Live (June 2026)]] · [[2026 Workbook Explorer]]
