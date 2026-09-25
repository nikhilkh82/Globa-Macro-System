---
title: Bonus Indicators (New Set)
category: indicators
type: live-read
data_asof: 2026-09-24
summary: 9 supplementary Leading/Coincident indicators from the New Bonus framework — 6 live, 3 catalog-only. Re-verified 2026-09-24: OECD CLI still Aug-2026 = 100.96; current account advanced to Q2-2026 = -$246.0bn.
tags: [global-macro, leading-indicators, coincident-indicators, bonus, new-indicators, oecd-cli, nahb, zew, chicago-pmi]
data_vintage: "framework 2017 (New Bonus.rtf); FRED re-pulled 2026-09-24 — OECD CLI through Aug-2026, Personal Income/PCE through Jul-2026, current account through Q2-2026; the 3 web rows still frozen at May/Jun-2026 snapshots; workbook + dashboard rebuilt 2026-09-24 16:56"
sources: 1 (New Bonus.rtf) + FRED + tradingeconomics
updated: 2026-09-25
---

# Bonus Indicators (New Set)

**What it is** — A supplementary set of **9 Leading/Coincident indicators** from the *New Bonus* framework (`raw_ORIGINAL_backup/New Bonus.rtf` — *"a few more indicators that may be needed… part Leading, part coinciding"*). Built into a structured workbook + catalog under **`new indicators/`** (project root). Extends the core [[Leading Indicators]] and [[Coincident Indicators]] pages.

> **Data status.** 6 of 9 carry live data (3 FRED full-history, 3 web recent-quarter); 3 are proprietary and catalog-only (not fabricated). See `new indicators/New Indicators - Catalog & Data.xlsx` (rebuilt 2026-09-24 16:56). The three FRED rows were re-pulled 2026-09-24 and each runs to its own latest observation (CLI Aug-26, PI/PCE Jul-26, current account **Q2-26**) — CLI and PI/PCE are unchanged since the 2026-09-16 pull, but the current account advanced a quarter and Q1-26 was revised; **the three web rows are frozen snapshots, not a live feed** — treat them as the oldest data on the page.

## The 9 indicators
| # | Indicator | Type | Freq | Why it matters | Data |
|---|---|---|---|---|---|
| I | Weekly Chain Store Sales (ICSC/Redbook) | Leading | Weekly | Real-time large-store retail direction | catalog-only |
| II | NAHB Housing Market Index | Leading | Monthly | Leads residential construction / housing cycle | **web** → Jun-26 = 35 |
| III | Bloomberg Consumer Comfort | Leading | Weekly | 0.88 corr, leads UMich sentiment | catalog-only |
| IV | ZEW Economic Sentiment | Leading | Monthly | Leads EU Economic Sentiment; German/EU growth | **web** → Jun-26 = +10.5 |
| V | OECD Composite Leading Indicator | Leading | Monthly | Global cycle turning-point signal | **FRED** → Aug-26 = 100.96 (+0.06 MoM; Jul-26 = 100.89. 15th consecutive monthly gain, 9th month above 100 — but the smallest gain since Sep-25) |
| VI | Global PMI | Leading/Coincident | Monthly | Gauge for the commodity market | catalog-only |
| VII | Personal Income & Spending (PCE) | Coincident | Monthly | Consumer drives the economy; Fed targets PCE | **FRED** → Jul-26: PCE $22,250bn (+0.16% MoM, +5.9% YoY); PI $27,115bn (+3.7% YoY); saving rate 3.0%; PCE inflation +3.7% YoY (snapshot PCEPI) |
| VIII | Chicago PMI (Business Barometer) | Leading | Monthly | Released ~1d before ISM; tracks national PMI ~60% | **web** → May-26 = 62.7 |
| IX | Current Account Balance | Coincident/Lagging | Quarterly | Trade reshapes US employment (~19M jobs) | **FRED** → Q2-26 = -$246.0bn (-246,023 $mn; Q1-26 revised to -$212.6bn, -$33.4bn QoQ) |

