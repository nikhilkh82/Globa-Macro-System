---
title: Risk Management
category: portfolio-risk
type: domain
data_asof: 2021-11-21
summary: "Preventative risk management from the corpus — Kelly sizing, ATRP and Distribution-of-Returns stops, track-record stats, exposure/margin ladders; worked Kelly example (W 0.50, R 1.84) gives K = 22.8% per trade."
tags: [global-macro, risk, kelly-criterion, position-sizing, stops, atrp, distribution-of-returns, track-record, margin, exposure]
data_vintage: "2013–2022, mixed (Kelly sheets generic, ATRP/DoR price histories to Nov-2020, track record Nov-2021, exposure/margin generic)"
sources: 9
updated: 2026-06-18
---

# Risk Management

**What it is & why it matters** — Risk management in the Global Macros strategy is *preventative* (PRM): the trader decides, before entering, how big a position can be, where it is wrong, and what the whole book can lose — rather than reacting after a loss. The dataset operationalises this with three pillars: **position sizing** via the Kelly Criterion (how much capital per trade), **stop and target placement** via volatility (ATRP) and the empirical [[Distribution of Returns]] (DoR), and a **track record** of realized stats that feeds the win-rate and win/loss-ratio inputs back into Kelly. Exposure and margin tables tie sizing back to broker leverage. This page is the defensive counterpart to [[Portfolio Management]].

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| Kelly_Criterion.xlsx | Kelly formula K = W − (1−W)/R from a 60-trade track record; `Explanation`, `KC_Trade_Causality`, `KC_R_Causality` tabs showing how W and R drive K | generic | — |
| Kelly_Criterion_Simulation.xlsx | 1,000-round wealth simulations at various bet sizes (win prob 52.5%), geometric-growth-rate function, Kelly vs W and vs R curves, gains-vs-losses asymmetry table | generic | wealth-growth index, % profit vs bet size, Kelly curves |
| ATRP Stops and Targets.xlsx | Average True Range Percentage for TREX and STZ at daily/weekly/monthly/quarterly horizons, with ATRP averaged over 4w/12w/52w/3y/5y windows | price histories to 2-Nov-2020 | — |
| DoR Stops and Targets.xlsx | Distribution of close-to-close and high-low returns for TREX and STZ; binned frequency, probability and cumulative-probability tables | price histories to 2-Nov-2020 | return-occurrence histograms |
| Beta_Spreadsheet_Risk_limits.xlsx | The long/short book under risk limits (net $31,872 / gross $85,314, portfolio beta ~0.49) | 2021-era | — |
| Portfolio_Volatility.xlsm | Portfolio-level σ and correlation engine for whole-book risk | n/a | diversification curve |
| Trading_Stats_and_Track_Record_Basic.xlsx | Live `Portfolio Monitor`, `Realized PnL` (return-per-trade histogram) and `Portfolio Value` equity curve | through 2021 | return-%-per-trade bars, equity curve |
| Trading_Stats_and_Track_Record_Advanced.xlsx | As Basic plus trade-time-horizon distribution and richer stats | snapshot 21-Nov-2021 | time-horizon + return histograms, equity curve |
| Exposure_Margin.xlsx | Margin-call %, exposure rate and $ exposure ladders for Stocks (4×) and FOREX (8×) | generic | — |

## Charts & key trends

