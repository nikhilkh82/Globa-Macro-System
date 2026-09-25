---
title: Distribution of Returns
category: technical
type: domain
data_asof: 2020-11-09
summary: Binned return histograms with mean/std/skew/kurtosis/percentiles, the probabilistic complement to ATR; AUDUSD daily kurtosis 10.5 and skew -0.28 prove fat tails, so stops/targets are set off percentiles, not a normal.
tags: [global-macro, distribution, returns, statistics, skew, kurtosis, fat-tails, percentiles, probability]
data_vintage: "1997–2020, mixed (FX AUDUSD example 2008-10 → 2015-03; cross-asset summary 9 Nov 2020)"
sources: 13
updated: 2026-06-18
---

# Distribution of Returns

**What it is & why it matters** — Where [[Average True Range (ATR)]] gives the *average* range, Distribution of Returns (DoR) gives the *whole shape*: it bins an asset's historical period returns into a frequency histogram and extracts mean (expected return), standard deviation (the strategy's volatility/risk measure), skew, kurtosis, range, and cumulative percentiles. The Global Macros use is explicitly probabilistic — it tells you the odds of a move of a given size, where to set probabilistic targets, and crucially that real asset returns are *not* normal: they are "peakier" with **fat tails**, so extreme moves happen far more often than a Gaussian assumes. This is the statistical backbone for stops/targets in [[Risk Management]] and a cross-asset ranking input to [[Trade Idea Generation Process]].

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `FX Distribution of Returns Tutorial.pdf` | 83-page methodology: normal distribution primer + full AUDUSD worked example (open-to-open & high-to-low returns, frequency tables, descriptive stats, std-dev occurrence table) | AUDUSD 2008-10-01 → 2015-03-01 | Height bell-curve; AUDUSD open-to-open & high-to-low histograms |
| `Distribution/S&P500 Distribution [PDF & Video Example].xlsx` | S&P 500 daily close-to-close returns binned −2%…+2%, with avg pos/neg & probability table | 1996-12 → 2012-11 (3,993 days) | Bar chart "Occurrences" |
| `Distribution/AUDUSD_return_dist.xlsx` | AUDUSD open-to-open & high-to-low return distributions | 2008-10 → 2017-08 (2,310 days) | "Open to Open returns", "High to Low Returns" |
| `Distribution/EURUSD_return_dist.xlsx`, `EUR-USD …`, `GBP-USD …`, `GDPUSD_return_dist.xlsx` | FX majors return distributions | various | histograms |
| `Distribution/WTI Distribution of Returns.xlsx` | WTI crude daily returns binned −6.5%…+6.5% | 1997-04 → 2013-04 (3,993 days) | Bar chart "Frequency" |
| `Distribution/FTSE100 Distribution of Returns.xlsx` | FTSE 100 daily return distribution | long history (~7,342 rows) | Frequency histogram |
| `Distribution/S&P500 Quarterly Distribution of Returns.xlsx` | S&P 500 quarterly-horizon return distribution | long history | — |
| `Distribution of Returns - Bond ETFs.xlsx` | Return distributions for bond ETFs (TLT, IEF …) | — | — |
| `Distribution of Returns - Mid Caps 1.xlsx` | Mid-cap return distributions | — | — |
| `Distribution of Returns - Summary File.xlsx` | Cross-asset C-C std dev & H-L return averages (Daily/Weekly/Monthly/Quarterly) by class | snapshot 9 Nov 2020 | — |
| `Distribution/Distribution_Rankings.xlsx` | Tradable FX ranked by Std Dev and Mean High-to-Low | trailing | — |
| `Risk Management/DoR Stops and Targets.xlsx` | TREX C-C / H-L / O-C returns with frequency bins, probabilities & cumulative % across timeframes | 2004-12 → 2020-11 | three "Occurrences" bar charts |

