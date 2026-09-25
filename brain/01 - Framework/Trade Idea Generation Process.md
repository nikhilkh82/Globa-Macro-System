---
title: Trade Idea Generation Process
category: framework
type: domain
data_asof: 2021-04
summary: "The funnel from macro bias → quantitative screening → qualitative/business → catalysts → trade template → structure & risk sizing, with the ZEN US and JetBlue worked examples."
tags: [global-macro, trade-idea, quantitative, qualitative, catalysts, risk-sizing]
data_vintage: "2015–2021, mixed (template & worked example 2017–2021)"
sources: 6
updated: 2026-06-18
---

# Trade Idea Generation Process

**What it is & why it matters** — This is the Global Macros funnel that turns a top-down macro view into a single, sized, structured trade. It runs macro bias → quantitative screening → qualitative/business analysis → catalysts → trade template → risk sizing, with each stage discarding candidates that fail. The curriculum dedicates ~16 of 42 videos to it (Videos 22–37), reflecting that *generating and processing ideas* — not forming the macro view — is where most of the work and most of the edge sits. The `Trade Idea Template.docx` (worked on Zendesk, "ZEN US") and the `Releases_Template.xlsx` (worked on JetBlue) are the canonical artefacts.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Video 43/Global Macros Video Series Content and Time Codes.xlsx` | Videos 22–37 define the quant → qual → catalyst → template → TA/price-action sequence | n/a | — |
| `Portfolio Management/Trade Idea Template.docx` | The filled-out template: annual quant table, sector comps, business analysis, catalysts, option trade structure | 2017–2021 (ZEN US) | annual fundamentals table |
| `Portfolio Management/Releases_Template.xlsx` | Catalyst-counting workbook: press-release frequency, earnings vs non-earnings | 2017-01 → 2021-04 (JetBlue) | release-count summary |
| `Portfolio Management/Price_Action_Watchlist.xlsx` | Long/short spread watchlist tracking weekly relative performance | rolling (12-week template) | spread % per week |
| `USA_Endogenous_Driver_Analysis.xlsx` (`US Endo' Score`) | Source of the macro bias that seeds the funnel | 2017-era | scorecard |
| `Video 03/Basic_Statistics_Guide.pdf` | The statistical toolkit (distribution, σ, correlation) used in quant screening | n/a | S&P-vs-GDP scatter |

## Charts & key trends — the funnel, step by step

**Step 0 — Macro view (the seed).** Start from the endogenous/exogenous bias (see [[The Global Macros Framework]]). E.g. the 2017-era US Endo score of **+36 / [–150,+160]** = mildly inflationary, which biases the book long cyclicals/short defensives, or toward rate-sensitive expressions.

**Step 1 — Quantitative screening (Videos 22–29).** Reduce the macro view to a shortlist of tradable single names, scored on:
- **Annual fundamentals** — the template tracks a 5-year grid of Stock Price, Market Cap, EPS, Earnings Growth %, P/E, PEG, Sales, Sales Growth %, Sales Multiple, Net Income. Worked example ZEN US: price $34 (2017) → $76 (2019) with EPS –0.13 → 0.317 and Sales Growth ~36–39%; a 2020 price target of **$136.80** is derived as 2019 price ×1.8 using the 2019 P/E (≈239×).
- **Sector comparables** — score the stock against 8 peers (Stock A–H) on PE1, EG1, EG2, PEG1 and Market Cap, then test whether it is a *quantitative outlier* vs the sector average. See [[Company Stats & Screening]] and [[Sector Analysis & Rotation]].
- **Volatility & positioning** — [[Average True Range (ATR)]] for expected per-day/per-week range, the [[Distribution of Returns]] for how far the stock typically moves over the 1–3 month horizon, [[Commitment of Traders (COT)]] for crowding/flip signals in the macro instrument, and **beta** for sizing the hedge.

**Step 2 — Qualitative / business processing (Videos 30–31).** Document the business model and the KPIs that actually drive revenue/earnings. ZEN example: B2B SaaS customer-support "Suite", 200,000 registered businesses, non-GAAP gross margin ~73–74%, free-cash-flow guidance $35–45m, geographic split US 52% / ex-US 48%. The goal is to confirm whether sector drivers give a *tailwind or headwind* to the fundamentals and to estimate single-stock volatility vs the rest of the sector.

**Step 3 — Catalysts (Video 32).** Quantify how *communicative* the company is, because release frequency creates the volatility the trade needs to pay off. The JetBlue `Releases_Template` counts **343 total press releases** over 2017-01 → 2021-04, split into **36 earnings-related** and **307 non-earnings** releases, and tags which headlines moved the price. Earnings announcements (consensus ranges and means) plus non-earnings catalysts inside the trade window are listed, alongside the risks to the trade.

**Step 4 — Trade Idea Template (Video 33).** All of the above is consolidated into one document with the explicit structure: *Annual Quantitative Analysis → Sector Comps → Comments on Business / KPIs → Earnings Announcements → Catalysts excluding Earnings → choice of trade structure with time horizon.*

**Step 5 — Idea sourcing variants (Videos 34–35).** *Macro-Driven Trade Ideas* (expressing the macro score directly via indices, rates, FX, commodities) and *International Trade Ideas via ADRs* (accessing foreign single names through US-listed [[Glossary|ADRs]]).

**Step 6 — Timing (Videos 36–37).** [[Technical Analysis & Price Action]] selects entry/exit and, with short-interest, the "path of least resistance." The `Price_Action_Watchlist` tracks each long/short pair's *spread* and weekly % return over a rolling 12-week window to monitor whether the relative thesis is working.

## How it's used in the strategy
The funnel enforces discipline: a name only becomes a position if it (a) fits the macro bias, (b) is a quantitative outlier vs its sector with favourable ATR/return-distribution math, (c) has a coherent business story, (d) has catalysts inside the 1–3 month horizon, and (e) can be structured with a defined risk/reward. The chosen structure is then sized. The worked ZEN trade is a **July $80–$100 bull call (vertical) spread**: buy 16× $80 calls at $5.27 ($8,432 debit), sell 16× $100 calls at $1.15 ($1,840 credit), net debit ≈ $6,592, max gross $32,000, net profit $25,408 → **ROI ≈ 3.85:1**. Defined-risk option structures cap downside while expressing the directional/relative view; sizing then flows into [[Risk Management]] (beta hedge, position limits, PRM/RRM) and the pair is logged on the [[Portfolio Management]] book.

## See also
[[The Global Macros Framework]] · [[Glossary]] · [[Company Stats & Screening]] · [[Sector Analysis & Rotation]] · [[Average True Range (ATR)]] · [[Distribution of Returns]] · [[Commitment of Traders (COT)]] · [[Technical Analysis & Price Action]] · [[Spread Trades]] · [[Portfolio Management]] · [[Risk Management]]
