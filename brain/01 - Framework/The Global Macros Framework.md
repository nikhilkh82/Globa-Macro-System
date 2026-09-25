---
title: The Global Macros Framework
category: framework
type: domain
data_asof: 2017-08
summary: The layered systematic top-down process (Field of Play → GDP → leading/coincident indicators → endo/exo scoring → long/short PM → quant/qual trade processing → catalysts → risk), mapped to the 42-video curriculum.
tags: [global-macro, framework, endogenous, exogenous, long-short, methodology]
data_vintage: "2013–2022, mixed (curriculum 42-video, scoring sheets 2015 & 2017-era)"
sources: 7
updated: 2026-06-18
---

# The Global Macros Framework

**What it is & why it matters** — The Global Macros framework is a *layered, systematic* approach to discretionary global-macro and long/short trading taught across a 42-video curriculum. It pushes top-down macro analysis through successive filters — Field of Play → GDP → Leading Indicators → Coincident Indicators → endogenous/exogenous driver scoring → long/short portfolio construction → quantitative then qualitative trade-idea processing → catalysts → risk management — so that "all the trades are subjected [to it] before having trading ideas in our portfolio" (Russell Lloyd, strategy README). The point of the layering is to *quantify and classify* macro data through historical statistical analysis "so as not to leave much to the personal and subjective economic interpretation" — a dynamic but rigorous, repeatable process rather than gut feel.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Video 43/Global Macros Video Series Content and Time Codes.xlsx` | The complete 42-video curriculum with titles & runtimes (total ≈ 2 days 16h of content) | n/a (course index) | — |
| `Updated Market Data/README!.docx` | Russell Lloyd's overview of the endogenous/exogenous/COT strategy and the automated template | 2021-era | — |
| `AUTOMATED ENDO TEMPLATE/ReadME!!! .docx` | Same author's companion note on the automated Endo/Exo/"Exo Combined" template | 2021-era | — |
| `USA_Endogenous_Driver_Analysis.xlsx` (sheet `US Endo' Score`) | The endogenous driver scoring engine for the USA — drivers, scores, sliding scale | 2017-era | scorecard (–150 to +160 scale) |
| `Exogenous_AUD_USD.xls` (sheet `AUD_USD Exo' Score`) | The relative (exogenous) scoring engine for a currency pair | 2015-era | scorecard (–40 to +40 scale) |
| `Video 03/Basic_Statistics_Guide.pdf` | Global Macros "Introduction to Statistics" — distribution, central tendency, dispersion, correlation | n/a (teaching) | height histogram; S&P-vs-GDP scatter (r≈0.25) |
| `Video 04/Bond Market and Interest Rate Basics.pdf` | Bond/yield mechanics underpinning the rates layer | n/a (teaching) | bond cash-flow & pricing examples |

## Charts & key trends
The framework is best read as the curriculum's own running order. The 42 videos group into seven blocks:

- **Block 1 — Foundations (Videos 1–2):** *The Framework* (1h46) and *The Field of Play* (33m). Establishes the universe of tradable macro instruments and the top-down logic.
- **Block 2 — GDP (Video 3, 1h27):** Gross Domestic Product as the anchor variable. The statistics guide shows the predictive linkage is weak/noisy — S&P 500 YoY (6-month lag) vs US Real GDP YoY has a full-series Pearson correlation of only **0.25**, falling to ~0 in sub-periods such as 1985–1995 — so GDP is a *backdrop*, not a timing tool.
- **Block 3 — Leading & Coincident Indicators (Videos 4–14, plus Recap V15):** Ten "Leading Indicators" videos (LI 1–10) plus a "Leading Indicator Accessory" video — the analytical heart of the macro layer. These feed the endogenous score.
- **Block 4 — Long/Short Portfolio Management foundations (Videos 16–21):** parts 1a/1b/2/3/4 plus a recap — how macro bias is expressed as a balanced long/short book.
- **Block 5 — Quantitative Processing (Videos 22–29):** seven parts plus a recap. The statistical screening layer (ATR, distribution of returns, COT, beta, volatility).
- **Block 6 — Qualitative Processing & idea sourcing (Videos 30–37):** qualitative parts 1–2, *Identifying Catalysts*, the *Trade Idea Generation Template*, *Macro-Driven Trade Ideas*, *International Trade Ideas via ADRs*, *Technical Analysis*, *Price Action*.
- **Block 7 — Psychology, Risk & Business (Videos 38–42):** Trading Psychology & Preventative Risk Management (PRM 1–2), Eliminating Emotion (PRM & RRM), and *Trading as a Business — Performance Statistics & Track Record* 1–2.

