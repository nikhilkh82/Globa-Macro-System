---
title: Coincident Indicators
category: indicators
type: domain
data_asof: 2022-10
summary: The confirmation layer — inflation (CPI/PPI/PCE), labour (NFP, unemployment, claims), retail sales, industrial production and durable-goods orders that validate the cycle turn.
tags: [global-macro, coincident-indicators, inflation, employment, retail-sales, industrial-production, durable-goods, cpi, ppi, pce]
data_vintage: "1913–2022, mixed (CPI/PPI to 2022; employment to 2021; jobless claims, retail sales, IP, durable goods to 2013–2017)"
sources: 9
updated: 2026-06-18
---

# Coincident Indicators

**What it is & why it matters** — Coincident indicators move *with* the business cycle in real time: they tell you where the economy is right now, not where it is heading. In the Global Macros global-macro framework they sit downstream of the [[Leading Indicators]] — they **confirm** the cycle turn that leading data (yield curve, M2, PMIs, building permits) already flagged. The headline coincident set is the "hard data" the desk scores monthly: inflation (CPI / PPI / PCE), the labour market (non-farm payrolls, unemployment, jobless claims), consumer demand (retail sales), and the production/capex pulse (industrial production, durable-goods new orders). When these align with the leading signal, conviction in a regime call rises; when they diverge, the desk waits.

