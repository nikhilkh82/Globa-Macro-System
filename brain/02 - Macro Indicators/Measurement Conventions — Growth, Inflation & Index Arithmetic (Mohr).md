---
title: "Measurement Conventions — Growth, Inflation & Index Arithmetic (Mohr)"
aliases: ["Measurement Conventions - Growth, Inflation & Index Arithmetic (Mohr)"]
category: indicators
type: reference
data_asof: 2026-08-15
summary: "Mohr's Economic Indicators arithmetic layer: annualisation compounds, never multiplies (codebase audited 2026-08-15 — passes, one ranking-signal exception); first estimates are provisional; measure inflation YoY."
tags: ["indicators", "methodology", "growth", "inflation", "index-numbers", "revisions", "mohr"]
updated: 2026-08-15
data_vintage: "book 6th ed. · codebase audited 2026-08-15"
sources: 2
---

# Measurement Conventions — Growth, Inflation & Index Arithmetic (Mohr)

From **Philip Mohr, _Economic Indicators_ (6th edition, Van Schaik)** — 12 chapters on how indicators are *constructed*, not which ones to watch. That makes it the third and most technical of the platform's indicator references:

| Book | Contribution |
|---|---|
| [[Global Macro Trading (Gliner) — Curriculum Map]] | the **craft** — process, sizing, the four product groups |
| [[Indicator Register — Grant Handbook mapped to live series]] | the **catalog** — what exists, at what frequency |
| **Mohr (this page)** | the **arithmetic** — how to compute and compare indicators without fooling yourself |

## Scope — read this honestly

Mohr is a **South African** text (SARB / Stats SA, rand-denominated worked examples). Its country-specific content does **not** map to this platform: there are no South African series in the 455-series catalog, ZAR is not in the trade universe, and unlike the Canadian gap that [[Indicator Register — Grant Handbook mapped to live series]] closed, adding one is not warranted — South Africa is not in the desk's coverage.

What *is* fully transferable is Chapters 1, 3, 6 and 12: the measurement rules, which are country-agnostic and directly govern how this platform computes ~455 series.

Its structure: 1 Introduction · 2 National accounts · 3 Economic growth · 4 Business cycles · 5 Employment · 6 Inflation · 7 International transactions · 8 Wages & productivity · 9 Financial indicators · 10 Fiscal indicators · 11 Social & political · 12 International comparisons.

## Rule 1 — Annualisation compounds; it does not multiply

The formula (Ch 3.1), for converting a period-on-period change into an annual rate:

> **rate = [ (Iₜ / Iₜ₋₁)^f − 1 ] × 100**, where **f = 12** monthly, **4** quarterly, **1** annual

Mohr's worked example: real GDP 761,397 → 781,144 between 2018 Q1 and Q2 gives **(1.025935⁴ − 1) × 100 = +10.78%**, and 801,180 → 761,397 gives **−18.43%**.

He states the trap explicitly in italics:

> *"it is incorrect to simply multiply the rate of change between two successive quarters by four to obtain an annual rate."*

**Audited against this codebase on 2026-08-15 — the platform passes.** Every place a rate is published uses the compounding form:

| Location | Form |
|---|---|
| `build_cycle_dashboard.py`, `build_cycle_exports.py`, `build_cycle_html.py` | `(GDPC1ₜ / GDPC1ₜ₋₁) ** 4 - 1` ✅ |
| `build_macro_deck.py` core CPI 3m/3m | `(CORECPI / CORECPI.shift(3)) ** 4 - 1` ✅ |
| `surprise_commod.py` 3m/3m | `((Σcur/3) / (Σprior/3)) ** 4 - 1` ✅ |
| `build_trading_system.py`, `pftm_system.py`, `hfrep.py` Sharpe/vol | mean × 12 ÷ (sd × √12) ✅ (correct for *moments*, which do scale linearly/by √t) |

**One deliberate exception, flagged rather than corrected:** `build_trading_system.py:158` blends momentum as `(r6 × 2 + r12) / 2` — the linear form. It is a **ranking signal**, not a published growth rate, and it is immediately divided by annualised vol and clamped to ±1, so the monotonic ordering is unaffected. Worth knowing that it diverges from the compounded form at large returns (r6 = 40% → linear 80% vs compounded 96%).

