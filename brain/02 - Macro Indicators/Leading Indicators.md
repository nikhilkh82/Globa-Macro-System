---
title: Leading Indicators
category: indicators
type: domain
data_asof: 2026-07-25
summary: Survey- and order-based series (ISM, global/China PMIs, UoM, NFIB, EU ESI, building permits) that turn before the real economy, anchored on the ISM 50-line.
tags: [global-macro, leading-indicators, ism, pmi, sentiment, housing]
data_vintage: 1948–2022, mixed (most series through 2013/14, 2017, 2020/21; UoM to Oct-2022)
sources: 18
updated: 2026-07-25
---

# Leading Indicators

**What it is & why it matters** — Leading indicators are the survey- and order-based series that *turn before* the real economy does. In the Global Macros global-macro framework they sit at the top of the indicator stack: a trader reads them to anticipate the direction of growth (and therefore the direction of equities, rates and cyclical assets) before the lagging hard data confirms it. The keystone series is the **ISM Manufacturing PMI** — a diffusion index where **50 is the dividing line between expansion (>50) and contraction (<50)** — backed by global PMIs (Markit/S&P Global, Caixin), confidence surveys (University of Michigan, NFIB, EU ESI) and housing permits. The job is not to forecast a number but to read momentum and the 50-line: is the leading set accelerating or rolling over, and is the breadth broad or narrow.

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `ISM/ISM_SP500.xlsx` | ISM Manufacturing PMI vs S&P 500 % returns | 1950–2013 (757 pts) | PMI vs S&P500 % returns 1972–2013 |
| `ISM/Manufacturing/ISM_Manufacturing_SP500_GDP.xlsx` | ISM Mfg PMI vs GDP QoQ-annualised & vs S&P 500 (level + YoY) | 1950–2020 | ISM vs GDP; ISM vs S&P500 (Area + YoY) |
| `ISM/Manufacturing/ISM_Manufacturing_Index.xlsx` | Headline ISM Mfg + all 10 sub-components (New Orders, Production, Employment, Deliveries, Inventories, Customer Inv., Prices, Backlog, Exports, Imports) + heat map | 1948–2020 (876 pts) | PMI all-time & 1990–; each component vs headline |
| `ISM/Non-Manufacturing/ISM_NonManufacturing_SP500_GDP.xlsx` | ISM Non-Mfg (services), NMI & Business Activity vs GDP and S&P 500 | 1997/2008–2020 | NMI vs GDP; Business Activity vs S&P 500 |
| `ISM/ISM-VS_ВВП.xlsx`, `ISM/PMI- ISM.xls` | US GDP vs ISM cross-checks | to ~2013 | line overlays |
| `Global Economic Indicators/10. Global Manufacturing PMIs.xlsx` | Global + 20-country manufacturing PMIs vs national GDP | 2010–2014 (≈50 pts ea.) | Global Mfg PMI; per-country PMI vs GDP |
| `Global Economic Indicators/7. Global Services PMI.xlsx` | Global + country services PMIs | 2010–2014 | Global Service PMI |
| `PMI/global_manufacturing_pmis_-_03.12.14.xlsx`, `..._service_pmis_-_04.12.14.xlsx` | Dated 2014 snapshots of the global PMI books | →Dec-2014 | per-country panels |
| `China Economic Indicators/18. China Official PMI.xlsx` | Official NBS China Mfg PMI + components | 2006–2014 (103 pts) | China Mfg PMI; vs Output/New Orders |
| `China Economic Indicators/19. China Caixin(Prev HSBC) PMI.xlsx` | Caixin/HSBC China Mfg PMI vs Official, vs GDP, vs FXI ETF, vs WTI | 2005–2014 (120 pts) | HSBC vs Official; PMI vs GDP YoY |
| `China Economic Indicators/20. China Conference Board PMI.xlsx`, `China_Manufacturing_PMIs.xlsx` | Conference Board leading index / combined China PMIs | mixed | overlays |
| `University of Michigan/3. UMCSI_2021.xlsx` | UoM Consumer Sentiment, Expectations, Current Conditions + vs GDP | 1978–Oct-2022 (538 pts) | UMCSI & change; Exp vs CC |
| `University of Michigan/UMCSI.xlsx` | UMCSI / Expectations / Current Conditions w/ MoM change, vs GDP & S&P 500 | 1978–Jan-2021 (517 pts) | UMCSI vs Exp vs CC; vs S&P 500 YoY |
| `NFIB Small Businesses/NFIB_Small_Business_Sentiment_Components.xlsx` | NFIB Small Business Optimism core index + 10 component plans, vs GDP & S&P 500 | 1986–2020 (420 pts) | SBO Index 1986–; SBO vs GDP YoY |
| `NFIB Small Businesses/NFIB_..._Industries.xlsx`, `..._Regions.xlsx` | NFIB optimism by industry & region | mixed | cross-section |
| `Building Permits/25. US Housing Report.xlsx` | Building Permits Authorised, Housing Starts, Completions, vs XHB ETF & GDP | 1960–2017 (692 pts) | Permits; Permits vs Starts; vs XHB |
| `Building Permits/US_Building_Permits.xlsx` | Permits series (standalone) | to ~2017 | permits |
| `EU Economic Sentiments/European_Economic_Sentiment_Indicator.xlsm`, `23. ESI Major Countires.xlsx` | EU/EA Economic Sentiment Indicator (ESI) + INDU/SERV/CONS/RETA/BUIL confidence, by country | 1985–Jan-2021 (433 pts) | ESI; sectoral confidence panels |
| `All EU Surveys/` (esi, industry, services, retail, consumer, building, investment) | Full EU DG-ECFIN survey set, NACE2, monthly/quarterly | →2017-era | BCI, investment plans |
| `US_Leading_Indicators_2017.xlsx` | Placeholder / near-empty GDP tab | 2017 | n/a |

