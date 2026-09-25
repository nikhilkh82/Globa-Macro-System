---
title: Bull & Bear Markets
category: positioning
type: domain
data_asof: 2021-10-11
summary: "Rules-based -20% bull/bear regime classifier across 14 global indices (S&P daily 1928–Oct-2021) framing net exposure and VIX-sized hedge intensity; ~39% of S&P days sit in bear state, GFC -57% the deepest modern bear."
tags: [global-macro, bull-bear, drawdowns, regime, net-exposure, indices]
data_vintage: "S&P 500 daily 1928–2021; other indices ~1980/1985–2021"
sources: 1
updated: 2026-06-18
---

# Bull & Bear Markets

**What it is & why it matters** — A simple, rules-based regime classifier applied to 14 major global equity indices. The definitions are mechanical: a **bear market** = a 20% fall in an index from its rolling high; a **bull market** = a recovery back above the bear-market level. Mapping where each index sits in its bull/bear cycle is the top-down context that frames overall **net exposure** (how net-long or net-short the book runs) and how aggressively the Global Macros trader leans on hedges. It pairs directly with [[VIX & Implied Volatility]]: bear regimes are where VIX spikes cluster and where hedging matters most.

> Framing note: Historical teaching dataset. The S&P 500 series runs daily from **3-Jan-1928 to 11-Oct-2021**; most other indices start in the 1980s–2010s and also end Oct-2021. Sheets are **reverse-chronological** (newest row at top). All figures below describe what the workbook shows, not live markets (today is 2026-06-18).

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Bull & Bear Market/Bull_Bear_Markets.xlsx` | One sheet per index. Columns: price (O/H/L/C for S&P), Rolling Index High, Rolling Bear Market Level (= high × 0.80), and two split series — **Bull Market Index** and **Bear Market Index** — that toggle as price crosses the −20% line. A LineChart per sheet overlays bull (normal) vs bear (highlighted) segments. | per index (see below) | 14 LineCharts, one per index |

**Indices covered (14):** S&P 500, Nasdaq 100, Nasdaq Composite, DJIA, Eurostoxx 50, Eurostoxx 600, FTSE 100, FTSE 250, FTSE 350, DAX 40, HSI, HSCEI, Nikkei 225, ASX 200. The Definitions tab notes that for "choppy markets" rough dates are used to delineate cycles.

## Charts & key trends

- **Mechanism.** Each sheet maintains a *rolling all-time high* and a *Bear Market Level* at **80% of that high**. While close ≥ level, the value populates the **Bull Market Index** column; once it breaches −20%, values flow into the **Bear Market Index** column (charted as the highlighted/red segment) until price recovers back above the level. This produces a clean visual of every 20%+ drawdown episode.
- **S&P 500 (1928–2021).** Spans low of **~4 (1-Jun-1932)** to high of **~4,537 (2-Sep-2021)**. Roughly **9,167 of 23,599 trading days (~39%)** are flagged bear-market state. Headline episodes the sheet captures, by peak→trough drawdown:
  - **1929–1932 crash:** −86% (trough ~Jun-1932) — the deepest in the series.
  - **1973–74:** −48% (trough Oct-1974).
  - **1987 Black Monday:** −34% peak-to-trough (peak ~338, trough ~224, Dec-1987).
  - **Dot-com bust:** S&P peak **1,553 → trough 777 (9-Oct-2002)**, **−50%**.
  - **Global Financial Crisis:** peak **1,576 → trough 677 (9-Mar-2009)**, **−57%** — the deepest modern bear.
  - **2011 EU/US-downgrade scare:** −30% (trough Oct-2011).
  - **2018 Q4:** −20% (touched the line on 24-Dec-2018).
  - **COVID crash:** peak **3,394 → trough 2,237 (23-Mar-2020)**, **−34%** — exceptionally fast.
- **Nasdaq Composite (1980–2021).** Low **124 (Mar-1980)** to high **15,374 (7-Sep-2021)**; ~3,999 of 10,484 days flagged bear — captures the dot-com collapse (Composite fell roughly 78% peak-to-trough into 2002, the most violent single bear in the file) plus the GFC and COVID drops.
- **Nasdaq 100 (1985–2021).** Low **107 (Oct-1985)** to high **15,676 (7-Sep-2021)**; ~3,740 of 9,086 days in bear state — again dominated by the 2000–02 tech wipeout.
- **Cross-index read.** Because all 14 sheets share the same −20% rule and end Oct-2021, they can be lined up to see *how synchronised* global bears are. The big drawdowns (2008 GFC, 2020 COVID) appear across virtually every index simultaneously; others (e.g. Hang Seng / HSCEI, Nikkei) carry idiosyncratic long bears that US indices do not, useful for relative net-exposure tilts and [[Spread Trades]].

## How it's used in the strategy

- **Net-exposure framing.** The bull/bear state of the benchmark sets the book's directional bias: a confirmed bull regime supports running **net long**; a bear regime (or indices clustering near their −20% lines) argues for cutting net exposure, raising the short book, or moving to market-neutral. This is the top-down gate that sits above single-name selection in [[Trade Idea Generation Process]].
- **Hedge intensity, sized with the VIX.** Bears are precisely when the [[VIX & Implied Volatility]] negative correlation bites — VIX spikes as indices break their −20% levels. The bull/bear context says *whether* to hedge; the VIX/implied-σ bands say *how much* a move is worth and how wide to set risk. The Global Macros note cautions that buy-and-hold VXX hedging fails structurally, so net-exposure reduction and beta-hedging are the preferred tools — see [[Risk Management]] and [[Portfolio Management]].
- **Drawdown context for position sizing.** Knowing that this dataset's bears reach −34% (COVID), −50% (dot-com) and −57% (GFC) calibrates worst-case sizing: positions are scaled so a regime-level drawdown does not impair the book. Links to [[Distribution of Returns]] and [[Average True Range (ATR)]] for the statistical sizing layer.
- **Regime confirmation.** Combined with macro signals ([[Leading Indicators]], [[Yield Curve & Recession Signals]]) and positioning ([[Commitment of Traders (COT)]]), the bull/bear classifier is a price-based confirmation input into the [[Macro Regime Snapshot]].

## See also

- [[VIX & Implied Volatility]]
- [[Risk Management]]
- [[Portfolio Management]]
- [[Distribution of Returns]]
- [[Sector Analysis & Rotation]]
- [[Yield Curve & Recession Signals]]
- [[Commitment of Traders (COT)]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
