---
title: Cyclical Commodities
category: indicators
type: domain
data_asof: 2021-03
summary: Industrial commodities (oil, copper, iron ore, coal, lumber) as a growth barometer under the demand-vs-supply rule, with the China-demand → iron-ore/coal → AUD linkage.
tags: [global-macro, commodities, leading-indicators, copper, iron-ore, coal, crude-oil, lumber, aud, china, demand-supply, cot]
data_vintage: "1980–2021 (price series mostly 1983–2021; coal monthly 1980–2015; coal/China consumption to 2013; COT 2020–2021)"
sources: 10
updated: 2026-06-18
---

# Cyclical Commodities

**What it is & why it matters** — Cyclical (industrial) commodities — crude oil, copper, iron ore, coal, lumber — are real-time barometers of global demand because they are consumed in production, not stored as a final good. In the Global Macros framework the *critical distinction is demand-driven vs supply-driven price moves*: per the methodology doc, **prices driven by demand factors give a STRONG signal to global GDP; prices driven by supply factors give a WEAK signal.** A copper or iron-ore rally on Chinese demand is a genuine growth read; the same rally on a mine outage is noise. The page also tracks the commodity-currency linkage — Australia is the world's #1 iron-ore exporter ($67.5bn, 2019) and a top coal/copper exporter, so its terms of trade (and the AUD) move with bulk-commodity demand from China, the dominant consumer.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Commodity_Prices.xlsx` | 15 tabs: WTI & Brent crude, Copper (COMEX/LME/SHFE) + cross-venue spreads, Lumber, Iron Ore (CME & DCE) + spread; each with daily%/weekly% returns, descriptive stats, distribution histograms & price line chart | WTI from 1983-03; Brent/Copper from 1988; Lumber long history; Iron Ore CME 2010-10 → 2021-03 | Per-commodity price LineChart + daily%/weekly% histograms (5 charts/tab) |
| `Iron_Ore_Prices.csv` | Iron Ore spot price, any origin (monthly, reverse-chron) | 2006-01 → 2015-02 (110 pts) | — |
| `Australia_Coal_Prices.csv` | Australia coal price, monthly (reverse-chron) | 1980-01 → 2015-02 (422 pts) | — |
| `Australia_Coal_Price_Vs_AUD_USD.csv` | Australia coal price paired with AUD/USD spot | 1980-01 → 2015-02 (AUD populated from ~2000s) | — |
| `China_Coal_Consumption.csv` | China annual coal consumption (Mtoe) | 1965 → 2013 (49 pts) | — |
| `Japan_Coal_Consumption .xls` | Japan annual coal consumption (Mtoe) | 1965 → 2013 (49 pts) | — |
| `USD_Trade_Weighted_Indices.xlsx` | USD trade-weighted indices: Broad, Narrow vs Advanced, Narrow vs EM, with daily%/weekly% & histograms | Broad from 1995-01 | USD index line charts + return histograms |
| `Commitment_of_Traders_Metals___Energy.xlsx` | Weekly COT manager net positioning (Longs−Shorts)/OI for WTI, Brent, heating oil, nat gas, palladium, platinum, silver, gold, copper, aluminium, steel; summary tab | ~2020-09 → 2021-02 (weekly summary) | Net-position line charts per commodity (2/tab) |
| `Summary_File.xlsx` | Daily & weekly std-dev / percentile return bands across all the above price series | Snapshot | — |
| `Cyclical_Commodities_Demand_Supply_Factors.pdf` | Methodology + source links (EIA, OPEC, IEA, USGS, ICSG, Cochilco) and 2019 top exporter/importer tables for oil, copper, iron ore, lumber | Reference (2019 trade data) | — |