## Charts & key trends

**ISM Manufacturing PMI (the keystone, 1948–2020, 876 pts).** As captured in the dataset the headline ISM Mfg index averages **~52.9**, oscillating around the 50 expansion line. Extremes frame the cycle: a low of **29.4** (deep recession reading) and a high of **77.5** (early-1950s boom). The last six monthly readings in the file run **53.7 → 55.6 → 55.7 → 58.8 → 57.7 → 60.5 (Dec-2020)** — a sharp V-shaped rebound out of the 2020 COVID trough back into strong expansion. The component sheets let a trader look *under the hood*: **New Orders** (most forward-looking), Production, Employment, Supplier Deliveries, Inventories, Customer Inventories, Prices, Order Backlog, Exports and Imports — each charted against the headline so you can see whether a move is driven by genuine demand (New Orders) or noise (Deliveries/Inventories).

**ISM vs GDP.** In `ISM_Manufacturing_SP500_GDP.xlsx`, PMI is overlaid on US Real GDP QoQ-annualised growth. The GDP series swings from a **-31.4%** annualised collapse to a **+33.4%** rebound (the 2020 Q2/Q3 whipsaw), with the PMI tracking the same turning points but leading them. This is the core teaching point: ISM is a real-time proxy for the GDP print that arrives weeks later.

**ISM vs S&P 500.** `ISM_SP500.xlsx` overlays PMI on S&P 500 % returns 1972–2013; the GDP/SP500 workbook extends the level series to 2020 (S&P from **44.72 in 1957 to 3,756 by Dec-2020**, YoY range **-44.8% to +52.9%**). PMI momentum (especially the rate-of-change) tends to lead equity YoY returns — a rising PMI off a sub-50 trough is historically the most bullish equity backdrop.

**ISM Non-Manufacturing / Services (1997/2008–2020).** The NMI averages **~54.3** (min **37.6**, max **60.8**), latest run **56.6 → 57.2 → 57.2 → 56.2 → 56.8 → 57.7**. The **Business Activity** sub-index (back to 1997) is even more cyclical, min **26** (COVID) to max **67.7**, ending at **60.5**. Services PMI matters because services dominate US GDP, but manufacturing PMI remains the cleaner cyclical signal.

**Global & country PMIs (2010–2014 snapshots).** The Global Manufacturing PMI sits in mild expansion, averaging **~51.8**, range **48.7–58.2**, ending **51.8 (mid-2014)**. The US national manufacturing PMI in the same book is firmer (avg **54.6**, up to **61.4**). Global Services PMI averages **~53.7** (range 49.2–59.3), ending **53.5 (Nov-2014)**. Each country tab pairs the PMI with national GDP QoQ so a trader can rank economies by momentum and spot divergences (e.g. Euro-area vs UK, France vs Germany, Italy vs Spain).

**China PMIs (2005–2014).** Two competing reads: the **Official (NBS) PMI** (avg **52.2**, range 38.8–59.2, ending **50.3 in Nov-2014**) skews to large state-owned enterprises; the **Caixin/HSBC PMI** (avg **51.2**, range 40.9–57.4, ending **49.5 in Dec-2014 — below 50**) skews to smaller private firms. The divergence (Official above 50, Caixin slipping below) is itself a signal of where the slowdown is concentrated. The Caixin book also overlays China PMI on the **FXI China ETF** and **WTI crude**, and on China GDP YoY (which fell from **~13% to ~7.3%** over the window).

