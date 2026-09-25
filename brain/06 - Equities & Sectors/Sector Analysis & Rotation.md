---
title: Sector Analysis & Rotation
category: equities
type: domain
data_asof: 2022-12
summary: "How the macro regime call becomes cyclical/defensive sector tilts via the GICS matrix (69 industries: 41 cyclical, 22 defensive, 6 both), country-index universes, value-chain mapping and the US/EU screeners."
tags: [global-macro, sectors, gics, rotation, cyclical-defensive, value-chain]
data_vintage: "2013–2022, mixed (GICS map static; US screener through 2022; index/sector breakdowns 2013-era)"
sources: 9
updated: 2026-06-18
---

# Sector Analysis & Rotation

**What it is & why it matters** — Sector analysis is the bridge between the Global Macros top-down macro regime call and bottom-up stock selection. Once the macro picture (growth, liquidity, the cycle) points to a regime, the trader expresses it by tilting toward cyclical or defensive sectors and then down the value chain into specific industries and stocks. This layer formalises a sector "view," classifies every GICS industry as cyclical/defensive, maps the constituents of major country indices, and provides the screener that ranks individual names within a chosen sector. It is where the macro thesis from [[Macro Regime Snapshot]] becomes a concrete long/short basket.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
| --- | --- | --- | --- |
| GICS Breakdown.xlsx | Full GICS taxonomy: 11 Sectors → 24 Industry Groups → 69 Industries → 158 Sub-Industries, each tagged Cyclical / Defensive / Both | Static classification | None (classification matrix) |
| US_Sector_Data.xlsm | "US Stock Screener >$1bn Mkt Cap": ~3,180 US names, 41 fundamental columns, NAICS sector tags | FY ends 2010–2022 | None (screener table) |
| Sector Breakdown_ US & Europe.xlsx | Multi-tab sector workbook: Country Indices, World View, Value Chain, ISM Manufacturing, S&P500, DJIA30, Eurostoxx600 (603 rows), FTSE AllShare (672 rows), EuroSectors super-sector map | 2013-era snapshot | None |
| Sector View Formalisation.xlsx | Country Indices, Value Chain (demand→supply), Portfolio Themes (idea/action/reason), Commodities View grid | 2013-era | None |
| EU Sector Construction Template.xlsx | Eurostoxx 600 Full constituent build template (601 rows, RIC/Sector/Subsector) | Static template | None |
| EU_industry_subsectors_sa_nace2/ | Eurostat NACE2 industrial sub-sector production (monthly, quarterly) | EU official series | None |
| EG_Profiles_Longs.xlsx | 11 earnings-growth-momentum "profile" buckets, each a bar chart ranking stocks vs sector average | Snapshot | 11 BarCharts (EG momentum profiles + "PE Ideal") |
| ADRs List.xlsx | ADR master + 17 country tabs (China 155 rows, Europe 96, UK, Japan, Korea, Brazil, India, etc.) for trading foreign names on US exchanges | Static reference | None |

## Charts & key trends
- **GICS cyclical/defensive split (GICS Breakdown.xlsx)** — The 69 GICS industries are tagged 41 Cyclical, 22 Defensive, 6 Both. Each of the 11 sectors carries a cyclical/defensive/both weighting; e.g. Energy is scored ~0.594 cyclical / 0.319 defensive / 0.087 both. This matrix is the master lookup that lets the trader convert a regime view ("late-cycle, slowing growth → go defensive") into a precise list of industries to favour or fade.
- **US Stock Screener (US_Sector_Data.xlsm)** — ~3,180 US stocks above $1bn market cap, sorted largest first (top names DELL ~$86bn, ARMK ~$9.4bn, TRGP ~$13bn). 41 columns span Revenue FY0–FY2, Revenue Growth FY1/FY2, EPS FY0–FY3, earnings-growth (EG F1–F3), forward PE (FY1–FY3), PEG (F1–F3), Debt/Equity, Net Profit Margin (LTM), Dividend Yield, Earnings Surprise FQ-3→FQ0, and 60-day EPS-estimate revisions. Median forward PEs cluster in the low-double-digits; revenue-growth FY1 averages ~0.42 across the universe with a long right tail. This is the bottom-up engine once a sector is chosen.
- **Country Indices map (Sector View Formalisation / Sector Breakdown)** — Catalogues tradable index universes: S&P500 (500 stocks), DJIA (30), DJ Composite (65), plus European indices down to the Swiss SPI (230). Constituent counts roll up to a ~6,550-stock tradable universe across the listed indices, with overlap columns flagging names that appear in multiple indices. Defines the "fishing pond" for stock selection.
- **EuroSectors super-sector map** — Aligns FTSE 350 Super Sectors (e.g. ^FTUB3300 Automobiles & Parts, ^FTUB8300 Banks) with STOXX Europe 600 super-sectors and the equivalent S&P500 / DJIA groupings, enabling apples-to-apples cross-region sector comparison.
- **Earnings-growth momentum profiles (EG_Profiles_Longs.xlsx)** — 11 bar-chart buckets rank stocks by where their earnings-growth momentum sits relative to the sector average, from "Sequentially Positive (above Sector Average)" down through loss-making negatives, plus a "PE Ideal" screen ("Stock P/E on a Premium to Sector and Positive"). This is the qualitative grid used to pick the strongest longs (above-average, accelerating EG at a justified premium) and weakest shorts within a sector.
- **ISM Manufacturing (Sector Breakdown)** — Tracks the ISM headline (e.g. 54.4 reading captured) and the ranked lists of industries reporting growth vs contraction in a given month — a real-economy cross-check on which sectors the macro cycle is actually favouring. See [[Leading Indicators]].
- **Value Chain framework (both workbooks)** — A demand→supply grid (commodities → manufacturers → wholesalers → distributors) that forces the trader to map a sector idea across its entire value chain, so the macro view is expressed at the link with the best risk/reward rather than just the obvious name.

## How it's used in the strategy
The macro regime determines a cyclical-vs-defensive tilt; the **GICS cyclical/defensive matrix** translates that tilt into a precise industry list. The **Country Indices** map defines the tradable universe, and the **value chain** framework directs the trader to the right link in the chain. Within the chosen sector, the **US/EU screeners** rank names on forward EG, PE, PEG, margins, debt and estimate-revision momentum, while the **EG momentum profiles** isolate the strongest longs and weakest shorts. The result feeds straight into the [[Trade Idea Generation Process]]: the best name becomes a long, the weakest a short — frequently paired within the same sector as a [[Spread Trades]] relative-value position to hedge out market and sector beta. ADRs let the trader access foreign names through US listings without direct foreign-market execution.

## See also
[[The Global Macros Framework]] · [[Trade Idea Generation Process]] · [[Macro Regime Snapshot]] · [[Bull & Bear Markets]] · [[Leading Indicators]] · [[Company Stats & Screening]] · [[Spread Trades]] · [[Cyclical Commodities]] · [[Sector Analysis & Rotation]] · [[CB LEI vs Financial Stocks — a Circularity Warning (July 2026)|CB LEI vs financials — circularity warning]]
