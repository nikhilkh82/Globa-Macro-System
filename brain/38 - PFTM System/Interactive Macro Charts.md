---
title: Interactive Macro Charts
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "48 key indicators (9 categories), one full-history interactive chart each at recon-pinned workbook coordinates; 2026-09-19 build: 0 skipped, 0 STALE, obs to 2026-09-04; 5 ranges x 4 transforms, z compare tray."
tags: [global-macro, dashboards, interactive-charts, ism, pmi, cpi, housing, umcsi, industrial-production, new-orders, 2026-excel]
data_vintage: "2026 Excel workbooks (2.8, 23 files); build 2026-09-19 15:42 - latest obs 2026-04-01 (GDP) to 2026-09-04 (weekly BBB/CCC), 37 of 48 end 2026-07/08"
sources: 23
updated: 2026-09-19
---

# Interactive Macro Charts — the key indicators, full history

**`Macro Charts/Interactive Macro Charts.html`** (tools: `macro_charts.py` engine → `macro_charts.json` →
`macro_charts_report.py`). Built for: *"create interactive charts for key macro indicators like ISM, PMI, CPI,
Building Permit, Housing Data, UMCI, IP, New orders and other excel files."*

> Decision-support / education only — **NOT investment advice**.

## What it is
**48 indicators, one full-size interactive chart each**, extracted at exact workbook coordinates from **23 of the
2.8 workbooks** (coordinates pinned by a 10-agent recon workflow, 2026-07-07 — no fuzzy detection at build time).

**Current build (generated 2026-09-19 15:42):** 48 series charted · 0 skipped · 0 STALE · 46,450 obs across 9 categories; latest obs run from 2026-04-01 (Real GDP, quarter-start dated) to 2026-09-04 (BBB spread / CCC yield, weekly, in-progress month) — 37 of 48 end in 2026-07/08. The rebuild added no observations (series payload identical to the 2026-09-16 rebuild; obs count and span match the 2026-09-10 build), so the charts lag live data — WTI still ends 2026-08-31 (live WTI $107.02 on 15 Sep) and Effective Fed Funds ends 2026-06 at 3.63%, before the Fed's 25bp hike to 3.75-4.00% effective 17 Sep. The daily rate series lag furthest: 10y Treasury and 2s10s both end 2026-07-15 (4.62% and +0.40pp) against 4.94% on 17 Sep and +0.25pp on 18 Sep. The adversarial audit under Honesty notes dates from the 2026-07-07 build.
*Superseded 2026-09-19: build stamp "generated 2026-09-10 13:10" and "21 of the 2.8 workbooks", the build label "2026-09-11 build" (summary: and the Honesty-notes staleness line), and data_vintage "2026 Excel workbooks (2.8); freshest series 2026-07, most 2026-05/06" / sources: 21 (the 2026-09-19 build's source fields name 23 distinct 2.8 files — the two the old count missed, "34. Global Services PMI.xlsx" and "37. US Macro_data_Summary 2015 to 2026.xlsx", carry no number prefix in the src strings but resolve into 2.8; tools/macro_charts.py is unchanged since 2026-08-14, so this is a corrected count, not a build change) — listed in [[log]].*
*Superseded 2026-09-11: data vintage "freshest series 2026-07, most 2026-05/06" (as of 2026-07-07).*

Every chart has:
- **5 ranges** (1Y/3Y/5Y/10Y/Max — Max reaches 1913 for PPI, 1939 for payrolls, 1948 for ISM/unemployment)
- **4 transforms** computed client-side from the level series: Level · YoY (Δ1y **points** for PMIs/rates/spreads,
  % for prices/flows) · 1-period change · **z-score** (full-history μ/σ)
- **NBER recession shading** (global toggle), **threshold lines** (50 = PMI breakeven, 0 = spreads/net-balance)
- stat chips: latest · YoY/Δ1y · z · 3m-vs-6m **pattern** (same classify() as the PTMI sweep) · **STALE** badge
- **Compare tray**: overlay up to 6 indicators as monthly z-scores (e.g. ISM vs UMich vs claims)
- category chips + live search; charts init in time-budgeted batches (no observer dependence)

## Categories (9)
Business Surveys (ISM mfg PMI/New Orders/Employment · ISM services ×3 · Philly Fed · CFNAI · NFIB (fresh, last 2026-07-28)),
Inflation (CPI/Core/PCE/Core-PCE/PPI-1913/CPI-Energy), Housing (Permits · Starts-1959 · Completions · XHB),
Consumer (UMCSI + Expectations · Retail headline — components excluded as hand-typed/synthetic), Industry & Orders
(IP + Mfg · CapUtil · Durables + ex-Transport · Real GDP), Labor (NFP · Unemployment · weekly Claims ×2 · Mfg
payrolls), Money/Rates/Credit (M2 · Fed Funds-1967 · 10y · 2s10s daily · **BBB credit spread** (sign-flipped from the
workbook's 10yr−BBB, labeled) · CCC yield), Global (China PMI + New Export Orders · US Services PMI S&P · EZ
industry/consumer confidence), Markets (S&P-1957 · WTI · Copper · USD TWI — long daily series downsampled to
weekly last-obs, disclosed on the card).

*Superseded 2026-09-11: NFIB **STALE 2020-12** (as of 2026-07-07).*

## Honesty notes
- Levels are extracted; **all transforms derived client-side** — the workbooks' own m/m / y/y columns (decimal
  fractions) are never charted. Fed Funds stored as fraction ×100. GDP is **quarter-start dated** (label says so).
- Staleness: >9 months → STALE badge (none in the 2026-09-19 build — NFIB now reads `20. NFIB_Small_Business_Optimism_Index_Regions.xlsx · SBO Index National`, last 2026-07-28). Retail components rejected — recon found
  placeholder-looking tails; only the clean headline is charted. In-progress months disclosed (BBB spread + CCC yield, last 2026-09-04).
  *Superseded 2026-09-11: STALE badge = NFIB only; in-progress month = XHB (as of 2026-07-07).*
- **Gap-honest transforms** (from the adversarial audit): all YoY/Δ transforms are **date-keyed with a lag
  tolerance** — across a data hole the pair is dropped (visible line break via injected gap markers), never
  silently mislabeled (the corp-bond series have a 2.5-year hole 2021→2023 that an index-offset would have
  charted as "Δ1y"). Compare-tray z uses YoY for trending price/flow indexes (level-z on CPI is just trend age).
- Adversarially verified (5 agents): 3 data-refuters re-extracted **all 48 series → 0 value mismatches** (incl.
  fed-funds ×100 vs FRED, PPI sheet-name trap, BBB sign flip, 2008 crisis spread +7.4pp), a JS-math auditor
  (found the index-offset-across-holes bug → fixed, invariant re-verified over 40,774 points), and an honesty
  auditor (labels/units/disclaimers all confirmed). See log 2026-07-07.

## Related
[[PTMI Trading Dashboard]] (per-workbook cards + patterns) · [[Dynamic Macro Panel]] (pick/overlay explorer) ·
[[PTM Endo Scorecard (2026 Excel Data)]] (the scored bias) · [[Macro Indicators Hub]] (your PPT decks) ·
[[2026 Trading System — Operating Manual]] · [[Global Macro Trading Dashboard]]