**University of Michigan Consumer Sentiment (1978–Oct-2022).** UMCSI averages **~85–86** (long-run avg ~85–87 referenced in-file), with a min near **50** and high of **~112**. The 2021/22 file captures the post-COVID consumer slump: readings collapse to **50 (the series low)** in mid-2022 before edging up (**58.4 → 50 → 51.5 → 58.2 → 58.6 → 59.9**). The companion file splits sentiment into the **Expectations Index** (more forward-looking, the leading half) and **Current Conditions** — when Expectations falls below Current Conditions it has historically flagged a coming consumption slowdown.

**NFIB Small Business Optimism (1986–2020).** Core index averages **~98.4** (range **81.6–108.6**). It ends at **95.7 (Dec-2020)** with a steep MoM drop of **-5.5** and YoY **-6.6%** — the COVID hit to Main Street. Component "plans" series (hiring, capex, inventory, expected sales, expected economy) are the leading sub-signals and are charted against GDP YoY and S&P 500 YoY.

**Building Permits & Housing (1960–2017).** Permits average **~1,355k**, range **513k (GFC trough)** to **2,419k (mid-2000s bubble peak)**, ending **~1,272k (Aug-2017)**. Permits *lead* Starts which lead Completions — the workbook charts all three plus the spread, and overlays permits on the **XHB homebuilder ETF**. Housing is one of the most reliably leading hard-data series because it is rate-sensitive and credit-driven.

**EU Economic Sentiment Indicator (ESI, 1985–Jan-2021).** The EU ESI (a composite of industry, services, consumer, retail and construction confidence) averages **~100** (it is normalised to 100 = long-run average), range **67.1–117.8**, ending **~91.2 (Jan-2021)** after the COVID trough near 88. Sub-confidence balances are negative through the pandemic (industry **-5.8**, services **-17.3**, consumer **-16.5**, construction **-9.8** in the latest EA reading). The `All EU Surveys` set adds the full DG-ECFIN survey universe — sectoral business climate (BCI) and investment-plan surveys at NACE2 granularity.

## How it's used in the strategy

- **Read the 50-line and the rate-of-change first.** A PMI rising *through* 50 from below is the highest-conviction pro-cyclical (long equities/cyclicals, short defensives) setup; a PMI rolling over *through* 50 from above flags the opposite. The *direction* matters more than the level.
- **Breadth check across the global PMI panel.** Synchronous global expansion (most country PMIs >50 and rising) supports a broad risk-on macro tilt; a narrowing set where only the US holds up warns of fragility. Rank economies by PMI momentum to find relative long/short pairs.
- **Component diagnostics.** Use ISM **New Orders** and **New Orders minus Inventories** as the cleanest forward signal; a headline rise driven only by Supplier Deliveries (supply friction) is lower quality.
- **Confirm with consumer/small-business sentiment.** UoM Expectations and NFIB plans corroborate or contradict the manufacturing read; divergences are early warnings.
- **Lead the lagging data.** ISM and permits front-run the GDP and employment prints used to confirm the regime — feeding the [[Trade Idea Generation Process]] and the [[Macro Regime Snapshot]].
- **Always state the vintage.** Every series here is historical (mostly 2013/14, 2017, 2020/21); these readings document the strategy's signals and a past macro picture, not live conditions as of 2026.

## See also
[[GDP & Growth]] · [[Coincident Indicators]] · [[Cyclical Commodities]] · [[M2 Money Supply & Liquidity]] · [[Sector Analysis & Rotation]] · [[Bull & Bear Markets]] · [[Macro Regime Snapshot]] · [[The Global Macros Framework]] · [[Trade Idea Generation Process]] · [[Glossary]]

**Live counterparts:** [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] runs this pillar as a point-in-time signal stack with ADF+KPSS diagnostics — live ISM **53.34** (Jun-2026), OECD CLI **100.80**, NFCI **−0.54**, regime read **Goldilocks** (asof 2026-07-25); see also [[Conference Board LEI & Leading-Lagging Map]] for the LEI/lead-lag map. [[US Leading Indicators — Usefulness in Tracking GDP (July 2026)]] operationalizes the published top-10 GDP-tracking ranking with full histories and Z-analysis; [[Business Cycle Dashboard - Live (June 2026)]] scores the Leading/Coincident/Lagging triad live; [[Global Macro Trading Deck (July 2026)]] carries the 23-country PMI panel.
