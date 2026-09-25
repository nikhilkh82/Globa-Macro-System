---
title: 2026 Trading System — Operating Manual
category: pftm-system
type: meta
data_asof: 2026-07-01
summary: "The start-here map of the Excel-driven PFTM trading system: every dashboard (what it answers / tool / data), the data flow, the one-command refresh (refresh_2026_suite.ps1), provenance, and what is audited vs data-gated."
tags: [global-macro, operating-manual, map, index, pftm, excel-data, dashboards, start-here]
data_vintage: "US macro: 2026 Excel · COT: live CFTC · prices: live Yahoo"
sources: 1
updated: 2026-07-01
---

# 2026 Global Macro Trading System — Operating Manual

The single **"start here"** map of the Excel-driven, PFTM-based global-macro trading system built in folder 38. It
turns the `Global Macro Trading Strategy.md` skill file + the user's 2026 macro workbooks into an actionable book
across **indexes, major FX pairs and commodities**, with charts/trends/patterns and a decision funnel.

> **Decision-support / education only — NOT investment advice.** Account & risk %s are illustrative.

## Start here — one command
```powershell
powershell "tools\refresh_2026_suite.ps1"      # rebuilds the whole suite (~150s); or tools\build_all_2026.py
```
Then open **`Global Macro Trading System.html`** (the project-root **Main Dashboard** / front door) — live regime &
book KPIs + one-click cards to every dashboard, grouped by purpose (Decide &amp; Trade · Understand the Macro ·
Validate). (`tools/main_dashboard.py`.) Everything regenerates from the Excel + live COT/Yahoo, so run the refresh
whenever data changes; the Main Dashboard's KPIs and links update automatically.
*(Python gotcha on this machine: the `python` alias hits the Windows Store shim — the `.ps1` resolves the real
interpreter `AppData\Local\Python\pythoncore-3.14-64\python.exe` automatically.)*

## The dashboards (what each answers)
| Dashboard | Answers | Tool | Data |
|---|---|---|---|
| **Main Dashboard** (`Global Macro Trading System.html`, project root) | *The front door* — live KPIs + one-click cards to every dashboard | `main_dashboard.py` | all engine JSONs |
| **[[Global Macro Hedge Fund Strategy (Memo)]]** | *The written strategy* — regime, patterns, 98-yr history, per-asset theses, playbook | `hf_strategy_memo.py` + `bull_bear.py` | all engine JSONs + Bull_Bear 1928→2026 |
| **[[Cross-Country Endo & Divergence Backtest]]** | *The 7-economy scorecard + does divergence predict FX?* (honest backtest) | `cc_endo.py` + `cc_backtest.py` | live FRED (guarded) + 2026 PMIs |
| **[[PTMI Trading Dashboard]]** | *The Instutrade course on your data* — V4 return distributions + all 26 workbooks mined for patterns | `ptmi_sweep.py` | 2.8 workbooks + Bull_Bear 1928→2026 |
| **[[Chart Room]]** | *The setup behind each ticket* — candles + Keltner + live entry/stop/target lines | `chart_room.py` | Yahoo daily + engine levels |
| **[[Global Macro Trading Dashboard]]** | *What do I trade now?* The skill's 4 modules → actionable tickets | `gm_trading_dashboard.py` | endo + COT |
| **[[Macro + COT Trade Signals]]** | The per-trade engine — endo bias × COT × technicals | `macro_cot_trades.py` | Excel endo + live COT + Yahoo |
| **PFTM Trade Console** (in [[Macro + COT Trade Signals]]) | *How was each trade arrived at?* the decision funnel | `pftm_console_report.py` | reads the engine |
| **COT Cross-Check** (in [[Macro + COT Trade Signals]]) | *Do the engine's COT signals match my own data?* | `cot_excel.py` | your 10-yr Excel COT vs live CFTC |
| **[[PTM Endo Scorecard (2026 Excel Data)]]** | *What's the US macro bias?* trend-aware endo (level+momentum+pattern) | `xl_macro.py` | 2026 Excel |
| **[[Dynamic Macro Panel]]** | *Explore any series* — interactive pick/transform/range/overlay | `macro_panel.py` | 2026 consolidated panel |
| **[[Macro Indicators Hub]]** | *Your PowerPoint analysis* — graph slides + commentary, navigable | `macro_hub.py` + `ppt_extract.py` | 2026 PPT decks |
| **[[PFTM Full Trading System]]** | Gate-keeping → ATR ranks → sizing (Kelly) → self-awareness stats | `pftm_system.py` | endo + Yahoo |
| **[[Analyst System — Live Cockpit (June 2026)]]** | *The hub* — links every dashboard as a drill-down | `build_analyst_system.py` | all |

