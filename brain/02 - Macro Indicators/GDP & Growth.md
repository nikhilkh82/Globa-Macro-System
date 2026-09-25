---
title: GDP & Growth
category: indicators
type: domain
data_asof: 2020-09
summary: "How real GDP growth correlates with equity indices (S&P/STOXX/Shenzhen at 0–12mo lags), the US demand-side decomposition, long-run US/UK growth, and relative US/EU/China size."
tags: [global-macro, gdp, growth, equity-correlation, business-cycle]
data_vintage: "1790–2031 (mostly 1947–2020 quarterly; long-run annual back to 1790); index-correlation work through 2020-Q3; some 2017-era and 2011/2019 ranking snapshots"
sources: 12
updated: 2026-06-18
---

# GDP & Growth

**What it is & why it matters** — GDP (Gross Domestic Product) is the top-of-funnel coincident measure of an economy's output, and in the Global Macros global-macro framework it is the anchor that the whole top-down process is calibrated against. The strategy's working thesis is that equity indices are a *leading* discount of real economic activity, so a trader needs to know (a) how tightly each major index actually tracks its home GDP, (b) at what lead/lag the relationship is strongest, and (c) where each economy sits in its growth cycle. These workbooks document exactly that: long-run growth history for the US and UK, rolling correlations of the S&P 500, STOXX 600 and Shenzhen Composite against their domestic GDP, the demand-side decomposition of US GDP, and relative-size/contribution snapshots across the US, EU and China. All figures below are historical teaching data as captured in the dataset — not live readings.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
| --- | --- | --- | --- |
| `GDP_Correlations.xlsx` | The core workbook. Quarterly index vs domestic GDP YoY, rolling correlations at 0/3/6/9/12-month lags for S&P 500 (US), STOXX 600 (EU & Eurozone) and Shenzhen Composite (China); plus a long-run US/UK nominal-vs-real annual GDP sheet (1790→) | 1950–2020 (US), 1995–2020 (EU), 1992–2020 (CN); annual 1790–2019 | "Rolling 10yr Correlations: S&P500 YoY (Lagged) vs GDP YoY"; "US/UK Nominal vs Real GDP Growth YoY" bar charts |
| `22. USA GDP Report.xlsx` / `USA_gdp_report.xlsx` | Full demand-side decomposition of US real GDP from FRED (GDPC1): consumption, investment, exports, imports, government — each with bln$, q/q, y/y and annualised rates | 1947–2017 quarterly | Area charts for GDP y/y, q/q, level; each component "VS GDP Growth 1992-2017" |
| `gdp_report.xlsx` | Earlier vintage of the same US decomposition (1992–2013 comparison charts) | 1947–~2013 quarterly | Same component charts, "VS Real GDP Growth 1992-2013" |
| `SP500_Correl.xlsx` | Standalone S&P 500 YoY vs US GDP YoY with the 6-month-lag scatter and 10yr rolling correlation | 1950–2020 quarterly | ScatterChart: S&P500 YoY (6-mo lag) vs GDP YoY |
| `S&P500 vs GDP.xls` | "Quadnomial" directional contingency sheet (816 rows) — counts quarters where index and GDP move same/opposite direction | 1950–2020 | n/a (.xls) |
| `Historical GDP US & UK.xlsx` | Long-run nominal & real GDP growth, US 1791–2011 and UK 1851–2011, plus US-real-vs-UK-real overlay | 1791–2011 annual | "U.S. Real GDP Growth 1791–2011"; "U.S. Real GDP Vs U.K Real GDP Growth 1851–2011" |
| `Historical_RealGDP_Values_Growth.xls` | Wide multi-country historical real GDP values & growth (103 columns) | long-run annual | n/a (.xls) |
| `Global_ GDP.xlsx` | 2019 nominal GDP ranking (top 25 + per-capita + rank), Eurozone members, and a China-vs-US GDP projection to ~2031 | 2019 snapshot + 2013–2031 projection | ranking table |
| `GDP World.xlsx` | 2011 top-25 GDP ranking + China-vs-US GDP catch-up projection to 2031 | 2011 snapshot + projection | ranking table |
| `US, EU & China GDP Contribution.xlsx` | Stylised contribution/weighting of US, EU and China to a growth aggregate | static parameter table | none |
| `Data_Extract_From_World_Development_Indicators.xlsx` | World Bank WDI extract, ~270 rows × 61 year-columns of cross-country indicators | multi-decade annual | none (raw data) |

