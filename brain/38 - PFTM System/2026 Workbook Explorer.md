---
title: 2026 Workbook Explorer
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "Chart lab over every 2026 workbook (456 series, 357,609 obs, to 2026-09-18): layout v3, forecast tournament, AHE-lead test. AU endo falls to +24 (CPI/M3 stale), so US−AU now agrees with the USD-positive exo read."
tags: [global-macro, dashboards, interactive-charts, workbooks, components, explorer, 2026-excel]
data_vintage: "2026 workbooks (2.8) + live FRED (retail components, PCE, GDP and IP components); data through 2026-09-18 for the live-FRED, rates and market groups; the wb-14 commodity group's weekly price legs end 2026-08-31 and its SHFE/DCE/arb legs 2026-06-26..2026-07-17, and the survey groups lag (Mfg PMIs Jun-2026, Services PMIs May/Jun-2026)"
sources: 25
updated: 2026-09-19
---

# 2026 Workbook Explorer — the interactive chart lab over ALL the workbooks

**`Workbook Explorer/2026 Workbook Explorer.html`** (tools: `wb_explorer_data.py` → `wb_explorer.json` →
`build_wb_explorer.py`). **456 series · 357,609 observations · 38 captioned groups** (data through 2026-09-18 · rebuilt 2026-09-19 15:47 · vhash 6d3783a9bace; four more group codes — AIDIF, ITGDP, EIA, STEO — carry 41 series without a caption yet; they come from explicit loaders, not auto-discovery. *Supersedes the 2026-09-15 13:19 build (458 series, 358,761 observations, data through 2026-09-14, vhash e52e29560029): two series left the catalog — AU:CPI (quarterly, 307 obs) and AU:M3 (monthly, 735 obs), gone between the 2026-09-16 09:19 and 11:09 rebuilds, which takes the Australia Endo group from 13 chart series to 11 and costs the AU scorecard two drivers (below). The remaining ~110 of the 1,152-observation fall is new prints netted against history that went missing in the same rebuilds — the 09-16 09:19 build was already 222 observations short with no series change — and no build log on disk explains either. That build superseded the 2026-09-11 16:19 build (358,721 observations, data through 2026-09-10, vhash 4206c88b8f57): the +40 are the prints that arrived between the two runs — no series added, no loader changed. That build superseded the 2026-09-11 15:43 build (358,706 observations, vhash b0646f7547aa). The +15 come from re-sourcing the GDP and IP components from FRED (see* Data integrity *below): investment, exports and imports regain the two 2017 quarters their sheets lacked (+6), the eight IP series gain July 2026 (+8), and the CEI proxy, which is built partly from IP, gains July too (+1). That build superseded the 2026-09-11 14:26 build (358,707 observations, vhash 490367d37802): the −1 is core CPI's October-2025 value, a fill dropped because BLS never published that month (see* Data integrity *below). That build superseded the 2026-09-11 morning read of 450 series · 354,909 observations · data through 2026-09-09 (vhash 2df203da0e45, built 2026-09-10 13:10): the +8 are five Statistics Canada series restored after a failed batch fetch, a clean headline PCE price index, and the employment report's two average-hourly-earnings copies. That read had superseded the 2026-07-24 build's 287 series · ~187k observations · 29 groups.*), every series read at exact,
recon-pinned workbook coordinates. Pick / overlay (≤4) / transform / zoom, live histogram + full-history
z & percentile stats, NBER recession bands, per-series VAL/YoY/MoM chips, PNG/CSV export, bookmarkable
URLs (`#s=` hash — the deep-link target for [[Macro Insights]]). **Key patterns & trends panel** (right of
the main chart, added 2026-07-18): auto-written per-series findings that recompute with every selection,
transform, range and zoom — latest value + honest percentile/z of the full transformed history, 3m-vs-6m
turning-point read on monthly levels (contiguous tail required), window move/range position, streaks,
volatility-regime notes, STALE warnings, and pairwise correlations over the visible window.

> Decision-support / education only — **NOT investment advice**.

## Coverage (groups)
US/AU/UK endo drivers (wb 26/27/28) · US Leading Indicators (29) · 24 Manufacturing PMI series (33 — 23 countries + global,
latest prints still Jun-2026 in the 2026-09-19 build — unchanged since the 07-24 read; honest 11.5-year gap-break) · Services PMIs (34: US/UK only in the 2026-09-19 build, US to 2026-05 and UK to 2026-06 — EZ/JP/IN are no longer in the catalog, superseding the 07-24 US/UK/EZ/JP/IN roster) · ISM Mfg + Services
components (8/6) · China PMI components (25) · UMich components (3) · Permits & Housing (17+11) · **Employment
Situation report** (5: payrolls by sector from 1939, plus both average-hourly-earnings series from live FRED since
2026-09-11) · GDP components (10; values live FRED since 2026-09-11, see *Data integrity*) · Inflation complex (15+2, PPI from 1913) · Durables components (9) ·
IP components (12; values live FRED since 2026-09-11) · Claims (4) · **NFIB 29-series set** (19+20+21: headline, 8 regions, 9 industries, 11
components) · EU ESI (24) · Rates & Credit (37+22+23) · **Commodities (14 — stale: the six weekly price
legs (WTI, Brent, the WTI–Brent spread, COMEX copper, lumber, iron ore) still end 2026-08-31 because the
source workbook was not updated, and the five remaining legs end earlier still — SHFE copper and DCE iron ore
at 2026-07-17, the two arbitrage spreads and the workbook's CNY/USD leg at 2026-06-26.
The live energy and metals read is not here — see [[Energy, Metals & Agriculture — the Sub-Complexes]])** · Markets · **Retail Sales &
components (wb 1 headline + 9 live-FRED components — the workbook's component columns failed a FRED
cross-check: hand-typed placeholder stretches since 2018, disclosed on every card)**.

**Groups in the 2026-09-19 catalog not itemized above** (series count each, from the build; every count below re-read from the 2026-09-19 15:47 build and unchanged; *supersedes the 2026-09-09 counts LEI 41 and Canada 10*): BoP trade balances (7, live FRED) · US Consumer Confidence (2, OECD/DBnomics, still to 2026-05) · US Leading Set / LEI components (42 incl. the new clean headline PCE, live FRED, to 2026-09-18) · Global Economy framework (10) · COT net positioning (18, weekly CFTC, cotrep as of 2026-09-15) · Canada BoC/StatCan set (15 with the five StatCan LFS/GDP/permits/manufacturing series restored, daily to 2026-09-18) · GDP forecasts SPF / NY Fed (6) · US equity sectors (6, SPDR proxies) · inflation expectations & Cleveland Fed nowcast (5) · World OECD inflation & policy rate (3) · Fed implied path & hawk-dove index (5, forward-dated to 2028-02) · EPU/EMV trackers (6) · Fear & Greed composite (6) · Bull/Bear Markov regime (2) · EIA weekly stocks (4) · STEO liquid-fuels balance (5, forecast to 2027-12) · IT contribution to GDP (3) · AI Diffusion Index (29 countries, quarterly to 2026-03) · 72 auto-discovered workbook series.

## Endo & Exo Scorecards section (added 2026-07-18)
Below the chart lab: **the reasoning applied to now** — per-country endogenous scorecards read LIVE from each
workbook's own Score Engine (🇺🇸 US 17 drivers **+36** of −150/+160 = +22% of scale, the workbook's own label
"Inflationary overall" · 🇦🇺 AU 13 drivers **+24** of ±130 = +18% · 🇬🇧 UK 15 drivers **+27** of ±150 = +18%, AU and
UK both labelled "MILDLY INFLATIONARY" — so 18–22% of scale, not the 18–26% of the last read; *2026-09-19
re-read: US +36 and UK +27 unchanged, AU **+34 → +24** because its CPI and M3 drivers now read STALE and score
0 — the same two series that left the chart catalog (above). The superseded readings are listed in [[log]].
That read superseded the 2026-07-24 UK +29; US/AU were unchanged at the 2026-09-09 re-read*), each driver with rate, ±10 score bar and the
workbook's own State commentary (hover), plus the **exogenous AUD/USD scorecard** (wb 39: 4 relative factors,
SCORE **−4 of ±40** = mildly USD-positive, unchanged; underlying wb-39 series still 2015-vintage — disclosed). A relation
strip normalizes totals to %-of-scale and cross-checks: the US−AU endo differential is now **+4pp of scale
(favors USD)** and **consistent** with the exo USD-positive read — the divergence flagged on 2026-09-09 has
closed, and it closed because the AU total fell, not because the exo read moved. Method per the course
*Endogenous Drivers Steps* + the user's *Global Macro Strategy Steps*; nothing rescored — the workbooks are
the authority, which is also why both cards still carry the **pre-hike Fed rate**: the US card's benchmark-rate
driver reads 3.63% and the AUD/USD carry factor "RBA 4.35% vs Fed effective 3.62%", while the Fed raised 25bp
to 3.75–4.00% effective 2026-09-17. Nothing here is rescored by hand for that.

