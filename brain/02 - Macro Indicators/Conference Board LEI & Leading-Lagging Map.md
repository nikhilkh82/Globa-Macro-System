---
title: Conference Board LEI & Leading→Lagging Map
aliases: ["Conference Board LEI & Leading→Lagging Map"]
category: indicators
type: live-read
data_asof: 2026-09-19
summary: "Filed LEI leading-to-lagging map, claims desk-tested on live FRED where free data exist: LEI-proxy +1.1% YoY (Aug-2026), no recession signal; the SF Fed LMSI 30-state rule confirms recessions (11/12) but lags NBER ~3m."
tags: [global-macro, leading-indicators, lagging-indicators, conference-board, lei, business-cycle, turning-points, gdp, unemployment, inflation]
data_vintage: "LIVE — Workbook Explorer wb_explorer.json (FRED, NY Fed HPW CSV, SF Fed LMSI workbook), data through 2026-08, rebuilt 2026-09-19; framework claims from a user-filed note (July 2026)"
sources: 1
updated: 2026-09-19
---

# Conference Board LEI & Leading→Lagging Map

**What it is & why it matters** — A filed framework note on using **composite leading indicators to predict turning points in the lagging metrics** (GDP, unemployment, inflation). Where [[Leading Indicators]] covers the desk's individual survey/order-based series and [[Lagging Indicators]] covers the confirmation layer, this page maps **which leading series predicts which lagging metric, at what typical lead** — anchored on The Conference Board's Leading Economic Index (LEI) as the canonical composite. It completes the conceptual bridge that the [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)|Macro Signal Stack]] implements econometrically.

> **Honesty note:** the lead times, correlations and rules below are **filed as stated in the source note** (e.g. the −0.85 labor-differential correlation, the ~7-month LEI lead, "GDP declines within 2–3 quarters of LEI YoY < 0"). They are *framework claims, not desk-verified results*. The desk's own test harnesses for exactly these claims are the [[2026 Workbook Explorer]]'s Desk Analyst (`>lead <target>` runs the ADL leader→laggard engine with held-out out-of-sample scoring; `>corr a vs b` gives the ±12m lead/lag scan) and the [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)|Signal Stack]]/Econometrics Lab — whose own published results include honest negatives (the NY-Fed-style curve model *underperformed* the base rate OOS 2002–2026). Trust a mapped relationship only after it survives that machinery.

## The Conference Board LEI

The **U.S. Leading Economic Index (LEI)** is designed to anticipate business-cycle turning points by **~7 months**. It aggregates 10 forward-looking components:

| Block | LEI components |
|---|---|
| **Manufacturing activity** | Average weekly hours in manufacturing · ISM New Orders |
| **Labor market** | Average weekly initial claims for unemployment insurance (inverted) |
| **Financial conditions** | S&P 500 stock prices · Leading Credit Index · interest-rate spread (10-year Treasury minus Fed Funds) |
| **Housing & consumption** | Building permits (new private housing) · average consumer expectations for business conditions |

**The headline rule (as filed):** when **LEI year-over-year growth falls below 0%**, U.S. GDP has historically seen a significant decline within the following **2–3 quarters**.

## The leading→lagging map

### 1. Predicting GDP (coincident, but reported with a long lag)
- **MM Economic Expectation Index** *(as filed — aggregates GDP forecasts from IMF, World Bank, OECD and think tanks)*: high correlation with realized Real GDP growth; effectively a real-time momentum read ahead of the official print.
- **BLS New Tenant Rent Index**: leads the CPI Rent component (and hence the rent share of GDP deflators) — new-lease pricing moves quarters before the stock of all rents does.

### 2. Predicting the unemployment rate (lagging — firms adjust workforce only after confirmed shifts)
- **Labor Market Differential** (Conference Board consumer survey: jobs "plentiful" minus "hard to get"): strong historical **negative** correlation with the unemployment rate (**≈ −0.85** as filed). A sharp decline in the differential typically **precedes** a rise in unemployment by **1–2 quarters**.
- **ISM Services Employment sub-index**: the US economy is ~70% services, so this is the real-time signal for service payrolls; **sub-50 readings preview job losses** before they reach the BLS reports.

