---
title: Average Hourly Earnings as a Leading Indicator of Inflation (September 2026)
category: indicators
type: deep-dive
data_asof: 2026-09-11
summary: "Tested whether average hourly earnings lead CPI/PCE by 3-6 months: wages move with inflation but do not lead it; the Explorer's audited test changes no headline forecast (wage gains -1% to +7%, none significant), and over 1985-2019 adding wages made forecasts worse."
tags: [global-macro, inflation, wages, average-hourly-earnings, leading-indicators, cpi, pce, forecasting, employment-report]
data_vintage: "Workbook Explorer catalog, data through 2026-09-10: FRED CES0500000003 (2006-03→2026-08), AHETPI (1964→2026-08), PCEPI and PCEPILFE (→2026-07); CPI and core CPI from wb 26 (→2026-07)"
sources: 1
updated: 2026-09-11
---

# Average Hourly Earnings as a Leading Indicator of Inflation (September 2026)

**The request (2026-09-11).** Add average hourly earnings from the monthly employment report to the
[[2026 Workbook Explorer]], and use it as a leading indicator of price pressure in the CPI and PCE forecasts
with a 3–6 month lag. The Explorer now does exactly that (see *How the Explorer tests it* below). This page
records what the data say about the idea, so the result is not re-derived every time the question comes up.

> **Answer in one line.** Average hourly earnings move *with* inflation, but they are not a reliable 3–6 month
> *leading* indicator of CPI or PCE. The forecast gains they add are small, come almost entirely from the
> 2021-23 episode, and vanish or turn negative in stable-inflation regimes.

## The series
- **Headline wage** — *Average Hourly Earnings, All Employees, Total Private* (BLS CES0500000003, FRED). This is the
  jobs-report headline. It only exists from **2006-03**.
- **Long-history wage** — *Production & Nonsupervisory* (AHETPI, from 1964). Its YoY growth tracks the headline at
  r ≈ 0.96 since 2007, so the two carry almost the same information.
- **Composition caveat.** In April 2020 low-wage layoffs lifted measured AHE **+4.5% in one month** while the
  composition-controlled ECI barely moved. Every test here drops or isolates 2020-03..07 (and, where noted, the
  whole 2020-03..2021-06 window).
- **Timing is not the problem.** AHE for month *m* is published in the first week of *m+1*, a week before that
  month's CPI and three to four weeks before its PCE. A 3-month lag is genuinely usable in real time.

## What the data say
1. **No timing lead.** Wage and price YoY correlate at 0.5–0.8, but equally at every lag from −12 to +12 months:
   two persistent series trending together. Once each series' own momentum is removed (prewhitening), the
   correlation inside the 3–6 month window is +0.0 to +0.2, and in every full, pre-2020 and ex-shock sample the peak
   sits at **0 to −3 months** — prices move first or together.
2. **A regime-specific, small forecasting gain.**
   - Long history (AHETPI, 1965-2026): adding wages cuts 3–6 month CPI and core-CPI forecast errors by about **3%**
     (Clark-West p < 0.001). Real, but small, and learnt in the high-inflation era.
   - **1985-2019, trained and scored inside that regime: adding wages made all 48 target × transform × horizon
     forecasts worse** (RMSE +0.1% to +4.0%). The in-sample wage coefficient for core CPI is −0.01 (t −0.16).
   - Core PCE (the Fed target): about 1%, not significant.
   - Headline AHE (since 2006): about 10% lower error on core CPI and core PCE from 2015, but 87-98% of that gain was
     earned at 2021-23 forecast origins. Pre-2020 origins show no gain, and once the 2020-21 composition shock is
     excluded core CPI gets slightly worse.
3. **The reverse direction is at least as strong.** Inflation predicts subsequent wage growth (PCE 3-month
   annualised → AHETPI: 3–4% lower error, Clark-West p ≤ 0.015).

## How the Explorer tests it (live, re-run with every data vintage)
- **Employment report group.** Both wage series now sit in the *Employment Situation report* group beside the payroll
  sectors (as PAYROLL:AHEALL / PAYROLL:AHE, copies of LEI:AHEALL / LEI:AHE). The **`>jobs`** command shows payrolls,
  unemployment and both wage prints (m/m, 3-month annualised, YoY).