Four further economies with **no scorecard workbook** (🇨🇦 CA **+3.06z** (4 live / 2 stale drivers) · 🇯🇵 JP **+3.15z** (5/2) · 🇨🇳 CN **+1.22z** (3/3) · 🇪🇺 EZ **+0.79z** (5/2) — 2026-09-19 read, *superseding the 2026-09-09 values CA +2.59z / JP +2.57z / CN +1.23z / EZ +0.67z (listed, with the rest of this refresh, in [[log]]): JP +0.6 and CA +0.5 are the moves, EZ +0.1 and CN flat, all four still positive and the live/stale driver split unchanged. That read superseded the 07-24 values CA +2.44z / JP +4.02z / CN +0.82z / EZ +0.05z; JP's drop is the largest move, all four still positive*) are carried by the audited **CC Endo engine** — each driver z-scored against its own history, point-in-time, stale drivers guarded to 0. Different scale from the workbook ±10 cards: **comparable in direction only**. A **computed exogenous read** (`exo_calc`, five USD pairs, non-USD leg named; positive = the named non-USD leg's factors read higher) decomposes that engine's pair divergence: EUR/USD **+1.47** · GBP/USD **−0.34** · USD/JPY **+3.83** · USD/CAD **+3.74** · USD/CNY **+1.90** (2026-09-19 build; *supersedes the 2026-09-09 values EUR/USD +1.65 · GBP/USD −0.33 · USD/JPY +3.55 · USD/CAD +3.57 · USD/CNY +2.21, listed in [[log]] — every sign is unchanged; USD/CNY −0.31 and USD/JPY +0.28 are the largest moves*).