### 3. Predicting inflation / CPI (lagging)
- **ISM Services Prices Paid**: input-cost pressure in labor-intensive sectors; elevated readings **precede persistent core inflation by ~2–3 months**.
- **Energy prices (WTI, gasoline)**: the primary leading driver of *headline* CPI — an oil-price drop typically cools headline inflation in the **next month's** report.

### Summary table (as filed)

| Leading indicator | Predicted lagging/coincident metric | Typical lead |
|---|---|---|
| Conference Board LEI | Business-cycle turning points / GDP | ~7 months |
| MM Economic Expectation Index | Real GDP (YoY) | real-time / leading |
| Labor Market Differential | Unemployment rate | 1–2 quarters |
| ISM Services Prices Paid | Core CPI / PCE inflation | 2–3 months |
| Building Permits | Construction spending / GDP | 6–9 months |
| KC Fed Labor Market Conditions Index (LMCI) | S&P 500 turning points | 3–4 months *(filed 2026-08-05, MacroMicro chart 400)* |
| NY Fed HPW Labor Market Tightness Index | ECI wage inflation (near-term) / AHE growth | 0–3 months *(filed 2026-08-05, MacroMicro chart 148753)* |
| SF Fed LMSI — 30+ states accelerating | US recession (threshold rule, not a lead) | **coincident/confirming, median −3m vs the NBER start** *(desk-tested 2026-08-05, MacroMicro chart 150850)* |

## Desk coverage — what the stack has (updated 2026-07-20: LEI group BUILT)

**Built 2026-07-20** — a dedicated **LEI group** in the [[2026 Workbook Explorer]] (live FRED, auto-refreshing): **Avg Weekly Hours — Manufacturing** (`AWHMAN`, LEI comp 1, 1939→), **Mfrs' New Orders — Consumer Goods** (`ACOGNO`, comp 3), **Mfrs' New Orders — Core Capex nondef ex-air** (`NEWORDER`, comp 5), **Yield Spread 10Y−Fed Funds** (`T10YFF`, comp 9, weekly from daily), and **US Regular Gasoline** (`GASREGW`, the headline-CPI energy driver). Together with the components already in the catalog (ISM New Orders, initial claims, S&P 500, permits, UMich Expectations proxy), **8 of the LEI's 10 components are now individually chartable and testable**. All five are wired into the Desk Analyst's leader×laggard ADL grid (with **GDP growth %** added as a laggard target) and into the agent's concept map + suggestion chips.

**First backtested reads from the new series (Jul-2026 vintage, held-out OOS vs AR baseline):** **core capex orders → GDP growth at a 9-month lead (−15% OOS error)** and **the 10Y−FF spread → payrolls at a 7-month lead (−7%, flagged FRAGILE ⚠ on half-sample stability)** — the spread's lead time landing near the doc's claimed ~7-month LEI lead, with the fragility flag as the honest caveat. Claims → GDP at 6m (−9%) also survives.

**Wave 2 (built 2026-07-20, from the expanded `US Macro Leading Indicators.docx`):** five more live-FRED framework indicators added to the same group — **Avg Hourly Earnings** (`AHETPI`, 1964→, the wage gauge), **Employment Cost Index** (`ECIALLCIV`, quarterly — the Fed's wage-price-spiral watch), **Total Vehicle Sales** (`TOTALSA`, 1976→ — the doc notes cars ≈20–22% of retail), **10Y−2Y spread** (`T10Y2Y` — the doc's four curve phases; complements the workbook's own 2s10s series in RATES), and **Case-Shiller National HPI** (`CSUSHPINSA` — the doc's ~18-year housing-cycle frame). Catalog 246 → **251 series**; wages/vehicles/2s10s wired into the leader grid, wages→core-CPI and vehicles→retail pairs into the agent suggestions. **First wave-2 backtested read: vehicle sales → GDP growth at a 7-month lead (−14% OOS, FRAGILE ⚠)** — honest support for the doc's car-sales claim. The expanded doc's methodology notes (SAAR vs YoY GDP conventions, the "YoY ≥2% = still strong" heuristic, AHE's exclusions, the curve's four phases) are filed here as framework context.

