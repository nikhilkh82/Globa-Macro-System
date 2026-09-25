---
title: "Workbook Charts — Excel Chart Gallery (August 2026)"
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "The user's own Excel charts from the 2026 workbooks as a filterable gallery: 431 charts from 29 of 30 curated books at the 19 Sep export (the AUS endo book yields none); caps disclosed, blank renders excluded."
tags: ["dashboard", "excel", "charts", "workbooks"]
updated: 2026-09-19
data_vintage: "Gallery counts from the 2026-09-19 14:56 export (re-exported whenever a workbook changes)"
sources: 30
---

# Workbook Charts — Excel Chart Gallery

**Dashboard:** [Workbook Charts.html](../../Workbook%20Charts/Workbook%20Charts.html) · built by `tools/wb_charts_export.py` (exporter) + `tools/build_wb_charts.py` (gallery), both hourly soft steps in `tools/auto_refresh.py`.

## What it is

The user's own Excel charts — the ones hand-built inside the 2026 workbooks — exported as PNGs and served as a filterable gallery. Nothing is redrawn or restyled: each image is Excel's own render of the chart as authored. This closes a long-standing gap: the 2.8 workbooks carry ~2,200 native charts that were invisible unless the workbook was open in Excel.

## Coverage and honesty rules

- **30 curated books** from the actively-maintained 2026 working set (endo books 26/27/28, US leading 29, ISM pair, UMCSI, NFIB, EU ESI, China PMI, global PMIs, both COT books, yields 22 / credit 23, M2, commodities/inflation/USD-TWI, Bull & Bear, and the coincident set) — **447 charts** on first export (2026-08-12). Current export (`Workbook Charts/charts_manifest.json`, generated 2026-09-19 14:56): **431 charts from 29 books**. Book 27 (AUS endo, workbook modified 2026-09-16) is still on the list, but the exporter finds no charts in it (0 of 0), so it drops out of the gallery. The 30 books hold 963 charts in all; 21 books hit the cap.
- Books are **capped at 16 charts each** and every cap is disclosed on the page per book ("showing 16 of 176").
- Charts that will not render headlessly are **excluded, never shipped blank** (Excel's `Chart.Export` writes empty PNGs for never-rendered charts; the exporter forces a render by activating sheet + chart, escalates to a visible instance, and drops anything still empty).
- The exporter is **mtime-guarded**: unchanged workbooks are never reopened, so the hourly runs cost nothing until a workbook actually changes — at which point its charts re-export automatically, keeping the gallery in lockstep with the workbook updates recorded in [[log]].

## How it connects

- Launcher card on the [main dashboard](../../Global%20Macro%20Trading%20System.html) (Research & macro coverage group) with a live "N charts" chip read from `Workbook Charts/charts_manifest.json`.
- Complements the [[2026 Workbook Explorer]] — the Explorer recomputes series interactively; this gallery shows the charts *as the user built them*, including layouts and annotations no recomputation reproduces.
- Sits beside [[Interactive Macro Charts]] and [[Macro Indicators Hub]] in the chart-viewing stack.

Related: [[2026 Workbook Explorer]] · [[Macro Indicators Hub]] · [[Dashboards - Brain Map]] · [[The Global Macros Framework]]
