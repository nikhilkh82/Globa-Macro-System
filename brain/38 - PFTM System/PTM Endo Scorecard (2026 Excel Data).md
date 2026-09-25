---
title: PTM Endo Scorecard (2026 Excel Data)
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "PTM US endo from the 2026 Excel workbooks: 19 drivers on LEVEL (z) + TREND (6m momentum); the 2026-09-19 rebuild reproduces 2026-09-11 exactly at +12.9, Mildly Inflationary / Reflation-Overheating, but is pre-hike."
tags: [global-macro, ptm, endo, business-cycle, excel-data, macro-indicators, decision-support]
data_vintage: "user 2026 Excel workbooks (raw/2. Macro Indicators/2.8 Updated Detailed Macro Indicators)"
sources: 1
updated: 2026-09-19
---

# PTM Endo Scorecard — from your 2026 Excel data

The PTM "Global Macros" **endo** (single-country inflationary/deflationary bias) scored **directly from the user's
updated-to-2026 Excel workbooks** rather than live FRED — the macro core of the [[PFTM Full Trading System]].
Built 2026-06-25 at the user's request ("use recent [Excel] data to build the whole system").

## How it works
- **Reader** (`tools/xl_macro.py`): for each driver, opens the specific 2026 workbook, finds the data sheet
  (substring match), auto-detects the date + value columns, collapses to monthly, and returns the series. Robust to
  the folder's heterogeneous layouts (TOC/weights front sheets, extra leading columns, `.xlsm`).
- **Trend-aware scoring:** each driver gets a **level** score (z vs its own Excel history, capped ±2σ ×5 → ±10;
  ISM/NMI as diffusion vs 50) **and** a **trend** score (6-month-momentum z) → a **combined = 60% level + 40%
  trend**, signed for inflation impact (rates / unemployment / jobless-claims inverse). So an indicator that is
  extreme *and* worsening scores more than one that is merely extreme. Sum = endo bias; growth axis vs inflation
  axis places the cycle quadrant.
- **Turning-point patterns:** each driver is tagged *Rising / Rising (accelerating) / Rolling over / Falling /
  Falling (accelerating) / Bottoming / Flat* from its 3m-vs-6m change, with a ↑/↓ momentum arrow.
- **Charts (from the 2026 files):** a 36-month **trend sparkline per driver** (small multiples), a **level-vs-trend
  score decomposition** (stacked), group totals, and the growth/inflation quadrant.

## 19 drivers read (all current to 2026)
*Superseded 2026-09-11: the prints below are the 2026-06-25 build (as of 2026-06-25); the 2026-09-11 rebuild's prints are under "Live read — 2026-09-11" below.*

CPI 4.17% YoY · Core CPI 2.82% · PCE 3.77% · PPI 13.1% · M2 +5.4% · Fed Funds 3.62% · 10Y 4.55% · ISM mfg 54.0 ·
ISM svcs 54.5 · U-Mich 49.8 *(build snapshot; latest print 44.8 — 0.1st pctl of 73y)* · NFIB 95.3 · building permits · retail sales +4.9% · industrial production · durable
goods +17% · nominal GDP · NFP · unemployment 4.3% · initial claims 226k.

## Live read — 2026-09-19 (current)
*Supersedes the 2026-09-11 read below: today's rebuild reproduces its every figure exactly, but two of its conclusions are qualified here — its "inflation rolling over" call (not confirmed by the August FRED prints) and its "nominal GDP is a laggard" line (the row is real GDP, and Q2-2026 is the latest published quarter). Source: `Endo Excel/endoexcel_latest.json`, generated 2026-09-19 15:47 (as_of 2026-09-19).*

- **Endo combined +12.9 (level +9.2) / ±190 → Mildly Inflationary**; **Reflation / Overheating** (growth axis
  +0.56, inflation axis +0.89). **19 of 19 drivers scored, 10 rising / 9 falling.** Group totals, every driver
  print, every score and every pattern are identical to 2026-09-11.
- **Why nothing moved: none of the 14 driver workbooks has been saved since 2026-09-07** (newest: Durable Goods,
  2026-09-07 16:53; oldest: Industrial Production 2026-08-07, ISM Services 2026-08-12, Retail Sales 2026-08-15).
  The inflation workbook's PPI sheet still marks August as not yet released (it came out 10 Sep). This read is
  therefore **pre-hike and pre-August-inflation**.