### Per-indicator monthly scorecards (added 2026-07-18)
Inside each US/AU/UK endo card, every driver matched to a monthly series is **re-scored every month, point-in-time**: ADF-decided stationary form (12m change where unit-rooted, level otherwise), z against its own history *up to that month only* (no lookahead), clipped ±3z onto the workbook's ±10 scale, polarity aligned to the workbook's own current sign. The **OVERALL row sums the indicator scores per month — the endogenous total, decomposed month by month**, so the score's *evolution* is visible rather than just today's snapshot. Coverage is disclosed per card (US 9/17 drivers matched, AU **11/13** — CPI and M3 fell out with the two dropped series, superseding the 13/13 of the last read — UK 12/15; unmatched drivers named), and months where fewer than 60% of indicators have printed are **suppressed rather than shown as a fake collapse**.

## Desk Analyst — econometric engines (v3, 2026-07-18/19)
A deterministic, in-browser forecasting agent (no LLM, no network) sitting above the catalog:

- **Unit roots by augmented Dickey-Fuller test** (constant + 2 lags, 5% critical value) — replaced the earlier AR(1) ρ>0.97 heuristic; AR orders by small-sample-corrected AICc.
- **Forecast tournament (~13 models)**: RW / RW+drift / seasonal naive benchmarks · AR(p) · ARI(p,1) · seasonal ARI · **Theta** (M3 winner) · **damped-trend Holt** · **damped Holt-Winters** · **SARI(2,1)(1)₁₂** · **recent-window ARI** (parameter-drift adaptation) · a **selection-free median-of-all combination** · a top-2 average. Every model judged **only** on rolling-origin pseudo-out-of-sample one-step errors; the top-2 ensemble is scored on the held-out final third that its member-selection never saw.
- **ADL leading→lagging engine** — Granger causality in its honest forecast form: lead k and lag count chosen on a *selection window*, every quoted RMSE/gain/interval measured on **held-out origins** with the AR baseline paired origin-for-origin; half-sample sign-stability flags fragile relations as untradeable; a bivariate two-leader variant competes and is promoted only when it earns it.
- **Prediction correlation** — Pearson r between predicted and realized month-over-month **changes** on out-of-sample origins (level correlations are flattered by persistence), plus a **visible backtest overlay**: the winner's actual one-step OOS predictions drawn against reality on the chart.
- **Skill-ranked input chips** and **US leading→lagging relation chips**, both precomputed from the backtests and cached per data vintage, so the suggestions the agent offers are ranked by its own measured accuracy — including honest nulls (e.g. claims→unemployment showed no gain before the OOS lead search found a real specification).