## Charts & key trends
- **WTI crude** — Daily% mean ~0%, range **−33% to +15.3%**; weekly% range **−31% to +39%** — fat-tailed, the widest single-day downside of any series in the file (the price tab itself caps at 1999 in this extract but the return distribution spans the full history). Crude's demand-vs-supply read is the explicit focus of the methodology doc (EIA/OPEC/IEA links).
- **Brent crude** — Range in the loaded window **$9.64–$40.15/bbl**, mean ~$20.5; daily% −34.8% to +14%. WTI–Brent spread has its own tab (the transatlantic arb / US shale signal).
- **Copper ("Dr. Copper")** — COMEX continuation ranged **$0.60–$1.62/lb** in the loaded window (mean ~$0.98); daily% −11.4% to +8.7%. Three venues tracked — COMEX, LME, SHFE — with COMEX-LME, COMEX-SHFE and LME-SHFE spread tabs, letting the trader read regional (esp. Chinese SHFE) demand premia. Copper is the headline demand-sensitivity gauge for global industrial activity.
- **Iron Ore (CME 62%)** — The freshest price series: **2010-10 → 2021-03**. Ran from $143.9/t (2010) down to a sample low of **$38.5/t** and back up to **$171.7/t (1-Mar-2021)**, with a peak of **$188.9/t**; the closing run accelerates ($163.9 → $164.2 → $164.5 → $165.0 → $165.6 → $171.7) — the post-COVID China steel-demand surge. A separate DCE (Dalian) tab and CME-DCE spread capture the China-onshore vs offshore price gap.
- **Lumber** — Longest daily history in the file; tracked for its read on US housing/construction demand.
- **China vs Japan coal consumption (Mtoe, 1965–2013)** — China consumption exploded from **112 Mtoe (1965)** to **1,925 Mtoe (2013)** — a ~17x rise that made China the marginal driver of seaborne bulk demand. Japan, by contrast, rose modestly from ~44 Mtoe (1965) to ~129 Mtoe (2013) and was flattening/declining at the end. This divergence is *why* the framework treats China as the swing consumer for iron ore and coal.
- **Australia coal price & AUD/USD** — Australia coal rose from ~$39.7 (1980) to a cycle high then eased to **$65.8 (Feb-2015)**; AUD/USD in the paired series falls in step into the end of the sample — **0.880 (Oct-2014) → 0.851 → 0.817 → 0.777 → 0.781 (Feb-2015)**. Falling bulk-commodity prices drag Australia's terms of trade and the currency together — the core iron-ore/coal → AUD link. Iron-ore spot in the standalone CSV fell from $74 (Nov-2014) to **$63/t (Feb-2015)** over the same window, confirming a *demand*-side cooling (China) rather than a supply shock.
- **USD trade-weighted (Broad) index** — From 85.7 (1995) into the loaded window; mean ~100, range **80.8–118.2**. The USD is the denominator for commodity prices — a stronger dollar mechanically pressures commodity prices and commodity-currency crosses, so it is monitored alongside (Broad, vs-Advanced, vs-EM cuts).
- **COT manager net positioning (2020-09 → 2021-02, weekly)** — Speculative net longs as a share of OI: **copper net long ~+25% to +36%** (ended ~+28.7%), **steel swinging from −25% to +37%** (a sharp positioning flip into early 2021), **palladium persistently long ~+12% to +42%**, **WTI hovering near flat (−3% to +2.4%)** while **Brent flipped from +3.6% to −12.3%** (net short). Crowded longs in copper/steel/palladium flag both the reflation trade and potential positioning risk.

## How it's used in the strategy
- **Demand vs supply triage (the core rule)** — Before treating a commodity move as a macro signal, the trader establishes the driver. A demand-led rally (broad across copper, iron ore, oil; corroborated by Chinese consumption) is a STRONG positive GDP read and confirms a risk-on regime; a supply-led move (single-commodity, inventory/outage-driven) is a WEAK signal and discounted. Source links (EIA, OPEC, IEA, USGS, ICSG, Cochilco, World Bank) are used to verify production/inventory/stock data.
- **Leading indicator for growth** — Cyclical commodity strength feeds the growth view alongside PMIs and yields. See [[Leading Indicators]] and [[GDP & Growth]].
- **China nowcast** — Because China dominates iron-ore and copper imports (and coal consumption ~1,925 Mtoe), SHFE/DCE prices and the onshore-offshore spreads are read as a proxy for Chinese industrial demand.
- **Commodity-currency / FX overlay** — The iron-ore/coal → AUD link (and copper → AUD/CLP) lets the trader express a China-demand view through FX as well as the underlying commodity; the USD trade-weighted indices are the cross-check on whether a commodity move is real or just a dollar move. See [[USD & G10 FX]] and [[FX Endogenous-Exogenous Framework]].
- **Positioning & risk** — COT net-position extremes (e.g. crowded copper/steel longs into 2021) are used as a contrarian/risk flag and for sizing; the std-dev return bands in `Summary_File.xlsx` and the per-commodity histograms feed volatility-aware sizing. See [[Commitment of Traders (COT)]], [[Distribution of Returns]], [[Average True Range (ATR)]] and [[Risk Management]].
- **Spread expression** — WTI-Brent, COMEX-LME-SHFE copper and CME-DCE iron-ore spreads are tradable relative-value legs. See [[Spread Trades]].

## See also
- [[Leading Indicators]]
- [[GDP & Growth]]
- [[M2 Money Supply & Liquidity]]
- [[USD & G10 FX]]
- [[FX Endogenous-Exogenous Framework]]
- [[Commitment of Traders (COT)]]
- [[Distribution of Returns]]
- [[Average True Range (ATR)]]
- [[Spread Trades]]
- [[Sector Analysis & Rotation]]
- [[Risk Management]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Glossary]]

**Live counterparts:** [[Global Macro Trading Deck (July 2026)]] tracks oil/gold/silver/copper weekly+daily with the OVX/GVZ/VXSLV vol add-on; [[Australia Endogenous Driver Analysis (July 2026)]] scores the iron-ore/copper terms-of-trade complex live; [[Economic Surprises & Commodities System]] is the honest test of growth-surprises -> commodity returns (null; gold counter-cyclical).
