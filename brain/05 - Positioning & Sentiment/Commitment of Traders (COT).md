---
title: Commitment of Traders (COT)
category: positioning
type: domain
data_asof: 2017-11-14
summary: "Weekly CFTC non-commercial positioning and the net 'Flip' (%NCP Long − %NCP Short) across 8 instruments as a contrarian/with-trend crowding signal; the 2013–Nov-2017 corpus ends with short-JPY at −37, a sample extreme."
tags: [global-macro, positioning, sentiment, cot, contrarian, fx, rates, vix]
data_vintage: "2004–2017 (AUD from 2004; most series Jan 2013 → Sep/Nov 2017)"
sources: 8
updated: 2026-06-18
---

# Commitment of Traders (COT)

**What it is & why it matters** — The CFTC's weekly Commitment of Traders report decomposes open interest in US futures into trader categories. The Global Macros strategy tracks the **non-commercial** (speculative / "large trader") category — hedge funds and CTAs who position directionally — to gauge how crowded a trade has become. The core insight is that speculative positioning is *mean-reverting*: when non-commercials are jammed to an extreme on one side, the marginal buyer/seller is exhausted and the position becomes a contrarian setup. Global Macros uses COT as a **positioning and sentiment overlay** that sits alongside the fundamental macro scoring — it confirms a thesis when positioning has room to run, and warns against a thesis when the crowd is already maxed out.

## Key datasets & files
Two parallel sets exist: the original `raw/Comitment of Traders/` (7 instruments) and `raw/Updated Market Data/COT/` (same 7 plus AUD). The schema is identical across files — columns `Date, NCP Long, NCP Short, ^NCP Long, ^NCP Short, %NCP Long, %NCP Short, Flip, <price>`. Every sheet is **reverse-chronological (newest row on top)**.

| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `COT_AUD_USD_Analysis.xlsx` | AUD futures spec positioning + AUD/USD spot. Longest history in the set (712 weeks). | 2004-01-20 → 2017-09-12 | LineChart "AUD-USD COT Flip" |
| `COT_EUR_USD_Analysis.xlsx` | EUR futures spec positioning + EUR/USD spot | 2013-01-08 → 2017-11-14 (254 wk) | "EUR-USD Flip" |
| `COT_GBP_USD_Analysis.xlsx` | GBP futures spec positioning + GBP/USD spot (extra working sheets) | 2013-01-08 → 2017-11-14 (254 wk) | "GBP-USD COT Flip" |
| `COT_USD_JPY_Analysis.xlsx` | JPY futures spec positioning + USD/JPY spot | 2013-01-08 → 2017-11-14 (254 wk) | "USD-JPY Flip" |
| `COT_DXY_Analysis.xlsx` | USD Index futures spec positioning + DXY | 2013-01-08 → 2017-09-12 (245 wk) | "DXY COT Flip" |
| `COT_10yr_Analysis.xlsx` | TY (10-yr Treasury) futures spec positioning + 10-yr yield | 2013-01-08 → 2017-09-12 (245 wk) | "TR 10YR COT Flip" |
| `COT_VIX_Analysis.xlsx` | VIX futures spec positioning + VIX level | 2013-01-08 → 2017-09-12 (245 wk) | "VIX COT Flip" |
| `COT_S&P_Analysis.xlsx` | E-mini S&P futures spec positioning + S&P index | 2013-01-08 → 2017-09-12 (245 wk) | "S&P COT Flip" |

## How the columns work — and the "Flip" signal
- **NCP Long / NCP Short** — non-commercial (speculator) open long and short contracts that week.
- **^NCP Long / ^NCP Short** — the week-on-week *change* in those positions (the caret means "delta"). This is the flow: who added or covered this week. Extremes here flag a positioning rush (e.g. EUR longs added +30,143 in one week at the historical max; 10-yr longs added +108,313 at peak).
- **%NCP Long / %NCP Short** — non-commercial longs/shorts as a percentage of total open interest. Normalising to a % makes the figure comparable across time as open interest grows.
- **Flip = %NCP Long − %NCP Short.** This is the headline net-positioning signal and the series plotted in every workbook's chart. Positive Flip = speculators net long; negative = net short. The magnitude measures *how crowded* the directional bet is.
- **Reading the Flip as a signal.** Global Macros uses Flip extremes two ways. (1) **Contrarian / fade** — when Flip pushes to the top or bottom of its multi-year range, the trade is crowded and prone to a violent unwind; a fresh entry *with* the crowd has poor reward-to-risk. (2) **With-trend confirmation** — a Flip moving off a neutral reading toward a fundamentally-supported direction confirms that real money is rotating into the macro view while there is still positioning room. The name "Flip" captures the moment net positioning *crosses zero* (longs overtaking shorts or vice-versa) — a sign the speculative consensus has changed sides, which often coincides with a regime change in the underlying price.

## Charts & key trends (as captured in the dataset)
Numbers below are real readings from the files; "latest" = the newest (top) row of each sheet. **Frame all of this as the historical positioning picture the dataset documents, not live markets.**