## Rule 2 — Choose the right aggregate, and know its blind spot

Ch 3.2. Nominal aggregates are never appropriate for growth. The real choice is **real GDP vs real GNI**:

- **GDP** is *geographic* — activity inside the borders. Use it for **volume of production**.
- **GNI** is *residents'* income worldwide. Use it for **economic welfare**.

The technical complication Mohr emphasises: **real GDP includes exports and excludes imports**, so when real GDP is computed, changes in *export* prices are accounted for but changes in *import* prices are effectively ignored. A country whose import prices surge sees no direct real-GDP hit — the terms-of-trade loss is invisible in the headline. His example: if the gold price rises but volume is unchanged, nominal GDP rises while real GDP does not.

Relevant here because the platform's commodity work ([[Commodities — Supply, Demand & the Cycle]]) tracks exactly the import/export price channel that real GDP suppresses.

## Rule 3 — First estimates are provisional, and the revisions are large

Ch 3.1. Mohr's documented South African case — the *same quarters*, as first published versus as later revised:

| Quarter (real GDE) | First published | Later revised to |
|---|---|---|
| 1993 Q1 | **+8.2%** | **+3.9%** |
| 1993 Q2 | **−11.5%** | **−3.0%** |
| 1993 Q3 | **+15.7%** | **+9.7%** |

> *"growth rates based on original estimates should always be treated as provisional estimates."*

Revisions of that size **reverse conclusions**, not just refine them. This is the same discipline the platform enforces elsewhere: point-in-time expanding windows in [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]], and the vintage guard that stopped forecast rows being published as realized data (log, 2026-08-13). See also the revision-asymmetry table in [[Release Frequency & What You Can Know When]] — national accounts are the *most* revised series in the catalog.

## Rule 4 — Inflation should be annualised, and monthly inflation is technically weak

Ch 6.4:

> *"The inflation rate should preferably always be annualised… since inflation is a process of sustained price increases, the rate should preferably be measured over a period of not less than one year."*

His technical reason is the one usually forgotten: **not all prices in the CPI are collected monthly** — some components are surveyed and adjusted only once a year. So a month-on-month CPI change is partly an artefact of the collection calendar, which makes short-period inflation measurement inadvisable *on both principle and mechanics*.

He is also candid about why short-period figures dominate anyway: market participants value them mainly because other participants do; politicians pick the window that flatters; forecasters pick the one that vindicates.

**Platform practice matches the rule** — the endo scorecards, signal stack and inflation complex all score on **YoY**; MoM exists in the Explorer as a user-selectable transform, not as the basis of any published score.

## Rule 5 — What the CPI is not

Ch 6.3–6.4:

- It is an **average for a "mythical average household"** — Mohr's phrase — and is *not* directly applicable to any individual household.
- It **includes indirect taxes** (VAT). A shift from direct to indirect taxation mechanically raises measured CPI, which can then be cited as grounds for further price and wage increases. Some countries exclude taxes for this reason; the counter-argument is that the CPI is meant to measure cost *to the consumer*.
- Fixed-basket construction ignores **consumer substitution**, which generally biases the index **upward** relative to actual prices paid.

This is why the platform carries core, trimmed and median measures alongside headline wherever the source publishes them — most completely in the new [[Indicator Register — Grant Handbook mapped to live series]] Canadian block, where `CA:CPITRIM` / `CA:CPIMED` / `CA:CPICOMMON` sit beside `CA:CPIYOY`.

## Note on sourcing

This PDF is a **scanned, image-only document** — no text layer, no bookmarks, so it cannot be text-extracted. It was read by rasterising pages (PyMuPDF) and reading them visually. The rules above come from the contents pages and from pages 47, 51 and 110 of the book (PDF pages 59, 63, 122); chapters cited but not read page-by-page are described only at the level the table of contents supports.

Related: [[Indicator Register — Grant Handbook mapped to live series]] · [[Release Frequency & What You Can Know When]] · [[Global Macro Trading (Gliner) — Curriculum Map]] · [[GDP & Growth]] · [[Leading Indicators]]
