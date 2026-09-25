---
title: Average True Range (ATR)
category: technical
type: domain
data_asof: 2020-11-09
summary: "Historical-volatility engine: True Range averaged and normalised to % of price (ATRP) across horizons to rank the universe and scale stops/targets/sizes; Nov-2020 ladder runs govt bonds ~0.5% daily to mid caps 3-4.5%."
tags: [global-macro, atr, atrp, volatility, stops, targets, position-sizing]
data_vintage: "2003–2020, mixed (FX through 2017; ATRP summary 9 Nov 2020)"
sources: 14
updated: 2026-06-18
---

# Average True Range (ATR)

**What it is & why it matters** — ATR is the Global Macros strategy's core *historical volatility* indicator: the rolling average of an asset's True Range, normalised by price into a percentage (ATRP). It answers the practical question "how far does this thing typically move in a day/week/month/quarter?" — which is exactly what you need to place volatility-scaled stops and targets, to rank a tradable universe by how much opportunity each asset offers, and to decide whether a market is "alive" enough to trade short-term or whether you must extend your horizon. It is the volatility engine behind [[Risk Management]] and a screening filter feeding [[Trade Idea Generation Process]].

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `ATR Calculation.pdf` | Step-by-step methodology: TR = High − Low; ATRₓ = (TRₜ+…+TRₜ₋ₓ)/Openₜ₋ₓ, expressed as % | n/a (teaching doc) | — |
| `S&P500 ATR Video & PDF Example.xlsx` | Worked S&P 500 example: rolling 1-day TR & ATRP, averaged over 5/20/60/250/750/1250-day horizons | 1997-03-31 → 2013-02-19 (3,999 days) | — |
| `ATRP - Summary File.xlsx` | Cross-asset ATRP table (Daily/Weekly/Monthly/Quarterly) by asset class: govt bonds, corp bonds, FX, equity indices, mid caps | snapshot 9 Nov 2020 | — |
| `ATR_Rankings.xlsx` | Tradable FX ranked by 1-yr avg Daily/Weekly/Monthly ATR | 1-yr trailing | — |
| `AUDUSD_ATR.xlsx`, `EURUSD_ATR.xlsx` | FX ATR workbooks with multi-horizon summary + daily/weekly/monthly TR | EURUSD 2003-01 → 2013-04; AUDUSD 2008-10 → 2017-08 | — |
| `ATR S&P500, GS, JPM.xls`, `GS JPM.xls`, `ATR_SP500.xls` | Single-name & index ATR (S&P 500, Goldman Sachs, JPMorgan) | various | — |
| `GBP-USD ATR Weekly Data.xlsx` (+ RU copy) | GBPUSD weekly ATR | weekly | — |
| `ATRP - Mid Caps 1/2.xlsx` | ATRP for a mid-cap basket (TPX, EVBG, VIRT, JBLU …) | trailing | — |
| `Heinz ATR.xlsx` | Single-stock ATR worked example (~7,140 rows) | long history | — |
| `Risk Management/ATRP Stops and Targets.xlsx` | TREX ATRP across Daily/Weekly/Monthly/Quarterly with horizon tables feeding stops/targets | 2004-12 → 2020-11 | — |

## Charts & key trends
Numbers are ATRP (True Range as a % of opening price) as captured in the datasets — frame all of these as historical volatility readings, not live levels.

- **The method (from `ATR Calculation.pdf`):** True Range = High − Low for the period; the rolling x-period ATR is the average of those True Ranges divided by the open x periods ago, then formatted as a percentage. The S&P 500 worked example computes a *rolling 1-day* ATRP, then averages it across nested windows.
- **S&P 500 multi-horizon ATRP (`S&P500 ATR …`, data through 19 Feb 2013):** averaged rolling 1-day ATRP rises with the lookback — **5-day 0.56%, 20-day 0.70%, 60-day 0.83%, 250-day (1yr) 1.03%, 750-day (3yr) 1.32%, 1250-day (5yr) 1.72%**. Daily TR over the full 3,999-day series ranged from a low of **0.25%** to a crisis-era spike of **10.57%**, mean ≈ **1.51%**. The PDF's punch-line: over ~50 years daily volatility has trended *down*, so intraday opportunity is usually thin — you must wait for high-vol regimes or lengthen horizon.
- **EURUSD ATRP (`EURUSD_ATR`, through Apr 2013):** daily TR mean **1.28%**, range 0.23%–5.33%; the 1-day ATRP averaged **~0.87%** at the 5-day window vs **~1.13%** at the 5-year window — i.e. EURUSD is a low-vol major.
- **AUDUSD ATR (`AUDUSD_ATR`, through Aug 2017):** average daily ATR **0.71% (1wk)** rising to **1.14% (2yr)**; average monthly ATR **3.8% (6m) → 4.95% (3yr)**. AUDUSD daily TR spiked to **8.48%** in the 2008 crash window — a commodity-currency volatility tell.
- **Cross-asset ATRP ladder (`ATRP - Summary File`, snapshot 9 Nov 2020) — the heart of the file.** All-time ATRP by asset class shows the volatility hierarchy the strategy ranks on:
  - Government bonds (TLT 20yr+): Daily **1.06%**, Weekly 2.59%, Monthly 5.64%, Quarterly 10.0%; IEF (7-10yr) far lower at Daily 0.51%.
  - Asset-class averages: Govt bonds Daily **0.50%**, Corp bonds Daily **0.63%** — bonds are the low-vol floor.
  - Equity mid caps are the high-vol tier: Daily ATRP **3–4.5%** (e.g. JBLU 4.08%, EVBG 4.47%), Weekly **9–10%**, Monthly **20–22%**, Quarterly **34–39%**.
  - Mid-cap basket daily ATRP ranged **0.41%–7.57%** across names, mean ≈ **2.93%** — roughly 5–6× a government bond.
