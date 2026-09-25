---
title: Portfolio Management
category: portfolio-risk
type: domain
data_asof: 2021-06-10
summary: "How the long/short book is sized and beta-hedged — net/gross exposure, CAPM beta from S&P500 regression, four sizing schemes, target portfolio beta; the 2021 base book runs $100k gross at portfolio beta 0.27."
tags: [global-macro, portfolio, beta-hedge, capm, net-exposure, gross-exposure, long-short, volatility, correlation]
data_vintage: "2013–2022, mixed (beta/exposure sheets 2021, volatility summary Jun-2021, performance stats 2013–2014, RFR/MRP 2016-era)"
sources: 12
updated: 2026-06-18
---

# Portfolio Management

**What it is & why it matters** — Portfolio management is the layer of the Global Macros strategy that converts a basket of individual long and short trade ideas into a single, market-aware book. The trader is not just picking stocks; they are deciding *how much* of each to hold, controlling net (directional) and gross (capital-at-work) exposure, and deciding how much residual market beta the book should carry. The dataset shows this being done concretely: a long/short equity book is built, position sizes are derived several ways (net-weight, risk-parity, beta-parity, equal-weight), and the whole thing is targeted to a chosen portfolio beta. This is where stock selection from [[Sector Analysis & Rotation]], [[Company Stats & Screening]] and the [[Trade Idea Generation Process]] gets sized and hedged.

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| Calculating_Beta.xlsx — `Portfolio Beta` | The flagship long/short book: 6 longs (VTRS, XPO, MOS, FEYE, TTEC, WING) and 4 shorts (LVS, BBY, LEN, SPLK) with per-stock beta, price, shares, $ net/gross exposure and four sizing schemes | 2021-era | Beta time-series + 2 regression scatter plots (SAFM, FLR vs S&P500) |
| Beta_Spreadsheet_Risk_limits.xlsx — `Portfolio Beta` | The same book under explicit risk limits — note shorts grew (LVS to -$12,259, SPLK to -$14,462), pushing net weight up | 2021-era | — |
| Beta Hedge/Beta Hedge.xlsx | Minimal two-stock hedge worksheet: CVX (β 1.32) + AZN (β 1.12), ~$20k committed, beta ratio 1.179 | n/a | — |
| Beta Hedge/Beta Hedge_ Multiple Securities.xlsm | Theme-beta hedging across many securities | n/a | — |
| Theme Betas.xlsx / Beta Hedge/Theme Betas.xlsx | A $100k "Discretionary vs …" theme trade: longs M (β 1.01) + DDS (β 1.27), shorts TGT (β 0.57) + FDO (β 0.32); total beta 3.17 | n/a | — |
| Beta Hedge/Calculating Beta_ Step by Step Guide.pdf | 28-page methodology: CAPM single-index regression of stock vs S&P500 returns; worked Heinz (HNZ) example | data 3-Mar-2010 → 3-Mar-2013 | regression line-fit plot |
| RFR & MRP.xls | CAPM macro inputs: equity risk premiums, default spreads and country risk by region (Damodaran-style) | ~2016 vintage | — |
| Portfolio_Volatility_and_Correlation.xlsm | Realized vs implied vol for ~48 names, var-cov & correlation matrices, portfolio-vol theory vs practice, two-portfolio DoR | snapshot 10-Jun-2021 | portfolio-σ diversification curve, DoR bars |
| Portfolio Volatility/Portfolio Volatility Calculator.xlsm | Standalone portfolio-σ calculator (theory + practice tabs) | n/a | diversification curve |
| Portfolio_Modelling.xlsx | Two model portfolios mapped to GICS sectors; Portfolio 1 longs EIX/IBM/SYK/VZ/TJX/NEM, shorts SPLK/VTRS/SYY/BDX; ~20 component price histories | histories to 2021 | per-name price lines, spread/ratio analysis |
| Portfolio Performance Statistics.xlsx — `Example Sheet` | Weekly equity curve with Sharpe/Sortino/Calmar, drawdown and annualised σ | 4-Mar-2013 → 18-Aug-2014 | equity-curve line |
| EG_Profiles_Longs.xlsx / EG_Profiles_Shorts.xlsx | Earnings-growth "profile" templates ranking long vs short candidates by EG momentum relative to sector | n/a | bar charts per profile |

## Charts & key trends

