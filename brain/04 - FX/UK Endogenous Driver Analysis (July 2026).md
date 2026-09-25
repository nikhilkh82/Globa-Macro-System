---
title: UK Endogenous Driver Analysis (July 2026)
category: fx
type: live-read
data_asof: 2026-09-19
summary: "Second live endo country scorecard (15 drivers, ±150) on ONS/FRED/BoE data: +27 Mildly Inflationary (Explorer asof 2026-09-18; drivers sum +29) — CPI 2.9%, debt/GDP 101%, gilt ~4.8%; PMIs unverified; no decisive US gap"
tags: [global-macro, uk, endogenous, fx, scorecard, live, ons, boe]
data_vintage: "LIVE — ONS / FRED / BoE via Workbook Explorer (asof 2026-09-18): consumer confidence through Aug-2026; CPI / core CPI / PPI / M4 through Jul-2026; unemployment / AWE / debt/GDP / Bank Rate / gilt through Jun-2026; govt balance 2025 annual (v1 built 2026-07-03; v2 refreshed 2026-07-04)"
sources: "raw/2. Macro Indicators/2.8 Updated Detailed Macro Indicators/UK_Endogenous_Driver_Analysis.xlsx (+ 28. …_2026.xlsx v2)"
updated: 2026-09-19
---

# UK Endogenous Driver Analysis (July 2026)

**What it is & why it matters** — The endo framework's **second full country scorecard**: a UK workbook mirroring the US Endogenous Driver Analysis's exact logic and layout (21 sheets, per-driver data tabs, embedded threshold→score LOOKUP tables, auto-calculating overall score), populated with **live UK data from ONS / FRED / Bank of England**. Stage 1 of the [[FX Endogenous-Exogenous Framework]] can now be run *live* for both legs of GBP crosses (GBP/USD endo differential directly computable). Built with a reproducible pipeline: `refresh_uk_data.py → uk_data_cache.json → build_uk_workbook.py → .xlsx`.

## Current read — UK Endo Score **+27** (scale −150…+150, 15 drivers) → *Mildly Inflationary*

> Live Explorer Score-Engine card (`wb_explorer.json` · asof 2026-09-18 · built 2026-09-19T15:47:15 · vhash 6d3783a9bace; `scorecards.endo[cc=UK]` “United Kingdom (wb 28)”, state MILDLY INFLATIONARY). Print dates (Explorer UK series, last obs): consumer confidence 2026-08; CPI / core CPI / PPI / M4 2026-07; unemployment / AWE / debt/GDP / Bank Rate / gilt 2026-06; govt balance 2025 annual. PMIs and building permits are manual workbook cells with no dated series in the Explorer UK group; the Explorer's `PMI` / `SVCPMI` groups do carry dated UK series (Mfg PMI 52.5, Services PMI 48.8, both 2026-06) that do not match the card's manual 51.7 / 52.5, so the two PMI cells are UNVERIFIED. The **+31 on −150…+170** below is the retired v1 z-score-lineage rubric — kept for provenance, superseded by this v2 card. *Superseded 2026-09-19: card stamp asof 2026-09-09 · built 2026-09-10T13:10:33 · vhash 2df203da0e45.* *Superseded 2026-09-11: card stamp asof 2026-07-24.*

| Group | Driver | Latest | Score |
|---|---|---|---|
| Leading | UK Manufacturing PMI | **51.7** | +0 |
| Leading | UK Services PMI | **52.5** | +2 |
| Leading | Consumer Confidence (OECD) | **-14** | -2 |
| Leading | Building Permits / Housing (k) | **84.1k** | +4 |
| Money | M4 Broad Money (YoY %) | **4.433% YoY** | +0 |
| Rates | Bank of England Bank Rate | **3.73%** | +0 |
| Sovereign | 10-Year Gilt Yield | **4.796%** | +0 |
| Inflation | CPI Rate % (ONS) | **2.9%** | +0 |
| Inflation | Core CPI Rate % (ONS) | **2.6%** | +0 |
| Inflation | PPI Output (YoY %) | **3.127% YoY** | +2 |
| Inflation | PPI Input (YoY %) | **4.796% YoY** | +2 |
| Employment | Unemployment Rate (ONS) | **4.9%** | +5 |
| Employment | AWE Earnings YoY % (ONS) | **3.5% YoY** | +2 |
| Sovereign | Govt Debt/GDP % (ONS) | **101%** | +6 |
| Sovereign | Govt Balance % GDP (GMD annual) | **-4.541% of GDP** | +8 |
| **TOTAL** | **15 drivers** | | **+27** of ±150 |

*Re-verified 2026-09-19 (Explorer asof 2026-09-18, rebuilt 2026-09-19): all 15 driver values and scores above are unchanged, as are the print dates; the card still reads **+27** MILDLY INFLATIONARY, and the drivers still sum to **+29** (the 2-pt gap noted below persists in this build).*

*Superseded 2026-09-11: TOTAL +29; Mfg PMI 48 (−2), Services PMI 50.9 (+0), confidence −16.75, M4 4.19% YoY, gilt 4.942%, CPI 2.8%, PPI output 3.989% YoY, PPI input 8.659% YoY (+4), AWE 4.6% YoY (+4), debt/GDP 100.2% (as of 2026-07-24). Re-verified unchanged: building permits 84.1k (+4), Bank Rate 3.73%, core CPI 2.6%, unemployment 4.9% (+5), govt balance -4.541% of GDP (+8).*

