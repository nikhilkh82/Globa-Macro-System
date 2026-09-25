---
title: Decisions & Rationale
category: meta
type: meta
data_asof: n/a
summary: "Decision log for the 2026-06-19 session: naming/de-attribution calls, real-prints-only data integrity (off-FRED metrics shown Awaiting, not faked), the Late-Cycle Reflation relabel, fix-generators-not-artifacts."
tags: [meta, session-record, decisions, rationale, 2026-06-19]
data_vintage: "n/a (decision log)"
sources: 0
updated: 2026-06-19
---

# Decisions & Rationale (2026-06-19)

The judgment calls made in the [[2026-06-19 Session - Dashboards, Rebrand & FRED|session]] and *why* — so they aren't silently reversed later.

## Naming & attribution
- **"Global Macros" (plural), verbatim as requested.** Kept distinct from the unchanged singular project/vault names ("Global Macro Hedge Fund Strategy", "Global Macro Brain"). Easy to flip to singular if intended.
- **Full de-attribution.** When asked to remove "Anton Kreil" (+ the non-existent "POTM"), chose to also drop "Professional Trading Masterclass" so the prose reads cleanly (`…encodes the *Global Macros* strategy`), rather than leaving an orphaned course name. **"Russell Lloyd" left in place** (not requested).
- **Raw source filename `PTM Video Series…xlsx` left unchanged** — it's the actual course product file in the read-only `raw/` corpus; renaming source data would be wrong and would break `build_library.py` paths.

## Data integrity (no fabrication)
- **Real prints only.** Every dashboard figure is pulled live from FRED (user key) or the maintained ISM workbook — nothing invented.
- **Off-FRED metrics flagged, not faked.** ISM *New Orders* sub-index, Conference Board confidence, shipping (BDI/SCFI), card-spend/TSA, and the transcript mention-tracker have no free source → shown as **Awaiting**, with a UMich/headline proxy where honest.
- **Fed Tracker stays "Awaiting."** No real June-2026 FOMC text exists, so the NLP score/keywords are not populated with live data; the tool is built + validated on a clearly-labelled *illustrative* sample, and the forward-guidance leg is anchored to the real Fed Funds path. The demo JSON was deliberately **kept out of the project root** so the live card doesn't masquerade demo data as a real read.

## Analysis
- **Regime relabel "slowdown" → "Late-Cycle Reflation."** A 3-lens adversarial workflow showed coincident data is *not* decelerating (ISM 54.0, GDPNow +3.0%, payrolls +188k); the slowdown is a *forward* risk in leading indicators. Nominal retail was haircut to real (~+2.6%); the equity tilt was moved off classic defensives toward inflation-beneficiary cyclicals (firm growth + expanding credit + easing Fed argue against defensives).

## Engineering
- **Fix generators, not artifacts.** All bug/format/theme fixes went into the `.py`/`.ps1` generators (durable) — never hand-edited the produced `.html`/`.xlsx`/`.pdf`.
- **`scores_cache.json` over rewriting the data source.** openpyxl can't read formula cells when `fullCalcOnLoad=True`; rather than re-architect the dashboard, cached the Excel-computed scores and added a fallback — then wired the cache into `refresh_all.ps1` so it never goes stale.
- **Installed a 2nd Python here vs. running on the main machine.** User chose to make this OneDrive-synced box self-sufficient; accepted a divergent local Python env as the cost.

## See also
- [[2026-06-19 Session - Dashboards, Rebrand & FRED]] · [[Open Items & Follow-ups]] · [[Artifacts - Tools & Deliverables]]
