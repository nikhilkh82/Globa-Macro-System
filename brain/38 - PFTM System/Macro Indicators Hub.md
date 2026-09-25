---
title: Macro Indicators Hub
category: pftm-system
type: dashboard-page
data_asof: 2026-09-24
summary: "Command-center unifying the 2026 Excel trend-aware endo scores with the user's 2026 PowerPoint decks; 2026-09-24 rebuild: 19/19 drivers, combined +12.9 of ±190, Reflation/Overheating — but the tiles are still pre-hike."
tags: [global-macro, dashboard, navigation, macro-indicators, excel-data, powerpoint, charts, trends, patterns]
data_vintage: "Excel half LIVE — Endo Excel/endoexcel_latest.json generated 2026-09-24 16:11 (as_of 2026-09-24), though the driver workbooks' own observations still end 2026-07/2026-08; PowerPoint half June-vintage (ppt_manifest.json, file stamp 2026-06-25, 81 graphs / 7 decks)"
sources: 1
updated: 2026-09-25
---

# Macro Indicators Hub

One **navigable command-center** that unifies the user's **2026 macro Excel data** with their **2026 PowerPoint
trend/pattern analysis decks** — every US macro indicator in one place, with a sticky sidebar for easy navigation.
Built 2026-06-25 ("use the updated Excel sheets for 2026 and the PowerPoint charts with trends & patterns and
generate all of it in a dashboard for easy navigation").

> **Decision-support / education only — NOT investment advice.**

## What's in it
- **Sticky sidebar nav** → jump to any category (Inflation · Growth & Activity · Surveys & Sentiment · Employment ·
  Housing · Rates & Money), plus one-click links to the [[Macro + COT Trade Signals]], [[PFTM Full Trading System]]
  and [[PTM Endo Scorecard (2026 Excel Data)]] dashboards.
- **Overview:** the trend-aware endo regime (state, business-cycle quadrant, momentum) + a combined-score bar across
  all 19 indicators.
- **Per indicator (computed live from your Excel, at the workbooks' last save — see the live-data note):** latest
  value, **combined score** (level + 6-month momentum), the
  turning-point **pattern** (Rising/Falling/Rolling-over/Bottoming…), and a **36-month trend sparkline**.
- **Per category (from your PowerPoint):** **only the graph slides** — each chart paired with the analysis text
  from its own slide as a caption (click any thumbnail → full lightbox). Cover / title / branding / agenda /
  disclaimer slides, banners and logos are filtered out.

## Build
- **`tools/ppt_extract.py`** — keeps **only graph slides**: an image is kept only if it looks like a chart (pixel
  size ≥ 560×300, chart-like aspect 0.4–4.6, not a full-bleed cover, not a thin banner/logo), and each graph is
  paired with its slide's analysis text as a caption. Branded decks skip the cover slide + apply the full-bleed
  test; pure-image decks (e.g. CPI — every slide is one full-slide chart) keep edge-to-edge charts. Folds in the CPI
  deck's ready-made analytical PNGs ("New folder"). **81 graph slides across 7 decks** (CPI, Retail, Housing, U-Mich,
  Employment, ISM Manufacturing, ISM Services) → `Macro Hub/assets/` + `ppt_manifest.json`.
- **`tools/macro_hub.py`** — renders the hub from `endoexcel_latest.json` (live scores/sparklines) + the manifest.
- **`tools/build_macro_hub.py`** — orchestrator (refresh endo → extract decks if needed → render). Output:
  **`Macro Hub/Macro Indicators Hub.html`**.

## Notes
- **Live-data note — refreshed 2026-09-24** *(rolling note; supersedes the 2026-09-19 note it replaces — every
  reading below is unchanged from it, only the payload date moved).* The Excel half was rebuilt today
  (`Endo Excel/endoexcel_latest.json`, `generated` **2026-09-24 16:11**, `as_of` **2026-09-24**) and **reproduces
  the 2026-09-19 and 2026-09-11 reads exactly**: 19 of 19 drivers scored, 0 failed; combined **+12.9**
  (level +9.2) of ±190 → *Mildly Inflationary*, quadrant *Reflation / Overheating* (growth axis +0.56, inflation
  axis +0.89), 10 rising / 9 falling. Every driver print, score and pattern is unchanged, so nothing on the Hub
  moved — the superseded-in-date-only 2026-09-11 and 2026-09-19 readings are listed in [[log]].
  **The tiles are therefore still pre-hike and, on the macro side, pre-August-print** (the CPI, core CPI, PCE
  and PPI tiles still carry 2026-07 observations, industrial production 2026-06). The *Nominal GDP* tile's
  2026-04 is **not** a lag: that is Q2-2026, the newest quarter published (`macro_pack.json` `series.GDPC1`,
  `latest_date` 2026-04-01). On the rate side the Rates & Money *Fed Funds rate* tile still reads **3.63%**
  (2026-09 obs) against an effective fed funds rate of **3.88%** after the September hike (`tools/macro_pack.json` `series.DFF`, 2026-09-22), and the *10-Year Treasury
  Yield* tile reads **4.78%** (2026-09 obs) against **4.96%** on 2026-09-22 (`series.DGS10`). On the price side the
  gap is now a full month rather than a few days: FRED's August prints are CPI **+3.35% y/y** and core CPI
  **+2.45%** (`series.CPIAUCSL` / `CPILFESL`, both keyed to a 2025-08 base) against the tiles' 2026-07 readings of
  3.3 and 2.47. The driver workbooks have not been re-saved.
- The PowerPoint half is **carried forward, not re-derived**: `Macro Hub/ppt_manifest.json` carries **no
  `generated` / `as_of` field of its own**, its file stamp is still **2026-06-25 14:51**, and no PowerPoint-extract
  step appears in today's refresh chain. Re-counted straight from the manifest on 2026-09-24: **81 graphs across
  7 decks** (CPI 21, Retail 15, Housing 6, U-Mich 3, Employment 9, ISM Services 13, ISM Manufacturing 14), which
  matches the rendered hub's "19 indicators · 81 graphs" — so the counts under **Build** above stand, but they are
  June-vintage by construction and only change when the decks do.
- The PowerPoint charts are the **user's own analysis** (trend lines, YoY/MoM, regimes, correlation heatmaps,
  seasonality, sub-index radars, cross-asset overlays). The Hub presents them next to the **independently-computed**
  live scores so the two corroborate. Decks: ISM-Mfg = "Chart Pattern & Trend Analysis"; Employment notes e.g. "+92k
  jobs/mo last 6m vs −8k prior — a sharp momentum inflection"; Retail "tracks GDP with sharper spikes & deeper troughs".
- Images are referenced from `Macro Hub/assets/` (relative paths; work on disk and via the local server).
- **Not investment advice.**

## Related
[[PTM Endo Scorecard (2026 Excel Data)]] · [[Macro + COT Trade Signals]] · [[PFTM Full Trading System]] · [[PTM Global-Macro Dashboard (Endo + Exo)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