*Source check 2026-09-11 (computed): the 15 driver scores above sum to **+29**, but the Score Engine TOTAL row the Explorer carries reads **+27** — a 2-pt gap inside the source build (four scores moved and net to zero — Mfg PMI −2→+0 and Services PMI +0→+2, PPI input and AWE +4→+2 each — so the driver sum is unchanged at +29). The headline follows the published TOTAL; read the card as +27…+29 until the workbook total is re-derived.*

**The UK picture:** a stagflation-tinted read — contracting manufacturing and depressed consumers (deflationary pulls), but sticky ~2.8% inflation, rising input PPI (+8.7%), 100%+ debt/GDP and a **gilt yield near 5%** (the standout stress signal, scored −10).

> **Flag 2026-09-11 (Explorer asof 2026-09-09): parts of this read are overturned — prose kept for provenance.** Manufacturing is no longer contracting (Mfg PMI **51.7**, Services **52.5**); input-PPI inflation slowed to **4.796% YoY** (prior 8.659%) and AWE to **3.5% YoY** (prior 4.6%); CPI **2.9%** is still sticky and debt/GDP **101%** still above 100%. The gilt (**4.796%**) scores **+0** on this v2 card — the “scored −10” stress signal is not on it (the gilt row read +0 at the 2026-07-24 read too; likely a v1-rubric carry-over, not re-verified). Consumers remain depressed (confidence **-14**). The state label (Mildly Inflationary) is unchanged.

> **Rubric note (two variants).** A second UK workbook (`UK_Endogenous_Driver_Analysis_2026.xlsx`, built 2026-07-03 in the US folder-26 Dashboard/Score-Engine format by `tools/build_uk_endo.py`) was **completed to the course's read-only UK reference sheet layout** — all 18 reference rows: Mfg/Services PMI + confidence + permits (seeded with verified Jun-26 values), M4, Bank Rate, 10Y gilt, CPI/core/PPI-output/PPI-input, unemployment + earnings, and the full 6-row sovereign block (debt 100.2%, **balance −4.5% of GDP from GMD 2026_06 annual actuals**, plus Interest/GDP · Liquidity · BoE-APF%GDP as clearly-flagged manual rows, excluded from the total until filled — the reference-era values for those are 2021-vintage and were *not* reused). Its contrarian-regime tables now read **+29 "Mildly Inflationary"** (refreshed 2026-07-04: the stale OECD M1-proxy that scored M4 at −10 was replaced with **true BoE M4** — IADB LPMAUYN, +4.2% YoY to May-2026 — and ONS revised unemployment to 4.9; the v2 workbook also gained the Analysis-3.0 statistical layer + 36 charts via `tools/uk_endo_fetch.py + uk_endo_build.py`) vs this v1 workbook's z-score-lineage **+31** — same inputs, different scoring philosophy; read the UK endo as a **+29…+31 mildly-inflationary range**, the same kind of rubric spread as the US +29/+35. *Superseded 2026-09-11: v2 +29 (as of 2026-07-04) — the v2 card now reads **+27** (Explorer asof 2026-09-09); the v1 +31 is not carried in the Explorer and was not re-verified.*

Versus the US endo (**+36** on −150…+160, the live wb-26 card; the early-July build variants read +29 automated / +35 toolkit): **no decisive endo differential — GBP/USD direction hangs on the exo (relative) drivers — carry, BoP, relative growth.** *Re-verified 2026-09-11 (Explorer asof 2026-09-09): US card still **+36** on −150…+160; UK now **+27** on ±150 — computed 22.5% vs 18.0% of scale; the no-decisive-differential conclusion stands.* *Re-verified 2026-09-19 (Explorer asof 2026-09-18): US wb-26 card still **+36**, UK still **+27** — the no-decisive-differential conclusion stands. The wb-26 card still scores the Fed rate at a pre-hike 3.63% (monthly FEDFUNDS was 3.63% in Jun, Jul and Aug-2026; the card carries no observation date), so it does not yet reflect the 2026-09-17 hike to a 3.75-4.00% range (EFFR 3.88% on 2026-09-17). The automated FRED-backed US template (`scores_cache.json`, recalculated 2026-09-19) now reads **+19** "Mildly Inflationary" (was +9 "Neutral / Balanced" on 2026-09-09), the same state label as the UK card.*

## How it stays live
- **Live series** (auto-refresh): ONS CPI/core/PPI/unemployment/earnings/debt/deficit (mm23, ppi, lms, pusf), FRED 10Y gilt / Bank Rate / consumer confidence / M4.
- **Manual cells** (flagged in-sheet): S&P Global/CIPS PMIs, housing approvals, BoE balance sheet, derived interest/GDP + liquidity — paste-in updates auto-score.
- Refresh: `py refresh_uk_data.py && py build_uk_workbook.py` in the indicators folder. The overall score is a live formula (recalcs on open).

## See also
[[FX Endogenous-Exogenous Framework]] (the method) · [[Endo-Exo Toolkit & Workflow]] (US templates + this workbook's place in the workflow) · [[USD & G10 FX]] (the tradeable universe) · [[Macro Regime - Live (June 2026)]] (the US-side read). GBP-cross ideas flow through [[Trade Idea Generation Process]].

*Educational; not investment advice. All values are the workbook's live computed readings as of the build date.*