**Wave 3 (built 2026-07-20) — the headlines themselves, as honest proxies + the remaining free legs:**
- **LEI Proxy — desk composite** (`LEI:PROXY`, 774 monthly obs 1962→): a reconstruction of the licensed LEI from **all 9 free components** using CB's own method simplified — symmetric % changes (200·Δ/(x+prev)), volatility-standardized, equal-weight, cumulated. **Validated against this page's own rule before shipping: proxy YoY was negative into/at 2001 (−4.2%), 2008 (−1.9%) and 2020 (−9.0%), positive mid-expansion (1997/2014/2021)** — it reproduces the LEI's signature behavior. Current read **+1.1% YoY (2026-08) → no recession signal** *(refreshed 2026-09-19 from the same-day Explorer rebuild; supersedes the +0.8% build-time read)*. Labeled PROXY everywhere; it is *not* the official index.
- **CEI Proxy** (`LEI:CEIPX`, 712 obs) from the 4 coincident components — enabling the doc's "LEI and CEI both declining → recession" read; plus the two CEI legs added as real series: **Real Personal Income ex Transfers** (`W875RX1`) and **Real Mfg & Trade Sales** (`CMRMTSPL`).
- **CPI Rent of Primary Residence** (`CUSR0000SEHA`, 1981→) — the lagging rent gauge, in place for the NTRR mapping.

**Wave 5 (built 2026-08-05, from the user-filed MacroMicro chart 400):** the **KC Fed Labor Market Conditions Index** — both legs live-FRED in the LEI group: **Activity Level** (`FRBKCLMCILA` → `LEI:LMCI`) and **Momentum** (`FRBKCLMCIM` → `LEI:LMCIM`), monthly 1992→, 24 labor variables (U-3/U-6, participation, openings, quits, wages, claims…). The filed claim — *declines before recessions; leads S&P 500 turning points by 3–4 months* — is wired into `FRAMEWORK_RELS` against the workbook's monthly S&P 500 (`MKTS:SPX`). **First verdict (Aug-2026, differenced ±18m lag scan): ✗ not supported — best lag −1m (the S&P slightly leads monthly LMCI *changes*), r₀ ≈ 0 on differences.** Honest caveat both ways: the scan tests month-over-month co-movement, while the claim is about **major cycle turning points** — a turning-point/episode test (like the LEI-proxy's episode scorer) is the sharper instrument and hasn't been run on this pair yet. Current read *(refreshed 2026-09-19; supersedes the build-time +0.09 / +0.12 for 2026-06)*: LMCI level +0.31, momentum +0.25 (2026-08) — both modestly above neutral, no labor-led warning. Catalog 300 → **302 series**. *(Same build: the rename-proof workbook resolver was made **move-proof** — the user's 2026-08-01 reorg had moved the ISM/NFIB source workbooks into topic subfolders, silently dropping ~26 series (incl. `MKTS:SPX`) from every refresh since; `tools/xlfind.py` now falls back to a one-level subfolder search, and the catalog recovered 261 → 302.)*

**Wave 6 (built 2026-08-05, from the user-filed MacroMicro chart 148753):** the **NY Fed HPW Labor Market Tightness Index** (Heise–Pearce–Weber, staff report 1128) — fetched from the Bank's own official CSV (`newyorkfed.org/research/labor-market-tightness/`, monthly 2000-12→): `LEI:HPW` (306 obs) plus `LEI:ECIQ`, the **ECI wage-growth q/q target column the index is fit to forecast**, deduped from the CSV's step-repeated months to a true quarterly series (102 obs). Construction (as published): weighted average of the **quits rate** and **vacancies per effective searcher**, weights = OLS coefficients on ECI wage growth, re-fit each ECI release. **First verdicts (Aug-2026): ✓ HPW → ECI wage growth SUPPORTED (+0.35 at 0m, inside the claimed 0–3m window, right sign) — the first framework claim to survive the scan cleanly. ✗ HPW → AHE fails on WRONG SIGN (−0.42): the 2020 AHE composition mix-shift (low-wage workers dropped out → measured AHE spiked exactly as tightness collapsed) dominates the differenced co-movement — a caution against reading AHE as clean wage pressure.** This wave also added **sign-aware verdicts** to the agent's framework judgments (`sign:` field on relations; "✗ wrong sign" chip) — right-timing-wrong-direction no longer reads as support. Current read *(refreshed 2026-09-19; supersedes the build-time HPW −0.02 for 2026-05 (that month reads +0.09 in the current, re-fit vintage) and ECI −0.10% q/q for 2026-Q1)*: HPW −0.08 (2026-07), essentially neutral tightness — still above the 2025 low (−0.26, 2025-09) but back below zero after +0.09 in both 2026-05 and 2026-06; ECI wage growth +0.40% q/q (2026-Q2), with ECI wages & salaries YoY decelerating to +3.14% (2026-Q2, Wave 8 below) — no wage-pressure signal. Catalog 302 → **304 series**.

