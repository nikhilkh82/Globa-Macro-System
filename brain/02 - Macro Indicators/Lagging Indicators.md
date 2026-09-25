---
title: Lagging Indicators
category: indicators
type: domain
data_asof: 2026-06
summary: "The third confirmation layer — unemployment duration, core/services inflation, unit-labour costs, C&I loans and the policy rate that turn after the cycle; the live pillar (Jun-2026) reads late-cycle on ~3.3% core PCE."
tags: [global-macro, lagging-indicators, unemployment, inflation, unit-labor-costs, interest-rates, credit, business-cycle]
data_vintage: "concept (framework) + live FRED Lagging pillar (June 2026); historical overlap series 2013–2022"
sources: 4
updated: 2026-07-25
---

# Lagging Indicators

**What it is & why it matters** — Lagging indicators turn *after* the business cycle has already turned: they confirm, with a delay, a regime change that the [[Leading Indicators]] flagged and the [[Coincident Indicators]] validated. In the Global Macros framework they are the **third and final confirmation layer** — most useful for ruling out a false signal (a leading/coincident turn that doesn't "stick") and for reading the late-cycle dynamics — sticky inflation, peaking unemployment, rising unit-labour costs, plateauing credit — that drive the central-bank reaction function. Because they lag by construction, they are never a *timing* tool; they are a "did-the-turn-actually-happen?" check and a late-cycle stress gauge. They complete the Leading → Coincident → **Lagging** triad that the [[Business Cycle Dashboard - Live (June 2026)|live Business Cycle Dashboard]] scores each month.

> Framing note: this page bridges two layers — the **framework concept** (the classic lagging set) and the **live** Business Cycle Dashboard's Lagging pillar (FRED series, June 2026). The historical teaching corpus carries the overlapping series (unemployment, CPI/core) at their vintages (employment → 2021, CPI → 2022); the lagging-specific series are read live. Read each as labelled — historical-teaching vs live.

## The lagging set
The classic (Conference Board–style) lagging indicators, and how the desk reads each:

| Indicator | FRED series (live pillar) | Why it lags / what it tells |
|---|---|---|
| **Average duration of unemployment** | `UEMPMEAN` | Peaks well *after* a recession ends — long-term unemployment is the last labour metric to heal; a falling mean duration confirms a durable expansion. |
| **Unemployment rate** | `UNRATE` | Troughs late and rises late; a *rising* rate **confirms** (rather than predicts) a slowdown — see [[Coincident Indicators]] for the timely labour read (claims, payrolls). |
| **Core / services inflation** | `CPILFESL`, `PCEPILFE` | The stickiest prices turn last; core / services inflation persisting above the Fed's **2% target** keeps policy restrictive after growth has already cooled — the master input to the rate regime. |
| **Unit labour costs** | `ULCNFB` | Wage growth net of productivity; accelerates late-cycle as the labour market overheats — a key second-round inflation signal the Fed watches. |
| **Commercial & industrial loans** | `BUSLOANS` | Bank lending peaks after the cycle as credit demand and lending standards adjust with a lag; a roll-over confirms tightening conditions. |
| **Average prime / policy rate** | `FEDFUNDS` | Policy rates move with and *after* inflation; the late peak in rates is itself a lagging confirmation of the inflationary phase. |

## Charts & key trends
**Unemployment — the canonical lagging signal (historical, through 2021; live read June 2026).** In the teaching corpus the unemployment rate spiked to its all-time high of **14.8% (April 2020)** and was still healing at **5.8% (May 2021)** — the rate kept falling for years *after* the 2020 recession ended, the defining lagging behaviour (see [[Coincident Indicators]] for the full employment dataset). Live, the rate sits at **4.2%** (Jun-2026) with **average duration of unemployment** (`UEMPMEAN`) the slowest sub-component to normalise.

**Core / services inflation — stickiness (historical CPI → Oct 2022; live).** Core CPI peaked at **6.66% y/y (mid-2022)** in the dataset and Core PCE — the Fed's gauge — has a long-run y/y peak of **10.22%** (1970s–80s). The lagging lesson: headline rolls over first, **core and services last**. Live, Core PCE has re-firmed to ~**3.3%**, above target — which, with sticky core, is exactly why the live Business Cycle Dashboard's **Lagging pillar reads bearish/late-cycle** even as coincident growth holds.

**Unit labour costs & credit (live pillar).** `ULCNFB` (unit labour costs) and `BUSLOANS` (C&I loans) round out the late-cycle read: accelerating unit labour costs signal second-round inflation pressure, while a plateau/roll-over in business lending confirms that restrictive policy is biting with the usual lag.

## How it's used in the strategy
1. **Confirm, don't time.** Lagging data validates that a [[Leading Indicators|leading]]/[[Coincident Indicators|coincident]] turn was real. A leading signal *not* eventually confirmed by lagging data is treated as a false alarm — size down and wait.
2. **Late-cycle stress gauge.** Rising unemployment duration, sticky core/services inflation, accelerating unit labour costs and a credit roll-over together mark the **late-cycle / stagflation-risk** quadrant — the desk's cue to favour quality and real assets and to fade cyclicals (see [[Macro Regime Snapshot]]).
3. **Feeds the endo score.** The lagging set populates the **Inflation** and **Sovereign & Balance-Sheet / rates** blocks of the endogenous score in [[The Global Macros Framework]] and the [[Endo-Exo Toolkit & Workflow]] — sticky core inflation and a high policy rate push the endo "inflationary".
4. **Sets the rate regime.** Because core inflation and policy rates are the last to turn, they anchor the central-bank reaction function that drives [[Government Bond Yields]], the [[Yield Curve & Recession Signals]] and the [[USD & G10 FX]] view.

## See also
- [[Leading Indicators]] / [[Coincident Indicators]] — the upstream layers this confirms (completing the triad)
- [[Business Cycle Dashboard - Live (June 2026)]] — operationalises the Lagging pillar on live FRED data
- [[GDP & Growth]] · [[Government Bond Yields]] · [[Yield Curve & Recession Signals]]
- [[The Global Macros Framework]] / [[Endo-Exo Toolkit & Workflow]] — how lagging data scores into the endogenous read
- [[Macro Regime Snapshot]] · [[Trade Idea Generation Process]] · [[index]]
