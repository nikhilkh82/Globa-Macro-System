---
title: Government Bond Yields
category: rates
type: domain
data_asof: 2021-02-09
summary: "G10 sovereign benchmark curves (US, DE, EU, JP, UK, AU, CA) plus US TIPS real yields — the risk-free anchor; its Jan–Feb 2021 snapshot is the pandemic zero-rate regime (5yr TIPS −1.55%, Bund curve all negative)."
tags: [global-macro, rates, sovereign-bonds, treasuries, yield-curve, real-yields]
data_vintage: "2000–2021 (history); curve snapshots Jan–Feb 2021"
sources: 9
updated: 2026-06-18
---

# Government Bond Yields

**What it is & why it matters** — Sovereign (government) bond yields are the "risk-free" benchmark term structure for each currency bloc. Per the Global Macros bond methodology, every bond yield decomposes into a *benchmark yield* (the sovereign curve, capturing inflation expectations + the real rate + monetary/fiscal policy) plus a *spread* (issuer-specific credit premium). The government curve is therefore the anchor for FX, equity discounting, credit, and the recession-signal work. This page covers the G10 nominal curves plus US real (TIPS) yields; the slope/inversion analysis lives in [[Yield Curve & Recession Signals]] and the credit-premium layer in [[Corporate Bond Yields & Credit]].

## Key datasets & files
| File                       | What's in it                                                                                                                     | Date range                                                                      | Notable charts                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `Benchmark_Yields_US.xlsm` | Full UST curve (Fed Funds, 1mo→30yr) + TIPS (5/7/10/20/30yr) real curve; per-tenor historical & 20yr charts                      | Data tab back to ~1962; Summary snapshot **2021-01-03**; weekly back to 2020-05 | "US Yield Curve – Comparative Analysis"; "US Real Yield Curve (TIPS)"; per-tenor Historical/Last-20yr |
| `Benchmark_Yields_DE.xlsm` | German Bund curve, 6mo→30yr                                                                                                      | Snapshot **2021-02-09**, weekly to 2020-12                                      | Curve comparative analysis                                                                            |
| `Benchmark_Yields_EU.xlsm` | EUR-area composite curve, 3mo→30yr                                                                                               | Snapshot **2021-02-05**                                                         | Curve comparative analysis                                                                            |
| `Benchmark_Yields_JP.xlsm` | JGB curve, 1yr→30yr                                                                                                              | Snapshot **2021-02-07**                                                         | Curve comparative analysis                                                                            |
| `Benchmark_Yields_UK.xlsm` | Gilt curve, 1yr→30yr                                                                                                             | Snapshot **2021-02-05**                                                         | Curve comparative analysis                                                                            |
| `Benchmark_Yields_AU.xlsm` | ACGB curve, 2yr→10yr                                                                                                             | Snapshot **2021-02-08**                                                         | Curve comparative analysis                                                                            |
| `Benchmark_Yields_CA.xlsm` | GoC curve, O/N (CORRA) + 1mo→30yr                                                                                                | Snapshot **2021-02-07**                                                         | Curve comparative analysis                                                                            |
| `RBA_Interbank_Rates.xls`  | Australian money-market: Cash Rate Target, Interbank Overnight Cash Rate, 30/90/180-day BABs/NCDs, 1/3/6m OIS, T-Notes (monthly) | 295+ monthly obs back to ~1990s                                                 | Short-end / policy anchor                                                                             |

## Charts & key trends
All snapshots below are the **pandemic-era zero/negative-rate regime** captured in the dataset (late-2020 to early-2021). Treat as a historical regime picture, not current.

**US Treasury nominal curve (data through 2021-01-03)** — A "normal" but ultra-low upward-sloping curve sitting on a near-zero front end:
- Fed Funds **0.09%**, 1mo **0.06%**, 3mo **0.08%**, 6mo **0.09%**, 1yr **0.12%**, 2yr **0.12%**.
- Belly/long end: 5yr **0.37%**, 7yr **0.66%**, 10yr **0.93%**, 20yr **1.46%**, 30yr **1.66%**.
- YoY column shows the COVID collapse: the front end fell ~**-1.46pp** vs a year earlier; the 30yr fell ~**-0.80pp**. The full Data tab spans decades — context: this is among the lowest the US curve has ever been.

