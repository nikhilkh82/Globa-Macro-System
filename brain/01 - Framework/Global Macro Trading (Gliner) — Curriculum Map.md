---
title: "Global Macro Trading (Gliner) — Curriculum Map"
category: framework
type: reference
data_asof: n/a
summary: "The organising spine: Gliner's Global Macro Trading mapped chapter-by-chapter onto Brain pages and live dashboards, with a plain list of what the platform does not cover (demographics, CDS, futures curves, vol surfaces)."
tags: ["framework", "curriculum", "gliner", "map", "structure"]
updated: 2026-08-13
data_vintage: "book 2014 · Brain pages live · platform data to 2026-08"
sources: 1
---

# Global Macro Trading (Gliner) — Curriculum Map

The organising spine of **Greg Gliner, _Global Macro Trading: Profiting in a New World Economy_** (Bloomberg Financial Series, 462pp), mapped onto this wiki and onto the live platform. The book splits the discipline in two, and that split is the useful one:

- **Part One — the craft** (Ch 1–6): what global macro *is*, how you run a process, size, and measure; how you test ideas; the four building blocks and how they move together; technicals; systematic construction.
- **Part Two — the domains** (Ch 7–12): FX → Equities → Fixed Income → Commodities → Central Banks → Economic Data.

This page is the index. Each row says where the Brain covers that chapter, what live surface backs it, and — where nothing covers it — says so plainly.

## Part One — The craft

| # | Chapter | Brain coverage | Live surface |
|---|---|---|---|
| 1 | Surveying the Global Macro Landscape — discretionary / systematic / HFT / CTA; return profile; why institutions allocate | [[The Global Macros Framework]] · [[Cross-System Synthesis — What Works]] | [Strategy Scorecard](../../Synthesis/Strategy%20Scorecard.html) |
| 2 | Trading Process, Sizing Trades, Monitoring Performance | **[[Position Sizing, Unit Size & Volatility Adjustment]]** · **[[Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR]]** · [[Risk Management]] | [PFTM Trade Console](../../Macro%20COT%20Trades/PFTM%20Trade%20Console.html) · [PFTM System](../../PFTM%20System/PFTM%20System%20Dashboard.html) |
| 3 | Back-Tests, Queries, and Analogs | [[Cross-System Synthesis — What Works]] · [[Trading System - Backtest (June 2026)]] · [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] | [Econometrics Lab](../../Econometrics%20Lab/Econometrics%20Lab.html) |
| 4 | The Building Blocks — four product groups & their relationships | **[[The Four Product Groups & Cross-Asset Relationships]]** | [2026 Workbook Explorer](../../Workbook%20Explorer/2026%20Workbook%20Explorer.html) |
| 5 | Technical Analysis — charts, trend, MAs, Bollinger, patterns, oscillators, CFTC positioning, seasonals, cycles | [[Technical Analysis & Price Action]] · [[Average True Range (ATR)]] · [[Distribution of Returns]] | [Chart Room](../../Chart%20Room/Chart%20Room.html) |
| 6 | Systematic Trading — framework, factors, risk factors, risk premia, risk parity | **[[Systematic Trading — Factors, Risk Premia & Risk Parity]]** | [Strategy Scorecard](../../Synthesis/Strategy%20Scorecard.html) · [Risk Parity](../../Risk%20Parity/Risk%20Parity%20Dashboard.html) |

## Part Two — The domains

| # | Chapter | Brain coverage | Live surface |
|---|---|---|---|
| 7 | Foreign Exchange — USD's role, regimes, valuation (PPP, carry, OIS/LIBOR differentials, trade-weighted) | [[USD & G10 FX]] · [[FX Endogenous-Exogenous Framework]] · [[Australia Endogenous Driver Analysis (July 2026)]] · [[UK Endogenous Driver Analysis (July 2026)]] | [FX Carry Value](../../FX%20Carry%20Value/FX%20Carry%20Value%20Dashboard.html) · [FX Signals](../../FX%20Signals/FX%20Signals%20Dashboard.html) |
| 8 | Equities — indices, derivatives, valuation | [[Sector Analysis & Rotation]] · [[Company Stats & Screening]] · [[Spread Trades]] | [Sector Rotation](../../Sector%20Rotation/Sector%20Rotation%20Dashboard.html) · [Equity Trend](../../Equity%20Trend/Equity%20Trend%20Dashboard.html) |
| 9 | Fixed Income — money markets, LIBOR/OIS, swaps, futures, sovereign curve, inversion, CDS, ETFs | [[Government Bond Yields]] · [[Corporate Bond Yields & Credit]] · [[Yield Curve & Recession Signals]] | [Curve Macro](../../Curve%20Macro/Curve%20Macro%20Dashboard.html) · [Treasury Trend](../../Treasury%20Trend/Treasury%20Trend%20Dashboard.html) |
| 10 | Commodities — supply/demand, ending stock, contango/backwardation, CRB, the sub-complexes | **[[Commodities — Supply, Demand & the Cycle]]** · **[[Energy, Metals & Agriculture — the Sub-Complexes]]** · [[Cyclical Commodities]] | [Surprise Commod](../../Surprise%20Commod/Surprise%20Commod%20Dashboard.html) |
| 11 | The Role of Central Banks — goals, tools, impossible trinity, monetary base, QE, communication | **[[Central Banks — Policy Rates, Balance Sheets & the Global Stance]]** · **[[Monetary Policy Tools, Transmission & Communication]]** | [Macro Signal Stack](../../Signal%20Stack/Macro%20Signal%20Stack.html) |
| 12 | Economic Data Releases and Demographics | [[Leading Indicators]] · [[Coincident Indicators]] · [[Lagging Indicators]] · [[GDP & Growth]] · [[Conference Board LEI & Leading-Lagging Map]] | [Explorer](../../Workbook%20Explorer/2026%20Workbook%20Explorer.html) · [Macro Charts](../../Macro%20Charts/Interactive%20Macro%20Charts.html) |

**Bold** = pages created 2026-08-13 to close a structural gap against the book.

## What the book covers and this platform genuinely does not

Stated plainly so the map is not read as complete coverage:

- **Demographics** (Ch 12) — no data feed. Population/dependency-ratio series are not in the 371-series catalog and no page pretends otherwise.
- **CDS and sovereign credit derivatives** (Ch 9) — no CDS feed. Sovereign risk is proxied only through yields and spreads.
- **Futures term structure / contango–backwardation** (Ch 10) — the platform holds spot and front-month prices plus CFTC open interest, but **no futures curve**, so roll yield cannot be computed. Discussed conceptually in [[Commodities — Supply, Demand & the Cycle]], not quantified.
- **Money-market plumbing** (Ch 9) — LIBOR/OIS, FRAs, repo, Eurodollar futures: no feed. The LIBOR-OIS stress spread the book leans on cannot be reproduced.
- **Options and volatility surfaces** (Ch 7, 8) — only VIX as a level; no surface, no skew.
- **Intraday / high-frequency** (Ch 1) — the platform is daily-or-slower by construction.

## How to use this map

Read Part One before Part Two — the book's own advice, and it matches how this platform is built: the process and sizing rules in [[Risk Management]] govern every ticket the engines produce, and the honest-verdict discipline in [[Cross-System Synthesis — What Works]] is what keeps the strategy lab from accumulating false positives.

Related: [[index]] · [[The Global Macros Framework]] · [[Trade Idea Generation Process]] · [[Dashboards - Brain Map]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]]
