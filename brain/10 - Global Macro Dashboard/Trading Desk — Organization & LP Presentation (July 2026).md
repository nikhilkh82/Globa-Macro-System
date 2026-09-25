---
title: Trading Desk — Organization & LP Presentation (July 2026)
category: meta
type: meta
data_asof: 2026-07-25
summary: "The desk layer: _DESK/ shortcut tree (38 validated links) + 00 DESK MAP.md, the LP-facing fund page built on audited evidence incl. published failures, and the fund identity applied to 51 dashboards by apply_lp_theme.py."
tags: [operations, desk, navigation, lp, fund-presentation, theme, governance]
data_vintage: "n/a (operations)"
sources: "_DESK/ · 00 DESK MAP.md · tools/main_dashboard.py · tools/apply_lp_theme.py"
updated: 2026-07-25
---

# Trading Desk — Organization & LP Presentation (July 2026)

**What it is** — The operations layer that turned the project into a presentable trading desk: physical-folder navigation, an LP-facing front door, and a single visual identity across every dashboard.

## The three layers
1. **Desk navigation** — `_DESK/` at project root: a numbered shortcut tree (00 Start Here · 01 Trading Desk · 02 Macro Research · 03 Strategy Lab · 04 Data Room · 05 Operations) with 38 validated shortcuts, plus `00 DESK MAP.md` documenting the layout, the daily/weekly workflow, and **why the physical folders were deliberately NOT mass-moved** (relative dashboard links, ~40 builders with hard-coded paths, the root is the Obsidian vault, and several root items are builder inputs — verified by reference-scan before any move). Only verified-unreferenced scratch went to `_archive/`.
2. **LP presentation** — `Global Macro Trading System.html` (built by `tools/main_dashboard.py`): an institutional fund page — philosophy → strategy ("harvest what works; time only what can be timed") → **audited evidence including the published failures** → risk framework → live platform cards → governance — with a live desk-state strip and full simulated-results disclosures. The integrity story ("trust the 0.69 *because* we published the −1.7") is the pitch.
3. **Fund identity everywhere** — `tools/apply_lp_theme.py`: an idempotent post-processor that applies the ivory/navy/gold serif identity + a brand bar (⌂ FUND OVERVIEW) to every dashboard in the theme script's walk (51 at the 2026-07-25 run) and centers table columns; appended to both refresh chains so rebuilds re-apply it automatically.

## Standards it enforces
- Every dashboard reachable within two clicks of the LP page; every page links back via the brand bar.
- Tables: headers centered over centered values; first (identifier) column left-aligned.
- Honest-evidence framing on client-facing surfaces: simulated/audited labels, nulls at equal prominence, licensed data gaps disclosed rather than faked.

The agent-facing build conventions for the dashboard system live in [[_Dashboard Agent - Operating Spec]]; the wiki's own conventions in [[_Vault Schema & Conventions]]. The candlestick execution view for tickets is documented in [[Chart Room]].

## See also
[[Analyst System — Live Cockpit (June 2026)]] · [[Global Macro Trading Deck (July 2026)]] · [[Trading System - Backtest (June 2026)]]
