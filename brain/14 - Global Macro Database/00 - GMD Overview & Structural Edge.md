---
title: GMD Overview & Structural Edge
category: gmd
type: deep-dive
data_asof: 2026-06
summary: "Hub page: what GMD is (240+ countries, 1086–2030, 158 vars, crisis dummies, full gov-finance), its four structural edges over FRED, the `global_macro_data` access layer, and the folder ToC; US debt 122% = 99th pctile."
tags: [global-macro, gmd, structural-edge, data-infrastructure, fred]
data_vintage: "GMD v2026_06 (current release; cross-country macro to 2024, IMF projections to 2030)"
sources: "Global Macro Database — Müller, Xu, Lehbib & Chen (2025), NBER WP 33714"
updated: 2026-07-25
---

# GMD Overview & Structural Edge

**What this is:** The top-level hub for the Global Macro Database (GMD) folder — what the dataset is, the four structural edges it holds over the project's FRED-based system, how it is accessed, and a linked map to every sub-page and the interactive dashboard.

## What GMD is

The **Global Macro Database** (Müller, Xu, Lehbib & Chen 2025; **NBER WP 33714**) is a cross-country macro panel spanning **240+ countries/territories**, **years 1086–2030** (including IMF projections), across **158 variables**. It is accessed through the official `global_macro_data` Python package via the `gmd()` call (locally cached), wrapped for this project in `tools/gmd_access.py`.

GMD is not a replacement for FRED — it is the long-history, cross-country, crisis-aware complement. FRED gives high-frequency, US-centric series for the live tape; GMD gives the centuries of context and the 240-country breadth that let us ask "how extreme is *this* by the standard of all recorded history" rather than just "how extreme is this by the standard of the last 60 US years."

## The four structural edges over FRED

| # | Edge | What it unlocks |
|---|------|-----------------|
| 1 | **Multi-century history** | UK nominal GDP from **1086**, US inflation/CPI from **1721**, US public debt/GDP from **1790**, UK debt from **1700**. Own-history percentiles instead of short-sample z-scores. |
| 2 | **240-country breadth** | Full cross-section vs FRED's US-centricity. Enables fragility scorecards, twin-deficit maps, and DM-vs-EM convergence work. |
| 3 | **Financial-crisis chronology** | `BankingCrisis` / `CurrencyCrisis` / `SovDebtCrisis` dummies (Reinhart-Rogoff / Laeven-Valencia lineage) — **absent entirely from FRED**. |
| 4 | **Full government-finance accounts** | Central + general government debt / deficit / revenue / tax over centuries. |

### Edge 1 in one number — US debt is near an all-time high

US public debt/GDP of **122.3%** sits at the **99th percentile** of its own history **since 1790** (n=235). The full own-history percentile work lives in [[01 - Where Today Sits vs History (US & G7 Percentiles)]].

### Edge 3 in one number — crises are the rule, not the exception

Across **1800–2017**, **1,117 distinct country-years** carry at least one crisis flag (banking, currency, or sovereign). The full chronology — including the worst years (1994 = 35 flags, 1992 = 33, 2008 = 32) — lives in [[02 - Crisis Chronology (Banking, Currency, Sovereign)]].

### Edge in one base rate — debt drags forward growth

Pooled across **197 countries** (n=13,374 country-year matches to exact year+5 real GDP), mean annualized forward-5y real growth declines **near-monotonically** with starting debt: **<30%: 3.57%**, 30–60%: 3.37%, 60–90%: 2.91%, 90–120%: 2.99%, **>120%: 2.77%** — a clear break above 60%. The US (122%) and Japan (236%) sit in the top buckets today. Full treatment in [[05 - DM vs EM Convergence & Debt-Growth Base Rate]].

## Coverage at a glance

- **Geography:** 240+ countries/territories
- **Time:** 1086–2030 (history + IMF projections)
- **Variables:** 158 (GDP, prices, rates, FX, full government finance, crisis dummies)
- **Verification:** every figure in this folder was computed from raw GMD by `tools/build_gmd_analysis.py` and independently re-verified — **55/56 metrics exact-match, 0 mismatches**.