**FX**
- **EUR/USD** (through 2017-11-14): Flip ranged from **−31.6 (max short) to +27.4 (max long)**, mean −9.9 (speculators structurally net-short EUR over 2013–17). Latest Flip −1.0 (%long 11.8 vs %short 12.8) with EUR/USD at 1.1791 — close to neutral after a 2017 swing back toward longs. The euro had run from ~1.05 (2015–16 lows) up to 1.18.
- **GBP/USD** (through 2017-11-14): Flip range **−37.9 to +51.4**, mean +1.7 — the widest swing in the FX set, reflecting Brexit (2016) positioning shocks. Latest Flip +7.8 (%long 22.0 vs %short 14.2), cable 1.3214 — speculators rebuilding net longs off the post-Brexit washout.
- **USD/JPY** (through 2017-11-14): persistently **net-short JPY** (i.e., positioned for a weaker yen / "short JPY carry"). Flip range −39.1 to +33.9, mean −16.0. Latest Flip −37.0 (%long 10.9 vs %short 47.9) — near the *most extreme short-JPY reading in the sample*, a classic crowded-carry warning, with USD/JPY at 112.09.
- **AUD/USD** (2004 → 2017-09-12, 712 weeks): the deepest history. Flip range **−48.1 to +69.3**, mean +20.8 (structurally net-long AUD, the high-yield carry currency). Latest Flip +40.0 (%long 47.6 vs %short 7.6) with AUD/USD 0.8004 — speculators heavily net long, in the upper third of the historic range.
- **DXY** (US Dollar Index, through 2017-09-12): Flip range **−64.8 to +34.9**, mean −7.8. Latest Flip −2.5 (%long 39.7 vs %short 42.2), DXY 91.83 — modestly net-short the dollar as DXY fell back from its 2016–17 highs (range 79.19–103.01).

**Rates**
- **10-yr Treasury** (TY futures, through 2017-09-12): Flip range **−14.2 to +24.6**, mean +3.0. Latest Flip +0.3 (%long 15.9 vs %short 15.6) — essentially neutral, with the 10-yr yield at 2.20% (yield range over the window 1.36%–3.00%). The most extreme net-long bond readings (Flip >+20) clustered in early 2013, before the "taper tantrum" sell-off — a textbook crowded-long-before-reversal episode.

**Volatility & equities**
- **VIX** (VIX futures, through 2017-09-12): speculators are **chronically net-short volatility** — Flip range −42.6 to +18.9, mean −18.4. Latest Flip −13.6 (%long 16.6 vs %short 30.2) with VIX at 10.17, near the lows of the 9.36–28.03 range. Persistent net-short VIX is the structural "short-vol" carry trade; Global Macros treats a deeply negative VIX Flip with VIX pinned at the floor as a fragility flag (the unwind risk that materialised in the Feb-2018 "Volmageddon").
- **S&P 500** (E-mini futures, through 2017-09-12): Flip range **−13.6 to −1.4**, mean −7.1 — note it is *always negative* in the sample, because commercials/index hedgers dominate the short side; the signal is read off changes within that band rather than the sign. Latest Flip −3.0 (%long 9.4 vs %short 12.4) with the S&P at 2500 (range 1472–2500 over 2013–17, a near-monotonic bull market).

## How it's used in the strategy
- **Positioning overlay on the macro score.** After ranking instruments on fundamentals (growth, [[Leading Indicators]], liquidity, rates), Global Macros checks COT before sizing. A bullish macro call on an instrument that is *already maxed-long* on the Flip gets sized down or shelved — the easy money is gone and the unwind risk is asymmetric.
- **Contrarian extremes.** A Flip sitting at the top/bottom decile of its multi-year range (e.g. short-JPY at −37, net-long AUD at +40) flags a crowded trade ripe to fade, especially if the macro thesis no longer supports it.
- **With-trend confirmation & the zero-cross.** A Flip pulling off neutral toward the fundamentally-favoured direction — or actually crossing zero — confirms speculative money is rotating into the view with room left to run; this strengthens conviction for a [[Trade Idea Generation Process]] entry.
- **Flow timing via ^NCP.** The weekly change columns show *this week's* additions/covers — useful for timing relative to a longer-term Flip read, and for spotting capitulation (a large ^NCP cover into a price low).
- **Risk & fragility flags.** Extreme short-vol positioning (deeply negative VIX Flip with VIX at the floor) and crowded carry (short-JPY, long-AUD) feed directly into [[Risk Management]] and position sizing — these are the configurations most prone to gap moves. Cross-checks against [[VIX & Implied Volatility]] and the [[Macro Regime Snapshot]].

## See also
- [[VIX & Implied Volatility]]
- [[USD & G10 FX]]
- [[FX Endogenous-Exogenous Framework]]
- [[Government Bond Yields]]
- [[Trade Idea Generation Process]]
- [[Risk Management]]
- [[Macro Regime Snapshot]]
- [[The Global Macros Framework]]
- [[Glossary]]

**Live counterparts:** [[Analyst System — Live Cockpit (June 2026)]] carries the weekly CFTC COT panel (net-spec, 3y percentile, crowding) with an independent cross-check; [[PTM Global-Macro Dashboard (Endo + Exo)]] uses COT in the exo stage; [[LangAlpha Strategy System]] scores positioning as a contrarian factor.