> **Re-verified 2026-09-24** (FRED re-pulled direct; workbook *and* dashboard rebuilt today 16:56). **The three FRED rows are now verified against source rather than carried: CLI and PI/PCE are unchanged, but the current account advanced to Q2-26 and Q1-26 was revised.** The **OECD CLI is still Aug-26 = 100.96** (`USALOLITOAASTSAM` = 100.956, **+0.064 MoM** over Jul-26's 100.892; no Sep-26 print yet), so the read below is confirmed, not restated: 15 straight monthly gains (Jun-25 → Aug-26), 9 months above 100 (Dec-25 → Aug-26), and August's increment is the equal-smallest of the run since Sep-25 (+0.064) — still expansionary, still decelerating. **Personal Income & PCE remain Jul-26** — PCE **$22,250.4bn** (+0.16% MoM, **+5.92%** YoY), PI **$27,114.8bn** (**+3.69%** YoY), saving rate **3.0%**, PCEPI **+3.70%** YoY — the **Current Account has advanced to Q2-26 = −$246.0bn** (`IEABC` −246,023 $mn at 2026-04-01) and **Q1-26 was revised from −226,828 to −212,597 $mn (−$212.6bn)** — so Q2 widened **−$33.4bn** QoQ, and on the revised vintage Q1 was **+$8.5bn narrower** than Q4-25's −$221.1bn, not $5.8bn wider. A FRED realtime query stamped 2026-09-24 returns those same revised rows, so the release was live on the refresh date; the **deliverable now lags the page** — `new indicators/New Indicators Dashboard.html` and the catalog workbook were rebuilt **2026-09-24 16:56**, before the BEA rows landed, and still carry the pre-revision `["2026-01", -226.83]` last point and the KPI **"$-227bn (2026-01)"**. The rest of what moved is surface, not data: so the dashboard banner now stamps **"as of 2026-09-24"** — the hard-coded 2026-06-20 constant flagged in the 2026-09-11 note below is gone, `ASOF` is generated — and breadth **4 bull / 2 bear / 0 neutral / 3 awaiting** was **recomputed in today's build**, not carried from 2026-09-08. The three **web rows were again not re-verified**: NAHB 35 (Jun-26), ZEW +10.5 (Jun-26) and Chicago PMI 62.7 (May-26) are still the hard-coded `WEB_NAHB` / `WEB_ZEW` / `WEB_CHI` constants in `tools/build_new_indicators.py` and `tools/build_new_indicators_html.py` (comment: *"fetched 2026-06-20"*), and later prints for all three almost certainly exist.

> **Superseded 2026-09-16** (FRED re-pulled direct, no dashboard rebuild): the **OECD CLI row now reads Aug-26 = 100.96**, superseding the Jun-26 = 100.80 figure carried in the note below — the Jul-26 (100.89) and Aug-26 prints that the 2026-09-08 pull lacked have since landed, so the "no Jul/Aug print" caveat is retired. The index has now risen for 15 straight months and has held above 100 for 9, but the monthly increment has been shrinking since Jan-26 (+0.17) and August's **+0.06** is the smallest since Sep-25: the global-cycle signal is still expansionary and still decelerating. **Personal Income & PCE (Jul-26) and the Current Account (Q1-26) were re-pulled today and are unchanged** — Jul-26 remains the latest PI/PCE print and Q1-26 the latest current-account print — so those two rows stand as written and are re-verified, not restated. The three **web rows were not re-verified** this session: NAHB 35 (Jun-26), ZEW +10.5 (Jun-26) and Chicago PMI 62.7 (May-26) are still the hard-coded constants in `tools/build_new_indicators_html.py`, and later prints for all three almost certainly exist. Dashboard breadth (4 bull / 2 bear / 0 neutral / 3 awaiting) is the 2026-09-08 rebuild's and was not recomputed.

> **Superseded 2026-09-11** (dashboard rebuilt 2026-09-08): the FRED rows above replace the 2026-07-25 readings — PCE advanced from Apr-26 to Jul-26, Current Account from Q3-25 (-$262.9bn) to Q1-26 (-$226.8bn); OECD CLI is unchanged at Jun-26 = 100.80. The three web rows (NAHB 35 Jun-26, ZEW +10.5 Jun-26, Chicago PMI 62.7 May-26) are static snapshots hard-coded in `tools/build_new_indicators_html.py` and did not move; the dashboard's own "as of 2026-06-20" banner is that same hard-coded constant, not the data vintage. Dashboard breadth: 4 bull / 2 bear / 0 neutral / 3 awaiting.

## How it's used in the strategy
These slot into the macro layer of [[The Global Macros Framework]]: the OECD CLI and ZEW/NAHB sharpen the **leading** read ahead of the cycle; Chicago PMI front-runs the national [[Leading Indicators|ISM/PMI]]; Personal Income & PCE and the Current Account are **coincident/confirmation**. They complement the live [[Business Cycle Dashboard - Live (June 2026)]] (esp. the Leading and Liquidity pillars).

## Build / refresh
`python tools/build_new_indicators.py` — re-pulls FRED and rebuilds the workbook (web values are static recent-quarter snapshots). The 3 catalog-only series need a licensed feed.

## See also
- [[Leading Indicators]] · [[Coincident Indicators]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[The Global Macros Framework]] · [[index]] · [[log]]
