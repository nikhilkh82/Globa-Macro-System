---
title: Glossary
category: framework
type: reference
data_asof: n/a
summary: Concise Global Macros-grounded definitions of core terms (endo/exo, leading/coincident, ISM/PMI, COT, DXY, carry, ATR, beta, Kelly, VIX, GICS, M2, YTM) plus Jul-2026 vol/derivatives terms (MOVE, OVX/GVZ, IV/RV, OAS).
tags: [global-macro, glossary, definitions, reference]
data_vintage: "n/a (reference); examples drawn from 2015–2022 dataset"
sources: 5
updated: 2026-07-09
---

# Glossary

**What it is & why it matters** — A concise reference for the terms and metrics used across the Global Macro Brain. Definitions are written as the Global Macros strategy uses them; where the dataset gives a concrete value, an example is included so the term stays grounded. Each entry links to its home page where one exists.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Video 03/Basic_Statistics_Guide.pdf` | Distribution, central tendency, dispersion, correlation definitions | n/a | height histogram; S&P-vs-GDP scatter |
| `Video 04/Bond Market and Interest Rate Basics.pdf` | Bond/yield/YTM/curve definitions | n/a | bond pricing examples |
| `USA_Endogenous_Driver_Analysis.xlsx` | Endogenous driver terms & example readings | 2017-era | scorecard |
| `Exogenous_AUD_USD.xls` | Exogenous/relative driver terms (GDP, BoP, carry) | 2015-era | scorecard |
| `Updated Market Data/README!.docx` | Strategy vocabulary (endo/exo/COT) | 2021-era | — |

## Definitions

**Endogenous drivers** — Macro variables analysed for *one economy in isolation* to judge whether it is inflationary/deflationary and growing/slowing. In `US Endo' Score` they are grouped into Leading-Indicator surveys, Money Supply, Interest Rates, Inflation, Employment and Sovereign/Balance-Sheet risk, each scored I/D and rolled into a single number on a –150 to +160 scale (US example: **+36**). See [[FX Endogenous-Exogenous Framework]], [[The Global Macros Framework]].

**Exogenous drivers** — *Relative* macro variables comparing two economies (used for FX). The four Global Macros exo drivers are Relative GDP Growth, Relative Balance of Payments, Interest-Rate Differentials & Carry, and Stock-Market Returns / Relative Wealth, each scored –10…+10 on a –40 to +40 scale (AUD/USD example: **–14**). See [[FX Endogenous-Exogenous Framework]].

**Leading indicators** — Data that *turns ahead of* the economic cycle (surveys, building permits, money supply, jobless claims), used to anticipate GDP. The bulk of the macro layer (10 dedicated curriculum videos). See [[Leading Indicators]].

**Coincident indicators** — Data that moves *with* the cycle, confirming the current state rather than predicting it (e.g. industrial production, employment levels, housing starts). Less actionable than leading data but used for confirmation. See [[Coincident Indicators]].

**ISM / PMI** — Institute for Supply Management *Manufacturing* index (a diffusion PMI); >50 = expansion, <50 = contraction. Example reading 58.8 (strong expansion, scored +8 in the US endo sheet). A leading business-sentiment indicator. See [[Leading Indicators]].

**NMI / NMI Services** — ISM *Non-Manufacturing (Services)* index, the services counterpart to the manufacturing PMI; same >50/<50 logic. Example 55.3 (expanding, +5). See [[Leading Indicators]].

**ESI** — *Economic Sentiment Indicator*, the European Commission's composite confidence survey across industry, services, consumers, retail and construction; a leading indicator for the euro area. See [[Leading Indicators]].

**UMCSI** — *University of Michigan Consumer Sentiment Index*, a leading gauge of US consumer confidence. Example 96.8 (high, but scored **–5** in the endo sheet as a possible cyclical peak). See [[Leading Indicators]].

**NFIB** — *National Federation of Independent Business* Small Business Optimism Index, a US leading indicator of small-business sentiment. See [[Leading Indicators]].

**COT (Commitment of Traders)** — Weekly CFTC report of futures positioning by trader category. **NCP** = Non-Commercial Positions (speculators), tracked as long vs short; a **flip** is when net positioning crosses from net-long to net-short (or vice versa), a positioning/sentiment signal. Used to gauge crowding and contrarian risk in macro instruments. See [[Commitment of Traders (COT)]].

