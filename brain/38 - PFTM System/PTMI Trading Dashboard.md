---
title: PTMI Trading Dashboard
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "The Instutrade PTM course on 2026 data: V4 distributions (all 7 indexes fat-tailed, S&P ex-kurt +7.7) + 26 workbook cards. The 2026-09-19 rebuild moved nothing: workbooks stop at 07 Sep, so the cards are pre-hike."
tags: [global-macro, ptmi, ptm, instutrade, distributions, patterns, trends, dashboard, excel-data, decision-support]
data_vintage: "your 2026 workbooks (2.8) · distributions from Bull_Bear 1928→2026"
sources: 1
updated: 2026-09-19
---

# PTMI Trading Dashboard — the Instutrade course on your 2026 data

The **original Anton Kreil "Professional Trading Masterclass" (Instutrade)** course logic — mapped from the 14
video-resource folders in `raw/Professional Trading Masterclass  Instutrade (PTMI)/` — applied to **every updated
workbook** in the 2.8 folder: each mined in depth for its key series, trends and turning-point patterns. Built
2026-07-07 ("prepare dashboard based on PTMI content & logic... go in depth for all excel file charts with key
patterns and trends").

> **Decision-support / education only — NOT investment advice.**

## The course, mapped
V4 Distribution of Returns · V6 Implied Vol · V7 ATR · V9 GDP · V13 Permits · V14 US Activity (durables/IP/claims/
employment) · V15 Europe (ESI) · V16 China (PMIs) · V18 Sectors & Spreads · V19 Company Stats · V21 Watchlist ·
V22 ATR sizing · V23 Beta hedge/Kelly/Exposure · V24 Beta.

## What the dashboard shows (`PTMI Dashboard/PTMI Trading Dashboard.html`)
- **V4 · Distribution of Returns** (the course's signature exercise, computed from your `Bull_Bear_Markets_2026`
  daily history): per index (S&P from 1928, 1,181 months; NASDAQ/DJIA/FTSE/DAX/Nikkei/ASX) a **monthly-return
  histogram** + mean/σ/skew/excess-kurtosis/%-within-1σ/%-positive/worst-best months and the **fat-tails verdict —
  all 7 indexes are fat-tailed** (S&P ex-kurtosis +7.7; worst month −29.9%) — the statistical case for stops and
  volatility-based sizing. "Last month (z)" flags when the latest move is already an outlier.
- **Module sections** (V9 GDP · V13 Permits & Housing · V14 US Activity / Inflation & Money / Sentiment ·
  V15 Europe · V16 China · Commodities): **26 workbook cards**, each with a 5-year sparkline (dark well), latest
  value (B/M/K formatted), YoY, z vs own history, the **3m-vs-6m turning-point pattern**, staleness flag, and the
  exact source file+sheet.
- **"Key patterns now" strip** — auto-picked extremes (largest |z|), accelerating patterns, and stale series.
- **Cross-links** for the course's remaining modules to where they already live: watchlist → Global Macro Trading
  Dashboard; ATR-sizing/Kelly/exposure (V22-23) → PFTM Full System; charts/ATR → Chart Room; endo scorecards
  (26/27/28 workbooks) → Cross-Country Endo.

## Live read — 2026-09-19 (current)
*Re-read from `ptmi_sweep.json` and `ptmi_deep.json` (both regenerated 2026-09-19 15:41; the dashboard HTML carries the same 15:41 build stamp) and cross-checked against the 2026-09-19 FRED snapshot. Supersedes the 2026-09-11 read below, which stays as the dated record.*

- **The rebuild changed no card, because no source workbook moved.** All 25 card workbooks were last saved on or before 2026-09-07 (the oldest: `2. US_CPI` 2026-07-18, `12. Industrial Production` 2026-08-07, `29. US_Leading_Indicators` 2026-08-10, `6. ISM Non Manuf` 2026-08-12, `1. Retail_Sales` 2026-08-15). Every card figure the 2026-09-11 read quoted is unchanged (its FRED cross-checks have since moved): 26 cards from 25 workbooks, **0 stale**, latest period 12 Aug · 8 Jul · 3 Jun · 2 Sep · 1 Apr; pattern tally Rising 12 · Rising (accelerating) 6 · Rolling over 3 · Bottoming 2 · Falling (accelerating) 2 · Falling 1; "Key patterns now" still Copper +3.17, M2 +2.79, Durable Goods +2.67.
- **V4 distributions unchanged, and older than they look.** S&P 500 still 1,181 months, excess kurtosis +7.73, worst −29.9%, best +39.1%; all 7 indexes fat-tailed. But `30. Bull_Bear_Markets_2026.xlsx` (saved 2026-06-27) ends its daily history on 2026-06-26, so "last month (z)" — S&P −2.98% (z −0.68), Nasdaq 100 −4.01% (z −0.80) — is a partial **June 2026**, not August or September. FRED has the S&P 500 at 7,637.76 (17 Sep, +15.7% y/y).
- **"0 stale" is the dashboard's 9-month rule, not freshness against FRED.** Cards now a month or more behind: CPI card Jun (YoY +3.46%) vs FRED CPIAUCSL Aug 334.131, +3.35% y/y; Industrial Production card Jun vs FRED Aug +1.42% y/y; Retail Sales card $763.6B (Jul) vs FRED RSAFS Aug $773.9B (+1.24% m/m, +6.01% y/y); Housing Starts card Jun 1,367k (sheet `Autorised`) vs FRED HOUST Aug 1,275k; the NFP-backed "US Leading Indicators" card ends Jul while FRED has Aug payrolls +162k (Jul +21k; 3-month avg +71k); the claims card's 206K vs FRED ICSA 196k (w/e 12 Sep; 4-wk avg 203,250). Still matching FRED: unemployment 4.1% (Aug) and M2 $23,218B (Jul, +5.41%). ISM, U-Mich, NFIB, EU ESI and the China cards could not be cross-checked today.
- **Where the cards now contradict the tape.** The WTI card ($85.76 Aug, YoY +34.0%) still reads **Rolling over**, but FRED daily WTI rose to $107.02 on 15 Sep ($97.26 on 9 Sep; +68.1% y/y) and Brent to $130.80 — `14. Commodity_Prices_2026.xlsx` was not updated (the Workbook Explorer's COMMOD group likewise ends 2026-08-31). The PPI card's Jul YoY +5.51% (Rising) differs from FRED PPIACO's Jul +8.70% for the same month, and FRED Aug is +9.85% y/y (+0.96% m/m) — check the workbook series. Copper card 6.688 $ (Aug COMEX, YoY +48.0%, z +3.17) vs IMF monthly $13,543/mt (Jul, +38.6% y/y): different series, same direction.
- **The deep yield-curve panel is pre-hike.** `ptmi_deep.json` (from `22. US Benchmark_Yields_2026.xlsm`, saved 2026-09-07) still plots Fed funds 3.63% and 10yr 4.78%, and the 10Y card reads 4.78% (Sep). Current: the Fed raised 25bp to **3.75–4.00%** effective 17 Sep (EFFR 3.88%), its first hike of the cycle; FRED 10Y 4.94% and 2Y 4.67% (17 Sep); 10Y−2Y flattened from +0.33 (15 Sep) to +0.25 (18 Sep).
- **Regime context the cards cannot show yet.** Both major central banks tightened in the same week that the energy shock re-intensified: the Fed's first hike and the ECB's second move (deposit rate to 2.50%, effective 16 Sep) came as WTI rose to $107 and Brent to $131 (15 Sep), with August PPI at +9.85% y/y. Demand is firm, not fading: retail sales +1.24% m/m, payrolls +162k, claims 196k. Core CPI is still only +2.45% y/y; its 3-month pace turned up to 1.97% from 1.64% but remains below 2%, while core PCE is 3.34% (Jul). Markets absorbed the hike: credit had already retraced on 16 Sep (HY 2.70, CCC 10.76) and VIX fell to 15.44 on hike day.
- **One more card caveat:** the "US Nominal GDP" card's YoY +2.1% (Q2-2026, period 2026-04) equals FRED real GDP (GDPC1) +2.10% y/y, so the card may be plotting real, not nominal, GDP. It joins the three caveats listed in the 2026-09-11 read (payrolls-as-LEI, China Real Rates on sheet `US Real Rates`, Housing Starts on sheet `Autorised`).

## Live read — 2026-09-11
*Re-read from `ptmi_sweep.json` (generated 2026-09-08 09:37) and cross-checked against the 2026-09-08 FRED snapshot. Supersedes the 2026-07-07 sweep notes below, which stay as the dated record.*

- **V4 distributions re-verified, unchanged:** S&P 500 has 1,181 months (1928–2026), excess kurtosis +7.73, worst month −29.9%, best +39.1%. All 7 indexes are still flagged fat-tailed. No index's last month is an outlier: the largest |z| is Nasdaq 100 (−4.01%, z −0.80), and S&P is −2.98% (z −0.68).
- **Coverage:** 26 cards from 25 workbooks (26 file+sheet pairs, because `14. Commodity_Prices_2026.xlsx` feeds both WTI and Copper). **0 stale.** Latest period: 12 cards Aug-2026, 8 Jul, 3 Jun, 2 Sep (10Y and the corporate-bond card), 1 Apr (GDP).
- **Pattern tally (3m-vs-6m):** Rising 12 · Rising (accelerating) 6 · Rolling over 3 · Bottoming 2 · Falling (accelerating) 2 · Falling 1. That makes 8 cards "accelerating".
- **"Key patterns now" strip:** the largest |z| are Copper +3.17, M2 +2.79 and Durable Goods +2.67. Accelerating: Industrial Production, Initial Claims and Unemployment Rate (the first three of eight). No stale series.
- **Activity / labour:** unemployment 4.1% (Aug, matching FRED UNRATE) and claims 206K (Aug; FRED 4-wk avg 207,250 w/e 2026-08-29) are both Falling (accelerating). ISM Manufacturing 54.6 (Aug) is Rising. ISM Services 54.1 (Jul) is Rising (accelerating). Industrial Production (Jun) is Rising (accelerating). Retail Sales $763.6B (Jul, matching FRED RSAFS) is Rising. Durable Goods has z +2.67 but is Rolling over.
- **Inflation & money:** CPI (Jun; YoY +3.46%, z +2.14) and PPI (Jul; YoY +5.51%, z +2.42) are Rising. M2 $23,218B (Jul; YoY +5.41%, z +2.79, matching FRED M2SL) is Rising (accelerating). 10Y 4.78% (Sep) is Rising. The CPI card ends in Jun, while FRED CPIAUCSL already has Jul (332.813).
- **Sentiment:** U-Mich 51.7 (Aug; z −2.27) is Bottoming. The workbook is a month ahead of FRED UMCSENT, whose latest print is Jul 55.2. NFIB is Rising (accelerating). EU ESI −5.5 (Aug) is Rising (accelerating).
- **China (all Aug):** Official PMI 49.8 Rolling over · Conference Board PMI 50.1 Rising · HSBC flash PMI 51.5 Falling · real rates 4.75% Rising.
- **Commodities (Aug):** WTI $85.76 (YoY +34.0%) is Rolling over (FRED daily WTI was 91.48 on 2026-09-01). Copper 6.688 $ (YoY +48.0%, z +3.17) is Rising.
- **Flag: 2026-07-07 pattern reads overturned.** U-Mich went from "Falling (accelerating)" to Bottoming. ISM Services went from "Rolling over" to Rising (accelerating). EU sentiment went from "rolling over" to Rising (accelerating). CPI and PPI are no longer "accelerating" (M2 still is). Activity is now mostly plain Rising, with only Industrial Production and ISM Services accelerating. China official PMI is still Rolling over.
- **Card caveats:** the "US Leading Indicators" card reads sheet `NFP` of `29. US_Leading_Indicators_2026.xlsx`, and its values track FRED PAYEMS (Apr 158,798 and May 158,861 are identical; the card's Jul 158,858 compares with FRED's 158,913). It plots nonfarm payrolls in thousands, not the LEI. Two more cards need checking: "China Real Rates" reads sheet `US Real Rates` of `25.4. China_Real_Rates.xlsx`, and "Housing Starts" reads sheet `Autorised` (its Jun 1,367k does not match FRED HOUST's Jun 1,415k).

## Notable (2026-07-07 sweep)
The user's workbooks are **fresher than the live engines** in places: unemployment 4.2 (June), ISM 53.3 (June),
claims 215K (June), all four China PMIs (June), WTI (July). Patterns: the whole inflation complex (CPI/PPI/M2) and
most activity series **Rising (accelerating)**; U-Mich **Falling (accelerating)** at 49.5 *(workbook sweep value; FRED UMCSENT latest 44.8 — z −2.92, 0.1st pctl of 73y)*; ISM Services & China
official PMI **Rolling over**; EU sentiment −8 and rolling over.

## Build
`tools/ptmi_sweep.py` (generic, layout-robust series detection per workbook + distribution stats) →
`ptmi_sweep.json` → `tools/ptmi_report.py` → the dashboard. Orchestrator `build_ptmi.py`; in `build_all_2026.py`
(regenerates each refresh), Main-Dashboard card + cockpit ★. Gotcha fixed: per-module sparkline canvas ids must be
unique across the three "V14 ·" modules (`mod[:3]` collided → 8 blank sparklines; now indexed by module position).

## Related
[[2026 Trading System — Operating Manual]] · [[Macro Indicators Hub]] · [[Dynamic Macro Panel]] · [[PFTM Full Trading System]] · [[Cross-Country Endo & Divergence Backtest]] · [[Global Macro Trading Dashboard]]
