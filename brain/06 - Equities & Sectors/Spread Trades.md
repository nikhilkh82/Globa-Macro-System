---
title: Spread Trades
category: equities
type: domain
data_asof: 2013-04
summary: "Intra-sector relative-value pair trades (long strong / short weak, trading the price ratio) that hedge out market and sector risk; the GS/JPM ratio ran from ~0.85 in 1999 to >5 around 2008, then settled ~3.0–3.5."
tags: [global-macro, spread-trade, relative-value, pairs, market-neutral, hedging]
data_vintage: "1999–2013 price histories (GS/JPM daily from 1999; ETF/stock pairs to Mar 2013)"
sources: 6
updated: 2026-06-18
---

# Spread Trades

**What it is & why it matters** — A spread trade is the core market-neutral expression in the Global Macros strategy: go long one stock and short another in the same sector, trading the *ratio* (spread) of their prices rather than either name outright. Dividing the two closing prices isolates relative performance — if the long outperforms the short the spread rises regardless of whether both go up or both go down. This deliberately **hedges out market risk and sector risk to isolate stock-specific (idiosyncratic) risk** — the statement "Goldman Sachs as a company will outperform JP Morgan as a company, regardless of what the market or the banking sector does." It is the mechanism that turns the long/short shortlist from [[Company Stats & Screening]] into a hedged position, and it is why hedge funds are called hedge funds.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
| --- | --- | --- | --- |
| GS_JPM.xls | Daily Goldman Sachs vs JP Morgan closes + GS/JPM spread (3,999 days); GS_JPM_Manu manual-calc tab | Apr 2013 back to ~1999 | Spread line chart (workbook) |
| Spread Trade Examples.xls | Three worked pairs: XLY/XLU (Cons. Disc. vs Utilities ETFs), CMG/ETR, CMG/MCD — daily closes + spread | Mar 2013 back ~4 yrs | Spread ratio series |
| ENG Спрэд трейды пошаговое руководство.pdf | "Excel for Spread Trading" step-by-step guide (download, build spread = B/C, chart it, risk framework) | Teaching guide (GS/JPM example) | Worked GS Vs JPM chart |
| Видео 18. Торговля по спрэдам.pdf | Lecture 18 "Trading Spreads" (RU companion) | Teaching guide | — |
| ENG/RU Анализ Сектора.xlsx | Sector-analysis workbooks (EN/RU) feeding pair selection within a sector | Teaching | — |
| ENG/RU Состовляющие сектора США_Европа.xlsx | US/Europe sector-constituents workbooks (EN/RU) for choosing the two names | Teaching | — |

> Note: the .xls price tabs are stored **reverse-chronological** (newest row at the top). "First" values below are the most recent date in the file (≈2013) and "last" values are the oldest (≈1999).

## Charts & key trends
- **GS / JPM spread (GS_JPM.xls)** — The canonical example. GS closes range ~$48.85 to $233.08 (mean ~$115) and JPM ~$11.40 to $50.68 (mean ~$33) across the 1999–2013 history. The **GS/JPM ratio** runs from ~0.0 lows to a peak of ~5.75, mean ~2.97. The teaching guide's worked snapshot: on 16 Sep 2011, GS $107.49 / JPM $33.43 = **3.22**; if GS rallied 20% to $129 with JPM unchanged the spread would rise to 3.86, i.e. +20% — confirming the spread captures pure relative outperformance. The full 1999–2011 chart shows the ratio climbing from ~0.85 at the 1999 IPO era to peaks above 5.0 around 2008, collapsing into the crisis, then settling ~3.0–3.5.
- **XLY / XLU — Consumer Discretionary vs Utilities (Spread Trade Examples.xls)** — A cyclical-vs-defensive *sector* spread. The XLY/XLU ratio ranges ~0.77 to 1.41 (mean ~1.15); near 1.36 in early 2013 vs ~0.77 at the early-history lows, so discretionary's relative strength vs utilities is itself a tradable risk-on/risk-off macro signal that ties to [[Bull & Bear Markets]] and [[Sector Analysis & Rotation]].
- **CMG / ETR and CMG / MCD (Spread Trade Examples.xls)** — Single-name pairs. CMG/ETR ranges ~0.93 to 7.07 (mean ~3.54); CMG/MCD (Chipotle vs McDonald's, same restaurant sub-sector) ranges ~1.06 to 4.83 (mean ~2.92), reaching ~3.38 in early 2013 — a tighter, more genuinely sector-neutral pair than CMG/ETR (a restaurant vs a utility, which retains macro beta).

## How it's built (Global Macros method)
1. **Pick two same-sector names** — from [[Sector Analysis & Rotation]] / [[Company Stats & Screening]], take the strongest fundamental name (long, the numerator) and a weaker peer (short, the denominator). Same currency for an equities spread; cross-border adds FX (see [[FX Endogenous-Exogenous Framework]]).
2. **Align daily closes** — download both stocks' "Close" history over the common window (the GS/JPM example starts 4 May 1999, GS's IPO date), placing dates and the two price columns side by side.
3. **Compute the spread** — `Spread = Price_long / Price_short` (e.g. `=B2/C2`), formatted to 2 decimals, filled down the full history.
4. **Chart and read it** — plot the spread line; a rising line means the long is outperforming the short. The trader judges whether the current ratio is stretched/cheap vs its own history and trend.

## Risk decomposition (why it hedges)
Every equity position carries **market risk, sector risk and stock (unique) risk**. Going long GS / short JPM neutralises the first two:
- *Market shock* (e.g. a sell-off where the whole market drops 15%): both bank stocks fall ~15%, the loss on the long is offset by the gain on the short — net flat. Market risk hedged.
- *Sector shock* (e.g. a peer like Morgan Stanley misses earnings, dragging all banks down 10%): GS and JPM fall together, again offsetting. Sector risk hedged.
- *Stock-specific outcome* remains: if GS management hedges a downturn better than JPM, GS outperforms and the spread rises — that residual is exactly the bet the trader wants to own.

## How it's used in the strategy
Spread trades are how the Global Macros book stays **market-neutral / low-net** while still expressing high-conviction single-stock views. Sizing uses beta (from [[Company Stats & Screening]]) to set the hedge ratio, and [[Average True Range (ATR)]] to scale and place stops on the spread itself. Entries/exits lean on where the ratio sits versus its historical range and on [[Technical Analysis & Price Action]] of the spread line. The aggregate of many such pairs is governed by [[Portfolio Management]] and [[Risk Management]], and the relative-value logic extends to sector-ETF spreads (XLY/XLU) as a direct, hedged way to trade a [[Macro Regime Snapshot]] cyclical/defensive view.

## See also
[[Sector Analysis & Rotation]] · [[Company Stats & Screening]] · [[Trade Idea Generation Process]] · [[Average True Range (ATR)]] · [[Technical Analysis & Price Action]] · [[Portfolio Management]] · [[Risk Management]] · [[Bull & Bear Markets]] · [[FX Endogenous-Exogenous Framework]]