**Wave 7 (built 2026-08-05, from the user-filed MacroMicro chart 150850) — and the first claim the desk scored on its OWN terms:** the **SF Fed Labor Market Stress Indicator** (Garimella–Jordà–Singh, FRBSF EL 2025-19), fetched live from the Bank's own workbook. Four series: `LEI:LMSI` / `LEI:LMSILF` (weekly state count + labor-force share, 1996→) and `LEI:LMSIM` / `LEI:LMSIMLF` (monthly, the count reaching back to **1949-03** — 928 obs). The index counts states whose claims-based unemployment rate sits ≥0.5pp above its trailing 12-month low.

The Bank's headline claim — *"whenever 30+ states accelerate simultaneously, the economy almost always enters a recession"* — is a **threshold rule, not a lead-lag claim**, so scoring it with the ±18m correlation scan would have been the wrong instrument (that scan asks whether the *wiggles* co-move; the rule asks whether *crossing the line* marks a recession). This wave therefore built the missing instrument: a **threshold-episode scorer** (`thrEpisodes`/`thrRuleStats`, surfaced as **`>lmsi`**, threshold adjustable via `>lmsi 25`) — the same class of test the LEI-proxy episode scorer uses, and the one flagged as missing when the [[#Wave 5]] LMCI turning-point claim could not be fairly judged.

**Verdict (928 months; reproduced independently in Python and in-page, then hardened by a 14-agent adversarial audit):** 13 episodes at ≥30 states, of which **12 are scorable** — the first (1949-03) is *left-censored*, because the series opens already above the line, so its onset is unobservable and its "hit" would be guaranteed by construction. Of the 12 scored: **11 coincided with a distinct recession (92%), 1 false alarm (Aug-2024, a single month exactly at 30), and 0 of 11 in-sample recessions missed.** So the rule holds as a **recession CONFIRMER** — it has never missed one. **But it is not a leading indicator: every scored episode's lead is ≤ 0 and the median crossing comes 3 months AFTER the recession's NBER start date** (range −9…−1). That is not a criticism of the index — NBER dates recessions with a *far* longer lag than 3 months, so a signal firing 3 months in is genuinely early in real time, which is exactly what the Bank claims for it. It is, however, a correction to any reading of the MacroMicro chart as a forward-looking recession *predictor*.