**The endogenous score (single-country / "absolute" view).** In `US Endo' Score` each macro driver is given a raw rate, then a discretionary **Score I/D** ("Inflationary / Deflationary") out of a total, with a written `State` and `Comment`. Drivers are grouped: Leading Indicator Surveys (ISM Manufacturing 58.8 → score +8; NMI Services 55.3 → +5; UMCSI 96.8 → –5 as a possible peak; Building Permits 1,230 → +3), Money Supply (M2), Interest Rates, Inflation (CPI/PPI headline & core), Employment (NFP), and Balance Sheets & Sovereign Risk (Govt Debt/GDP 102% → +10; CB balance sheet 25.35% of GDP → +3; US 10Y at 2.14% → +7). The block sub-totals (e.g. Leading Indicators +11/40, Inflation +10/40, Sovereign +25/50) roll into a single number: **+36 on a sliding scale of –150 to +160** ("Inflationary overall… most indicators outside Central-Bank action are 'normal' to deflationary"). That single score is the country's macro bias *as captured in the 2017-era dataset* — not a current reading.

**The exogenous score (relative / pair view).** `AUD_USD Exo' Score` scores the *difference* between two economies across four relative drivers: Relative GDP Growth (–2), Relative Balance of Payments (–6), Interest-Rate Differentials & Carry (–4) and Stock-Market Returns / Relative Wealth (–2), each out of 10. They sum to a **SCORE of –14 on a –40 to +40 scale** (mildly bearish AUD vs USD *as captured ~2015*). Endogenous = how an economy looks on its own; exogenous = how it looks *relative to the counter-currency*.

## How it's used in the strategy
A Global Macros global-macro trader runs the layers in order and only lets ideas survive that pass each filter:
1. **Form the macro bias** — score the economy endogenously (inflationary/deflationary, growing/slowing) and, for FX, exogenously vs the counter-economy. This produces a directional view on rates, currencies, indices and sectors.
2. **Translate bias to a long/short book** — express the view as paired longs and shorts so the book is broadly market-neutral and the *alpha* comes from relative selection, not beta. See [[Portfolio Management]].
3. **Quantitatively screen candidates** — filter single names with [[Average True Range (ATR)]], the [[Distribution of Returns]], positioning via [[Commitment of Traders (COT)]], and beta for hedging. See [[Trade Idea Generation Process]].
4. **Qualitatively process** — business analysis, sector tailwinds/headwinds, and identify [[Trade Idea Generation Process|catalysts]] (earnings + non-earnings press releases) that can realise the view inside a 1–3 month horizon.
5. **Time and size** — use [[Technical Analysis & Price Action]] for entry and [[Risk Management]] (PRM/RRM, position sizing, beta hedge) to control downside.
6. **Run it as a business** — track performance statistics and a verifiable track record (Videos 41–42).

Statistics underpins every layer: the statistics guide stresses standard deviation as *the* volatility measure (1σ ≈ 68.27%, 2σ ≈ 95.45%, 3σ ≈ 99.73% of a normal distribution), warns that *correlation is not causation*, and shows correlations across equities "tend to 1" as the VIX rises — directly motivating the volatility and risk layers.

## See also
[[Global Macro Brain]] · [[Trade Idea Generation Process]] · [[Glossary]] · [[GDP & Growth]] · [[Leading Indicators]] · [[Coincident Indicators]] · [[FX Endogenous-Exogenous Framework]] · [[Portfolio Management]] · [[Risk Management]] · [[Distribution of Returns]] · [[Macro Regime Snapshot]]
