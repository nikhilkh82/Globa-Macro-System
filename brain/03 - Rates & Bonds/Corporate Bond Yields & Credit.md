---
title: Corporate Bond Yields & Credit
category: rates
type: domain
data_asof: 2026-09-16
summary: "IG vs HY corporate yields (AAA/BBB/CCC), credit spreads as a risk-appetite barometer and bond ETFs; the live tail is diverging — CCC OAS 10.81 (14 Sep 2026), 2026's high, while HY OAS 2.71 sits near 3-year tights."
tags: [global-macro, credit, corporate-bonds, ig, high-yield, spreads, risk-appetite]
data_vintage: "2005–2021 teaching corpus (ICE BofAML & ETFs daily) + LIVE: workbook CCC−10y spread through 2026-09-04, FRED ICE BofA OAS (CCC / HY / IG) through 2026-09-14"
sources: 2
updated: 2026-09-16
---

# Corporate Bond Yields & Credit

**What it is & why it matters** — Corporate bond yields = the sovereign benchmark + a *credit spread* (the issuer-specific risk premium). Per the Global Macros methodology, the spread "captures all microeconomic factors specific to the issuer — credit risk, rating changes, liquidity" and "is the risk premium over the risk-free rate." Tracking yields by rating band (AAA → BBB → CCC) and the spreads between them turns the credit market into a real-time risk-appetite barometer: tight spreads = complacent, risk-on; blowing-out spreads = stress and recession. This page sits on top of the risk-free curve from [[Government Bond Yields]] and confirms the slope signals in [[Yield Curve & Recession Signals]].

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `Corporate_Bond_Indices.xlsm` — *US Corp Yield Indices* | ICE BofAML AAA, BBB, CCC(-or-below) yields + UST 10yr | **2005-11-23 → 2021-01-07** (~4,000 daily) | AAA / BBB / CCC historical + Last-5yr |
| `Corporate_Bond_Indices.xlsm` — *US Corp Yield Spreads* | Pairwise spreads: AAA-BBB, AAA-CCC, BBB-CCC, 10yr-AAA, 10yr-BBB, 10yr-CCC | **2005-11-23 → 2021-01-07** | 12 charts (full + Last-5yr for each spread) |
| `Corporate_Bond_Indices.xlsm` — *ETFs* | TLT, SHY, LQD (IG), JNK, HYG (HY) prices | **2005-11-23 → 2021-01-07** | SHY/LQD/TLT/JNK/HYG historical + Last-5yr |
| `Corporate_Bond_Indices.xlsm` — *Summary* | Recent AAA/BBB/CCC, ETF levels, recent spread changes | Snapshot **2021-01-07**, ~24 days | — |
| methodology: `Bond Market and Interest Rate Basics.pdf` | Rating scale (Aaa/AAA → D), spread = benchmark + credit premium, duration/convexity | reference | rating ladder, price/yield convexity |

> Note: in the spread sheet the values are stored as **(benchmark − higher-yielder)**, so they print negative (e.g. AAA-CCC ≈ -6.6 means CCC yields ~6.6pp above AAA). Below they are described as conventional *positive* credit spreads.

## Charts & key trends
**Rating-band yields, 2005 → Jan 2021** — the credit cost-of-funds ladder and its crisis extremes:
- **AAA (IG, top quality)**: range **1.40% → 8.25%**, mean **~3.3%**; latest (2021-01-07) **1.70%**.
- **BBB (lowest IG)**: range **2.05% → 10.23%**, mean **~4.6%**; latest **2.16%**.
- **CCC (junk / "extremely speculative")**: range **7.91% → 45.02%**, mean **~12.7%**; latest **8.34%**. The **45% peak is the late-2008 GFC blow-out** — CCC issuers were effectively shut out of funding.
- UST 10yr (benchmark on the same sheet): **0.52% → 5.26%**, latest **1.08%**.

**Credit spreads (risk-appetite gauge)** — magnitude of the rating premium:
- **AAA-to-CCC spread**: widened to roughly **39.5pp** at the 2008 stress peak (sheet min -39.53) vs a calm-market low near **3.5pp** — a >10x swing. As of **2021-01-07** it had compressed back to ~**6.6pp** (post-COVID stimulus rally).
- **BBB-to-CCC spread**: peaked ~**35pp** in 2008, compressed to ~**6.2pp** by Jan-2021.
- **AAA-to-BBB spread** (within IG): typically modest, ~**0.5pp** (latest -0.46 → ~0.46pp), widening to ~**4.7pp** in 2008 — even high grade re-priced in the crisis.
- **10yr-to-CCC**: the full junk premium over the risk-free 10yr ran from ~**4.1pp** (calm) to ~**42.5pp** (2008), latest ~**6.6pp**.
- Behaviour: spreads are **tight and stable** in expansions, then **gap wider violently** at the onset of stress — the asymmetry the strategy watches for.