**DXY** — *US Dollar Index*, the trade-weighted value of USD against a basket of major currencies; the headline gauge of broad dollar strength. See [[USD & G10 FX]].

**Carry / rollover** — *Carry* is the return earned (or paid) simply for holding a position, principally the interest-rate differential between two currencies in an FX trade; *rollover* is the daily credit/debit applied to a held FX position reflecting that differential. A positive interest-rate differential favours the higher-yielding currency. Scored under "Interest-Rate Differentials and Carry" in the exo sheet. See [[FX Endogenous-Exogenous Framework]], [[Government Bond Yields]].

**ATR / ATRP** — *Average True Range* is the average size of an instrument's daily true range (a volatility measure); **ATRP** (ATR Percent) expresses it as a % of price so instruments of different prices are comparable. Used to estimate expected movement and to set stops/targets. See [[Average True Range (ATR)]].

**Distribution of returns** — The empirical frequency distribution of an asset's periodic returns, summarised by mean, standard deviation, skewness and kurtosis. The statistics guide notes 1σ ≈ 68.27%, 2σ ≈ 95.45%, 3σ ≈ 99.73% of a normal distribution; financial returns often show negative skew and positive excess kurtosis ("fat tails"). Used to judge how far a name typically moves over the trade horizon. See [[Distribution of Returns]].

**Beta hedge** — Offsetting a position's *market* (systematic) risk by taking an opposing position in the index, sized by the position's beta, so the residual exposure is the stock-specific (alpha) view. Central to running a market-neutral long/short book. See [[Portfolio Management]], [[Risk Management]].

**Kelly criterion** — A position-sizing formula that sets the optimal fraction of capital to risk given the edge (win probability and payoff) of a trade, balancing growth against ruin risk. Used as a sizing reference within risk management. See [[Risk Management]].

**VIX / implied volatility** — *Implied volatility* is the volatility the options market is pricing into an option (the forward-looking expectation); the **VIX** is the headline 30-day implied-vol index on the S&P 500, a market "fear gauge." The statistics guide shows cross-asset correlations rising toward 1 as the VIX spikes (liquidity drying up). See [[VIX & Implied Volatility]].

**GICS** — *Global Industry Classification Standard*, the sector/industry/sub-industry taxonomy used to map and compare companies; the basis for Global Macros sector breakdowns and peer comps. See [[Sector Analysis & Rotation]], [[Company Stats & Screening]].

**ADR** — *American Depositary Receipt*, a US-listed certificate representing shares of a foreign company; lets a US-based trader express international single-name ideas without trading the foreign exchange directly (Video 35). See [[Trade Idea Generation Process]].

**Spread trade** — A relative-value position that is simultaneously long one instrument and short another (a pair), profiting from the *spread* between them rather than outright direction; the core structure of a market-neutral long/short book, tracked weekly in the `Price_Action_Watchlist`. See [[Spread Trades]].

**Yield curve inversion** — When shorter-dated government bond yields exceed longer-dated yields (a downward-sloping curve); historically a leading recession signal. Bond yields and prices move inversely (Time Value of Money), so the curve reflects the market's growth/inflation/policy expectations. See [[Yield Curve & Recession Signals]], [[Government Bond Yields]].

**M2** — A broad *money-supply* aggregate (currency + demand deposits + savings/retail money-market balances). Its growth rate is an endogenous driver: "normal M2 growth in 1 std = GDP ~2%" in the US endo sheet, with two-plus 30%+ prints flagged as crisis-correlated central-bank action. See [[M2 Money Supply & Liquidity]].

**YTM (Yield to Maturity)** — The internal rate of return on a bond's expected cash flows if bought today, held to maturity, with coupons reinvested at the YTM; inversely related to price. Worked example: a 4-year 3% bond prices at $1,000 when YTM = 3%, $963.71 at 4%, $1,038.08 at 2%. See [[Government Bond Yields]].

**Skewness & kurtosis** — The 3rd and 4th central moments of a distribution. *Skewness* measures the tilt of the tails (negative = longer left tail; normal = 0). *Kurtosis* measures "peakedness/tailedness" (normal = 3; Excel reports *excess* kurtosis with normal = 0; positive excess = leptokurtic, fat tails). See [[Distribution of Returns]].