- **FLAG — the Fed Funds row is stale after the hike.** It still reads 3.63% (Sep obs, from a workbook saved
  2026-09-07) and scores +0.9 *Bottoming*. The Fed raised 25bp to a **3.75-4.00%** target range effective
  2026-09-17 (EFFR 3.88% on 17 Sep; 3.63% through 16 Sep), and the ECB raised its deposit rate to 2.50% (from
  2.25%) effective 16 Sep. The 10Y row's 4.78% (Sep) also predates the daily FRED prints of 5.01% (16 Sep) and
  4.94% (17 Sep). Both rows are scored inversely (higher rates = disinflationary), so their scores will fall when
  the yields workbook is updated.
- **FLAG — August FRED prints do not confirm the 2026-09-11 "inflation rolling over" call, and the PPI row is not
  the all-commodities index.** The row labelled *PPI (all commodities)* reads the workbook sheet of that name, whose
  series header is PPI Final Demand: Finished Goods (NSA): +5.51% y/y in July. FRED PPI all-commodities was +8.70%
  (Jul) and **+9.85% y/y (Aug)**, +0.96% m/m. August CPI rose to +3.35% y/y (Jul +3.30%), +0.40% m/m. Core CPI
  eased to +2.45% y/y (Jul +2.47%), but its 3-month annualised pace turned up to 1.97% from 1.64% in July; that is
  still below 2% and below the y/y rate. Core PCE is +3.34% y/y (Jul).
- **Other workbook prints now behind FRED:** retail sales +4.93% (Jul) vs FRED **+6.01% y/y (Aug)** and +1.24% m/m
  (FRED Jul +5.03%); industrial production +1.14% (Jun) vs **+1.42% y/y (Aug)**; initial claims 206k (Aug) vs
  **196k (week of 12 Sep)**, 4-week average 203.25k. Unemployment 4.1% (Aug), M2 +5.41% (Jul) and PCE 3.7% (Jul)
  agree with FRED.
- **Label error (not fixed):** the *Nominal GDP* row reads sheet `US_GDP`, whose series is GDPC1, i.e. **real**
  GDP. Its 2.1 (2026-04 obs = Q2-2026, the latest published quarter) equals FRED real GDP +2.10% y/y (Q2-2026), so
  the row is neither nominal nor lagging.
- **Cross-validation re-run:** the live-FRED endo ([[PTM Global-Macro Dashboard (Endo + Exo)]],
  `PTM Macro/ptmmacro_latest.json`, generated 2026-09-19 15:33) reads **+20.5 / ±200, Mildly Inflationary,
  Reflation / Overheating** (growth +0.77, inflation +1.40). The regime and quadrant are the same. Its inflation axis
  is higher because it already carries August CPI (3.35%) and PPI all-commodities (9.85%). It too still reads Fed
  Funds 3.63% (monthly, Aug), so neither endo reflects the hike yet. The FRED-backed US Endogenous Excel template,
  recalculated today, reads +19 *Mildly Inflationary* (was +9 *Neutral / Balanced* on 2026-09-09); its Inflation
  category is +4 (was -12).
- **Regime context:** both major central banks tightened in the same week that the energy shock re-intensified. The
  Fed's first hike (to 3.75-4.00%, effective 17 Sep) and the ECB's second move (to 2.50%, effective 16 Sep) came as
  WTI rose to $107.02 and Brent to $130.80 (15 Sep), with August PPI at +9.85% y/y. Demand is firm, not fading:
  retail sales +1.24% m/m, payrolls +162k, claims 196k. The curve flattened (10Y-2Y +0.33 on 15 Sep → +0.25 on
  18 Sep), and markets absorbed the hike: credit had already retraced on 16 Sep (HY OAS 2.70, CCC 10.76) and VIX
  fell to 15.44 on hike day. The Excel endo's *Mildly Inflationary* label points the same way, but its inflation
  and rates rows describe July and early September, not this week.

## Live read — 2026-09-11
*Supersedes the 2026-06-25 read below: +19.5 combined (level +15.2), growth axis +0.64, inflation axis +1.69, 13 rising / 6 falling (as of 2026-06-25). Source: `Endo Excel/endoexcel_latest.json`, generated 2026-09-11 09:20.*

- **Endo combined +12.9 (level +9.2) / ±190 → Mildly Inflationary**; **Reflation / Overheating** (growth axis
  +0.56, inflation axis +0.89). **All 19 of 19 drivers scored — 10 rising, 9 falling.** Regime label and quadrant
  are unchanged from 2026-06-25; the total is lower and the inflation axis has roughly halved.
