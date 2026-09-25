---
title: GMD Folder Log
category: gmd
type: meta
data_asof: 2026-07-03
summary: "Append-only build record for the GMD folder: the 2026-06-21 ingest of GMD v2026_03 (package, 12-panel dashboard, 8 pages, 55/56 verified) and the 2026-07-03 refresh to v2026_06 (US debt 122.3% = 99th pctile)."
tags: [global-macro, gmd, log]
updated: 2026-07-03
---

# Global Macro Database — folder log

Append-only build record for `14 - Global Macro Database/`. Prefix convention: `## [YYYY-MM-DD] type | title`.

## [2026-06-21] ingest | Global Macro Database (GMD v2026_03) — Python package, dashboard, 8 wiki pages

- **Source.** Global Macro Database, Müller, Xu, Lehbib & Chen (2025), NBER WP 33714 — 240+ countries/territories, **1086–2030** (incl. IMF projections), **80 variables**. Installed the official `global_macro_data` Python package from the attached source (`raw/10. Global Macro Database/Global-Macro-Database-Python-main`); verified `gmd()` end-to-end (filtered country/variable pulls, the crisis chronology, local caching to `~/.global_macro_data`). Current release confirmed **2026_03** (2026_06 not yet published).
- **Access layer.** `tools/gmd_access.py` wraps the official package with a fast cached-CSV path for bulk analysis (`panel()`, `series()`, `latest()`, `official()`). The distribute CSV is cached at `raw/10. Global Macro Database/GMD_2026_03.csv`; a full Excel extract sits at `raw/10. Global Macro Database/Global Macro Database 2026_03.xlsx`.
- **Design.** A 4-lens design panel (long-run historian / crisis economist / cross-country comparativist / PM) proposed analyses exploiting GMD's structural edge over the FRED-based system (multi-century history, 240-country breadth, crisis chronology, full government-finance); synthesized into a 12-panel dashboard spec + 12 headline findings.
- **Computation.** `tools/build_gmd_analysis.py` computes all 12 panels deterministically from raw GMD → `gmd_analysis.json` (no fabrication). Panels: (1) US own-history percentile gauges; (2) G7 debt level-vs-percentile; (3) crisis chronology 1800–2017; (4) banking-crisis rGDP event study (343 episodes); (5) 2024 fragility scorecard (184 countries); (6) DM-vs-EM convergence (+IMF tail); (7) debt→forward-5y-growth base rate; (8) two-roads-out-of-war-debt deleveraging; (9) hyperinflation universe; (10) twin-deficit map; (11) REER pre-crisis signal; (12) debt at sovereign default.
- **Verification.** Adversarial workflow independently re-derived every headline number from raw data: **55/56 exact match, 0 mismatches**, HIGH confidence (the lone "close" was a method artifact in the verifier's own forward-match, not a code error). Disclosure notes folded into the dashboard (P7 exact year+5 matching rule → n=13,131; P3 sum-of-flags vs 1,117 distinct country-years).
- **Dashboard.** `tools/build_gmd_dashboard.py` → `Global Macro Database Dashboard.html` (self-contained Chart.js v4.5.1, light theme). Headless-verified: 0 console errors. Linked from the [[Analyst System — Live Cockpit (June 2026)]] drill-downs and the Brain [[index]].
- **Pages.** Eight wiki pages written (`00`–`07`) covering overview/edge, percentile framing, crisis chronology, aftermath base rates, current snapshot, DM/EM + debt-growth, long-run regimes, and currency collapse — drafted from verified numbers and lint-checked for fabrication and broken links.

## [2026-06-21] note | Key findings (all computed from raw GMD)

- US public debt/GDP **121.0% = 98th percentile** of its own history since 1790, while the US real long rate sits at only the **28th percentile** since 1798 — a debt-extreme / cheap-real-rate tension.
- UK debt **103% = only its 52nd percentile** (twice carried >250%) vs US **121% = 98th** — proven debt capacity differs sharply across the G7.
- **1,117 country-years (1800–2017)** carry ≥1 crisis flag (362 banking, 547 currency, 278 sovereign); 2008 had 25 banking crises.
- Across **343 banking crises**, median real GDP recovers from 100 (t−1) to **113.5 by t+5** — a measurable but non-catastrophic scar.
- Sovereign default debt/GDP **median 61% (IQR 31–94%)** — no universal safe-debt threshold.
- Forward 5y real growth declines with debt: **3.67% (<30%) → 2.97% (>120%)** across 196 countries.

## [2026-06-21] build | GMD context panel wired into the live cockpit

- Added a **"Historical context — where today sits vs centuries"** card to the [[Analyst System — Live Cockpit (June 2026)]] Decision Desk (`tools/build_analyst_system.py`), reading the static `gmd_analysis.json` (no new live calls). Surfaces five GMD chips — US debt/GDP percentile (**98th**), US real-rate percentile (**28th**), CPI percentile (**67th**), the debt→growth prior at >120% debt (**~3%/yr** vs 3.7% at <30%), and the banking-crisis recovery (median GDP **113/100** by t+5) — plus a framing note and a link to the GMD dashboard. Rebuilt + headless-verified the cockpit: GMD context loads, **0 console errors**. The live decision surface is now long-run-history-aware.

## [2026-07-03] refresh | GMD vintage 2026_03 → 2026_06

- **New release.** Downloaded the **GMD 2026_06** vintage (20.4 MB, **158 variables** — up from 80; the varlist doc still lists the 79 core codes) and re-ran the full pipeline: `tools/build_gmd_analysis.py` re-computation → `gmd_analysis.json` → dashboard rebuild (`Global Macro Database Dashboard.html`).
- **Headline shifts.** US public debt/GDP now **122.3% = 99th percentile** since 1790 (was 121.0% / 98th); **Japan revised down to 236.1%** debt/GDP, 96th percentile (was 251.2% / 97th — vintage revision); the 2024 fragility top-5 is now **Sudan, Timor-Leste, Lebanon, Venezuela, Argentina** (Lebanon and Venezuela in, Zimbabwe and Maldives out; coverage 184→190 countries); the debt→forward-5y-growth buckets shift to **3.57% (<30%) → 2.77% (>120%)** on n=13,374 / 197 countries.
- **Smaller revisions.** G7 table: GBR 101.2%/54th, ITA 134.7/93rd, CAN 111.3/94th (FRA, DEU unchanged). Banking-crisis event study n=343→345 (median t+5 112.8, t+6 115.9). Hyperinflation universe 107 episodes / 42 countries (>1000%: 68 unchanged). REER pre-crisis signature +7.8% vs +0.6%. Debt-at-default IQR 32–94% (median 61%, n=181 unchanged). DM/EM convergence 71.4→102.1 vs 45.2→74.6. US 1946→1981 deleveraging 121.5→41.2. UK spending ratchet 6.9%→44.6% (2029 incl. IMF projection).
- **Unchanged.** Crisis chronology totals identical (362 banking / 547 currency / 278 sovereign; 1,117 distinct country-years; peak years 1994=35, 1992=33, 2008=32, 1931=30). **Story unchanged everywhere** — every page's thesis (record US debt at cheap real rates, no safe debt level, debt drags growth with a >60% break, DM↔EM convergence, inflate-out as the modern exit, REER overvaluation as the pre-crisis tell) survives the vintage intact. Updated the eight wiki pages (00–07), the Brain [[index]] rows, and frontmatter to v2026_06.