Method and limits are stated in every answer; see [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] and [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] for the univariate and multivariate layers this agent draws on.

## Average hourly earnings → price pressure, 3–6 month lead (added 2026-09-11)
Desk request: put the jobs report's average hourly earnings in the Explorer and use it as a 3–6 month leading
indicator in the CPI and PCE forecasts. What was built:
- **The series.** The headline wage (all private employees, FRED CES0500000003, from 2006-03) and the production &
  nonsupervisory wage (AHETPI, from 1964) now also sit in the *Employment Situation report* group, as copies of
  LEI:AHEALL / LEI:AHE that the page de-duplicates everywhere else. The **`>jobs`** command (or typing "jobs report" /
  "employment report") shows payrolls, unemployment and both wage prints.
- **In the forecasts.** CPI, core CPI, PCE and core PCE each run a wage-led challenger (wages lagged 3–6 months, the
  2020-03..07 composition months dropped) against a no-wage twin fitted on exactly the same rows at the same AR order.
  It takes over the headline forecast only when the wage term clearly helps (more than 3% lower error than the twin,
  t above 1) *and* the challenger is more accurate than the best non-wage model on the origins both cover;
  otherwise it draws its own dashed green path. "What predicts CPI/PCE" tests both wage series at a 3–6 month lead;
  four claims sit in the `>lei` scorecard, judged on YoY growth with both sides differenced and a ±1.96/√n noise band.
- **Clean PCE targets.** "pce" and "core pce" now route to the live FRED series (LEI:PCEPI, new; LEI:COREPCE), because
  the workbook's INFL:PCE / INFL:CPCE carry a February 2021 base-year splice. *(Fixed later on 2026-09-11: INFL:PCE /
  INFL:CPCE are now FRED mirrors; see* Data integrity *below.)*
- **Audited result (2026-09-11, page rebuilt 15:59 on the 15:43 data, vhash b0646f7547aa, data through 2026-09-10):**
  against the no-wage twin the wage term changes one-step error by **−1.0%** for CPI (it makes it slightly *worse*,
  t −0.4, 39 origins), **+3.1%** for core CPI (t 0.6, 39), **+1.2%** for PCE (t 0.4, 42) and **+6.6%** for core PCE
  (t 1.5, 42). Core PCE clears the wage-term bar, but the challenger as a whole is 7.8% less accurate than the
  headline ensemble, so **no headline forecast changes**. In the leader test the production & nonsupervisory wage is
  now the top-ranked leader for all four targets, but its held-out gains (3–8%, none for core CPI) rest on only
  10–14 recent origins. All four claims are *not supported*: the strongest YoY correlations sit at −2 to −16 months,
  so prices lead or move together. Full table in [[Average Hourly Earnings as a Leading Indicator of Inflation (September 2026)]].
