---
title: CB LEI vs Financial Stocks — a Circularity Warning
category: equities
type: live-read
data_asof: 2026-09-24
summary: "The CB LEI contains S&P 500 prices, so LEI-vs-financials is partly equities predicting equities; an ex-equities LEI does not lead (lag 0/−1m), 12m r ≈ −0.09 and sign-flips — only a +10.7% vs +5.8% regime tilt survives."
tags: [global-macro, lei, leading-indicators, equities, sectors, financials, circularity, honest-negative, lead-lag]
data_vintage: "LIVE — LEI proxies through Aug-2026, sectors Sep-2026 month-to-date, read from the Workbook Explorer asof 2026-09-23 / vhash 750401593e26 (built 2026-09-24T17:08:51); sector TR proxies via Yahoo, LEI proxies computed from free FRED components; the lead-lag / forward-return / regime-split tests stand on the 1999–2025 sample and were not re-run"
sources: 1
updated: 2026-09-25
---

# CB LEI vs Financial Stocks — a Circularity Warning

The Conference Board's Leading Economic Index is built from 10 components — manufacturing hours, jobless claims, new orders, building permits, the yield spread, consumer expectations — **and S&P 500 stock prices**. That last component is the reason this page exists.

The familiar chart pairs LEI YoY against the S&P 500 Financials total-return index and reads: LEI rising → cyclicals and financials benefit. Tested properly, that reading does not hold up, and the reason is largely mechanical.

## The circularity

**Equity prices are inside the predictor.** The CB LEI carries S&P 500 prices as one of its ten components, and financials are ~13% of the S&P 500 and **0.83 correlated** with it (YoY, 1999–2026). So plotting the LEI against financial stocks is, in meaningful part, plotting equities against equities. Any apparent "signal" inherits that overlap.

The desk's own reconstruction had the same problem: `LEI:PROXY` (the free-component stand-in for the licensed CB index) also included the S&P leg. So a second variant was built — **`LEI:PROXYXE`, identical but with the stock-price component removed** — as the only honest basis for testing an LEI→equity claim. Both now live in the Explorer.

## What the tests show

**It does not lead. It coincides — or lags.**

| Setup | Best lag | Correlation |
|---|---|---|
| LEI YoY (with S&P component) vs Financials YoY | **0 months** (contemporaneous) | +0.60 |
| LEI YoY **ex-equities** vs Financials YoY | **−1 month** — *financials lead the LEI* | +0.49 |

On a ±18-month scan the relationship peaks at zero lag with the equity component in, and at *minus one* with it removed. The "leading" index does not lead financial stocks; if anything the sector moves first and shows up in the index afterwards — unsurprising, since equity prices are a component and the other components are slower-published.

**As a forward-return signal it is unstable.** The tradeable version of the claim is: does today's LEI reading predict the *next* 12 months of financial-sector returns?

| Signal → next 12m financials return | Full sample | First half | Second half |
|---|---|---|---|
| LEI YoY (with equities) | **−0.10** | +0.12 | **−0.48** |
| LEI YoY **ex-equities** | **−0.09** | +0.19 | **−0.48** |

n = 319 months, 1999–2025. The full-sample correlation is **approximately zero and slightly negative**, and the sign **flips hard between halves** (+0.19 → −0.48). A relationship that reverses sign across the sample is not a signal; it is an artifact of whichever era you look at.

**The one thing that survives is a regime tilt, not a magnitude relationship.** Splitting on the sign of the reading rather than its level:

- LEI ex-equities **positive** → next-12m financials return averaged **+10.7%**
- LEI ex-equities **negative** → next-12m financials return averaged **+5.8%**

So positive-LEI regimes have historically been the better environment for financials by roughly 5 points a year — a directional prior worth knowing. But the *continuous* relationship carries no reliable information, and the gap is a long-run average across only two-ish cycles, not a timing rule.

## How to use it

- **Never** cite the LEI as a leading indicator *for equities* without disclosing that equities are inside it. For any LEI→market work use **`LEI:PROXYXE`** (ex-equities).
- Treat "LEI positive" as a weak regime **prior** for cyclical/financial exposure, sized accordingly — not as a timing signal, and never as a forward-return forecast.
- The LEI remains useful for what it is actually built to lead: real activity (see [[Conference Board LEI & Leading-Lagging Map]]). This page is about one specific misuse.

## Data

`SECTOR:FIN/IND/DISC/TECH/STPL/UTIL` — total-return proxies from the SPDR Select Sector ETFs (Yahoo adjusted close = price + reinvested dividends), 333 monthly observations, Jan-1999 to Sep-2026 (Explorer asof 2026-09-23; the Sep-2026 point is month-to-date, and this build **still** stores the 2026-09-01 row twice in every `SECTOR:*` series — 334 rows, 333 unique months — so dedupe before computing returns). *Superseded 2026-09-11: 332 monthly observations (as of Jul-2026).* The S&P 500 sector **total-return indices are licensed by S&P and not free**, so the ETFs are the disclosed free stand-ins. Latest prints (Explorer asof 2026-09-23, vhash 750401593e26, built 2026-09-24T17:08:51 — 427 series, 357,797 observations): Financials YoY **+8.55%** at the Aug-2026 month-end (`SECTOR:FIN` 57.5065 vs 52.9775 a year earlier), **falling to +2.84%** on the Sep-2026 month-to-date point (54.54 vs 53.0337; this point moves until month-end, and it has given back most of its lead in the last stretch of the month — the same point read +5.0% on 09-19 and +7.2% on 09-11). Note the Yahoo adjusted-close history itself restates slightly between builds — the same Aug-2026 YoY was computed from 57.71 / 53.165 on 09-19 and rounded to +8.5% — so quote the **ratio**, not the level. LEI proxy YoY **+1.12%**, ex-equities **+0.81%** (both Aug-2026; neither proxy has a Sep-2026 print). The ex-equities reading has been positive for five straight months (Apr **+0.52%**, May **+0.65%**, Jun **+0.59%**, Jul **+0.88%**, Aug **+0.81%** — all calendar-keyed), so on this page's sign split the current backdrop still sits in the *positive-LEI* bucket — a weak regime prior, not a timing signal. **The lead-lag, forward-return and regime-split tests above were not re-run in this refresh**; they stand on the 1999–2025 sample as tested, and nothing in today's data bears on them. *Superseded 2026-09-24: Financials YoY +8.5% at the Aug-2026 month-end (57.71 vs 53.165), easing to +5.0% on the Sep-2026 month-to-date point (55.86 vs 53.2214); LEI proxy YoY +1.1%, ex-equities +0.8% (Explorer asof 2026-09-18, vhash 0c98fb54bbc2).* *Superseded 2026-09-19: Sep-2026 month-to-date Financials YoY +7.2% (57.06 vs 53.2214; Explorer asof 2026-09-09, vhash 2df203da0e45); the Aug-2026 prints re-verified unchanged.* *Superseded 2026-09-11: Financials YoY +9.2%; LEI proxy YoY +0.8%, ex-equities +0.5% (as of Jul-2026).*

## Related

[[Leading Indicators]] · [[Conference Board LEI & Leading-Lagging Map]] · [[Sector Analysis & Rotation]] · [[Inventory-to-Sales Ratios & the Inflation Channel (July 2026)]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] · [[2026 Workbook Explorer]]
