---
title: M2 Money Supply & Liquidity
category: indicators
type: domain
data_asof: 2026-09-16
summary: "Broad money as the liquidity/inflation gauge from a 1959–2021 corpus (M2 +25.8% YoY into Jan-2021 on negative real rates) — a regime the 2026-09-16 check shows fully reversed: M2 +5.41% YoY, real 10y now +1.62%."
tags: [global-macro, money-supply, m2, liquidity, central-banks, inflation, fractional-reserve, real-rates]
data_vintage: "1959–2021 teaching corpus (M2 + real rates through Jan-2021); live counterpart re-checked 2026-09-16 (M2 through Jul-2026, yields through 2026-09-14) — the 2021 regime has reversed, see the note in How it's used"
sources: 5
updated: 2026-09-16
---

# M2 Money Supply & Liquidity

**What it is & why it matters** — M2 is the broad money supply: M1 (notes/coins in circulation + demand deposits + other checkable deposits) plus "close substitutes" — savings deposits, retail time deposits under $100k, and money market deposit accounts. In the Global Macros framework M2 is the *key liquidity gauge used to forecast inflation* and to read the central bank's stance — expanding M2 (injection) is a tailwind for risk assets and a currency negative; contracting M2 (withdrawal) is the reverse. Because banks create money through fractional-reserve lending, the central bank's policy levers (rate moves, QE, reserve requirements) propagate through the deposit multiplier into the broad aggregate that actually circulates in the economy.

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `US_M2_Money_Supply_Template.xlsx` | Nominal US M2 stock ($bn) with MoM% and YoY% change, descriptive stats and std-dev bounds, MoM/YoY histograms; a second tab regresses S&P 500 (log) against M2 WoW | 1959-01 → 2021-01 (745 monthly pts) | M2 MoM% & YoY% bar charts; MoM%/YoY% probability histograms; "S&P 500 (Log Prices) vs M2 (Nominal) WoW" |
| `China_Real_Rates.xlsx` | China & US 10yr benchmark yield, CPI YoY, and derived "real" 10yr rate (yield − CPI); plus a China-vs-US comparison tab | China/compare 2000-09 → 2021-01 (238 pts); US 1962-01 → 2021-01 (709 pts) | China Real Rates, US Real Rates, China vs US Real Rates line charts |
| `Money_Supply_Definition_Example.pdf` | Definitions of M0/MB/M1/M2/M3 and a worked Laura example showing how deposits, loans and FX flow through the aggregates; central-bank levers (M2 injection/withdrawal, QE, rate differentials) | Reference doc | — |
| `Fractional_Reserve_Banking_Example.pdf` | Two-bank worked example of money creation; deposit multiplier M = 1/RR | Reference doc | "$100 expansion under varying reserve requirements" |
| `Fed_Resources_Links.pdf` | Source links: FRED M2SL & M2REAL, Fed balance sheet (WALCL), fed funds target/effective, FOMC calendar & long-run goals | Reference doc | — |

## Charts & key trends
- **Nominal US M2 stock (1959–2021)** — As captured in the dataset, M2 rose from **$286.6bn (Jan-1959)** to **$19,390bn (Jan-2021)**, a ~68x increase, mean over the sample ~$4,483bn. Growth is near-monotonic but the slope steepens sharply at the end: the final readings run $18,390 → $18,618 → $18,750 → $19,010 → $19,090 → $19,390bn over the closing months — the 2020 COVID monetary surge.
- **M2 MoM % change** — Mean monthly growth **+0.57%**, ranging from **−0.56% to +6.45%**. The +6.45% single-month spike sits at the far right of the MoM histogram (a multi-sigma event) and corresponds to the 2020 stimulus injection; the closing months show elevated prints (+1.23%, +1.34%, +1.60%) versus the long-run ~0.5% norm.
- **M2 YoY % change** — Sample mean ~**7.0%**, but the series ends at its all-time extreme: the final readings climb **+23.1% → +23.8% → +23.7% → +24.5% → +24.6% → +25.8%**, the highest year-on-year money growth in the entire 1959–2021 record (prior floor in the sample was ~0.2%). This is the headline signal of the dataset — an unprecedented liquidity expansion into early 2021 that the Global Macros framework would read as strongly inflationary and risk-on.
- **S&P 500 (log) vs M2 WoW** — The second tab pairs equity prices against money growth, encoding the framework view that broad-money expansion is a structural tailwind for nominal asset prices.
- **US real 10yr rate (1962–2021)** — Computed as 10yr yield − CPI YoY. Fell from **+3.43% (1962)** to **−0.26% (Jan-2021)**, sample mean +2.26%, spanning **−4.70% to +9.58%**. The closing run is negative (−0.60%, −0.72%, −0.31%, −0.30%, −0.37%, −0.26%) — deeply negative real rates that, alongside the M2 surge, define an ultra-loose liquidity regime.
- **China real 10yr rate (2000–2021)** — From +2.79% (2000) to **+3.53% (Jan-2021)**; mean +1.19%, range −4.62% to +5.35%. China's CPI turned slightly negative at the end (−0.3% YoY), lifting the real rate.
- **China vs US real rates** — The comparison tab shows the gap inverting late in the sample: China real 10yr **+3.53%** versus US **−0.26%** at Jan-2021 — a wide positive China-minus-US real-rate differential, which in the FX framework is yuan-supportive / dollar-negative.