> Framing note: every figure below is from the Global Macros teaching dataset and reflects **historical** vintages (CPI/PPI through Oct 2022, employment through May 2021, jobless claims/retail/IP/durable-goods through 2013–2017). These are *not* live readings as of 2026-06-18. Read each as "what the dataset shows, data through <date>."

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Consumer Price Index/2. US_CPI_2022.xlsx` | Headline CPI (1982-84=100, NSA), m/m & y/y, plus Food, Energy and Core-CPI tabs; Fed funds & 2% target overlay | 1967-01 → 2022-10 | "CPI Change 1970–2022 y/y%", "CPI, Core-CPI & Food y/y%" |
| `Inflation _CPI___PPI.xlsx` | CPI, Core CPI, **PCE, Core PCE** and **PPI All Commodities** each with MoM/YoY series **and full descriptive statistics + std-dev bounds + MoM/YoY histograms** | 1913 (PPI) / 1947 (CPI) / 1959 (PCE) → 2021-01 | MoM% & YoY% histograms per series |
| `Employment Situation Report/8. Employment Situation Report_2021.xlsx` | Total NFP, government, private, and 9 industry breakdowns (goods, services, construction, manufacturing, trade/transport/utilities, financials, business services); unemployment rate | 1939 (NFP) / 1948 (rate) → 2021-05 | "Total Non Farm Payrolls", "Unemployment Rate", per-sector m/m change |
| `Jobless Claims Initial Continuing/5. Jobless Claims Report.xlsx` | Initial claims (new filings) & Continuing claims (insured unemployment), weekly, SA, with w/w change & % | 1967-01 → 2013-02 | "Initial Claims 1967–Present", "Continuing Claims 2000–Present" |
| `Retail Sales/1. Retail_Sales.xlsx` | Retail & Food Services Sales ($mn) + 10 category tabs (motor, gas, food/bev, non-store/online, clothing, health, general merch, housing supplies, food service) | 1992-01 → 2014-11 | "Retail Sales vs GDP Growth y/y%", "Composition of Retail Sales Growth" |
| `Industrial Production/26. Industrial Production.xlsx` | IP index (2012=100) + components: manufacturing, mining, utilities, consumer goods, business equipment, materials, construction; **S&P 500 overlay** | 1972-01 → 2017-08 | "IP Index 2012=100", "IP Index vs S&P 500", "IP vs Market Groups" |
| `Durable Goods Shipments/21. US Durable Goods New Orders.xlsx` | Total durable-goods new orders + **ex-transport** and **ex-defence** (core capex proxies) + 8 component tabs (primary/fabricated metals, machinery, computers, electrical, transport) | 1992-02 → 2017-08 | "Durable Goods Total New Orders", "New Orders ex Transport" |
| `Updated Market Data/Datafeed_CPI.xlsx` | Newer CPI sub-index datafeed (BLS chained series, 1999-2018) — cross-check vintage | 1999-12 → 2018-05 | (raw datafeed, no charts) |
| `Updated Market Data/5. & 1. & 26. & 21.` duplicates | Confirming copies of jobless-claims, retail-sales, IP, durable-goods workbooks (same vintages) | as above | same |

## Charts & key trends

**Inflation — CPI (data through Oct 2022, `US_CPI_2022.xlsx`).** Headline CPI index rose from 32.9 (Jan 1967) to 298.062 (Oct 2022). The y/y change series (mean 4.06% over the full sample) shows the two big regimes: a 1970s–80s peak of **14.76%** y/y, a brief deflationary dip to **−2.1%** y/y around 2009, then the post-COVID surge. In the Tabs sheet (2019–2022 zoom) headline CPI y/y climbed from 1.5% (Jan 2019) to a **9.0% peak (June 2022)** and was rolling over to **7.76% by Oct 2022** — the first signs of disinflation in the dataset. Core CPI (ex food & energy) peaked at **6.66%** y/y in the same window. The component split is dramatic: **Food y/y peaked at ~10.9%** and **Energy y/y peaked at +41.5%** (June 2022) before collapsing toward +17.6% by October — energy is the most volatile sleeve (range −18.3% to +41.5% y/y).

**Inflation — PCE, Core PCE & PPI (data through Jan 2021, `Inflation_CPI_PPI.xlsx`).** This workbook is built for the Global Macros distribution lens (see [[Distribution of Returns]]): each series carries mean, std-dev and 1/2/3-sigma bounds plus MoM/YoY histograms. CPI All Items MoM mean is +0.28% (≈3.4%/yr), with ~79% of months inside ±1σ. **Core PCE** (the Fed's preferred gauge) ran y/y from ~2.1% (1959 start) to **1.53% as of Jan 2021** — historically subdued, with a long-run y/y peak of **10.22%** in the 1970s/80s. **PPI All Commodities** (the upstream cost series, 1913→2021) is far wilder: y/y range **−43.9% to +47.2%**, latest reading +2.51% (Jan 2021) — PPI turns *before* CPI, so the desk watches it as a pipeline-pressure tell.

**Labour market — payrolls & unemployment (data through May 2021, `Employment Situation 2021`).** Total non-farm payrolls grew from 29.9mn (1939) to **144.9mn (May 2021)**. The m/m change series captures the COVID shock vividly: a record **−20,679k collapse (April 2020)** followed by the **+4,846k rebound** — the largest swings in the 1939–2021 record (long-run mean +116k/month). The unemployment rate (1948→2021) sits at **5.8% (May 2021)**, having spiked to its all-time high of **14.8% (April 2020)** from a cycle low near the **2.5%** floor; sample mean 5.77%. Sector tabs let the desk see *where* jobs are being added (services vs goods, construction, manufacturing, financials, professional/business services).

**Labour market — jobless claims (data through Feb 2013, `Jobless Claims Report`).** Weekly **initial claims** ranged 162k–695k (mean ~363k), ending the sample near 362k. **Continuing claims** (insured unemployment) ranged 988k–**6,628k** (the 2009 crisis peak), ending near 3.15mn. Initial claims are the single most *timely* labour signal — weekly, leading the monthly NFP print — so the desk treats a sustained break above/below trend as an early confirmation of a labour-market turn.

**Consumer demand — retail sales (data through Nov 2014, `Retail_Sales`).** Retail & food-services sales rose from $164.1bn (Jan 1992) to **$449.3bn (Nov 2014)**. The y/y growth series (mean +4.56%) shows the cycle clearly: a **−11.38% trough (2009 recession)**, a +11.18% boom-time high, and a **+4.27% reading at the end of the sample** — solid mid-cycle expansion. The "Retail Sales vs GDP Growth" chart anchors why this matters: consumption is ~70% of US GDP, so retail-sales y/y tracks [[GDP & Growth]] closely. Category tabs (online/non-store growing fastest, gas stations most price-driven) feed [[Sector Analysis & Rotation]].

**Production — industrial production (data through Aug 2017, `Industrial Production`).** The IP index (2012=100) ran from 40.0 (1972) to **104.74 (Aug 2017)**, with an all-time high of **106.7** and a 1970s low near 39.9. The most recent prints show a slight m/m softening (−0.9% in the final month) off the highs. The standout Global Macros chart is **"Industrial Production Index vs S&P 500"** — production and equity prices are co-cyclical, and divergences between the two are a classic mean-reversion / regime tell the desk flags. Components (manufacturing, mining, utilities, business equipment, materials) localise the strength.

**Capex pulse — durable-goods new orders (data through Aug 2017, `Durable Goods New Orders`).** Total new orders ran from $114.6bn (1992) to **$228.9bn (Aug 2017)**, range up to $290.7bn; the volatile m/m change series swung from **−17.9% to +22.1%** (transport orders, esp. aircraft, drive the noise). The cleaner signal is **new orders ex-transport** ($82.9bn → $154.8bn, far smoother) and **ex-defence** — the desk's preferred core-capex / business-investment proxy. Rising core durable orders confirm a capex-led, mid-to-late-cycle expansion.

## How it's used in the strategy

In the Global Macros global-macro process, coincident indicators are the **confirmation layer** in a monthly macro scorecard:

1. **Confirm, don't lead.** The [[Leading Indicators]] (yield curve, M2, building permits, PMIs) call the turn first. Coincident data — payrolls, claims, retail sales, IP, durable orders, CPI/PCE — then *validate* whether the economy is actually expanding or contracting. Alignment raises conviction; a leading/coincident divergence is a flag to size down and wait.
2. **Inflation drives the rate regime.** CPI/PCE vs the **Fed's 2% target** (explicitly overlaid in the CPI workbook) tells the desk whether the central bank is in tightening or easing mode — the master input for [[Government Bond Yields]], the [[Yield Curve & Recession Signals]] and the [[USD & G10 FX]] view. PPI is the upstream early-warning on the same.
3. **Distribution-based scoring.** The std-dev bounds and histograms in `Inflation_CPI_PPI.xlsx` let the desk score each new print as a z-score (how many σ from its own mean) rather than eyeballing — the same statistical discipline applied in [[Distribution of Returns]] and [[Average True Range (ATR)]].
4. **Most-timely-first.** Weekly jobless claims > monthly payrolls > quarterly GDP: the desk weights the freshest data most for nowcasting, while using slower series to confirm the trend.
5. **Translate macro into trades.** A confirmed expansion (rising IP, core durable orders, retail sales; falling claims) supports a risk-on, cyclicals-long tilt and feeds [[Sector Analysis & Rotation]], [[Macro Regime Snapshot]] and ultimately the [[Trade Idea Generation Process]]. The IP-vs-S&P-500 overlay also informs equity [[Risk Management]] when production and prices diverge.

## See also
- [[Leading Indicators]] — the upstream signals these confirm
- [[GDP & Growth]] — retail sales & IP are the high-frequency read on GDP
- [[M2 Money Supply & Liquidity]] — liquidity that feeds through to inflation
- [[Government Bond Yields]] / [[Yield Curve & Recession Signals]] — CPI/PCE set the rate regime
- [[Sector Analysis & Rotation]] — category & industry breakdowns drive rotation
- [[Distribution of Returns]] / [[Average True Range (ATR)]] — the statistical scoring lens
- [[Macro Regime Snapshot]] — where the scored coincident data lands in the regime call
- [[The Global Macros Framework]] / [[Trade Idea Generation Process]] — how it all becomes a trade
