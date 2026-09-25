---
title: Global Macro Brain
category: meta
type: meta
data_asof: n/a
summary: "The Map of Content: three start-here doors, an intent-based navigator, one entry page per folder, the link hubs, and the mixed-vintage caveat — the curated map; the generated [[index]] is the full catalog."
tags: [global-macro, moc, home, index]
data_vintage: "curated entry map — restructured 2026-09-12; page data vintages live on the pages themselves (data_asof)"
sources: 0
updated: 2026-09-12
---

# Global Macro Brain

**What this is** — a persistent, interlinked Obsidian wiki that encodes the *Global Macros* global-macro / long-short hedge-fund strategy: the method, every macro domain, the live reads, a 20+-system strategy lab, and the live PFTM trading system, all maintained by an LLM agent under [[_Vault Schema & Conventions]]. This page is the **curated map**. The **full catalog** — every page, its type, one-line summary and data date, one table per folder and a second view by type — is the generated [[index]]; it cannot drift because it is rebuilt from page frontmatter on every sync. Do not re-catalog pages here.

> **Data-vintage caveat (read first).** This is a *mixed-vintage* vault. Roughly half its pages are a **historical teaching corpus** (datasets from ~2013—2022) and half are **live** (re-pulled from FRED, CFTC, BoC/StatCan, EIA and the desk's own engines). Every page declares which it is in `type:` and dates its data in `data_asof:`; a `live-read` older than 45 days or a `strategy-system` older than 120 is flagged in [[_Brain Health]]. Never quote a figure without checking the page's `data_asof`.

## Start here — three doors

| You want to | Open |
|---|---|
| **Trade the live system** — dashboards, scorecards, tickets, the one-command refresh | [[2026 Trading System — Operating Manual]] |
| **Learn the method** — the end-to-end top-down process and the trade-idea funnel | [[The Global Macros Framework]] · [[Trade Idea Generation Process]] |
| **Read the market now** — the cross-asset regime on live data, and the unified cockpit | [[Macro Regime - Live (June 2026)]] · [[Analyst System — Live Cockpit (June 2026)]] |
| **Define a term** | [[Glossary]] |

## Navigate by what you need

| Question | Go to |
|---|---|
| What regime are we in, and what does the business cycle say? | [[Macro Regime - Live (June 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[Macro Regime Snapshot]] (historical corpus) |
| Chart or query any of the 458 series | [[2026 Workbook Explorer]] (the Desk Analyst answers plain-English questions) · [[Macro Insights]] |
| Which indicators lead, and by how much? | [[Leading Indicators]] · [[Conference Board LEI & Leading-Lagging Map]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] |
| Which strategies actually work? | [[Cross-System Synthesis — What Works]] (the capstone over the whole lab), then the systems in [[index#15 - Strategy Systems]] |
| Size, stop and manage risk | [[Risk Management]] · [[Portfolio Management]] · [[Average True Range (ATR)]] |
| Central banks and the policy stance | [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]] · [[Monetary Policy Tools, Transmission & Communication]] |
| Commodities and the cycle | [[Commodities — Supply, Demand & the Cycle]] · [[Energy, Metals & Agriculture — the Sub-Complexes]] · [[Cyclical Commodities]] |
| FX bias for a pair | [[FX Endogenous-Exogenous Framework]] · [[USD & G10 FX]] · the live [[UK Endogenous Driver Analysis (July 2026)]] / [[Australia Endogenous Driver Analysis (July 2026)]] scorecards |
| Positioning and sentiment | [[Commitment of Traders (COT)]] · [[VIX & Implied Volatility]] · [[Bull & Bear Markets]] |
| Country tearsheets | [[USA Country Analysis]] · [[Major Economies Analysis]] |
| Deep history and base rates (240 countries, multi-century) | [[00 - GMD Overview & Structural Edge]] |
| How this vault works, and what changed when | [[_Vault Schema & Conventions]] · [[log]] · [[_Brain Health]] · [[Dashboards - Brain Map]] |

## Folders — one entry page each

Nineteen top-level folders. Each row names the page to open first; the folder's full contents are in [[index]].

| Folder | Holds | Entry page |
|---|---|---|
| `00 - Home` | This map, the generated index, the append-only log, the schema, auto health + dashboard map | [[index]] |
| `01 - Framework` | The method, the trade-idea funnel, the endo/exo toolkit, the econometric frameworks, curriculum map, glossary | [[The Global Macros Framework]] |
| `02 - Macro Indicators` | GDP, leading / coincident / lagging, money, inventories, commodities, measurement and release-frequency references | [[Leading Indicators]] |
| `03 - Rates & Bonds` | Sovereign yields, the curve as a recession signal, corporate credit | [[Yield Curve & Recession Signals]] |
| `04 - FX` | The endo-exo framework, the G10 dollar page, live UK + Australia scorecards | [[FX Endogenous-Exogenous Framework]] |
| `05 - Positioning & Sentiment` | COT, implied vol, bull/bear history | [[Commitment of Traders (COT)]] |
| `06 - Equities & Sectors` | Sector rotation, screening, spread trades, the LEI-circularity caveat | [[Sector Analysis & Rotation]] |
| `07 - Technical & Statistical` | ATR, return distributions, price action | [[Average True Range (ATR)]] |
| `08 - Portfolio & Risk` | Portfolio construction, risk, sizing, performance metrics | [[Risk Management]] |
| `09 - Synthesis` | Live regime page + cockpit, the historical snapshot, the desk's engine write-ups, the strategy-lab capstone | [[Macro Regime - Live (June 2026)]] |
| `10 - Global Macro Dashboard` | *Meta despite the name:* session records, decisions, open items, operating specs | [[Decisions & Rationale]] |
| `11 - USA Country Analysis` | The live USA report (Word/PDF/HTML) + companion page | [[USA Country Analysis]] |
| `12 - Major Economies Analysis` | The seven-economy comparative report | [[Major Economies Analysis]] |
| `13 - Macro Cycles & Asset Returns` | The cyclical-strength → asset-returns notebook | [[Macro Cycles & Asset Returns]] |
| `14 - Global Macro Database` | Eight GMD chapters + dashboard + its own build log | [[00 - GMD Overview & Structural Edge]] |
| `15 - Strategy Systems` | Every backtested strategy replication — free data, point-in-time, audited, nulls published | [[Cross-System Synthesis — What Works]] |
| `16 - Central Banks & Monetary Policy` | Policy rates, balance sheets, transmission, communication | [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]] |
| `17 - Commodities` | The commodity cycle and its sub-complexes | [[Commodities — Supply, Demand & the Cycle]] |
| `38 - PFTM System` | **The live, actively-traded system** — one companion page per dashboard; numbered 38 to mirror `raw/` | [[2026 Trading System — Operating Manual]] |

## Browse by page type

Every page carries a `type:`; the generated [[index#By type]] lists them grouped. In one line each: **live-read** asserts current figures (45-day clock) · **dashboard-page** documents one HTML/Excel tool (45-day clock) · **strategy-system** is a backtest with an audit verdict (120-day clock) · **domain** teaches a macro domain from the historical corpus · **deep-dive** is a long-form research chapter · **reference** is a glossary, register or convention · **meta** is a record of the vault itself.

## Hubs — the most-linked pages

Where the graph converges (inbound links at the 2026-09-12 lint): [[The Global Macros Framework]] (74) · [[Risk Management]] (40) · [[Analyst System — Live Cockpit (June 2026)]] (40) · [[Leading Indicators]] (35) · [[Trade Idea Generation Process]] (31) · [[USD & G10 FX]] (28) · [[Macro Regime Snapshot]] (28) · [[Macro Regime - Live (June 2026)]] (27). A new page should link *to* at least two of these and be linked *from* its folder's entry page.

## How this Brain is maintained

The LLM-Wiki pattern: the agent owns this markdown layer; the raw datasets in `../raw/` are immutable. **Ingest** a source → update the relevant pages, set their `data_asof` and `summary`, log it. **Query** the [[index]] → drill in → synthesise with `[[wikilink]]` citations → file durable answers back as pages. **Refresh** with `python tools/auto_refresh.py` (also hourly from Task Scheduler). **Lint** with `python tools/lint_brain.py` (must report 0 broken, 0 orphans; flags data-bearing pages past their clock). **Sync** with `python tools/brain_sync.py` (regenerates [[index]], [[Dashboards - Brain Map]], `brain_index.json`). **Log** every operation as `## [YYYY-MM-DD] <verb> | <title>` in [[log]]. The full ritual and the dated-record rule are in [[_Vault Schema & Conventions]].
