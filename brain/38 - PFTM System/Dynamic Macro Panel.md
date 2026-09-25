---
title: Dynamic Macro Panel
category: pftm-system
type: dashboard-page
data_asof: 2026-09-24
summary: "Interactive charting dashboard over the US Macro_data_Summary 2015-2026 panel. JSON + HTML rebuilt 2026-09-24; the workbook (saved 2026-08-10) is unchanged: 26 series still end 2026-07, +live Nat Gas $3.182 (2026-09)."
tags: [global-macro, dashboard, interactive, charts, excel-data, time-series, macro-indicators]
data_vintage: "your 2026 consolidated panel (US Macro_data_Summary 2015→2026), workbook columns through 2026-07-15 + live Yahoo NG=F through 2026-09; payload re-read 2026-09-24"
sources: 1
updated: 2026-09-25
---

# Dynamic Macro Panel

A fully **interactive, dynamic** charting dashboard built **from your 2026 Excel time-series** (not images): pick any
series, switch the transform, choose a range, overlay up to four, and read live stats. Built 2026-06-26 ("continue to
build a more dynamic dashboard with charts from the Excel files updated to 2026").

> **Decision-support / education only — NOT investment advice.**

## Source
The user's **`US Macro_data_Summary 2015 to 2026.xlsx`** — a single consolidated daily panel of **26 workbook series**
(18 of them carrying real FRED series ids — `FEDFUNDS DGS2 DGS10 T10Y2Y DGS3MO CPIAUCSL CPILFESL PCEPI PCEPILFE INDPRO
HOUST UMCSENT UNRATE PAYEMS BAA10YM AAA10YM DTWEXBGS DCOILWTICO`; the other 8 are workbook-named columns —
`CPI_YOY ISM_MFG ISM_SERVICES NFP CONSUMER_SENTIMENT HOUSING_STARTS DURABLE_GOODS RETAIL_SALES`), all aligned and
current to **2026-07-15** (`macropanel_latest.json` `as_of`; last monthly bucket **2026-07**, 139 points/series from
2015-01), **plus one live series** — Natural Gas (NG=F monthly close, pulled from Yahoo by the loader;
2016-10→2026-09, 103 points, latest **$3.182** in the 2026-09 bucket) — for **27 series** in total. By category
(the JSON's own `cat` labels): Rates & Curve — Fed Funds / 3M T-Bill / 2Y / 10Y / 2s10s (5); Inflation — CPI /
Core CPI / PCE / Core PCE / CPI YoY (reported) (5); Growth & Activity — Industrial Production / Retail Sales / Durable
Goods / Housing Starts / Housing Starts (alt) (5); Surveys — U-Mich / Consumer Sentiment / ISM Mfg / ISM Services (4);
Labor — Unemployment / Nonfarm Payrolls (level) / NFP (3); Markets — Trade-Weighted USD / WTI Crude / Natural Gas (3);
Credit — Baa & Aaa spreads (2). `tools/macro_panel.py` reads it to monthly series → `macropanel_latest.json` (this build: generated
**2026-09-24 16:11**).

> **Rebuilt again 2026-09-24 — payload refreshed, workbook still frozen, one series moved.** Today's data-layer
> re-run regenerated `macropanel_latest.json` (`generated` **2026-09-24 16:11**, superseding the *2026-09-19 15:51*
> stamp) and `Macro Panel/Macro Panel Dashboard.html` (header now "through 2026-07-15 (built **2026-09-24 16:11**)";
> the file was re-themed afterwards, styling only — the re-theme writes no stamp of its own, so quote the 16:11 header
> the page renders, never the file's mtime). **Structure unchanged**: still 27 series, `as_of` still
> **2026-07-15**, still 139 monthly points per workbook series from 2015-01 and 103 for NG=F, still the same 7
> categories. The cause is still the source file: workbook 37 (`37. US Macro_data_Summary 2015 to 2026.xlsx`) was
> last saved **2026-08-10**, so today's Excel recalc window — which did run, with Excel closed, at 16:15 — extends the
> FRED-backed endo/exo templates but *not* this user-maintained panel. **The one genuine move is Natural Gas**:
> `NATGAS` now reads **$3.182** in the 2026-09 bucket, up from **$2.912** in the 2026-09-19 build and $2.936 in the
> 2026-09-16 one — three different values for the same monthly bucket, which is what a live front-month close in an
> unfinished month looks like. Treat every workbook column on this page as a **July-2026 vintage**, not a current read.

> **Rebuilt 2026-09-19 — payload refreshed, data unchanged.** Today's data-layer re-run regenerated both
> `macropanel_latest.json` (`generated` **2026-09-19 15:51**, superseding the *2026-09-16 09:20* stamp, which is listed
> in [[log]]) and `Macro Panel/Macro Panel Dashboard.html` (its own header now reads "through 2026-07-15 (built
> 2026-09-19 15:47)"; the file was re-themed afterwards, at ~15:59 and 16:09, which changed styling, not data).
> **The content did not move**: still 27 series, `as_of` still **2026-07-15**, still 139 monthly points per workbook
> series from 2015-01 and 103 for NG=F. The cause is the source file, not the loader: workbook 37
> (`37. US Macro_data_Summary 2015 to 2026.xlsx`, resolved via `find_wb`) was last saved **2026-08-10** and is the
> user's own panel, not a FRED-backed template, so recalculating the Excel templates does not extend it (on 2026-09-16
> the Excel COM steps had also been skipped because the user had Excel open). Only Natural Gas is genuinely live
> ($2.936 → **$2.912** in the 2026-09 bucket). Treat every workbook column on this page as a **July-2026 vintage**,
> not a current read.

> **Superseded 2026-09-11.** The 2026-06-26 description read *26 series, current to 2026-06-24*; the rebuilt JSON
> (generated 2026-09-08, `as_of` 2026-07-15) carries **27**. *Initial & Continuing Claims*, listed before, are **not**
> in the rebuilt JSON — the loader's `META` still maps them, so the workbook column is either absent or below the
> loader's 12-numeric-month floor; *Housing Starts (alt)* is carried as its own series; *Natural Gas* is new.

## What's dynamic (`Macro Panel/Macro Panel Dashboard.html`)
- **Series picker** — 27 chips grouped by category (7 categories; was 26 chips before the 2026-09-08 rebuild — the
  27th is Natural Gas); click to overlay up to 4 (auto dual-axis when units differ).
- **Transforms** — Level · YoY % · MoM % · Z-score · Rebase=100 (computed client-side, instantly).
- **Range** — 1Y / 3Y / 5Y / 10Y / Max.
- **Presets** (9) — Yield curve · Policy vs inflation · Inflation (CPI/Core/PCE) · Growth surveys · Activity (IP/Retail) ·
  Labor · Credit spreads · USD vs Oil · Energy (Oil vs Nat Gas). The ninth (energy) came with the NATGAS series in the
  2026-09-08 rebuild; the page listed 8 until 2026-09-11. **Caveat (checked 2026-09-16; still true in the 2026-09-19
  build):** the *Labor* preset still asks for `["UNRATE","JOBLESS_INITIAL"]`, and `JOBLESS_INITIAL` is not among the
  27 series — `preset()` filters with `keys.filter(k=>k in S)`, so the button silently plots **Unemployment alone**.
  Harmless but a one-series preset until claims are restored to the workbook. *Re-checked 2026-09-24: still true in
  today's build — `JOBLESS_INITIAL` is still referenced by the preset and still absent from the 27 series.*
- **Stats strip** — latest, Δ1y (green/red), and range for each selected series.
- **Sparkline grid** — every series as a 5-year mini-chart (`data.slice(-60)`, green if the 60-month change is up, red
  if down); click to focus it in the main chart.
- **Light page, dark charts** (professional finance hybrid): a light UI (white panels, dark-on-light text) with the
  **chart wells themselves dark** (deep-navy `#0d1320`) — the main chart and every sparkline sit on dark canvases with
  a vivid finance series palette (blue/red/teal/amber), dark grids & tooltips, light legend/ticks, and a **highlighted
  zero baseline** on the YoY/MoM/z-score views for instant above/below reading. `animation:false` → instant
  terminal-style redraws; the main chart sits in a fixed-height `.chartbox` wrapper, stable across re-renders — **660px
  in the 2026-09-24 build**, unchanged since 2026-09-16 (the page recorded 440px through 2026-09-11).
- All Chart.js, inlined, offline. `tools/macro_panel_report.py` + `build_macro_panel.py`.

## Data integrity — what the columns actually contain (payload audited 2026-09-16; re-audited 2026-09-19 and 2026-09-24)
Reading `macropanel_latest.json` series-by-series turned up three things a user of this dashboard needs to know
before quoting it (re-read against the **2026-09-24 16:11** payload: all three still hold, and every panel figure
below is byte-identical to the 2026-09-19 15:51 read — the counts of divergent months were recomputed, not carried):

- **`CPI_YOY` is not a YoY series.** It is labelled *"CPI YoY (reported)"* with unit `%`, but its 139 values run
  **234.913 (2015-01) → 332.568 (2026-07)** — CPI **index levels**. It is a second, slightly different CPI vintage
  rather than a duplicate: **94 of 139 months differ** from `CPIAUCSL` (2015-01: 234.913 vs 234.747). Consequence: the
  **Policy vs inflation** preset loads `FEDFUNDS + CPI_YOY` at the *level* transform, so it plots Fed Funds **3.63%**
  (the workbook's July-2026 value, not today's rate — see below) against a **~332 index** on the auto dual-axis. Hit
  **YoY %** to get the comparison the preset name promises.
- **U-Mich and "Consumer Sentiment" are two different columns, not a de-dupe miss.** Both are `index`, both print
  **44.8 @ 2026-07**, but they diverge in **59 of 139 months** (2017-10: 95.1 vs 100.7). Unlike INDPRO / Housing
  Starts, they were left in deliberately.
- **The workbook is the user's own vintage, not a FRED mirror.** For the *same* 2026-07 month the workbook's U-Mich
  reads **44.8** where FRED's `UMCSENT` reads **55.2**, and its `HOUST` reads **1177k** where FRED reads **1239k**
  (FRED re-pulled 2026-09-16). Never cite a figure off this panel as a FRED value. *Flagged 2026-09-19:* that
  **1239k** FRED July leg now needs a re-pull before it is quoted again — today's FRED print is **1,275k** for
  **2026-08** at **-2.6% m/m**, and a month that fell 2.6% m/m cannot print *above* the prior month — yet 1,275k
  sits above that 1239k July, so the July level has moved since the 09-16 pull.
  The workbook-vs-FRED *point* stands; only the FRED side of that one comparison is stale.
  ***Resolved 2026-09-24*** (`HOUST` re-pulled direct): the July leg was **revised up to 1,309k**, so the arithmetic
  now closes — August **1,275k** is **-2.6% m/m** against 1,309k, exactly as the 09-19 flag predicted it had to be.
  Use **1,309k**, not 1,239k, as the FRED July figure. The workbook-vs-FRED gap for 2026-07 is therefore *wider* than
  this bullet originally recorded — **1,177k (workbook) vs 1,309k (FRED)**, a 132k divergence — which strengthens
  rather than weakens the point. U-Mich is re-verified unchanged: FRED's `UMCSENT` still stops at **55.2 @ 2026-07**
  (no August print), against the workbook's 44.8.

The freshness gap that follows from the un-updated workbook (re-checked 2026-09-24 against `tools/macro_pack.json`,
generated 2026-09-24 16:04): live FRED carries **August** CPI (334.131, +3.35% YoY), August payrolls (+162k m/m; level
159,075k) and August unemployment (4.1%), and the Fed's **25bp hike to a 3.75-4.00% target range** (effective
2026-09-17) has held — daily fed funds `DFF` prints **3.88%** every day through **2026-09-22** — while every workbook
column here still stops at **July** (CPI 332.568, payrolls 158,984k, unemployment 4.2%, Fed Funds 3.63%). So the
panel's Fed Funds column is now **25bp** below the live policy rate as well as two months behind it. The gap is
starkest in oil: the *USD vs Oil* and *Energy (Oil vs Nat Gas)* presets end WTI at the workbook's **$69.6** (2026-07),
while live WTI is **$96.41** on 2026-09-22 — a $26.81 gap, though narrower than the $37.42 this page recorded against
the 09-15 spike of $107.02, because crude has retraced. The whole *Rates & Curve* group is stale the same
way, and it has changed *shape*, not just level: the panel's July column reads 2Y **4.26**, 10Y **4.62**, 3M **3.89**
and 2s10s **+0.40**, against live 2Y **4.85**, 10Y **5.11**, 3M **4.19** and 2s10s **+0.26** — all four on the same
**2026-09-23** vintage, which is the date the spread comes from (`macro_pack.json` `T10Y2Y`; its `DGS2`/`DGS10`/`DGS3MO`
legs stop a day earlier at 4.71 / 4.96 / 4.16, where the spread is +0.25, so the legs were re-pulled direct to match).
So the *Yield curve* preset still draws July's steeper **+0.40** curve, not the flatter **+0.26** one.
Among the market series, only the dollar has gone the other way, and by less than before: workbook `DTWEXBGS`
**120.69** @ 2026-07 against **119.51** on 2026-09-18 (the latest H.10 print, up from 118.21 on 2026-09-11), so the
panel now overstates the dollar by 1.18 index points rather than 2.48. Use the panel for *shape and history*; use the
live-read pages for the current print.

## Relation to the other 2026-Excel dashboards
- [[Macro Indicators Hub]] — the *navigable* hub of your PowerPoint **chart images + analysis** by category.
- [[PTM Endo Scorecard (2026 Excel Data)]] — the *scored* trend-aware endo (level + momentum + pattern).
- **This** — the *interactive* raw time-series explorer over the consolidated panel.
- Together: images+analysis (Hub), scores (Endo), and free-form exploration (Panel) over the same 2026 data.

## Notes
Monthly sampling (last obs per month; 139 points/series 2015-01→2026-07 for the 26 workbook series and 103 points
2016-10→2026-09 for the live Natural Gas series — was ~138 points to 2026-06 before the 2026-09-08 rebuild) — clean
and fast for macro trends. Two columns were near-duplicates in the source (INDPRO, Housing Starts) and de-duped; the
rebuilt JSON still carries `HOUST` and `HOUSING_STARTS` ("Housing Starts (alt)") as two distinct series (latest
1177k vs 1410k @ 2026-07). **Not investment advice.**

## Related
[[Macro Indicators Hub]] · [[PTM Endo Scorecard (2026 Excel Data)]] · [[Macro + COT Trade Signals]] · [[PFTM Full Trading System]] · [[Analyst System — Live Cockpit (June 2026)]]