- **Group totals:** Inflation +6.3 · Employment +3.9 · Growth & Activity +1.8 · Leading Surveys +1.0 · Money &
  Rates +0.9 · Sovereign -1.0. Biggest scores: PPI +4.8, ISM mfg +3.5, unemployment +3.4, durable goods +2.7,
  ISM services +2.5; biggest drags: U-Mich -7.1, Core CPI -1.5, NFP -1.3, nominal GDP -1.3, 10Y -1.0.
- **FLAG — the 2026-06-25 "inflation re-accelerating" trend story below is overturned.** CPI (3.3% YoY), PCE
  (3.7%) and PPI (5.51%) are now **Rolling over** and Core CPI (2.47%) is **Falling (accelerating)**: 3-month
  momentum is negative on all four (CPI -0.48, Core -0.28, PCE -0.07, PPI -0.95) though 6-month momentum is still
  positive on CPI / PCE / PPI. Sentiment turned too: U-Mich is **Bottoming** (51.7, Aug — still the biggest drag,
  level z -2.27) and NFIB and ISM Services are **Rising (accelerating)**, where the 2026-06-25 read had them
  Falling (accelerating) / Falling (accelerating) / Rolling over.
- **Driver prints (last obs):** CPI 3.3% YoY · Core CPI 2.47% · PCE 3.7% · PPI 5.51% (all Jul) · M2 +5.41% (Jul) ·
  Fed Funds 3.63% (Sep) · 10Y 4.78% (Sep) · ISM mfg 54.62 (Aug) · ISM svcs 54.1 (Jul) · U-Mich 51.7 (Aug) ·
  NFIB 99.5 (Jul) · retail sales +4.93% (Jul) · durable goods +11.95% (Jul) · unemployment 4.1% (Aug) · initial
  claims 206k (Aug). Laggards: nominal GDP (last obs 2026-04), industrial production (2026-06). Spot-check against
  the 2026-09-08 FRED snapshot agrees: CPI 3.3% YoY (Jul), unemployment 4.1% (Aug), effective Fed Funds 3.63%.
- **The 2026-09-07 and 2026-09-08 builds were empty — 0 of 19 drivers scored — and are not reads.**
  `tools/xl_macro.py` built each workbook path as `os.path.join(XLDIR, name)`; after the user filed every workbook
  into a topic subfolder (2026-08), all 19 rows returned "missing file". The build still completed, so
  `endoexcel_latest.json` carried n = 0, combined +0.0 and the default *Strongly Inflationary* label. Fixed
  2026-09-11: the loader now resolves each workbook with `tools/xlfind.find_wb`. A guard added the same day refuses to
  overwrite `endoexcel_latest.json`, the dashboard or the build note when fewer than 10 of 19 drivers score, and
  an empty endo now reads *No data* instead of *Strongly Inflationary*.
- **Two registry rows corrected in the same rebuild:** NFIB now reads the **national** index
  (`20. NFIB_Small_Business_Optimism_Index_Regions.xlsx` / 'SBO Index National') instead of the Construction
  industry sheet, so do not compare its 99.5 with the 95.3 in the list above; Initial Claims reads the renamed
  `4.  Jobless_Claims_Initial_Continuing_2026.xlsx`.
- Cross-validation against the live-FRED endo ([[PTM Global-Macro Dashboard (Endo + Exo)]]) was not re-run for
  this rebuild.

## Current read (2026-06-25)
- **Endo combined +19.5 (level +15.2) / ±190 → Mildly Inflationary**; **Reflation / Overheating** (growth axis
  +0.64, inflation +1.69). **13 of 19 drivers rising, 6 falling.**
- **The trend overlay sharpens the story:** CPI / Core CPI / PCE / PPI are all **Rising (accelerating)** (inflation
  axis +1.13 → +1.69 once momentum is added — inflation re-accelerating), while **U-Mich and NFIB are Falling
  (accelerating)** (sentiment deteriorating) and ISM Services is **Rolling over**.
- **Cross-validates the live-FRED endo** ([[PTM Global-Macro Dashboard (Endo + Exo)]]) — same regime, confirming
  the Excel reads are sound.

## Output
`Endo Excel/PTM Endo Scorecard (2026 Excel Data).html` (signed driver bars, group totals, growth/inflation
quadrant) + note + `endoexcel_latest.json` (consumed by the PFTM System dashboard for its regime line).

## Caveats
US endo only (the data the user updated to 2026); z-scores use each series' full Excel history (incl. 1970s–80s
high inflation), which can make current readings look low vs history. Decision-support / education — **NOT
investment advice.**

## Related
[[PFTM Full Trading System]] · [[PTM Global-Macro Dashboard (Endo + Exo)]] · [[The Global Macros Framework]] · [[Global Macro Brain]]
