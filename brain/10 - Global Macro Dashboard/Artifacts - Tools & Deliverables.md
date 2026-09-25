---
title: Artifacts - Tools & Deliverables
aliases: ["Global Macro Dashboard"]
category: meta
type: meta
data_asof: n/a
summary: "Catalog of every tool, export, deliverable, wiki page and environment change created or modified in the 2026-06-19 session: the cycle-dashboard builders, fed_tracker.py, the xlsx/docx/pdf/html exports, scores_cache.json."
tags: [meta, session-record, artifacts, tools, deliverables, 2026-06-19]
data_vintage: "n/a (file catalog)"
sources: 0
updated: 2026-06-19
---

# Artifacts — Tools & Deliverables (2026-06-19)

Catalog of files **created or modified** in the [[2026-06-19 Session - Dashboards, Rebrand & FRED|2026-06-19 session]], with their role. Paths are relative to the project root (`Global Macro Hedge Fund Strategy/`).

## New tools (`tools/`)
| File | Role |
|---|---|
| `tools/build_cycle_dashboard.py` | Pulls 18 business-cycle indicators (FRED + local ISM); prints latest/prev/delta with bps·YoY·MoM·3mo-avg·QoQ-ann transforms. The data backbone. |
| `tools/build_cycle_html.py` | Generates the self-contained interactive **Business Cycle Dashboard.html** (Chart.js inlined): regime banner, KPI strip, 4 signal tables, breadth doughnut, trend charts, Fed Tracker card. |
| `tools/fed_tracker.py` | FOMC-NLP engine — Hawk/Dove score (−10…+10), keyword tracker, statement-vs-statement diff, and the **"FOMC NLP Analysis"** tear-sheet. Writes `fed_tracker_latest.json`. |
| `tools/build_cycle_exports.py` | Extracts the live dashboard data into this folder as **Excel** (`Global Macro Dashboard - Data <date>.xlsx`, 7 sheets) + **Word** (`… - Brief <date>.docx`). |

## Data exports (this folder — `Global Macro Brain/10 - Global Macro Dashboard/`)
| File | Contents |
|---|---|
| `Global Macro Dashboard - Data 2026-06-19.xlsx` | Summary KPIs · Leading · Coincident · Lagging · High-Freq & Liquidity (signal-coloured) · COT Positioning (13 markets) · Scorecards (endo/exo). |
| `Global Macro Dashboard - Brief 2026-06-19.docx` | Narrative brief — exec summary, the 4 indicator tables, cross-asset implications, Fed Tracker, data provenance. |
| `Global Macro Dashboard - Brief 2026-06-19.pdf` | PDF render of the brief (Word→PDF via Word COM; interactive session, no headless hang). |
| `Global Macro Dashboard - Interactive 2026-06-19.html` | Self-contained interactive dashboard (copy of `Monthly Report/Business Cycle Dashboard.html`) — regime banner, KPI strip, 4 signal tables, breadth gauge, trend charts, Fed card. |

## Modified tools (`tools/`)
| File | Change |
|---|---|
| `tools/fred.py` | API key → user's registered key (`ae4a9ac7…`). |
| `tools/cot.py` | +3 markets (NASDAQ/Silver/Nat Gas); "PTM"→"Global Macros". |
| `tools/build_cot_dataset.py` | Rebrand only. |
| `tools/build_dashboard.py` | Fixed `scoreChart()` brace `SyntaxError`; rebrand; **light theme**; `scores_cache.json` fallback in `read_scores()`. |
| `tools/build_endo_template.py` | Rebrand + de-attribution ("Anton Kreil"/course name removed). |
| `tools/build_report.py`, `build_report_pdf.py`, `build_exo_template.py`, `build_library.py` | Rebrand. |
| `tools/refresh_all.ps1` | Now writes `scores_cache.json` from the Excel-recalc step (keeps endo/exo readable by the dashboard). |

## Deliverables (`Monthly Report/`)
| File | Notes |
|---|---|
| `Monthly Report/Business Cycle Dashboard.html` | **New** — interactive 5-section cycle dashboard, light theme. |
| `Monthly Report/Global Macro Dashboard.html` | Bug-fixed, 13-market COT, rebranded, light theme, endo=27 restored. |
| `Monthly Report/Global Macro Weekly Update 2026-06-19.{pdf,docx}` | Regenerated (13 COT markets). |

## Wiki pages (`Global Macro Brain/`)
| Page | Change |
|---|---|
| [[Business Cycle Dashboard - Live (June 2026)]] | **New** synthesis page (5 sections + cross-asset). |
| `01 - Framework/The Global Macros Framework.md` | **Renamed** from `The PTM Framework.md`. |
| [[Macro Regime - Live (June 2026)]] | Positioning section updated for the 3 new COT markets. |
| [[index]], [[log]], [[Global Macro Brain]], [[_Vault Schema & Conventions]] | Rebrand + new-page entries + session log. |
| `10 - Global Macro Dashboard/*` | **New** folder — session-record files + data exports (xlsx/docx). |

## Other root-level files
| File | Notes |
|---|---|
| `scores_cache.json` | **New** — Excel-computed endo/exo scores cache (workaround for openpyxl/`fullCalcOnLoad`). |
| `Automated_Endo_Template.xlsx`, `Endo_Analysis_Template_BLANK.xlsx` | Regenerated (de-attribution) + Excel-recalced. |
| `raw/9. Live Data …/9.6 Positioning (CFTC COT)/*.xlsx` | **13 workbooks** (was 10). |

## Environment changes (this machine only — not synced)
- **Python 3.12.10** installed (winget, user scope) + `openpyxl`, `matplotlib`, `python-docx`.
- User PATH prepended with `%LOCALAPPDATA%\Programs\Python\Python312` (ahead of the WindowsApps alias).
- Task Scheduler job **`GlobalMacroWeeklyUpdate`** registered (Mon 07:00 → `tools/weekly_task.ps1`).

## See also
- [[2026-06-19 Session - Dashboards, Rebrand & FRED]] · [[Decisions & Rationale]] · [[Open Items & Follow-ups]] · [[log]]