- **The long/short book (Calculating_Beta `Portfolio Beta`, 2021-era).** Six longs totalling **$61,874 gross** (VTRS, XPO β 2.17, MOS β 1.84, FEYE, TTEC β 0.83, WING) and four shorts totalling **-$38,111 net / $38,111 gross** (LVS, BBY, LEN, SPLK). The book runs **$23,763 net long, $99,986 gross**, a net weight of ~24% and a **portfolio beta of 0.27** against a $100k target gross. So the book commits roughly its full capital but carries only a quarter of the market's directional risk.
- **Risk-limited variant (Beta_Spreadsheet_Risk_limits).** Same names but shorts are scaled up (LVS to -$12,259, SPLK to -$14,462), lifting net exposure to **$31,872 net / $85,314 gross**, net weight ~37% and **portfolio beta ~0.49** — illustrating how changing short sizing alone re-rates the book's beta.
- **Sizing schemes side by side.** Each name is sized four ways: *net-weight* (dollar-equal), *risk-parity* (gross weighted to equalise risk — e.g. WING's high vol shrinks it from 10.3% to ~10.3% gross while low-beta TTEC grows), *beta-parity* (gross weighted by beta so each name contributes equal market risk — high-beta XPO is cut to ~10% beta-gross), and *equal-weight*. This is the practical core of position sizing in the strategy.
- **Beta methodology (PDF + Heinz worksheet).** Beta is the slope of an OLS regression of weekly stock returns on S&P500 returns (single-index model, standard not excess returns). The worked **Heinz (HNZ) example returned β ≈ 0.39** over 3-Mar-2010→3-Mar-2013 (156 weekly points), with **R² ≈ 0.153** (only 15% of HNZ moves explained by the market) — confirming a defensive consumer-staple. Defensive stocks sit below 1; cyclicals/airlines sit above 1.
- **Volatility & correlation snapshot (10-Jun-2021).** Realized annualised σ for the ~48-name universe ranged widely: defensives like Hershey (HSY) and Verizon (VZ) near the bottom vs high-vol names; e.g. **FB annualised realized σ ≈ 36%**, with 1-day σ ≈ 2.3%, 1-week ≈ 5.0%, 1-month ≈ 10.5%, 1-quarter ≈ 21.8%. The workbook then builds the variance-covariance and correlation matrices that feed portfolio σ.
- **Diversification curve (Portfolio Volatility Theory).** A 4-series chart shows portfolio standard deviation falling as the number of equally weighted assets rises, decomposing total risk into the part that diversifies away and the irreducible covariance/market floor.
- **Two model books, distribution of returns (Portfolio DoR).** Over 106 daily observations in 2021, **Portfolio 1** (the hedged long/short book) had **mean daily return 0.068%, σ 0.525%**, range -1.1% to +2.5%; **Portfolio 2** (more directional) had **mean 0.194%, σ 0.959%**, range -1.69% to +4.54%. Portfolio 1 shows higher kurtosis (3.28) — the hedge compresses the body of the distribution at the cost of fatter relative tails.
- **Equity curve & ratios (Performance Statistics, 2013–2014).** A weekly book grew from **$15,000 (4-Mar-2013) to ~$17,140 (18-Aug-2014)**, ~+14% over ~18 months, with annualised σ ≈ 10.2%, downside σ ≈ 5.7%, max drawdown -3.96%. Headline ratios: **Sharpe ≈ 0.98, Sortino ≈ 1.77, Calmar ≈ 2.56**.

## How it's used in the strategy

A Global Macros global-macro trader treats the portfolio, not the single trade, as the unit of risk:

1. **Generate and screen ideas** via the [[Trade Idea Generation Process]], [[Sector Analysis & Rotation]] and the EG-profile long/short templates, producing a list of longs and shorts.
2. **Estimate beta** for each name by regressing its returns on the relevant index (the Heinz method), so every position has a market-sensitivity number.
3. **Decide net vs gross exposure.** Gross = longs + |shorts| (capital at work, drives margin — see [[Risk Management]] and Exposure_Margin). Net = longs − |shorts| (directional tilt). A market-neutral macro book targets low net and low portfolio beta; an expression of a directional macro view deliberately carries net long or short beta.
4. **Beta-hedge to a target.** Because longs and shorts have different betas, dollar-neutral is *not* beta-neutral. The trader sizes the shorts (or adds an index/ETF hedge) until the weighted portfolio beta hits the chosen target (0.27 in the base book, ~0.49 in the risk-limited one, or ~0 for true neutrality). The two-stock CVX/AZN sheet and the theme-beta sheets are the building blocks.
5. **Choose a sizing scheme** — net-weight, risk-parity (equalise σ contribution) or beta-parity (equalise market-risk contribution) — depending on whether the trader wants dollar, volatility or beta balance.
6. **Feed CAPM inputs** (risk-free rate and market risk premium from RFR & MRP) when computing expected returns and the cost of carrying beta. See [[Government Bond Yields]] for the RFR side.
7. **Monitor the book** with the volatility/correlation matrices and the performance-statistics ratios (Sharpe/Sortino/Calmar, drawdown), filing the equity curve into the track record handled in [[Risk Management]].

## See also
[[Risk Management]] · [[Trade Idea Generation Process]] · [[Sector Analysis & Rotation]] · [[Company Stats & Screening]] · [[Spread Trades]] · [[Average True Range (ATR)]] · [[Distribution of Returns]] · [[VIX & Implied Volatility]] · [[Government Bond Yields]] · [[The Global Macros Framework]] · [[Glossary]]

**Live counterparts:** [[Target-Beta Factor Portfolio (June 2026)]] proves the target-β dial live (realized β tracks target); [[Macro-Aware Risk Parity System]] and [[Hedge-Fund Replication System]] are the working allocation siblings; the LP-facing summary of the whole book lives in [[Trading Desk — Organization & LP Presentation (July 2026)]].