- **Kelly Criterion sizing (Kelly_Criterion).** With a 60-trade record of **30 wins / 30 losses (W = 0.50)** but winners averaging more than losers, the inputs were **W = 0.50, R = 272,000/148,000 = 1.84**, giving **K = 0.50 − (0.50/1.84) = 22.8%** — i.e. stake ~22.8% of capital on the next trade to maximise long-run geometric growth. The sheet stresses that a 50% hit-rate can still be highly profitable because R > 1.
- **Reverse-engineering Kelly from a stop rule (KC_R_Causality).** Fixing the win/loss ratio via a stop discipline: a **1-to-3 rule** (15% stop, 45% target → R = 3.33) at **W = 0.30** yields **K = 9%** (≈ a max of ~11 positions); a **1-to-4 rule** (R = 4) at **W = 0.25** yields **K = 6.25%** (≈ 16 positions). So the chosen R and required win-rate directly set the maximum number of concurrent positions.
- **Bet-size simulation (Kelly_Criterion_Simulation).** Over 1,000 rounds at a 52.5% win probability, the wealth-growth-index chart shows under-betting grows slowly while over-betting (well above Kelly) eventually destroys capital — the geometric-growth curve peaks at the Kelly fraction and turns negative beyond it.
- **Gains-vs-losses asymmetry.** The break-even table makes the case for tight stops: a +1% gain is undone by a -0.99% loss, but a +100% gain needs a -50% loss to break even, and a +10x gain is wiped by -90.9%. Losses compound against you faster than gains compound for you — the core argument for PRM and stops.
- **ATRP-based stops (ATRP Stops and Targets).** For **STZ weekly**, the **average weekly True Range % was ~7.9% over 4 weeks, ~5.8% over a quarter, ~8.5% over a year, ~6.0% over 3 years and ~5.2% over 5 years** (single-week TRP ranged 1.3%–41.6%, mean ~6.3%). Stops/targets are placed a multiple of the relevant-horizon ATRP away from entry, so wider-vol names get wider stops. See [[Average True Range (ATR)]].
- **DoR-based stops (DoR Stops and Targets).** For **STZ weekly close-to-close returns**, the binned distribution showed ~46% of weeks within ±2% (cumulative prob 0.68 by the 0%–2% bin) and ~92% of weeks better than -8%; high-to-low weekly ranges clustered around 2%–6% (the 2%–4% bin alone held 28% of weeks). A trader sets a stop at a return level the stock only breaches with low historical probability rather than an arbitrary %. See [[Distribution of Returns]].
- **Track record (Advanced, 21-Nov-2021).** A live 13-position long/short book ran **~$311,249 gross, ~$73,380 net**, with **+$19,977 unrealized PnL (+23.6% on net)**. Best names IRTC (+47.4%) and KRNT (+22.5%); worst W (-10.3%) and LC (-11.0%). The Realized-PnL trade-horizon table shows most trades held 35–60 calendar days (median bucket ~50–55 days). These realized win-rate and return stats are exactly what feed back into the Kelly W and R inputs.
- **Exposure & margin ladders (Exposure_Margin).** Stocks are shown at **4× leverage** (e.g. $100k margin → $400k exposure) and FOREX at **8×** ($100k → $800k). A margin-call-% column converts an exposure rate into the loss that triggers a call (e.g. exposure rate 5 → 20% adverse move, rate 10 → 10%), linking position size directly to survivability.

## How it's used in the strategy

A Global Macros trader runs preventative risk management (PRM) as a closed loop:

1. **Keep a track record.** Log every trade's PnL, hold period and outcome (Trading_Stats workbooks). This produces the realized **win-rate (W)** and **win/loss ratio (R)**.
2. **Size with Kelly.** Plug W and R into **K = W − (1−W)/R** to get the fraction of capital per trade. Many traders use a fraction of full Kelly to reduce variance; the simulation shows why over-betting full-or-more Kelly is dangerous.
3. **Cap concurrent positions.** Because each position takes a Kelly slice, the K% implies a maximum number of simultaneous trades (e.g. 9% → ~11 positions), enforcing diversification.
4. **Place stops and targets before entry** using either ATRP (a volatility multiple sized to the trade's horizon) or the DoR (a return level rarely breached historically). The chosen stop fixes the loss leg, which combined with the target fixes R — closing the loop back to Kelly.
5. **Control book-level exposure.** Translate position sizes into gross/net exposure and margin usage via the Exposure_Margin ladders, and check the whole-book σ and portfolio beta in [[Portfolio Management]] against risk limits.
6. **Respect loss asymmetry.** The gains-vs-losses table is the discipline anchor: small, controlled losses preserve the capital base that compounding depends on.

## See also
[[Portfolio Management]] · [[Average True Range (ATR)]] · [[Distribution of Returns]] · [[Technical Analysis & Price Action]] · [[VIX & Implied Volatility]] · [[Spread Trades]] · [[Trade Idea Generation Process]] · [[The Global Macros Framework]] · [[Glossary]]

**Live counterparts:** [[Million Dollar Traders — 5-Step Global Macro (July 2026)]] runs the LVDTA fractional-Kelly budget live (and its audit shows the formula sizing a no-edge system down to the floor); [[Global Macro Trading Deck (July 2026)]] operationalizes the IV÷RV sizing rule and the 5-signal stress checklist; [[Macro-Aware Risk Parity System]] is the risk-budgeting sibling.
