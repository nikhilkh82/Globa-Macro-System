---
title: USD & G10 FX
category: fx
type: domain
data_asof: 2015-03
summary: "The tradeable FX universe (pegged vs floating, commodity vs ex-commodity) plus carry, ATR and return-distribution rankings and 8x leverage/margin mechanics; vol scales commodity minors > JPY/CHF majors > USD/EUR/GBP."
tags: [global-macro, fx, g10, carry, volatility, commodity-currencies]
data_vintage: 2008–2015 (volatility/ATR/distribution sheets), universe taxonomy undated
sources: 11
updated: 2026-07-25
---

# USD & G10 FX

**What it is & why it matters** — This page maps the *tradeable FX universe* the Global Macros global-macro strategy actually trades and the mechanics that govern it: how the world's currencies are classified (pegged vs floating, commodity vs ex-commodity), which subset is liquid and tradeable, and how each tradeable cross is then ranked on **carry** (interest-rate differential / rollover), **volatility** (ATR), and **return distribution** (standard deviation, high-to-low range). FX is where the macro thesis from the rates and growth work gets *expressed* — a view on relative growth, money supply and policy is sized against a pair's carry and its volatility envelope. The universe and rankings here are the screening layer that sits in front of the [[Trade Idea Generation Process]]; the directional view comes from [[GDP & Growth]], [[Government Bond Yields]], [[M2 Money Supply & Liquidity]] and positioning from [[Commitment of Traders (COT)]].

## Key datasets & files

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `FOREX_Universe_Tradable_Complex.xlsx` | Full taxonomy: Pegged / Floating split, then Commodity vs Ex-Commodity, then Tradable vs Non-Tradable. `LB_UB` sheet holds peg bands (lower/upper bound). | Undated (structural) | none |
| `FOREX_Markets_Organised.xlsx` | `ORG` (4-quadrant master grid by region), `SET` (clean tradeable set), `MAJORS_CROSSES` (~1,275 rows of cross history). | history to ~2015 | none |
| `Tradeable_Crosses_Opportunity_Ranked.xlsx` | Spot cross-rate matrix (~18×18) for the tradeable complex + `PFTM_Covered_Examples` — the crosses the course works through. | ~2015 snapshot | none |
| `Carry_Rollover.xlsx` | Generalised carry/rollover calculator (deposit vs lending rate, differential, daily interest long/short) at four leverage tiers: Lots / Minis / Micros / Nanos. | structural | none |
| `ATR_Rankings.xlsx` | All 27 tradeable crosses ranked by 1-yr-average Daily/Weekly/Monthly ATR, with group averages. | 1-yr avg to ~2015 | none |
| `Distribution_Rankings.xlsx` | Same crosses ranked by open-to-open Std Dev and Mean High-to-Low. | to ~2015 | none |
| `Comm Float Majors Volatility Analysis.xlsx` | Per-pair Dist + ATR (daily/weekly/monthly) for AUDUSD, AUDJPY, AUDNZD, AUDCAD, USDCAD. | ~2008 → Mar 2015 | Open-to-Open Histogram; High-to-Low Assessment (2 per pair) |
| `Comm Float Minors Volatility Analysis.xlsx` | EURNOK, EURRUB, GBPZAR, USDNOK, USDRUB, USDZAR. | ~2008 → 2015 | as above |
| `Ex Comm Float Majors Volatility Analysis.xlsx` | EURUSD (longest, ~4,400 rows), GBPUSD, USDJPY, USDCHF, GBPEUR, GBPJPY, GBPCHF, EURJPY, EURCHF, CHFJPY. | ~1999/2008 → 2015 | as above |
| `Ex Comm Float Minors Volatility Analysis.xlsx` | EURHUF, USDSEK. | ~2008 → 2015 | as above |
| `Exposure_Margin.xlsx` | Margin→exposure ladder for Stocks (4×), FX (8×) and combined (6×) books; margin-call % at each level. | structural | none |

## Charts & key trends

