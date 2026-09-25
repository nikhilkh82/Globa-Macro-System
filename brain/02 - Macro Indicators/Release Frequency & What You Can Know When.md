---
title: "Release Frequency & What You Can Know When"
category: indicators
type: reference
data_asof: 2026-08-15
summary: "Grant's structural point that frequency, lag and revision are three different properties: surveys arrive early and unrevised, hard data late and revised; platform series by cadence, plus two rule-breaks fixed 2026-08-15."
tags: ["indicators", "release-calendar", "revisions", "vintage", "grant"]
updated: 2026-08-15
data_vintage: "catalog 2026-08-14"
sources: 2
---

# Release Frequency & What You Can Know When

Grant's handbook is organised by **release frequency**, not by economic theme, and that choice is the book's real contribution. The question it answers is not *"what does this indicator mean"* but *"on any given morning, what do I actually know?"*

Three properties travel together and are usually confused:

1. **Frequency** — how often it prints.
2. **Lag** — how far behind the reference period the print is.
3. **Revision** — whether the number you traded on survives.

A monthly indicator with a three-month lag is *less current* than a quarterly one released promptly. Grant's central warning is that analysts rank indicators by importance when they should rank them by **what is knowable now**.

## The revision asymmetry — the rule worth internalising

> **Surveys arrive early and are never revised. Hard data arrives late and is revised repeatedly.**

Grant makes this point about the CPI (*"REVISIONS: NONE — the complete pre-set survey is run every month"*) and about the survey indicators generally. It has a direct consequence for this platform:

| Type | Examples here | Timeliness | Revision risk |
|---|---|---|---|
| **Surveys / diffusion** | `US26:ISM`, `ISMC:*`, `US26:NMI`, `NMIC:*`, `NFIB:*`, `UMICH:*`, `PMI:*`, `ESI:*` | first out, ~1–3 days after month-end | none to trivial |
| **Prices** | `US26:CPIAUCSL`, `US26:PPIFGS`, `INFL:*` | ~2–3 weeks | CPI never revised; PPI lightly |
| **Hard activity** | `IPC:*`, `RETAIL:*`, `DUR:*`, `HOUSING:*` | 2–6 weeks | revised for months |
| **National accounts** | `GDPC:*`, `US26:GDPPCT` | ~4 weeks after quarter-end | revised for **years** |

This is why the platform's point-in-time discipline matters, and why [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] uses expanding-window scoring: a backtest fed final-vintage hard data is testing knowledge nobody had at the time. The survey block is the part you could genuinely have acted on.

## What is knowable, by cadence, on this platform

### Weekly — the only genuinely current reads
`USLEAD:CLAIMS` · `CLAIMS:CONT` · `LEI:LMSI` / `LEI:LMSILF` (SF Fed labour stress) · `LEI:GAS` · `GLOB:VIX` · `GLOB:HYOAS` · `COT:*` (18 markets, Friday, Tuesday positions) · `EMV:EMVDIS` / `EMV:EPUUS` · `INFEXP:BE5` / `BE10` · `FG:*` (Fear & Greed)

Everything outside this list is, to some degree, history.

### Monthly — the workhorses
Surveys first (`ISM`, `NMI`, `NFIB`, `UMICH`, `PMI`, `ESI`, `CNPMI`), then labour (`US26:NFP`, `PAYROLL:*`, `USLEAD:UNEMP`), then prices (`CPI`, `PPI`, `INFL:*`), then hard activity (`IPC:*`, `RETAIL:*`, `DUR:*`, `HOUSING:*`), then the lagging balance-sheet reads (`LEI:IS*` inventory/sales, `LEI:HPI`).

### Quarterly — confirmation, not news
`GDPC:*` · `US26:GDPPCT` · `LEI:ECI` / `ECIQ` · `AU:CPI` · `GDPFC:SPF1Y`

By the time GDP prints, the monthly series have already said it. Quarterly data settles arguments; it does not start them.

### Annual / structural
`AU:GDEBT` · `AU:GBAL` · `UK:DEFGDP` — and the multi-century panel in [[00 - GMD Overview & Structural Edge]].

## Where this platform breaks the rule (honestly)

Two places where the catalog's *stated* frequency is not the whole story, both found and fixed on 2026-08-15:

- **Forecast rows published as realized data.** Workbook 37 extends itself past the last real print and flags the extension `Data_Status = "Forecast"`. Three dashboards read the values and ignored the flag. Now guarded — see the log entry for 2026-08-13.
- **Series with holes.** Three Services PMI series carried monthly history to 2014, an **11.6-year gap**, then one or two freshly-pasted 2026 points — which made an expired series look current and turned every "monthly change" across the hole into a twelve-year change. Now excluded by a contiguity guard, with the reason named.

Both were the same underlying error: **a date on a row is not evidence that the row is a current observation.**

## The practical sequence

1. **Weekly block** — has anything broken since the last monthly round?
2. **Survey block** — what do respondents say about the month just ended? (early, unrevised)
3. **Hard block** — did activity confirm the surveys? (late, revised)
4. **Quarterly** — does the national-accounts arithmetic agree?

Divergence between (2) and (3) is where most of the analytical value sits — and it is exactly what [[Macro Insights]] scans for.

Related: [[Indicator Register — Grant Handbook mapped to live series]] · [[Leading Indicators]] · [[Coincident Indicators]] · [[Lagging Indicators]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]]
