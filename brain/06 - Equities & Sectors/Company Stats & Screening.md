---
title: Company Stats & Screening
category: equities
type: domain
data_asof: 2014-12-09
summary: Bottom-up ~2014 regional fundamental snapshots and screening fields (forward P/E, EPS growth, beta, surprise, estimate revisions, cost of capital) that rank single stocks into candidate longs and shorts.
tags: [global-macro, screening, fundamentals, valuation, beta, regional]
data_vintage: "2013–2022, mixed (regional snapshots ~2014; us_stocks Dec 6th ~2014; US screener through 2022)"
sources: 8
updated: 2026-06-18
---

# Company Stats & Screening

**What it is & why it matters** — This is the bottom-up data layer that turns a sector view into a ranked shortlist of individual stocks. Once [[Sector Analysis & Rotation]] has chosen which sectors to favour or fade, these regional fundamental snapshots and screeners let the Global Macros trader rank every company in the universe on growth, valuation, profitability, leverage and estimate momentum — and identify the strongest longs and weakest shorts. The regional files also supply the **beta** and **country-risk** inputs needed to size positions and build market-neutral pairs.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
| --- | --- | --- | --- |
| us_stocks_Fundamental Snapshot.xlsx | "Dec_6th" tab: ~2,030 US stocks with valuation/growth screen (P/E F1 & F2, EPS growth, consensus est., NRI-adjusted EPS) | ~Dec 6th (≈2014) | None |
| us_stocks.xlsx / us_stocks_dec.xlsx | US stock snapshots, 19 columns (~2,030 rows) | ~Dec (≈2014) | None |
| Company Stats_ Europe.xls | Company-specific data (~5,000+ names): Industry Group, Country, Market Cap (US$), Beta; plus Cost-of-capital and Country-risk-premia/tax tabs | ≈2014 | None |
| Company Stats Europe.xls | Earlier Europe snapshot (same schema) | ≈2014 | None |
| Company Stats_ Aus, NZ, Can.xls | Regional fundamentals + cost of capital + country risk premia/tax | ≈2014 | None |
| Company Stats_ China, Hong Kong.xls | Regional fundamentals (name, industry group, country, mkt cap, beta) | ≈2014 | None |
| Company Stats_ Emerging.xls / India.xls / Japan.xls | Regional fundamental snapshots (Japan ~3,520 names) | ≈2014 | None |
| eu_stocks.xlsx / eu_stocks_9.12.14.xlsx | European stock screens (dated 9 Dec 2014) | Dec 2014 | None |

## Screening fields & metrics
- **Valuation:** Forward P/E (F1 = current FY, F2 = next FY); the broader US screener in [[Sector Analysis & Rotation]] adds P/E FY3, PEG (F1–F3) and Net Profit Margin (LTM).
- **Growth:** Last year's growth (F0/F-1), EPS % growth F1 and F2, F1 consensus estimate, last year's EPS before NRI (non-recurring items). Earnings-growth momentum is the headline ranking variable.
- **Risk / structure:** Beta (vs local market), Market Cap in US$, Debt/Equity %, Dividend Yield.
- **Momentum / surprise:** Earnings Surprise % over the last four fiscal quarters (FQ-3 → FQ0) and percentage change in F1/F2 EPS estimates over the prior 60 days — the estimate-revision signal.
- **Cost of capital inputs (regional .xls tabs):** Per-country risk premia, tax rates and cost-of-capital details — used to assess whether a valuation is justified and to compare names across borders on a like-for-like discount-rate basis.

## Charts & key trends
- **US Fundamental Snapshot (us_stocks_Fundamental Snapshot.xlsx, "Dec_6th")** — ~2,030 US names tagged by Sector/Industry. Forward P/E (F1) ranges from single digits (HERBALIFE ~7.3, TRINITY ~7.6, INGRAM MICRO ~10.7) to extreme outliers (MELLANOX ~838, MARTIN MIDSTREAM ~2,193, ZULILY ~197) where near-zero or trough earnings inflate the multiple; universe mean ~28x. F2 (next-year) P/E compresses sharply toward the low-to-mid 20s as forecast earnings recover, flagging "expensive on F1, cheap on F2" recovery candidates. EPS % growth F1 averages ~0.50 with #DIV/0! and negative readings marking loss-makers to screen out or short.
- **European universe (Company Stats_ Europe.xls)** — ~5,000+ names with Beta as the headline risk field. Betas cluster around 1.0 (mean ≈1.01) but span a wide range — defensives and small caps near or below 0.6–0.9 (e.g. several names 0.69–0.90) up to high-beta cyclicals above 1.5 (JCDecaux ~1.53, Havas ~1.52, WPP ~1.43). Market caps run from mega-cap (>$200bn) down to micro-caps under $5m, so a liquidity/size filter is essential before trading.
- **Regional coverage** — Snapshots span Europe, Aus/NZ/Can, China/Hong Kong, Emerging, India and Japan (Japan ~3,520 names), giving global single-stock coverage so the strategy can find the best long and short in any region a macro view points to.

## How it's used in the strategy
After [[Sector Analysis & Rotation]] selects a sector, the trader filters these screens to the chosen industry and ranks names on the variables above. The **best name** (above-average and accelerating EPS growth, positive estimate revisions, a defensible forward P/E and PEG) becomes a candidate **long**; the **weakest** (decelerating or negative growth, negative surprises, stretched multiple) becomes a candidate **short**. **Beta** drives position sizing and the hedge ratio for market-neutral construction, while the **country-risk and cost-of-capital** tabs let the trader compare and discount names across regions consistently. The output is the raw material for [[Spread Trades]] (long the strong name, short the weak peer in the same sector) and feeds the [[Trade Idea Generation Process]] and [[Risk Management]] sizing.

## See also
[[Sector Analysis & Rotation]] · [[Spread Trades]] · [[Trade Idea Generation Process]] · [[The Global Macros Framework]] · [[Risk Management]] · [[Portfolio Management]] · [[Distribution of Returns]] · [[Glossary]]