**Bond ETFs (tradeable proxies), 2005 → Jan 2021** — used as liquid instruments and as a risk-on/off read:
- **TLT** (20+yr Treasuries): **52.1 → 170.7**, latest ~**151.8** — long-duration, rallies in flight-to-quality.
- **SHY** (1–3yr Treasuries): **62.7 → 86.4**, latest **86.4** — short-duration safe parking.
- **LQD** (IG corporates): **51.0 → 138.1**, latest **135.9**.
- **JNK** (high-yield, SPDR): **33.9 → 108.9**, latest **108.9** — note the deep drawdown to ~34 in the 2008 crisis.
- **HYG** (high-yield, iShares): **29.2 → 87.3**, latest **87.2** — likewise collapsed in 2008.
- The **HY vs IG / Treasury ETF ratio** (JNK,HYG vs LQD,TLT) is a clean risk-appetite spread; HY underperformance is an early stress tell.

## How it's used in the strategy
- **Risk-appetite regime**: Tight, stable credit spreads → risk-on (favour equities, cyclicals, short vol); rapidly widening AAA-CCC / 10yr-CCC → de-risk and raise recession odds in [[Macro Regime Snapshot]]. Spread widening typically *confirms* (and sometimes leads) equity weakness in [[Bull & Bear Markets]] and spikes in [[VIX & Implied Volatility]].
- **Recession confirmation**: Credit blow-out alongside curve inversion is the high-conviction combination — pairs the signal here with [[Yield Curve & Recession Signals]].
- **Decomposition discipline**: Per the PDF, separating a corporate yield into benchmark ([[Government Bond Yields]]) + spread tells you *whether a move is macro (all bonds) or idiosyncratic (issuer credit)* — central to ranking long-short credit/equity ideas.
- **Implementation**: TLT/SHY/LQD/JNK/HYG give liquid long-short and hedging legs; HY-vs-Treasury and IG-vs-HY are natural [[Spread Trades]]. Duration/convexity from the methodology PDF governs sizing of the rate-sensitive legs.
- **Quality tilt**: The Aaa→D rating ladder frames the "up-in-quality" rotation late-cycle (buy AAA/IG, sell CCC) when spreads are historically tight.

## The CCC spread, live and tested (added 2026-08-17)

`RATES:CCCSPRD` — **CCC high-yield yield minus the 10-year Treasury**, weekly 1997-01 → 2026-09, the gauge behind the user-filed MacroMicro *Credit Spread vs S&P 500* chart. Sourced from the desk's own **workbook** (`23. US Corporate_Bond_Indices_2026.xlsm`, `10yr-CCC` column, sign-flipped) rather than FRED, because every ICE/BofA series truncates to ~2023-08 through the FRED API — re-confirmed again on 2026-09-08, when the API returned `None` for all four BAML columns while the workbook carried them through 4 Sep. Cross-validated three ways: workbook spread −10.13 → **+10.13%**, the workbook's own yields (CCC 14.92 − 10y 4.79 = 10.13), and MacroMicro's own text ("a modest 9-10%") — which the spread has now edged just above.

**The `>credit` command tests the chart's takeaway on its own terms** — "during past downturns credit spreads surged close to 20% or above" is a threshold claim, so it is scored with the same episode machinery as the SF Fed 30-state rule, not a lag scan.

| Threshold | Episodes | Hit a distinct recession | False alarms | Recessions missed |
|---|---|---|---|---|
| **20%** (as stated) | 3 | 2 (67%) | 1 — *2002-08, a post-recession second spike* | **1 — 2020-03** |
| **15%** | 4 | 3 (75%) | 1 — *2015-12, the EM/energy scare* | 0 |

**This corrects the chart's own claim: COVID never crossed 20%.** The CCC spread peaked at **18.80%** in 2020, so a literal 20% rule would have sat out the pandemic entirely — "close to" is doing real work in that sentence. It holds for 2002 (23.4%) and 2008 (**39.8%** peak). At ~15% the rule catches all three recessions, but with only **three in-sample recessions** this is a regime description, not a tested signal, and the panel says so.