- **First result (data through 2026-09-10):** the wage term adds +0.0% (CPI), +2.2% (core CPI), +1.0% (PCE) and +5.4%
  (core PCE, t 1.1) against the no-wage twin, so every headline forecast is unchanged. The full study is
  [[Average Hourly Earnings as a Leading Indicator of Inflation (September 2026)]]: wages move with inflation but do
  not lead it. *(Superseded the same day by the audited result above: that build's twin trained on 9–11 extra
  months at its own AR order, so its "wage gain" mixed in a sample difference.)*
- Also fixed on the way: bare "cpi" routed to UK CPI; "predict X from Y" ignored the named leader; buttons re-resolved
  series by name (core PCE landed on the spliced series — *fixed later on 2026-09-11: INFL:PCE / INFL:CPCE are now
  FRED mirrors*); "employment report" fuzzy-matched GDP exports.
- **Code audit (2026-09-11), all fixed in the 15:59 build.** An adversarial review replicated every number and found
  these defects in this change (plus minor wording issues). (1) Forecast buttons send series ids, and any id containing "lead" (USLEAD:ISM,
  USLEAD:UMCSI and eight more) was read as a correlation request, so the forecast buttons on the default chart failed.
  Intent words are now read with the ids blanked out. (2) The 26 AUTO ids that contain spaces answered for a sibling
  series; ids are now matched whole, longest first. (3) The new group label's wage words sent "predict core cpi from
  wages" to the quarterly ECI, which the monthly leader test cannot use. The label is fixed, and a quarterly match now
  falls back only to a monthly series from the same curated concept; otherwise the page says the series is quarterly.
  (4) Leaders were ranked on gains over different AR baselines, which put UMich sentiment ahead of the wage series
  for CPI and PCE despite a higher selection-window error on the same origins. They are now ranked on one common
  baseline. (5) The "jobs report" shortcut swallowed forecast, anomaly and breakdown questions. (6) The no-wage twin
  was not nested, (7) the claim scan differenced only one side, which manufactured CPI's "+16m" wage lead, and (8) the
  skill chips showed the wage challenger's direction-hit rate beside a different winner. Fixes 6–8 were already in
  place for the audited result.

## Chart-to-message layer (added 2026-07-16, per the chart-to-message-mapper method)
The main chart is a **message-driven exhibit**: an auto-composed **action title** above it states the takeaway
of whatever is charted (salience-ranked: records → stretch (|z|≥2) → turning patterns → streaks → strongest
pair relationship), with exactly **one gold highlight** — regenerated on every selection/transform/range/zoom.
Toolbar toggles: **Trend** (OLS fit per series over the visible window, muted dashed, slope/yr in the legend)
and **Turns** (prominence-filtered local peaks ▲ / troughs ▼ in a single gold accent; the strongest gets the
ONE callout, e.g. "peak Feb 2020"). Both persist in the URL hash and are excluded from value tags, hi/lo
markers and CSV export.

## Data integrity — base-year splices and unpublished months (added 2026-09-11)
Found while testing average hourly earnings as a price lead; fixed in `tools/wb_explorer_data.py` and
`tools/build_wb_explorer.py` (build of 2026-09-11 15:43, vhash b0646f7547aa). The GDP and IP splices the break
guard then found were fixed in the 16:19 build (vhash 4206c88b8f57).
- **PCE base-year splice (fixed).** Workbook 15's *PCE All Items* and *PCE All Items Less F&E* sheets switch from
  2012=100 to 2017=100 at 2021-02: a fake one-month move of −5.4% (PCE) and −7.1% (core). It broke every YoY,
  lead-lag scan, ADL test and forecast across that month (core PCE YoY for 2021-06 read −4.0% instead of +3.9%).
  The older segment is also a pre-2023-revision vintage, so rebasing it by the overlap ratio would still leave
  YoY up to 0.30pp off (164 of 799 months by more than 0.05pp). INFL:PCE and INFL:CPCE therefore now carry the live
  FRED values (PCEPI, PCEPILFE) as **mirrors** of LEI:PCEPI / LEI:COREPCE. They keep the same ids, so bookmarks and
  journal calls still resolve; they are listed in the Inflation group and counted once everywhere else. Verified:
  INFL:CPCE YoY equals LEI:COREPCE YoY to 0.000pp over all 799 months (core PCE YoY 2021-06 now +3.86%), and the
  workbook's post-2021 segment matches FRED within 0.06%. If FRED is unreachable, the build keeps the workbook series
  with the splice chain-linked by estimate and says so in the unit.