**Endogenous score / Exogenous score (sliding scale)** — The single composite numbers produced by the scoring sheets: endo on a –150 to +160 scale (per-country bias), exo on a –40 to +40 scale (relative pair bias). Positive = inflationary / favours the base economy. See [[The Global Macros Framework]].

## How it's used in the strategy
The glossary is a lookup, not an analysis page — it lets any wiki reader decode the abbreviations used in the scoring sheets, the trade-idea template and the indicator pages without leaving the vault. Terms cluster around the framework's layers: macro drivers (endo/exo, leading/coincident, ISM/PMI/NMI/ESI/UMCSI/NFIB, M2, DXY, carry, yield curve), the quantitative toolkit (ATR/ATRP, distribution of returns, skew/kurtosis, VIX/implied vol, beta, Kelly, COT) and structure/classification (GICS, ADR, spread trade, YTM).

## Volatility & derivatives additions (2026-07)

**MOVE** — ICE BofA's Treasury-option implied-volatility index: the bond market's VIX and the free proxy for swaption volatility. Read alongside VIX for the rates-vs-equity stress split. See [[Global Macro Trading Deck (July 2026)]].

**OVX / GVZ / VXSLV** — Cboe's commodity ETF volatility indices (crude oil / gold / silver), the implied-vol gauges for the commodity book. VXSLV−GVZ is the *silver vol premium* (speculative froth gauge). OVX repriced around EIA/OPEC events, GVZ around real-rate and safe-haven shocks. ETF-implied, not futures-implied — a liquid proxy, disclosed. See [[Global Macro Trading Deck (July 2026)]], [[Cyclical Commodities]].

**Realized volatility (RV)** — Volatility actually delivered by the price series (annualized σ of daily log returns, typically 20-day). The live FX-vol gauge in this system, since Cboe's FX-vol indices (EUVIX/JYVIX/BPVIX/EVZ) are all discontinued. See [[Global Macro Trading Deck (July 2026)]].

**IV/RV ratio** — Implied ÷ realized volatility. Above ~1.25 and rising = options pricing more movement than the tape is delivering → the deck's mechanical sizing rule: widen stops or cut notional so vol-adjusted risk stays constant. See [[Risk Management]].

**Implied correlation (COR)** — Cboe's index-option-derived average stock-stock correlation by horizon (COR1M…COR1Y). Low = a single-stock market (diversification working); spikes = systemic, everything-moves-together risk. See [[Global Macro Trading Deck (July 2026)]].

**OAS (option-adjusted spread)** — A corporate bond index's spread over Treasuries after adjusting for embedded options; HY/BBB/IG OAS are the credit-stress dials. Moody's Baa−10y serves as the 20-year full-cycle anchor where index history is truncated. See [[Corporate Bond Yields & Credit]].

**Breakeven inflation / 5y5y** — The inflation rate that equates nominal Treasury and TIPS yields (market-implied expected inflation); the 5y5y forward isolates the *long-run* expectation the Fed watches. The free proxy for inflation swaps; its realized vol proxies *inflation uncertainty*. See [[Global Macro Trading Deck (July 2026)]].

**Sovereign spread → default-probability proxy** — A euro-periphery 10y spread over Bunds converted to a cumulative default probability via P = 1 − e^(−s·T/(1−R)) with recovery R≈40%. A bond-derived stand-in for licensed CDS: ranking and trend are meaningful, levels approximate. See [[Global Macro Trading Deck (July 2026)]].

**Regime board** — The deck's rules-based classification: growth × inflation z-composites → Goldilocks / reflation / stagflation / hard landing, with a 5-signal stress checklist (equity vol, rates vol, FX vol, credit, USD squeeze) that escalates to RISK-OFF / liquidity-shock and overrides everything else. See [[Global Macro Trading Deck (July 2026)]], [[Macro Regime - Live (June 2026)]].

## See also
[[The Global Macros Framework]] · [[Trade Idea Generation Process]] · [[Global Macro Brain]] · [[Leading Indicators]] · [[Coincident Indicators]] · [[FX Endogenous-Exogenous Framework]] · [[Commitment of Traders (COT)]] · [[Distribution of Returns]] · [[Average True Range (ATR)]] · [[VIX & Implied Volatility]] · [[Yield Curve & Recession Signals]] · [[M2 Money Supply & Liquidity]] · [[Measurement Conventions — Growth, Inflation & Index Arithmetic (Mohr)|Measurement Conventions]]