**The universe → tradeable funnel (FOREX_Universe / FOREX_Markets_Organised).** The whole FX world is sorted on two axes — peg status and commodity status — into a 4-quadrant grid (`ORG` sheet): *Ex-Commodity Floating, Ex-Commodity Pegged, Commodity Floating, Commodity Pegged*, each split by region (Developed / EMEA / AsiaPac / LATAM). The strategy then keeps only the liquid, freely-tradeable names:
- **Ex-Commodity Floating (Developed):** USD, EUR, JPY, GBP, CHF, SEK — plus DKK as an EUR-pegged "managed float."
- **Commodity Floating (Developed):** AUD, NZD, CAD, NOK.
- Tradeable EMEA/EM names that survive the screen: CZK, HUF, PLN (ex-comm float); RUB, ZAR, TRY (comm float); INR (Asia comm float); BRL, MXN, PEN (LATAM comm float).
- **Non-tradeable** (filtered out for illiquidity / capital controls / hard pegs): most AsiaPac floats (KRW, PHP, TWD, BHT, VND), Gulf USD-pegs (SAR, AED, QAR, etc.), CNH, and thin LATAM floats (ARS, CLP, COP). The G10 commodity bloc (AUD/NZD/CAD/NOK) is the cleanest expression of a global growth / [[Cyclical Commodities]] view; the ex-commodity bloc (EUR/JPY/CHF/GBP) is where rates and safe-haven flows dominate.

**Carry / rollover mechanics (Carry_Rollover.xlsx).** A generalised calculator: for a pair A/B you earn the deposit rate on the long leg and pay the lending rate on the borrowed leg, so the relevant number is the *differential*. The worked example uses A deposit 1% / lending 4% vs B deposit 7% / lending 12%, giving a long-A "carry" differential of **−0.11** (you pay to be long the low-yielder) versus **+0.03** short. On 1 standard lot (100,000 units) at a 0.9451 exchange rate that translates to roughly **−$31.89 daily interest** if long the wrong way vs **+$8.70** the favourable way; the same table re-bases for Mini (10k), Micro (1k) and Nano (100) lots. Takeaway for the strategy: **carry is a tailwind only when you are long the high-yielder**, and at FX leverage (up to 8×, see margin below) a few bp of daily roll compounds materially — so the carry sign must agree with the macro/rate view, not fight it.

**Volatility ranking — ATR (ATR_Rankings.xlsx, 1-yr averages).** All 27 tradeable crosses ranked by average true range. The RUB crosses sit far out at the top of the risk distribution (**USDRUB Daily ATR 0.0208, Monthly 0.146; EURRUB 0.0205 / 0.139**) — a 2014-15 rouble-crisis fingerprint. Among the **commodity minors** the average Daily ATR is ~0.0133 (GBPZAR 0.0109, USDZAR 0.0102, USDNOK 0.0092, EURNOK 0.0081). Among **ex-commodity majors** the average is ~0.0068, led by CHFJPY (0.0090), USDCHF (0.0079) and GBPCHF (0.0077) — note CHF crosses are elevated, an SNB-floor / Jan-2015 de-peg footprint. The **lowest-volatility** majors are GBPUSD (0.0052), GBPEUR (0.0057), EURUSD (0.0060) and USDCAD (0.0062). So volatility scales by group: *commodity minors > ex-commodity majors with a JPY/CHF leg > vanilla USD/EUR/GBP majors.*

**Return distribution (Distribution_Rankings.xlsx + per-pair Dist sheets).** Each pair's daily open-to-open return is profiled with full descriptive stats. By **Std Dev / Mean High-to-Low**, the widest-ranging tradeables are USDZAR (StdDev 0.0110, mean H-L 0.0152), AUDJPY (0.0120 / 0.0147) and GBPZAR (0.0082 / 0.0132); the tightest are GBPEUR (0.0047 / 0.0057) and EURCHF (0.0064 / 0.0059). The distributions are decidedly **non-normal and fat-tailed** — e.g. AUDUSD (2008–2015, n=2,020): mean ≈ 0, **Kurtosis 10.1**, slight negative **Skewness −0.28**, range −7.6% to +7.5%; AUDJPY is even more extreme (**Kurtosis 18.1**, range −11.7% to +13.2%) reflecting carry-unwind tail risk; USDCAD is tamer (Kurtosis 4.1, range ±3.6%). See [[Distribution of Returns]] for the leptokurtic framing and [[Average True Range (ATR)]] for the ATR mechanics.