- **CPI October 2025 (left as a gap).** BLS never collected or published October-2025 CPI or household-survey data
  (the federal shutdown); FRED has no value for CPIAUCSL, CPILFESL, food, energy, rent or the unemployment rate.
  Headline CPI already showed the gap. Workbook 26's core CPI carried 330.7305, the exact midpoint of September and
  November, which faked an October print. The build now drops any value in a registered no-print month (`NO_PRINT`),
  so both series carry the same honest gap.
- **Every engine now keys by calendar month.** The chart's YoY/MoM, the Monitor, the claim scans and the wage
  challenger were already date-keyed. The forecast tournament, ADL leader engine and decomposition were not: they
  worked on the hole-skipping monthly array, so across a gap a two-month change was read as one month. That
  included the Manufacturing PMIs' 2014-12 → 2026-04 gap, treated as a single month. They now run on a calendar
  grid with the gap left empty. Any difference, lag or scored origin that touches the gap is dropped, and the
  smoothers treat a missing month as prediction-only. The anomaly sweep's Δ12m, the `>jobs` payrolls m/m and the
  "5y trend" slope were fixed the same way. Regression-tested in the page against the pre-fix engines on the same
  data: 398 of 458 forecasts, all 11 hole-free ADL targets tested and every hole-free decomposition are identical,
  and all 60 forecasts that changed have calendar holes. Visible effects: headline CPI's forecast winner moves from
  RW + drift (5y) to ARI(p,1), and the 24 Manufacturing PMIs and US26:IR% now show no forecast, because they cannot
  be backtested across their gaps.
- **Break guard (new).** Every build now scans monthly and quarterly base-referenced series (indexes and
  chained/real levels; diffusion indexes are skipped) for isolated jumps. A move is flagged when it is more than 6σ
  from its neighbours, measured against the more volatile of the year before and the year after, and also more
  than 3σ against the series' own history. A plain "6σ against history" rule missed four IP splices and flagged
  about 80 real moves, mostly COVID. Flags go to the build log and onto the series itself (a `breaks` list and a ⚠
  note in the unit shown on the page); the data is not altered. Known shocks (WWII 1939-09, the 1987 crash,
  Katrina/Rita 2005-09, fiscal-cliff income timing 2012-12/2013-01, COVID 2020-03..06) are logged as events, not
  flagged. **It currently flags 11 unfixed splices, all verified against FRED:**
  - workbook 10: real GDP, consumption and government at 2016-Q3 (+14% to +17%, chained-2012 to chained-2017 dollars);
  - workbook 12, industrial production: total, manufacturing, mining, materials and construction at 2017-09
    (−4.3% to −8.7%), consumer goods and mining at 2012-01, and construction at 2008-01 (+29%).

  YoY and period changes across those points are wrong until the series are re-sourced. *(Superseded by the 16:19
  build: all 11 are re-sourced from FRED, along with three GDP splices the guard could not see; the guard now flags 0.
  See the next bullet.)*