*(The scorer was audited twice — the second pass caught three defects the first round's **fixes** had introduced, including one that fabricated a false alarm at thresholds 35–45 and one where chronological claiming let a 1-month blip steal a recession from the 14-month episode that contained it, biasing the leads toward "leading". Both are fixed; episode-to-recession assignment is now a directionally-neutral nearest-onset match. The headline threshold-30 result was unaffected.)*

**Two honest caveats the audit forced into the scorecard.** (1) **Vintage:** the −3m lead distribution is computed on the SF Fed's *current, fully revised* workbook, so it is an **upper bound** on true real-time performance — the only genuinely out-of-sample observation is the 2024 spike. (2) **One-to-one accounting:** each recession can be credited only once; a later episode matching an already-credited recession is reported as a *re-trigger*, never as a second hit — so hits can never exceed the number of recessions (at `>lmsi 25` the old code scored 13 hits against 12 recessions). Current *(refreshed 2026-09-19; supersedes the build-time 0 states for 2026-06, weekly 1 state, 0.2% of the labor force)*: **0 states (2026-07), weekly 3 states (week of 2026-08-22), 3.3% of the labor force — far below the line.** Catalog 304 → **308 series**.

*(Same build, a pre-existing charting bug found via the new data: the lab force-rebases series to 100 (`y/base×100`) whenever 3+ are overlaid or the rebase toggle is on. On a **sign-changing** series a negative base **mirrored the line** — a 10y−2y spread starting inverted at −0.73 and normalising to **+0.43** was drawn at **−58.9**, i.e. still inverted, on one of the most-watched recession indicators — and a base of exactly **0** silently left that series un-normalised. Fixed: if any visible series can't be ratio-rebased, the whole chart switches to min–max 0–100 (labelled "scaled 0-100" vs "rebased=100"), preserving true shape and sign ordering. Regression-verified across 48 series: 39 all-positive still rebase to exactly 100 unchanged, 9 correctly switch, 0 failures.)*

**Wave 8 (built 2026-08-17, from the user-filed MacroMicro AHE-vs-ECI chart) — AHE's composition problem, finally measured.** Both legs of that chart were missing even though the catalog already held *an* AHE and *an* ECI: `LEI:AHE` is production & **nonsupervisory** workers (AHETPI, 1964→, $32.53/hr in 2026-08 *(refreshed 2026-09-19; supersedes the build-time $32.40)*) and `LEI:ECI` is total **compensation** for **all civilian** workers. Added the chart's actual series — **`LEI:AHEALL`** (all employees, total private, 2006-03→, $37.75/hr in 2026-08 *(refreshed 2026-09-19; supersedes the build-time $37.62)*) and **`LEI:ECIWAG`** (ECI **Wages & Salaries, private industry**, quarterly 2001→). Catalog 430 → **433 series**.

**The measured result:** on YoY — what the chart plots — the two gauges correlate **r = +0.73** over 77 overlapping quarters, and **r = +0.92** once 2020-03…2021-06 is excluded. That excluded window *is* the composition shock: **April 2020, AHE +8.10% YoY against ECI +2.92%** — a 5.2pp gap opened because low-wage workers left the sample, so a raw average rose while the fixed-job-mix index did not. Latest (2026-04): AHE +3.57%, ECI +3.14%, converged and both decelerating *(re-verified 2026-09-19: still the latest overlapping quarter; monthly AHE has since eased to +3.09% YoY in 2026-08)*. So the chart's implicit point is confirmed *and* quantified — the two are the same signal **except when composition moves, and then the ECI is the truer read**. This also retro-explains [[#Wave 6]]'s wrong-sign failure of HPW-tightness → AHE: the 2020 AHE spike is exactly what flipped that sign.

Two honesty notes. The pair answer's **level** correlation reads +1.00 because both are trending indices — meaningless; the differenced scan and the YoY figures above are the real reads. And the ECI → **core CPI** wage-price-spiral claim in the user's own description is left as an **honest negative** (r₀ = +0.80 but best lag −3m, ✗ not supported at the claimed 3–12m lead) — strong co-movement, no demonstrated wage-leads-prices direction. *(The AHE↔ECI relation was initially mis-encoded as a lead claim and read "not supported" at −3m — one quarterly grid step from zero. It is a **tracking** claim, so the window was corrected to a symmetric ±3m and labelled as such in the claim text; disclosed because an undisclosed window change would be a goalpost move.)*

**Remaining gaps (licensed / no free source):**
- The official **CB LEI/CEI headlines**, the **Leading Credit Index**, and the **Labor Market Differential** — Conference Board licensed (the proxies above cover the shape, not the official prints).
- **ISM Services Prices Paid / Employment sub-indices** — wb 6 carries Business Activity / New Orders / Employment but **no Prices Paid**; ISM data left FRED in 2016.
- **BLS New Tenant Rent Index** — fetch attempted 2026-07-20; both known BLS XLSX URLs now 404. The NTRR→CPI-rent relation stays wired in the agent's knowledge base and auto-activates if the series ever lands.

**Where the desk has already tested this class of claim:** the Explorer's leader×laggard ADL grid (relation chips) backtests US leading→lagging pairs with an AR baseline and held-out scoring — several survive honestly, others show "correlation ≠ predictive value"; the Econometrics Lab's sup-F break scan found **structural breaks in ISM level→INDPRO YoY +3m (2003-08, sup-F 84.5) and curve 10Y−3M→ΔUNRATE-next-12m (2011-06, sup-F 12.0) — both against the Andrews F-form 5% critical value 5.86** — a caution against treating any fixed lead time in the table above as stable across regimes.

## The visual section (built 2026-07-22)

The Explorer now carries a dedicated **🇺🇸 US Leading Indicators** dashboard section (below the Macro Monitor): a rule-based **cycle-phase banner** (the doc's four phases mapped onto the two proxy composites' YoY momentum — current read **Recovery** *(refreshed 2026-09-19; supersedes the build-time +0.8% / −2.2%, "negative 8 straight months" read)*: LEI-proxy momentum +1.1% (2026-08, improving vs six months earlier) with CEI-proxy momentum −2.3% (2026-07) — below zero every month since 2024-01, and the CEI-proxy index itself down 12 straight months), the **LEI-Proxy YoY chart with the zero rule-line** against every NBER recession since 1963, the **LEI-vs-CEI drawdown-from-3-year-high** overlay (the doc's second transform), and **16 clickable component tiles** with sparklines feeding the main chart lab.

## The claims, judged (built 2026-07-20: the agent now KNOWS this map)

This page's mappings are wired into the Explorer's Desk Analyst as a 15-relation knowledge base (`FRAMEWORK_RELS`): ask about any mapped pair and the answer carries a **📚 Framework map** line judging the claim against the computed lag scan (ADF-tested, differenced when trending, quarterly-grid-aware); the **`>lei` command** renders the full scorecard — all 10 live series' readings plus every claim's verdict. **Jul-2026 verdicts (correlation screen, full history):** ✓ **claims→unemployment (+0.53 at exactly +1m)**, ✓ ISM-services→payrolls, ✓ vehicles→retail; ≈ near-window: gasoline→headline CPI (+0.64 @ 0m vs claimed 1–2m), hours→payrolls; ~ right-direction-different-tempo: wages→core CPI (+14m), house prices→GDP; **✗ not supported (8)** — including *both curve→GDP claims* (best lags negative — consistent with the [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)|Signal Stack]]'s honest OOS negative on the curve-recession model) and both new-orders→GDP mappings (strong r ≈ +0.5–0.7 but contemporaneous, not leading). The relation chips run the stricter held-out *predictive* test — where core capex orders→GDP (−15% OOS at 9m) and vehicles→GDP (−14% at 7m) DO survive, showing the two tests answer different questions.

**Audited verdicts, 2026-09-11 (after a code audit; data through 2026-09-10, build vhash b0646f7547aa):** the scan now
differences *both* sides when either has a unit root and treats a best correlation inside ±1.96/√n as no lead. On that
basis **all four wage → price claims are not supported**: CPI +0.14 at −8m (noise band ±0.13), core CPI +0.17 at −2m,
PCE +0.18 at −8m and core PCE +0.17 at −16m. Prices lead or move together. CPI's earlier "+16m, right direction" came
from differencing only the wage side. In the held-out forecast test, the wage term changes one-step error against an
exactly nested no-wage twin by −1.0% (CPI), +3.1% (core CPI), +1.2% (PCE) and +6.6% (core PCE, t 1.5); none is
significant and no headline forecast changes. *This supersedes the verdicts in the next paragraph.*

**Added 2026-09-11 (desk request, marked ★ in `>lei`):** four claims that the jobs report's headline wage (average hourly
earnings, all private employees) leads **CPI, core CPI, PCE and core PCE by 3–6 months**, judged on YoY wage growth
against YoY inflation with the 2020-03..07 composition months dropped. **Verdicts on data through 2026-09-10:** CPI best
+0.13 at +16m (right direction, far outside the window); core CPI +0.18 at −2m, PCE +0.18 at −8m and core PCE +0.17 at
−16m (prices lead or move together — not supported). The held-out forecast test agrees: the wage term cuts one-step
error against a no-wage twin by only 0.0–5.4%. Full study: [[Average Hourly Earnings as a Leading Indicator of Inflation (September 2026)]].

## Related
[[Leading Indicators]] · [[Coincident Indicators]] · [[Lagging Indicators]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[Yield Curve & Recession Signals]] · [[GDP & Growth]] · [[2026 Workbook Explorer]] · [[Global Macro Brain]]

**Caveat page:** [[CB LEI vs Financial Stocks — a Circularity Warning (July 2026)]] — the LEI contains the S&P 500, so any LEI→equities lead test is partly circular; read it before quoting an LEI/stocks lead.