## Charts & key trends
Two return definitions run throughout: **open-to-open** (overnight directional return, can be ±) and **high-to-low** (the day's range as a % of the low — always ≥ 0, a pure intra-period volatility/opportunity gauge). All figures are historical, as captured in the datasets.

- **AUDUSD open-to-open (the canonical worked example, 2008-10-01 → 2015-03-01, n = 1,995 days):** Mean (expected daily return) **0.003%** — economically zero. Std dev **0.876%**. **Kurtosis 10.495** (strongly fat-tailed) and **skew −0.281** (negative — downside moves more extreme). Range **15.077%** (min **−7.623%**, max **+7.453%**). Average positive day **+0.576%** (988 up days), average negative **−0.571%** (986 down days), 21 flat days. Cumulative reads such as "94.69% of days ≤ +1.2%" and "16.09% of days ≤ −0.6%" come straight off the cumulative-% column.
- **AUDUSD high-to-low:** **mean 1.153%**, max **10.892%**, kurtosis and skew both well above 0 — a one-sided, non-normal distribution. The tutorial flags this as the single best cross-asset *opportunity/volatility* comparator alongside open-to-open std dev. (The independent `AUDUSD_return_dist.xlsx` workbook through 2017 corroborates: O-O mean ≈ 0.004%, n ≈ 2,309, O-O range −8.82% to +7.76%, H-L mean ≈ 1.31%, H-L max ≈ 11.53%.)
- **Normal vs actual (std-dev occurrence table):** a Gaussian predicts 68.2% / 95.4% / 99.8% of data within ±1/±2/±3 σ. Actual AUDUSD counts were **79.65% / 94.74% / 98.35%** — *more* mass inside ±1σ and *more* mass beyond ±3σ than normal predicts. Since 1σ ≈ 0.87% here, **moves beyond ±2.6% occur more often than normal distribution allows** — the practical fat-tail warning.
- **S&P 500 daily (1996-12 → 2012-11, n ≈ 3,992):** average return **+0.029%**, average up day **+0.676%**, average down day **−0.693%**; daily extremes from **−8.72%** to **+10.79%**. Frequency table peaks hard in the −0.5%…+1.5% bins (e.g. the 0%→+0.5% bin holds 3,473 days, 27.1% of the sample) with long thin tails.
- **WTI crude daily (1997-04 → 2013-04, n ≈ 3,993):** average return **+0.044%**, average up day **+1.39%**, average down day **−1.35%** — roughly double an FX major; daily range **−12.77%** to **+26.99%**. Confirms commodities sit high on the volatility ladder (see [[Cyclical Commodities]]).
- **Cross-asset DoR summary (`…Summary File`, 9 Nov 2020):** close-to-close *daily std dev* climbs by class — govt bonds (TLT) **0.88%**, IEF 0.42%; equity mid caps **3–4%** daily, with weekly H-L return averages up near **9–10%** and quarterly std dev up to ~**19%** for the most volatile names. The same volatility hierarchy as ATR, expressed as σ rather than range.
- **TREX DoR stops/targets (`DoR Stops and Targets`, 2004–2020):** builds C-C, H-L and O-C return distributions per timeframe with frequency, probability and cumulative-% columns and bins like "−6.0% to −4.5%", "−1.5% to 0.0%", "3.0% to 4.0%". Daily C-C returns ranged **−29.66% to +25.91%**, mean ≈ 0.12% — the file then reads percentiles off the cumulative column to set probabilistic stops and targets.
- **Tradable-FX ranking (`Distribution_Rankings`):** ranked by std dev and mean H-L, the most volatile majors/crosses (USD/ZAR std dev **1.1%**, AUD/JPY **1.2%**, GBP/ZAR) sit at the top; calm crosses (GBP/EUR **0.47%**, EUR/CHF) at the bottom — the FX selection lens (cross-link [[USD & G10 FX]]).

## How it's used in the strategy
- **Probabilistic targets & stops.** Percentiles of the return distribution set realistic target distances ("≈26% of days exceed a 1.4% H-L move") and stop placement that respects the fat-tailed reality rather than a normal assumption. Operationalised in [[Risk Management]] via the DoR stops/targets workbook.
- **Risk = standard deviation.** Open-to-open std dev is the strategy's headline volatility/risk number, feeding sizing and the beta/risk limits in [[Portfolio Management]].
- **Expected-return reality check.** Because daily mean returns are ~0% and average up/down days are tiny (and symmetric), the tutorial's conclusion is that unleveraged day-trading has essentially no edge after costs — pushing the trader to *longer horizons* where larger moves (and the fat tails) create the opportunity. This frames the medium-term, position-style bias of the Global Macros book.
- **Cross-asset opportunity ranking.** Comparing std dev (open-to-open) and mean high-to-low across assets — on identical timeframes/periods — ranks which markets offer the most risk/opportunity to deploy capital into ([[Trade Idea Generation Process]], [[Sector Analysis & Rotation]]).
- **Fat-tail / regime awareness.** Elevated kurtosis and negative skew warn that downside gaps cluster — a risk-management overlay that pairs with [[VIX & Implied Volatility]] and [[Macro Regime Snapshot]].

## See also
- [[Average True Range (ATR)]] — the average-range twin; ATR and DoR are read together for stops/targets/sizing.
- [[Risk Management]] — where return percentiles become stop/target distances and position sizes.
- [[Portfolio Management]] — std-dev-based risk budgeting and beta limits.
- [[Technical Analysis & Price Action]] — distribution context overlaid on price structure.
- [[VIX & Implied Volatility]] — implied vol vs the realised distribution's fat tails.
- [[USD & G10 FX]] · [[Cyclical Commodities]] — assets ranked by their return distributions.
- [[Spread Trades]] — relative volatility/distribution informs hedge ratios.
