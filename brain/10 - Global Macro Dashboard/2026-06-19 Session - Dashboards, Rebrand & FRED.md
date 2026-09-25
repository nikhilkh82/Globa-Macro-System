---
title: 2026-06-19 Session - Dashboards, Rebrand & FRED
category: meta
type: meta
data_asof: 2026-06-19
summary: "The 2026-06-19 session record: new-machine setup, live refresh, COT expanded to 13 markets, 'Global Macros' rebrand & de-attribution, the 5-section Business-Cycle Dashboard, light theme, endo-score fix."
tags: [meta, session-record, 2026-06-19, dashboard, rebrand, fred, fed-tracker]
data_vintage: "work performed 2026-06-19; live data through May/Jun 2026"
sources: 0
updated: 2026-06-19
---

# 2026-06-19 Session — Dashboards, Rebrand & FRED

Narrative record of the 2026-06-19 working session. Canonical one-liners are in [[log]] (entries from *"refresh | Live system re-pulled (new machine)"* through *"query | Live Business Cycle Dashboard"*). Catalogs: [[Artifacts - Tools & Deliverables]] · [[Decisions & Rationale]] · [[Open Items & Follow-ups]].

## What this session set out to do
Started as "understand the structure," then became an extended build-out: get the live system running on this machine, fix a broken dashboard, expand positioning data, rebrand/de-attribute the vault, and build a brand-new **Business-Cycle Dashboard** (Leading/Coincident/Lagging/Alt-HF + a Fed NLP tracker), finally restyling to a light theme.

## Timeline (what happened, in order)
1. **Explored the vault** — confirmed the three-layer LLM-wiki structure (raw → wiki → schema) and the live FRED/CFTC pipeline.
2. **New-machine setup + live refresh.** This box (OneDrive-synced) had no Python and no scheduled task. Installed **Python 3.12.10** (winget, user scope) + `openpyxl`/`matplotlib`/`python-docx`; fixed the User PATH ahead of the `WindowsApps` alias stub; ran `refresh_all.ps1` (FRED 50-series + CFTC) and `weekly_report.ps1` (PDF + dashboard + docx). Registered the **`GlobalMacroWeeklyUpdate`** Task Scheduler job (Mon 07:00) and validated it end-to-end (exit 0).
3. **Fixed the dashboard "blank page" bug.** `Global Macro Dashboard.html` rendered nothing — root cause was a **JS `SyntaxError`** in `scoreChart()` (one extra `}` — 7 closing braces where 6 were correct), which aborted the entire render script. Fixed in the generator `build_dashboard.py` (durable) and verified in headless Chrome (0 console errors). Also surfaced that the machine's default `.html` handler is **Comet** with a legacy IE fallback (IE can't run Chart.js v4).
4. **Expanded COT positioning to 13 markets** — added **NASDAQ 100 E-mini (`209742`)**, **Silver (`084691`)**, **Natural Gas (`023651`)**, codes verified against the live CFTC API. Flowed automatically into the dashboard, report, and signals.
5. **Rebrand "PTM" → "Global Macros"** — 137 uppercase + 30 lowercase-tag replacements across 31 wiki pages + tools; renamed `The PTM Framework.md` → **`The Global Macros Framework.md`** with all 37 wikilinks rewritten (0 broken links). Protected the immutable raw `PTM Video Series…xlsx`.
6. **Removed source attribution** — stripped **"Anton Kreil"** and **"Professional Trading Masterclass"** (full de-attribution; "POTM" was a typo — never existed). 0 residual across all text + regenerated Excel templates.
7. **Switched to the user's registered FRED key** (`ae4a9ac7…298a823`) in `fred.py`; verified.
8. **Built the Business-Cycle Dashboard** (the session's centrepiece) — see [[Business Cycle Dashboard - Live (June 2026)]]. Five sections grew incrementally:
   - **§1–3 Leading / Coincident / Lagging** (18 indicators, real FRED + ISM prints).
   - **§4 Alternative & High-Frequency** (Net Liquidity, NFCI, WEI; shipping/card-TSA/transcript flagged off-FRED).
   - **§5 Fed Tracker** — deterministic FOMC-NLP tool + the **"FOMC NLP Analysis"** tear-sheet format.
   - Three layers: data tool (`build_cycle_dashboard.py`), markdown synthesis page, interactive HTML (`build_cycle_html.py`).
   - Regime call **"Late-Cycle Reflation"** was **adversarially verified** by a 3-lens workflow panel (relabeled from "slowdown," nominal prints haircut to real, equity tilt revised toward inflation-beneficiary cyclicals).
9. **Light theme** — converted **both** dashboards from dark to light (durable color map in the generators); verified 0 console errors.
10. **Fixed the "US Endo Score: None" bug** — endo template score cells are formulas with `fullCalcOnLoad=True`, so openpyxl `data_only` reads None. Fix: cache Excel-computed scores to `scores_cache.json`, fallback in `build_dashboard.py`, and wired the JSON dump into `refresh_all.ps1` (stays fresh weekly).

## Headline live numbers captured this session (data through May/Jun 2026)
- **Regime:** Late-Cycle Reflation · breadth 5 Bullish / 9 Bearish / 10 Neutral / 3 N/A
- **Endo +27** (Mildly Inflationary) · **AUD/USD Exo −6** (Short)
- CPI **+4.27% YoY**, Core PCE **+3.29%**, ISM **54.0**, U-3 **4.30%**
- 10Y–2Y **+27 bps** (flattening) · Net Liquidity **$5.77T** (−$151B WoW, RRP buffer drained) · NFCI **−0.51** (loose) · WEI **3.10**
- Fed Funds **3.63%** (−170 bps from 5.33% peak, on hold ~5mo) → easing stalled, bias skews hawkish
- COT (wk 2026-06-09): Gold +52%, **Silver +22%**, **NASDAQ −0.4%**, **Nat Gas −12%**, JPY −29%, VIX −18%

## See also
- [[Business Cycle Dashboard - Live (June 2026)]] · [[Macro Regime - Live (June 2026)]] · [[The Global Macros Framework]]
- [[Artifacts - Tools & Deliverables]] · [[Decisions & Rationale]] · [[Open Items & Follow-ups]] · [[log]]