## Data flow
```
2026 Excel workbooks ──► xl_macro (US endo, trend-aware) ─────────┐
   (2.8 Macro Indicators)  global_growth (cross-country PMI) ──────┤
                          macro_panel (consolidated 29-series)     │
                          ppt_extract (PowerPoint graph slides)    ├─► dashboards
live CFTC COT ───────────► macro_cot_trades (bias×COT×technicals) ─┤     (+ cockpit)
live Yahoo prices ───────► technicals / ATR / Keltner ────────────┘
```

## Data provenance & vintages (honest)
- **Current-from-Excel (2026):** US macro drivers (CPI/PCE/PPI, ISM, employment, GDP, yields, M2, permits, NFIB,
  retail, IP, durables, claims, U-Mich); the consolidated 29-series panel; the PowerPoint graph decks; Services PMI
  (US/UK/EZ/JP/AU…) + China PMI + EU ESI; Commodity_Prices_2026; COT Metals/Energy (13).
- **Live (not from Excel):** CFTC COT positioning, Yahoo prices/ATR/technicals — used because they're the freshest
  authoritative source (and the Excel COT file **13.1 is frequently locked/open**).
- **Stale → excluded:** Global *Manufacturing* PMIs (2017), Exogenous_AUD_USD (2015). Never scored by this engine. *(Both since rebuilt elsewhere on current data: the PMI workbook is maintained to Jun-2026, and the AUD/USD exogenous is scored live — EXO −4, LOW-conviction short; see [[Australia Endogenous Driver Analysis (July 2026)]].)*

## The PFTM skill file, mapped
1. **Macroeconomic Scorecard** → US GDP/CPI/Rates/Employment +1/0/−1 (Module 1 of the trading dashboard).
2. **Cross-Asset Matrix** → bias per instrument + the cross-country Global-Growth panel (Module 1b/2).
3. **Technical Execution** → daily trend / Keltner / ATR entry-stop(2·ATR)-target(2R), align-gate (Module 3).
4. **Risk & Portfolio** → 1% conviction-scaled sizing, 2×ATR stops, **correlation clustering** (Module 4).

## What's audited · what works · honest limits
- **Adversarially audited (lean workflows):** the Macro+COT trade engine (COT signs, FX pair-inversion, entry/stop/
  target geometry, sizing — all verified, *no backwards trades*), the PFTM sizing/Kelly, and the endo/exo. See
  [[the-dv01-both-legs-flattener-bug]] for the discipline that drives it (inline checks ≠ the formal audit).
- **Data-gated (not effort-gated):** a **full cross-country Big-Four** (US/EZ/UK/JP/AU on GDP/CPI/Rates/Employment)
  needs foreign macro the folder doesn't carry → kept US-full + cross-country growth-only + COT-led FX. An
  **Excel-COT repoint** needs `13.1` closed → engines use live CFTC (same data).
- **Snapshots drift:** every "current book" is a point-in-time snapshot; the **dashboards are the source of truth**
  (the book changed 5 → 11 TAKE on the 2026-07-01 refresh as positioning turned broadly extreme-short — watch the
  USD-theme concentration: 5 pairs = one bet).

## Related
[[Global Macro Trading Dashboard]] · [[Macro + COT Trade Signals]] · [[PTM Endo Scorecard (2026 Excel Data)]] · [[Dynamic Macro Panel]] · [[Macro Indicators Hub]] · [[PFTM Full Trading System]] · [[Cross-System Synthesis — What Works]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