- **Forecast challenger.** Every forecast of CPI, core CPI, PCE (clean live PCEPI) and core PCE runs a *wage-led
  challenger* — a log-difference ARI plus the mean month-on-month wage growth 3–6 months earlier — on the same
  rolling origins as every other model (except origins whose inputs straddle a calendar gap, which it skips), against
  an **identical no-wage twin**: same rows, same AR order, only the wage term removed. The wage gain is always quoted
  against the twin. The challenger becomes the headline forecast only when the wage term clearly helps (more than 3%
  lower error than the twin, t above 1) *and* the challenger beats the best non-wage model on the origins both cover;
  otherwise its path is drawn as a dashed green line.
- **Leader test.** "What predicts CPI/PCE" now includes both wage series, restricted to a **3–6 month lead**. Each wage
  row's gain is scored against an AR baseline fitted on that wage series' own sample; leaders are *ranked* against one
  common baseline, so a late-starting series is neither credited nor penalised for its shorter history.
  "Predict core CPI from wages" runs the test on the headline wage alone.
- **Claims.** Four claims (headline AHE → CPI, core CPI, PCE, core PCE at 3–6 months) are filed in the `>lei`
  scorecard and judged on YoY growth against YoY inflation, both sides differenced when either has a unit root, and a
  best correlation inside the ±1.96/√n noise band counts as no lead.

**Audited readings (2026-09-11; page build 15:59 on data vhash b0646f7547aa, data through 2026-09-10).** These
supersede the first readings below.

| Target | Wage gain vs no-wage twin (one-step origins 2023-02..2026-07) | Headline forecast | Leader test, top-ranked leader (held-out) | Leader test, headline AHE only (held-out) | Claim scan (YoY, ±18m) |
|---|---|---|---|---|---|
| CPI | −1.0% (t −0.4, 39 origins): wages make it slightly worse | ARI(p,1). The no-wage twin itself beats it by 3.0% (t 2.3), which is the log-difference structure, not wages | Prod. & nonsup. AHE at 4m: 3% lower error, stable | 6.5% lower at 6m, fragile | best +0.14 at −8m (noise band ±0.13): not supported |
| Core CPI | +3.1% (t 0.6, 39) | ARI(p,1) recent-10y. The challenger is 2.5% more accurate, but its wage term is not clear enough (t < 1) to take over | Prod. & nonsup. AHE + UMich sentiment at 4m/1m: 0.5% *higher* error, an honest null | 9.2% lower at 5m, fragile | best +0.17 at −2m: not supported |
| PCE | +1.2% (t 0.4, 42) | RW + drift (5y); the challenger is 2.4% less accurate | Prod. & nonsup. AHE + UMich sentiment at 3m/3m: 6.4% lower, stable | 7.9% lower at 6m, fragile | best +0.18 at −8m: not supported |
| Core PCE | +6.6% (t 1.5, 42) | Ensemble (RW + drift + seasonal ARI). The wage term clears its bar, but the challenger is 7.8% less accurate than the ensemble on the 14 origins both cover | Prod. & nonsup. AHE at 5m: 7.6% lower, stable | 6.3% lower at 6m, stable | best +0.17 at −16m: not supported |

How to read it:
- **No wage term is statistically clear** (largest t 1.5), and **no headline forecast changes**.
- **The two forecast tests look at different windows.** The challenger's gain is averaged over 39–42 origins since
  2023. The leader test quotes only its held-out window, the last 14 origins (2025-06..2026-07); CPI and core CPI lose
  four of those to the October-2025 gap. Its 3–9% gains are therefore a one-year read, and for the headline wage they
  are fragile in three of four targets.
- **The correlation scan finds real co-movement but no lead.** Every best lag sits at or before zero, so prices move
  first or together.
