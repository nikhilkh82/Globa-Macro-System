---
title: Open Items & Follow-ups
category: meta
type: meta
data_asof: 2026-06-19
summary: "Open items left at the 2026-06-19 session end: five Awaiting data gaps (ISM New Orders, Conf. Board, BDI/SCFI, card/TSA, live FOMC text), two naming confirmations, cache/automation robustness, suggested builds."
tags: [meta, session-record, follow-ups, todo, 2026-06-19]
data_vintage: "n/a (open items)"
sources: 0
updated: 2026-06-19
---

# Open Items & Follow-ups (as of 2026-06-19)

Things left open at session end — for the next session or the user to pick up.

## Data gaps (flagged "Awaiting" in the dashboards)
- [ ] **ISM "New Orders" sub-index** — only the headline PMI (54.0) is captured; the leading sub-index needs a web/paid source.
- [ ] **Conference Board Consumer Confidence** — proprietary; UMich (49.8) used as proxy.
- [ ] **Global Shipping (BDI / SCFI)** — Baltic Exchange / Shanghai Shipping Exchange; paid feed.
- [ ] **Real-time consumer spend (card / TSA)** — BofA/JPM/Opportunity Insights (card) + tsa.gov (TSA throughput).
- [ ] **Corporate-pulse + Fed Tracker text** — earnings-transcript "weakness/layoffs" mentions and a live FOMC statement → both could be sourced via the vault's **bigdata.com** integration. Once a FOMC `.txt` is dropped in the project root, `fed_tracker.py` + `build_cycle_html.py` populate Section 5 automatically.

## Decisions awaiting user confirmation
- [ ] **"Global Macros" (plural) vs "Global Macro" (singular)** — used plural verbatim; confirm or flip.
- [ ] **"Russell Lloyd"** still cited twice in [[The Global Macros Framework]] — remove too?

## Engineering / robustness
- [ ] **`scores_cache.json` freshness** — now refreshed by `refresh_all.ps1`; if the endo/exo templates are ever rebuilt *outside* that pipeline, re-run `refresh_all.ps1` (or an Excel recalc) so the dashboard doesn't read a stale score.
- [ ] **Fold `build_cycle_html.py` into the weekly automation** — `weekly_task.ps1` currently builds the Global Macro deliverables only; add the cycle dashboard for a one-command weekly refresh of both.
- [ ] **Second Python environment** on this machine is not on the *system* PATH persistently for non-login contexts beyond the User PATH fix — fine for the scheduled task, but note if other automation is added.

## Possible next builds (suggested, not committed)
- [ ] Business-cycle **clock** quadrant (growth × inflation) plotting the current regime dot.
- [ ] Convert `Global Macro Dashboard.html` styling fully in line with the cycle dashboard (already both light; minor polish).
- [ ] Auto-pull a real recent FOMC transcript via bigdata.com to populate the Fed Tracker live.

## See also
- [[2026-06-19 Session - Dashboards, Rebrand & FRED]] · [[Decisions & Rationale]] · [[Artifacts - Tools & Deliverables]] · [[log]]