## How it is accessed

GMD is pulled through the official `global_macro_data` package's `gmd()` function (locally cached so queries are fast and offline-reproducible). The project wrapper is **`tools/gmd_access.py`**; all the analytics that feed these pages are produced by **`tools/build_gmd_analysis.py`**. The numbers are stable across sessions because they trace to a fixed local cache, not a live API.

## Folder map — table of contents

| Page | What it covers |
|------|----------------|
| [[01 - Where Today Sits vs History (US & G7 Percentiles)]] | US debt/inflation/real-rate vs full own history; G7 debt level-vs-percentile; proven debt capacity differs |
| [[02 - Crisis Chronology (Banking, Currency, Sovereign)]] | 1,117 distinct crisis country-years; banking/currency/sovereign counts; worst contagion years |
| [[03 - Crisis Aftermath & Recovery Base Rates]] | 345-episode banking-crisis GDP aftermath; 181 default episodes, median debt 61%, IQR 32–94% |
| [[04 - Current Cross-Country Snapshot (Fragility & Twin Deficits)]] | 2024 fragility quad; twin-deficit map; most-vulnerable cluster |
| [[05 - DM vs EM Convergence & Debt-Growth Base Rate]] | DM debt converging up toward historically-EM levels, 1995→2024; debt→forward-growth base rate, break above 60% |
| [[06 - Long-Run Fiscal & Monetary Regimes]] | Two roads out of war debt; 1971 inflation-regime break; government-spending ratchet |
| [[07 - Currency Collapse & Early-Warning Signatures]] | Hyperinflation universe; REER pre-crisis overvaluation early-warning signature |

**Interactive dashboard:** [Global Macro Database Dashboard](Global%20Macro%20Database%20Dashboard.html)

## Adjacent folders

- `11 - USA Country Analysis` — US-specific deep dives that draw on Edge 1 long-history context.
- `12 - Major Economies Analysis` — country work that uses the 240-country breadth (Edge 2).
- `13 - Macro Cycles & Asset Returns` — cycle and asset-return studies (the crisis chronology and debt base rates themselves live here in [[03 - Crisis Aftermath & Recovery Base Rates]] and [[06 - Long-Run Fiscal & Monetary Regimes]]).

## How to use this folder

Start here for orientation, then drill into the sub-page that matches the question:
- "Is this level historically extreme?" → [[01 - Where Today Sits vs History (US & G7 Percentiles)]].
- "What does a crisis look like, and how do they cluster?" → [[02 - Crisis Chronology (Banking, Currency, Sovereign)]].
- "Where is the next fault line?" → [[03 - Crisis Aftermath & Recovery Base Rates]] and [[04 - Current Cross-Country Snapshot (Fragility & Twin Deficits)]].
- "What does heavy debt do to growth?" → [[05 - DM vs EM Convergence & Debt-Growth Base Rate]].

For the live macro picture this context feeds into, see [[Macro Regime Snapshot]], [[Macro Regime - Live (June 2026)]], and [[The Global Macros Framework]]; for the instrument-level read-through, [[Government Bond Yields]], [[Yield Curve & Recession Signals]], [[USD & G10 FX]], [[GDP & Growth]], [[Commitment of Traders (COT)]], and [[Risk Management]]. The vault catalog is [[index]]; activity is logged in [[log]]; this folder's own build record is [[GMD Folder Log]].

## What it means for positioning

GMD's edge is calibration, not signal. It tells a macro PM whether today's debt, inflation, real rate, or external imbalance is ordinary or near the edge of recorded experience — and it supplies the base rates (crisis frequency, banking-crisis scars, debt-vs-growth, default thresholds) that consensus, anchored on a short US sample, systematically misjudges. Use it to set priors and size tail hedges, then let FRED-based live data drive the timing.

*Sources & method:* Global Macro Database (Müller, Xu, Lehbib & Chen 2025, NBER WP 33714); figures computed from raw GMD by `tools/build_gmd_analysis.py` and re-verified (55/56 metrics exact-match, 0 mismatches).

*Educational; not investment advice.*