- **Tradable-FX ATR ranking (`ATR_Rankings`):** ranked by 1-yr-average ATR, the most volatile pairs are EM crosses — **USD/RUB (Daily 2.08%, Monthly 14.6%)** and **EUR/RUB (2.05% / 13.9%)** sit at the top; the calmest majors cluster near the bottom — **USD/CAD 0.62% daily**, AUD/NZD 0.72%, with the commodity-major average ≈ 0.75% daily. This ordering is the volatility lens for sizing and pair selection (see [[USD & G10 FX]], [[Cyclical Commodities]]).
- **TREX multi-timeframe ATRP (`ATRP Stops and Targets`, 2004–2020):** horizon tables give average True-Range-% per window — Daily 1-week **5.13%**, 1-month 3.59%; Weekly 1-month **8.41%**, 1-quarter 8.92%, 1-year 11.4%; Monthly 1-quarter **17.3%**, 1-year 24.7%. These per-horizon averages are read straight off into stop/target distances.

## How it's used in the strategy
- **Volatility-based stops & targets.** A Global Macros trader sizes the stop as a multiple of the relevant-horizon ATRP rather than a round number, so the stop sits outside normal noise for that asset and timeframe. A weekly-horizon trade in TREX uses the ~8–11% weekly ATRP; a daily scalp in EURUSD uses ~0.9%. This is the mechanical link documented in `ATRP Stops and Targets.xlsx` and elaborated in [[Risk Management]].
- **Position sizing.** Because ATRP is already a %-of-price, two assets sized to the *same* ATRP-scaled risk get equalised exposure — a high-ATRP mid cap gets a smaller notional than a low-ATRP bond ETF for the same risk budget. Feeds the dollar-risk and beta limits in [[Portfolio Management]].
- **Universe ranking / screening.** `ATR_Rankings` and the `ATRP - Summary File` rank the tradable universe by volatility so the trader concentrates on assets with enough range to make a trade worth the cost (the S&P PDF's explicit lesson: low daily vol ⇒ no day-trading edge ⇒ lengthen horizon).
- **Regime read.** ATRP expanding across horizons flags a higher-volatility regime (risk-off, see [[VIX & Implied Volatility]] and [[Bull & Bear Markets]]); compression flags a quiet, mean-reverting tape. Captured in [[Macro Regime Snapshot]].

## See also
- [[Distribution of Returns]] — the probabilistic complement: ATR gives average range, DoR gives the full shape (skew, fat tails, percentiles).
- [[Risk Management]] — where ATRP stops, targets and sizing are operationalised.
- [[Portfolio Management]] — risk budgeting and beta limits that consume ATR.
- [[VIX & Implied Volatility]] — market-implied volatility vs ATR's realised/historical volatility.
- [[Technical Analysis & Price Action]] — ATR pairs with moving averages and price structure for entries/exits.
- [[USD & G10 FX]] · [[Cyclical Commodities]] — assets ranked by ATR in the FX/commodity universe.
- [[Spread Trades]] — relative ATR informs leg sizing in pair trades.

**Live counterparts:** [[PFTM Global-Macro Execution Strategy]] executes 2×ATR stops with 1%-of-account sizing across FX/indexes/commodities; [[Million Dollar Traders — 5-Step Global Macro (July 2026)]] runs Turtle ATR risk units live; [[Trading System - Backtest (June 2026)]] uses ATR-family vol sizing at cluster level.