## How it's used in the strategy
- **Liquidity regime read** — Accelerating M2 YoY (the +25.8% terminal print) flags an injection regime: bullish for cyclical equities, commodities and risk credit; a stalling or contracting M2 would flag withdrawal and a defensive tilt.
- **Inflation forecasting** — M2 is treated as the leading money-side input to the inflation view; rapid M2 growth feeds the expectation that CPI follows, which in turn drives the rates and bond positioning. See [[Government Bond Yields]] and [[Yield Curve & Recession Signals]].
- **FX cross-check** — Money-supply *injection* (and falling real rates) is currency-negative; relative real-rate differentials (e.g. China +3.5% vs US −0.3%) feed directly into the carry/positioning leg of the [[FX Endogenous-Exogenous Framework]] and [[USD & G10 FX]].
- **Mechanism awareness** — The fractional-reserve / deposit-multiplier framing (M = 1/RR; a 10% reserve ratio allows up to 10x deposit expansion from new reserves) explains *why* central-bank actions amplify into the broad aggregate, and why QE and reserve-requirement changes matter beyond the policy rate.
- **Risk sizing** — A negative-real-rate, surging-M2 backdrop argues for higher gross exposure to inflation-sensitive longs; it is logged in the regime view. See [[Risk Management]] and [[Portfolio Management]].

> **⚠ The regime described above is the Jan-2021 one, and it has fully reversed (re-checked 2026-09-16; previously checked 2026-09-08).** The figures in *Charts & key trends* are the correct terminal readings of this page's **1959–2021 teaching dataset** and are left as they stand. But the three bullets above restate them in the present tense, and as a *live* read every leg is now wrong:
> - **M2 YoY: +25.8% (Jan-2021) → +5.41% (Jul-2026).** Re-verified against FRED `M2SL` on 2026-09-16 — $23,218.0bn for Jul-2026, +5.41% on Jul-2025, **unchanged from the 2026-09-08 check** because no newer month has been published. Not an injection regime — that is roughly normal broad-money growth, a little above nominal-GDP trend.
> - **US real 10y: −0.26% (Jan-2021) → +1.62% (2026-09-14)** on this page's own method (10y **4.97%** − CPI YoY **3.35%**), and the market-priced 10y TIPS real yield is **+2.60%** (FRED `DFII10`, 2026-09-14). *Supersedes the 2026-09-08 read of +1.47% (10y 4.77% − CPI 3.30%) and TIPS +2.42%.* **Real rates got tighter, not looser, over the eight days**: the nominal 10y rose 20bp while August CPI added only 5bp to the YoY rate, so both the derived real rate (+15bp) and the market-priced one (+18bp) went up. Real rates are firmly *positive*, not "deeply negative".
>   - *CPI base, stated explicitly because it moves this number:* **+3.35%** is the strict 12-month change, `CPIAUCSL` 334.131 (2026-08) ÷ 323.291 (2025-08). July's own YoY was +3.30%, so the inflation leg barely moved and the real-rate rise is almost entirely a nominal-yield move.
> - So the "negative-real-rate, surging-M2" sizing conclusion **does not apply to today** and must not be read as current — and it is now further from applying than it was a week ago. The live liquidity read lives in [[Macro Regime - Live (June 2026)]]; the China-vs-US real-rate differential quoted above is a Jan-2021 snapshot and has **not** been re-verified against current Chinese data (unresolved at this refresh, as at the last one).

## See also
- [[Leading Indicators]]
- [[GDP & Growth]]
- [[Government Bond Yields]]
- [[Yield Curve & Recession Signals]]
- [[Corporate Bond Yields & Credit]]
- [[FX Endogenous-Exogenous Framework]]
- [[USD & G10 FX]]
- [[Cyclical Commodities]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Glossary]]