- **What changed from the first readings.** (1) The no-wage twin now uses exactly the challenger's rows and AR order;
  before, it trained on 9–11 extra months, including the 2020 rebound, and the "wage gain" mixed in a sample
  difference. (2) The claim scan differences both sides; differencing only the unit-root side had manufactured CPI's
  "+16m" lead. (3) Leaders are ranked against one common baseline. Before, UMich sentiment ranked first for CPI and
  led the PCE pair despite a higher selection-window error than the wage series on the same origins. (4) The
  calendar-grid fix (see *Data defects* below) moved the CPI rows.

The answer in one line stands.

**First readings (data through 2026-09-10):**

| Target | Wage gain vs no-wage twin (42 one-step origins, 2023-02..2026-07) | Headline forecast | Leader test, headline AHE only (held-out) | Claim scan (YoY, ±18m) |
|---|---|---|---|---|
| CPI | +0.0% (t 0.0) | unchanged, univariate | −8.7% error at 6m, fragile | best +0.13 at +16m, outside window |
| Core CPI | +2.2% (t 0.4) | unchanged, univariate | −7.5% at 5m, fragile | best +0.18 at −2m, not supported |
| PCE | +1.0% (t 0.3) | unchanged, univariate | −7.9% at 6m, fragile | best +0.18 at −8m, not supported |
| Core PCE | +5.4% (t 1.1) | unchanged (the wage model qualifies but is not the most accurate) | −6.3% at 6m, stable | best +0.17 at −16m, not supported |

*Superseded the same day by the audited readings above.* Kept as the record of what the pre-audit build reported.

"Fragile" (in both tables) means the correlation changes sign between the two halves of the sample, which is the
2021-23 episode again.

## Data defects found on the way
- **The workbook PCE series are spliced.** INFL:PCE and INFL:CPCE (wb 15) switch base year in February 2021
  (2012=100 before, 2017=100 after), a fake −5.4% / −7.1% month. Any YoY, lead-lag or forecast across that month is
  wrong. The Explorer now routes "pce" and "core pce" to the clean live series (LEI:PCEPI, LEI:COREPCE).
  - *Fixed 2026-09-11 (build vhash b0646f7547aa):* INFL:PCE and INFL:CPCE now carry the live FRED values, as mirrors
    of LEI:PCEPI / LEI:COREPCE. Their YoY matches the clean series to 0.000pp over all 799 months, and core PCE YoY
    for 2021-06 reads +3.86%. A new build guard flags this kind of splice automatically. Details are in the
    *Data integrity* section of [[2026 Workbook Explorer]].
- **CPI has a hole.** US26:CPIAUCSL has no October 2025 value (the shutdown), and US26:CPILFESL's October 2025 value is
  an interpolated midpoint. The wage challenger refuses to forecast across the gap; older engines difference across it.
  - *Fixed 2026-09-11:* the gap is kept in both series. The core-CPI midpoint fill is dropped, because BLS never
    published October 2025. The forecast tournament, ADL engine and decomposition now key by calendar month, so no
    engine differences across the gap. The effect on the CPI rows above, measured on the same data (engine before →
    after):
    - CPI: wage gain vs the no-wage twin +0.9% → −1.0%; headline winner RW + drift (5y) → ARI(p,1); AHE-only
      leader test 8.7% → 6.5%.
    - Core CPI: wage gain +4.0% → +3.1%; AHE-only leader test 7.4% → 9.2%.

    The PCE and core PCE rows are unaffected, and the conclusion (wages do not reliably lead) stands.

## Caveats
- Revised data, not real-time vintages; AHE is revised in the next two jobs reports and at the annual benchmark.
- Headline AHE starts in 2006, so every test on it rests on one inflation cycle.
- The composition-controlled Employment Cost Index for wages & salaries (LEI:ECIWAG) is the cleaner wage read; its own
  filed claim against core CPI is judged in the same `>lei` scorecard.

## Related
[[2026 Workbook Explorer]] · [[Conference Board LEI & Leading-Lagging Map]] · [[Leading Indicators]] ·
[[Inventory-to-Sales Ratios & the Inflation Channel (July 2026)]] · [[Measurement Conventions — Growth, Inflation & Index Arithmetic (Mohr)]]