**US real curve (TIPS, through 2021-01-03)** — Deeply negative real yields across the entire curve, the signature of financial-repression/QE liquidity:
- 5yr TIPS **-1.55%** (the dataset minimum), 7yr **-1.28%**, 10yr **-1.03%**, 20yr **-0.58%**, 30yr **-0.35%**.
- Implied 10yr inflation (nominal − real) ≈ **1.9–2.0%** (Summary "Implied Inflation" 1.92–2.04, mean ~1.97%). Negative real yields = strong tailwind for gold, equities, and risk assets per the framework.

**Germany (Bund, through 2021-02-09)** — Entirely negative nominal curve; even the long end barely above zero: 6mo **-0.65%**, 2yr **-0.73%** (curve trough), 5yr **-0.70%**, 10yr **-0.27%**, 30yr ≈ **-0.01%**. Bunds are the EUR risk-free anchor and the most negative-yielding G10 curve in the dataset.

**EUR-area composite (through 2021-02-05)** — 3mo **-0.567%** rising to 10yr **≈ -0.105%** area, 30yr **+0.737%**; negative out to ~7–10yr.

**Japan (JGB, through 2021-02-07)** — BoJ yield-curve-control fingerprint: 1yr **-0.123%**, trough around 3yr **-0.137%**, crossing zero near 10yr **+0.061%** (pinned ~0% by YCC), then steepening to 20yr **+0.45%**, 30yr **+0.656%**.

**UK (Gilt, through 2021-02-05)** — Front end just negative, long end positive: 1yr **-0.034%**, 2yr **-0.003%**, 5yr **+0.144%**, 10yr **+0.542%**, 20yr **+1.065%**, 30yr **+1.136%** — the steepest G10 long end in the snapshot.

**Australia (ACGB, through 2021-02-08)** — 2yr **0.09%**, 3yr **0.105%** (RBA 3yr YCC target era), 5yr **0.415%**, 10yr **1.225%** — a steep curve, with the 10yr the highest G10 10yr reading here.

**Canada (GoC, through 2021-02-07)** — Overnight CORRA **0.19%**, 1mo **0.05%**, 3mo **0.06%**, climbing to ~**0.96%** at the long end.

**Australian money market (RBA file, monthly history)** — The long-run policy anchor: Cash Rate Target ranged from a **14%** high down to **2.275%** (mean ~5.47%); the Interbank Overnight Cash Rate maxed at **20.77%**; 90-day BABs/NCDs maxed **21.75%**. Illustrates how far global short rates fell from the high-inflation era into the 2020 zero-rate regime.

## How it's used in the strategy
- **Risk-free anchor & FX**: The sovereign curve is the discount-rate input for everything. Yield differentials across these G10 curves (e.g. AU 10yr 1.225% vs DE 10yr -0.27%) drive carry and the rate-differential leg of [[FX Endogenous-Exogenous Framework]] and [[USD & G10 FX]].
- **Real yields as a regime gauge**: Deeply negative US TIPS yields signal accommodative liquidity — cross-referenced with [[M2 Money Supply & Liquidity]] and supportive of risk assets / [[Bull & Bear Markets]] positioning.
- **Curve construction → recession signal**: The nominal tenor data feeds the slope/inversion work in [[Yield Curve & Recession Signals]] (10yr-3mo, 10yr-2yr).
- **Credit decomposition**: Subtracting the sovereign benchmark from a corporate yield isolates the credit premium — see [[Corporate Bond Yields & Credit]].
- **Duration/positioning**: Per the methodology PDF, longer-maturity and lower-coupon bonds carry more duration; the strategy sizes rate exposure (and bond-ETF proxies like TLT/IEF) using these curve levels and the WoW/MoM/QoQ momentum columns in each Summary tab.

## See also
- [[Yield Curve & Recession Signals]]
- [[Corporate Bond Yields & Credit]]
- [[M2 Money Supply & Liquidity]]
- [[FX Endogenous-Exogenous Framework]]
- [[USD & G10 FX]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Glossary]]

**Live counterparts:** [[Global Macro Trading Deck (July 2026)]] section 11 tracks the full CMT curve (today/1m/1y), 2s10s/5s30s/3m10y slopes, the US/DE/UK/JP/IT/CA/AU 10y panel and TIPS breakevens; [[Treasury Macro-Trend System]] and [[Macro Curve-Trade Strategy]] are the honest timing tests (trend weak; curve null after the DV01 fix).