## Charts & key trends
- **US real GDP level & growth (`22. USA GDP Report`, US_GDP sheet, 1947→2017, oldest row first).** Real GDP rose from ~$1,933bln (1947 Q1) to ~$17,030bln (2017 Q3). Quarterly q/q growth averaged ~0.78% over the full span (range −2.59% to +3.98%); y/y growth averaged ~3.2% but had decayed to ~2.2% by 2017 Q3 — the post-1947 mean is structurally higher than the post-2010 "new normal" of ~2%. The deepest y/y contraction in the series is −4.09% (Global Financial Crisis trough).
- **US GDP demand-side decomposition (same workbook).** Component y/y means over 1947–2017: Personal Consumption ~3.3%, Gross Private Domestic Investment ~4.5% (by far the most volatile — y/y range −29% to +68%), Exports ~5.1%, Imports ~6.2%, Government ~2.8% (and roughly flat/negative recently, y/y −0.07% in 2017 Q3). The expenditure weights captured on the Indicator sheet are roughly Consumption 0.68, Investment 0.17, Net Exports (X 0.12 / M −0.15) and Government 0.18 — i.e. the US consumer drives ~two-thirds of output, which is why consumption is the component most worth watching. Investment is the cyclical swing factor: it collapses fastest into recessions and rebounds hardest.
- **S&P 500 vs US GDP — the headline correlation (`GDP_Correlations`, S&P500_USGDP sheet, 1950–2020).** Contemporaneous (no-lag) rolling 10yr correlation of S&P 500 YoY vs GDP YoY averages only ~0.31 and is noisy (range −0.21 to +0.83). The relationship strengthens markedly when GDP is treated as lagging the market: the 6-month-lag rolling correlation averages ~0.57 and the 9-month-lag ~0.50, peaking near +0.80–0.84. Latest 5yr-block averages on the sheet run No-lag 0.31 → 3-mo 0.49 → 6-mo 0.57 → 9-mo 0.50 → 12-mo 0.35, i.e. **the market leads GDP by roughly two to three quarters.** Note the 6-mo-lag correlation collapsed to −0.09 in the COVID quarter (2020 Q2) as the relationship temporarily broke.
- **STOXX 600 vs EU/Eurozone GDP (1995–2020).** Weaker and shorter than the US. No-lag rolling 5yr correlation averages ~0.06 (essentially nil and frequently negative). With lags it improves to ~0.58 (6-mo) and ~0.63 (9-mo) on average, peaking above +0.90, but is unstable — the 12-mo-lag block swung from +0.88 to −0.57. European indices track domestic GDP far more loosely than the S&P does, partly because STOXX 600 constituents earn a large share of revenue outside the Eurozone.
- **Shenzhen Composite vs China nominal GDP (1992–2020).** The weakest and most counter-intuitive of the three. No-lag rolling 5yr correlation averages only ~0.04 and the lagged correlations are frequently *negative* (6-mo-lag block mean ~0.14 but range −0.74 to +0.83; recent readings deeply negative around −0.25 to −0.35). Chinese equity prices have historically been a poor proxy for Chinese growth — a key Global Macros caution against assuming the index-GDP link is universal.
- **Long-run US vs UK growth (`Historical GDP US & UK` / `GDP_Correlations` annual sheet, 1790/1851–2019).** Over the full sample US real growth averaged ~3.8% YoY (nominal ~5.5%) versus UK real ~2.0% (nominal ~4.2%) — the US has compounded faster for two centuries. Extremes captured: US real growth ranged −12.9% to +18.9%; UK real −12.9% to +10.6%. By 2019 both had converged toward low-2% real (US +2.33%, UK +1.41%), illustrating the maturation of both economies.
- **Relative size & catch-up (`Global_ GDP`, `GDP World`).** In the 2019 snapshot the US is #1 at ~$21.4trln (≈24.8% of world GDP) and China #2 at ~$14.7trln (≈18.2%); the top-25 total ≈ $58.9trln in the 2011 ranking. The China-vs-US projection sheets model China nominal GDP growing ~8% p.a. against US ~2%, crossing/overtaking the US around the late 2020s and reaching ~$33.6trln by 2031 — a forward scenario, not realised data.
- **"Quadnomial" directional test (`S&P500_US_Quadnomial`, `S&P500 vs GDP.xls`).** Rather than a continuous correlation, this builds a 2×2 contingency table on the *sign* of S&P (6-mo lagged) and GDP YoY: cells 1,1 (both up), 0,0 (both down), 1,0 and 0,1 (disagree). On the lagged data the overwhelming majority of quarters fall in the "both up" cell (n≈167 of ~277 in the joint count), confirming a strong same-direction tendency once the market's ~2-quarter lead is accounted for; disagreements cluster around turning points (the 2020 quarters land in the off-diagonal 1,0 / 0,1 cells).

## How it's used in the strategy
A Global Macros global-macro trader uses GDP as the *destination* the rest of the top-down read is trying to forecast, not as a tradeable signal in itself (it is released with a long lag and heavily revised). The practical workflow:
- **Calibrate the lead/lag.** Because the S&P leads US GDP by ~2–3 quarters with a ~0.55–0.60 correlation, the trader reads the equity index and leading indicators *first* and treats incoming GDP as confirmation, sizing conviction by how well the index-GDP relationship is currently holding (the rolling-correlation series tells you whether the link is "on" or, as in 2020 Q2, temporarily broken).
- **Region selection.** The much weaker STOXX-EU and SZSC-China correlations are a warning: index direction is a reliable GDP proxy in the US, far less so in Europe, and unreliable in China. Long/short macro tilts therefore lean harder on the US growth read and use more caution exporting the same logic abroad.
- **Cycle scoring.** Where each economy's real GDP YoY sits versus its long-run mean (US ~3.8%, UK ~2.0%) and versus its own recent trend feeds the regime call (expansion/slowdown/recession), which then drives sector rotation and net exposure.
- **Component watching.** Because consumption is ~two-thirds of US GDP and investment is the cyclical swing factor, the demand-side decomposition is screened to spot whether a slowdown is consumer-led (broad, persistent) or investment-led (sharp, mean-reverting), informing how aggressively to fade or follow it.
- **Structural backdrop.** The relative-size and catch-up data frame the long-horizon allocation question (US vs China weight) that sits behind the tactical book.

## See also
- [[Leading Indicators]]
- [[Coincident Indicators]]
- [[Cyclical Commodities]]
- [[M2 Money Supply & Liquidity]]
- [[Bull & Bear Markets]]
- [[Sector Analysis & Rotation]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Trade Idea Generation Process]]
- [[Global Macro Brain]]
- [[Glossary]]
- [[Measurement Conventions — Growth, Inflation & Index Arithmetic (Mohr)]] — the arithmetic rules (annualising, chain-weighting, index rebasing) every growth number on this page depends on