**Direction, honestly.** The spread is a market *price*, so it moves **with** equities rather than ahead of them. It is encoded as an **inverse co-movement** claim against `MKTS:SPX` on a symmetric ±3m window (sign −1) — *not* a lead claim, because the chart asserts none. Verdict: r₀ = −0.17, best −0.22 @ −1m, ✓ supports (right sign, contemporaneous). Per-episode leads scatter from −9m to +10m, which is itself the answer to "does it lead?".

**A nuance the chart understates:** at **10.13%** (4 Sep 2026) the spread sits at the **62.7th percentile** of its own 1997-2026 history (n=1,420 weekly obs; median 9.09%, range 4.16–39.76%) — *above* the median, and drifting up. "Modest" is fair against crisis levels of 20–40%, but this is mid-pack, not calm.

### Refresh 2026-09-16 — the CCC tail is repricing and the index is not

**The workbook spread is unchanged, and that is a vintage fact, not a market one.** `RATES:CCCSPRD` still reads **10.13% at 2026-09-04** — the workbook (`23. US Corporate_Bond_Indices_2026.xlsm`) was last written **2026-09-07** and today's Excel COM appliers (`update_yields_credit.py`) were **deliberately not run** because the user has Excel open. So the **62.7th percentile stands unchanged**: same value, same 1,420-observation weekly history, same method. Nothing was recomputed and nothing should be read into it.

**What did move is the ICE BofA option-adjusted spreads, re-pulled from FRED today** (own observation date **2026-09-14**):

| Series | FRED id | 2026-08-14 | 2026-09-08 | **2026-09-14** | Pctile in FRED's window |
|---|---|---|---|---|---|
| CCC & lower OAS | `BAMLH0A3HYC` | 10.12 | 10.56 | **10.81** | **99.2nd** |
| High-yield OAS | `BAMLH0A0HYM2` | 2.67 | 2.67 | **2.71** | 11.1st |
| Investment-grade OAS | `BAMLC0A0CM` | 0.80 | 0.81 | **0.80** | 23.6th |

**That is the story.** In a month the CCC tail widened **+69bp** (+25bp in the last week alone) to the **highest level of 2026**, while HY OAS moved **+4bp** and IG OAS **−1bp**. Percentiles are within the rolling ~3-year window FRED serves (2023-09-18 → 2026-09-14, n=785) and must be read as such — it contains no 2008 and no 2020. On that window CCC sits essentially at its ceiling: only **5 days** print above today's 10.81, all in the April-2025 episode that peaked at **11.37 (2025-04-07)**. HY, on the same window, sits near its *floor* (min 2.59). **Low-rated credit is being repriced while the index it belongs to is not** — the classic shape of stress concentrating in the tail before it becomes a market-wide event, and the cleanest new credit signal on this page.

**A method correction, honestly.** This section's opening paragraph says every ICE/BofA series "truncates to ~2023-08 through the FRED API". Re-checked 2026-09-16: the truncation is at the **start**, not the end — the API serves a rolling ~3-year window (now beginning 2023-09-18) but it **does run to the latest business day**. So the OAS series are perfectly usable for the live tail; only the 1997→ history the percentile test needs still requires the workbook. Both sources are now cited above, each with its own date.

**Still not a signal by this page's own test.** 10.81 (OAS) and 10.13 (CCC−10y) are both far below the tested **15% / 20%** thresholds, and the two measures are not interchangeable — one is an option-adjusted index spread, the other a CCC yield minus the 10-year Treasury. Watch the *divergence*, not the level.

Prior dated record, kept verbatim:

*Refreshed 2026-09-08: 9.77% → **10.13%**, 59th → **62.7th percentile** (the 9.77% reading was 7-10 Aug). The spread has widened ~36bp over four weeks while HY OAS has **tightened** (2.75 → 2.65) — the two disagree because OAS is index-wide investment-grade-to-junk while this is the CCC tail against duration-matched Treasuries. Worth watching, not yet a signal: the tested thresholds below (15% / 20%) are both far away.*

## See also
- [[Government Bond Yields]]
- [[Yield Curve & Recession Signals]]
- [[Spread Trades]]
- [[VIX & Implied Volatility]]
- [[Bull & Bear Markets]]
- [[Macro Regime Snapshot]]
- [[Commitment of Traders (COT)]]
- [[The Global Macros Framework]]
- [[Glossary]]

**Live counterparts:** [[Global Macro Trading Deck (July 2026)]] section 8 runs credit live — Moody's Baa/Aaa spreads as the 20-year anchor, HY/BBB/IG OAS, the credit-vs-breakeven cushion, a computed credit-vol proxy and the euro-sovereign default-probability ranking; [[Credit ML Classification System]] is the honest macro-timing test (null vs the credit-premium base rate).