- **GDP and industrial-production splices (fixed in the 16:19 build).** Each of the 14 GDPC / IPC sheets equals its
  FRED series (ratio 1.0000) only from its latest splice on: 2016-Q3 for real GDP, consumption and government,
  2017-Q3 for investment, exports and imports, and 2017-09 for all eight IP series. Before that, each sheet holds an
  older base year and an older vintage, so rebasing would still leave YoY wrong (the PCE finding again). Beyond the
  guard's 11, the ratio test found more splices:
  - Investment, exports and imports change base inside a two-quarter hole (2017-Q1/Q2) in their sheets, and the
    guard compares adjacent periods only.
  - Utilities and business equipment splice at 2017-09 by less than their own noise.

  The newest values were stale too. 2–7 of each IP sheet's latest months lag FRED's revisions (business
  equipment's June YoY was 1.4pp off), and government held a typed 3999.0 for 2025-Q3 (FRED: 4014.983).
  **The fix:** `gdp_ip_from_fred()` keeps the ids, because bookmarks, journal calls and claims key on them. It
  replaces the values with the live FRED series from each sheet's first period: GDPC1, PCECC96, GPDIC1, EXPGSC1,
  IMPGSC1, GCEC1; INDPRO, IPMAN, IPMINE, IPUTIL, IPCONGD, IPBUSEQ, IPMAT, IPB54100S. The "Construction" sheet is
  construction *supplies*; IPB54100S is the only IP series it matches. Each build re-measures where every sheet
  agrees with FRED and writes that into the unit. A pairing is used only if the sheet matches FRED over at least
  12 periods. If FRED is down, the build keeps the workbook series, chain-links its detectable jumps by estimate
  and says so. **Verified:**
  - YoY equals FRED YoY to 0.000pp on all 14 series, both in the catalogue and in the page's embedded data. Before
    the fix, 29–81% of periods were more than 0.05pp off, and the worst errors reached 28.7pp.
  - The guard flags 0 splices. Its only IP events are COVID (2020-04) and Katrina (2005-09).
  - Investment, exports and imports regain the two missing 2017 quarters, and IP gains July 2026.

  **Knock-ons:**
  - The CEI proxy's fake −1.21% month at 2017-09 is gone (+0.04%).
  - The capacity-utilization test in [[Indicator Register — Grant Handbook mapped to live series]] re-measures
    at r +0.946 (was +0.907).
  - [[Macro Insights]] re-ranks its IP correlation shifts and analogs at its next refresh.

## Layout v3 — one page, section bar, Now strip, chart-first Lab (2026-09-15)

*Supersedes the two-tier sticky toolbar and the analyst-above-chart placement of the 2026-09-12 redesign
below; everything else in that record still holds.* Template and CSS only — the data pipeline, the chart
engine and all ten Desk Analyst engines are untouched (verified: the answer HTML of all 10 canned questions
is byte-identical before and after).

**What changed**
- **One scrolling page with a slim section bar.** The second toolbar tier is gone. A single 49px sticky bar
  carries eight `data-wx-nav` jumps (Now · Lab · Monitor · US Leading · Global · COT · COT Reports ·
  Scorecards) plus Ask, with scroll-spy highlighting. Jump targets land 61px from the top — the bar height
  plus 12px — instead of the 126px overshoot the old `scroll-padding-top` + `scroll-margin-top` stacking gave.
- **"Now" strip.** Five tiles at the top answer *what moved* before any clicking: the page opens on a read,
  not on an empty chart. The band reserves its height so the Lab does not jump when the tiles arrive, and
  releases it if nothing renders.
- **Chart first.** The main chart starts at 587px on a 1366×768 screen (it used to open below the fold), with
  its own toolbar — `＋ Series` (drawer), transform, range, and a "Chart tools" disclosure for the rest.
- **Series browser as a drawer.** The permanent sidebar that squeezed every section into a column is now a
  left drawer (Escape closes it, focus moves to its search box, focus leaving it closes it). Report sections
  are full width.
- **Answer under the chart.** The Desk Analyst answer renders 16px below the chart it explains (it used to sit
  above it); its close button sticks under the section bar while a long answer is read.
- **Readability and phones.** Sub-11px text fell from 21.3% of the page's characters to 5.5%; at 390px the
  page no longer scrolls sideways (`scrollWidth === innerWidth`) — the culprits were the absolutely-positioned
  chart-tools panel and a `<select>` sized to its longest option.
- **Keyboard and screen readers.** Section landmarks with headings, focus moved to the landing section's first
  *visible* heading, Enter/Space on every `role="button"` chip and row, visually-hidden toolbar group labels,
  navy focus rings on light surfaces (gold on the active navy row).

**Verification** (headless Edge over CDP plus a real browser, on the live file): all 78 contract ids present,
no duplicates, 10/10 charts drawn, 58 sparkline tiles non-empty, 14 interaction probes pass, 8/8 section jumps
at 61px, deep links (`#s=…&m=…&r=…`) restore state, zero console errors — at 1366×768 and again at 390×844
(re-run 2026-09-16). The probes live in `tools/explorer_regress.js` (functional/layout) and `tools/cdp_shot.js`
(scrolled screenshots), with the id contract in `tools/explorer_ids_baseline.json`. Artifact edition
republished (Version 8). Full record in [[log]] under `[2026-09-15] redesign`.

## Redesign — hierarchy, toolbar, analyst hero (2026-09-12)

The page template was redesigned for appeal and ease of use without touching the JavaScript or any data: a proper type scale (13px body), a two-tier sticky toolbar (four segmented chart controls / an "On this page" jump strip), exits moved to a top-right nav, the long subtitle and tips folded into native `<details>`, the Desk Analyst input made the hero with its engine description moved below it, and the four dark sections given a 20px gold-ruled header and 32px rhythm. The change is guarded by an id/class contract check and was verified functionally and geometrically in the browser. Full record in [[log]] under `[2026-09-12] redesign`.

## Engineering honesty (accumulated fixes)
- **Gap-honest transforms**: YoY/MoM/Δ are date-keyed with lag tolerance — pairs across data holes drop
  (visible line breaks), never mislabeled; net-balance series use point diffs; MoM blank on quarterlies.
- **Calendar-grid engines (2026-09-11)**: the forecast tournament, ADL engine and decomposition now apply the same
  rule, via `gridMonthly()`; see *Data integrity* above.
- **Learned memory can no longer outvote the concept map (2026-09-11)**: the Desk Analyst's `agLearn` counted
  every query word, so after a few core-CPI questions the token `cpi` pointed at core CPI (count 7). That +6
  memory boost beat the curated 5-vs-4 headline-first order, and "forecast cpi" / "what predicts cpi" quietly
  answered with core CPI; bare `pce` answered with core PCE. Intent words did the same damage on their own: a
  learned `predicts` → core CPI hijacked "what predicts cpi" even with `cpi` exempt. Now concept words, country
  words and intent words (`INTENT_RX`) are neither learned nor boosted from memory (`memTok`), so counts
  already stored in a browser go inert without a reset. Descriptive words still learn: "underlying" taught ×4
  → core CPI. Checked in a Node harness on the extracted page script: the fixed source passes all 26 checks,
  including end-to-end `agRun` sessions; the unfixed source fails 15 of them.
- **The theme post-processor used to flip dark pages light on its second run (2026-09-14)**: `apply_lp_theme.py` decided LIGHT vs DARK from `--bg:` in the page, but a page it had already themed carries an *empty* `<style id="lp-theme">` marker and its `else True` fallback then called it light — so a second run without a rebuild gave the Explorer and Workbook Charts centred table cells, square cards and lower-contrast muted text. It now reads the existing marker block: filled means LIGHT, empty means DARK. Checked idempotent over three consecutive runs on one dark and one light page (byte-identical), and across all 55 light dashboards.
- **freq bug fixed**: weekly series had been classified daily (claims "YoY" was a 4.8-year change).
- **Rename-proof**: all workbook paths resolve through `tools/xlfind.py find_wb()`; Excel-locked files read
  via a shadow copy (CopyFileW); the >9-month honesty guard **excludes** dead workbook series from the catalog
  rather than tagging them (`wb_explorer_data.py`: "dead data excluded, not just flagged"), so **no series in
  the 2026-09-19 build carries a STALE name tag** (0 of 456) and the ⛔ STALE-series warning never fires. One
  catalogued series is still older than 9 months — GDPFC:REAL (last 2025-06) — because it comes from the live
  NY Fed Outlook-at-Risk feed, which the workbook guard does not cover. *US26 IR%, the old example, is no
  longer stale: it runs to 2026-08 again, though its 2017-09 → 2025-01 hole is still open, which is why it
  still shows no forecast.*
- Flush chart alignment (`bounds:'data'`, `offset:false`), dynamic header counts, US-text-date parsing.

## Related
[[Macro Insights]] (analytics + deep-links into this) · [[Interactive Macro Charts]] · [[Dynamic Macro Panel]] ·
[[PTMI Trading Dashboard]] · [[2026 Trading System — Operating Manual]]