**Spot cross matrix (Tradeable_Crosses_Opportunity_Ranked.xlsx).** An ~18×18 grid of every tradeable cross rate (e.g. USDJPY 120.79, EURJPY 131.51, GBPUSD 0.6624, EURUSD 1.0887 in the snapshot) so any opportunity can be quoted directly and the non-USD crosses (the "opportunity" set) screened alongside the dollar pairs.

**Exposure & margin (Exposure_Margin.xlsx).** FX is leverable to **8×** (vs 4× stocks, 6× combined book): $10,000 margin controls **$80,000** FX exposure. The ladder shows margin-call % rising as exposure rate climbs (e.g. exposure rate 8 → 12.5% buffer; rate 4 → 25%). This is the bridge from the carry/volatility numbers to position sizing — see [[Risk Management]] and [[Portfolio Management]].

## How it's used in the strategy

A Global Macros global-macro trader uses this layer as a **pre-trade screen and sizing engine**, not a signal generator:
1. **Form the macro view** elsewhere — relative growth, money supply, rate trajectory ([[GDP & Growth]], [[M2 Money Supply & Liquidity]], [[Government Bond Yields]]) and commodity backdrop ([[Cyclical Commodities]]) for the commodity bloc (AUD/NZD/CAD/NOK).
2. **Pick the cleanest expression** from the *tradeable* universe — avoid pegs, capital-controlled and illiquid EM names; prefer floats where the macro mechanism transmits to the exchange rate.
3. **Check the carry sign** — confirm the rate differential pays you (or at least doesn't bleed you) for holding the directional view; size the roll into expected holding period.
4. **Rank by volatility/distribution** — use ATR and the return distribution to set stops, targets and position size so each FX trade carries comparable risk (ATR-normalised sizing); high-kurtosis carry pairs like AUDJPY get smaller notional for the same risk budget.
5. **Confirm with positioning** — overlay [[Commitment of Traders (COT)]] for DXY/EUR/GBP/JPY to see whether speculators are crowded for or against the view, and [[VIX & Implied Volatility]] as a risk-on/off filter (carry longs underperform when vol spikes).
6. **Size against margin** — translate the chosen risk into notional via the 8× FX exposure ladder, respecting the margin-call buffers.

## See also
[[The Global Macros Framework]] · [[Trade Idea Generation Process]] · [[FX Endogenous-Exogenous Framework]] · [[Commitment of Traders (COT)]] · [[Average True Range (ATR)]] · [[Distribution of Returns]] · [[Cyclical Commodities]] · [[M2 Money Supply & Liquidity]] · [[Government Bond Yields]] · [[VIX & Implied Volatility]] · [[Risk Management]] · [[Portfolio Management]] · [[Spread Trades]] · [[Macro Regime Snapshot]]

**Live counterparts:** [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] holds the live cointegration screen on this page's crosses — on the full sample AUD/USD vs iron ore (trace 7.5), USD/CAD vs WTI (8.3) and EUR/USD vs the US−DE 10Y differential (12.8) **all FAIL**, so none qualifies as a tradeable equilibrium spread under the framework's own rule; the one relation that survives honest re-testing is **EUR/USD vs the US−DE 10Y differential post-2003** (trace 21.2, EG ADF −3.90). [[Global Macro Trading Deck (July 2026)]] runs the 9-pair FX panels and the realized FX-vol add-on (all Cboe FX-vol indices are discontinued — disclosed); [[FX Signals System (Common Sense vs ML)]] and [[FX Carry-Valuation System]] establish that carry is the one robust FX premium; the endo legs live in [[Australia Endogenous Driver Analysis (July 2026)]] and [[UK Endogenous Driver Analysis (July 2026)]].
