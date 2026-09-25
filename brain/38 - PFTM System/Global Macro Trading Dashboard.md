---
title: Global Macro Trading Dashboard
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "The skill file's 4 modules (Big-Four scorecard, cross-asset matrix, Keltner/ATR technicals, 1% risk) on 2026 Excel + COT; re-checked 2026-09-19: engine back to Reflation/Overheating, US +3, 3 TAKE."
tags: [global-macro, strategy, pftm, skill-file, scorecard, cross-asset, technical, risk, indexes, fx, commodities, excel-data, decision-support]
data_vintage: "SNAPSHOT 2026-06-26 (US macro: 2026 Excel workbooks; COT: CFTC; prices: Yahoo) — regime re-checked 2026-09-19 against the dashboard rebuilt that day (COT positions 2026-09-15; endo Excel inputs pre-date the 2026-09-17 Fed hike)"
sources: 1
updated: 2026-09-19
---

# Global Macro Trading Dashboard

> ### Regime re-checked — 2026-09-19 (current; supersedes the 2026-08-15 check below)
>
> The engine has returned to the reflation quadrant. `Macro COT Trades/macrocot_latest.json` (`as_of` **2026-09-19**, built
> 15:36; CFTC positions as of **2026-09-15**) reports `state = "Mildly Inflationary"`, `quadrant = "Reflation / Overheating"`,
> `growth = +0.56`, `inflation = +0.89`, `rr_falling = false`. The label this page uses matches the engine again, so the
> 2026-08-15 "Stagflation" reading below is superseded. The dashboard as rendered today shows Module 1 as **GDP 0, CPI +1,
> Rates +1 (Fed Funds ↑ · 10Y ↑), Employment +1 → US net +3 (Strong)**. That supersedes Module 1's "Current" line, which
> had GDP +1 and Rates 0. The book is **3 TAKE (2 long / 1 short): short USD/JPY, long WTI, long Dow, all HIGH; 10 WATCH;
> Gold and Silver stand aside; $3,000 at risk, $4,823 margin (4.8%)**, which supersedes the 2026-07-01 book below. The three
> TAKEs are three distinct themes (USD, global growth, risk), with no correlation cluster. Only WTI's technical is aligned.
> USD/JPY and the Dow both show "await trigger", and the Dow's daily trend is DOWN, so the engine takes it on conviction alone.
> **Caveat:** the endo's Excel inputs lag the policy move. Its Fed Funds row still reads 3.63%, from before the hike. The Fed
> raised 25bp to **3.75–4.00%**, effective 2026-09-17 (EFFR 3.88% on 17 Sep). The ECB deposit rate rose to **2.50%**,
> effective 2026-09-16.
> **Backdrop:** both major central banks tightened in the same week that the energy shock re-intensified. The Fed's first
> hike and the ECB's second move came as WTI rose to $107 and Brent to $131 (15 Sep), with August PPI at +9.85% y/y. Demand
> is firm, not fading: retail sales +1.24% m/m, payrolls +162k, claims 196k. Core CPI is still only +2.45% y/y. Its 3-month
> pace turned up to 1.97% from 1.64% but remains below 2%, while core PCE is 3.34% (Jul). The curve flattened (10Y-2Y +0.33 →
> +0.25), and markets absorbed the hike: credit had already retraced on 16 Sep (HY 2.70, CCC 10.76), and VIX fell to 15.4 on
> hike day.

> ### ⚠️ Regime label superseded — re-checked 2026-08-15
>
> This page calls the regime **"Mildly Inflationary / Reflation-Overheating"**. The project's own engine
> (`Macro COT Trades/macrocot_latest.json`, `as_of` **2026-08-15**) now reports the same *state* but a
> **different quadrant**: `quadrant = "Stagflation"`, `growth = -0.13`, `inflation = +2.01`, `rr_falling = true`.
> Growth has crossed below zero since this was written, moving the call out of the reflation quadrant.
> The trade table below was derived under the reflation read and should be re-derived before use.


The **`Global Macro Trading Strategy.md` skill file** turned into ONE actionable surface across **indexes, major FX
pairs and commodities**, driven by the user's 2026 Excel data. Built 2026-06-26 ("build a global macro trading
dashboard based on the skill + all the Excel info, with charts/trends/patterns, to take actionable trades").

> **Decision-support / education only — NOT investment advice.** Account ($100k) & risk %s are illustrative.

## The four modules (exactly the skill file)
1. **Macroeconomic Scorecard** — the US economy scored on the skill's Big-Four (**GDP · CPI · Rates · Employment**)
   as **+1 / 0 / −1** → a net score, mapped from the trend-aware 2026 endo ([[PTM Endo Scorecard (2026 Excel Data)]]).
   *At the 2026-06-26 build (superseded — see the 2026-09-19 banner above): GDP +1, CPI +1, Rates 0 (Fed Funds ↓ vs 10Y ↑), Employment +1 → **US net +3 (Strong)**; regime Mildly
   Inflationary / Reflation-Overheating.*
- **1b · Global Growth (cross-country)** — Services/official **PMI for 11 countries** (US/EZ/UK/JP/AU + DE/FR/IT/ES/CH
   + China) from the **current 2026 Excel** (Global Services PMI + China PMI): expansion/contraction, the mean-PMI /
   %-expanding read, and **US-relative** PMI. *Current (`globalgrowth_latest.json`, built 2026-09-19): US 50.7 (May-26),
   JP 50.0 (May-26) (exp); China 49.8 (Aug-26), UK 48.8 (Jun-26), EZ 47.7 (May-26), AU 43.6 (Oct-14)(con) → mean 50.3, 55%
   expanding, US-relative +0.5, global growth "stalling". ⚠ The mean and the share include six Services PMIs (DE, FR, IT,
   ES, CH and AU) whose last print is **2014-10**. On the five 2026-dated prints alone the read is 49.4 mean and 40% expanding,
   as the 2026-09-11 audit found. This supersedes the 2026-08-15 readings, which are listed in [[log]].* Feeds Module 2's "global PMI ≥ 50 → risk-on
   + oil/copper demand" and the long-USD tilt. `tools/global_growth.py`. (Growth read only — no full Big-Four
   CPI/Rates/Employment for EZ/UK/JP/AU in the folder; Global *Manufacturing* PMIs are 2017-stale, excluded.)
2. **Cross-Asset Matrix** — the fundamental bias applied to each instrument: indexes (risk-on/off), FX (divergence /
   COT-led), gold (real rates), oil/copper (PMI + USD). A bias × conviction table + signed bias bar.
3. **Technical Execution** — daily trend, Keltner trigger, ATR%, and **entry / stop (2·ATR) / target (2R)** per
   actionable instrument; the skill's rule enforced: *don't enter unless the technical aligns with the macro bias.*
4. **Risk & Portfolio** — 1% conviction-scaled sizing (HIGH 1.0 / MED 0.6 / LOW 0.3%), 2×ATR stops, and
   **correlation clustering** (same-USD / same-real-rate trades sized as one — the skill's non-negotiable rule).
   The **actionable tickets** (entry/stop/target/R:R/size) for the TAKE-grade setups.

## Current actionable book (snapshot 2026-07-01 — regenerated every refresh; the dashboard is the live source)
**11 TAKE (10 long / 1 short), 3 WATCH; gross margin $16,714 (16.7%).** HIGH: Silver, WTI. The book expanded (5 → 11)
because positioning went **broadly extreme-short** (WTI p6, NASDAQ p9, NZD p4, GBP p5, CAD p6…) → contrarian-longs
fire across FX & indexes; **USD/CAD flipped to SHORT**; Gold (p95) & Copper (p97) crowded → trimmed.
**⚠ Concentration:** 5 of 11 TAKEs are the **USD** theme — one bet split five ways; per the skill, take the
single largest-divergence leg per cluster (effective book ≈ 4 distinct bets, 10-long/1-short). *Numbers drift each
refresh — open the dashboard for the live state.*

## Build
- **`tools/gm_trading_dashboard.py`** renders the dashboard from the two audited engine outputs:
  `Endo Excel/endoexcel_latest.json` (the US scorecard, from Excel) + `Macro COT Trades/macrocot_latest.json` (the
  trades). **`tools/build_gm_dashboard.py`** refreshes the endo then renders. Output:
  **`Global Macro Trading Dashboard/Global Macro Trading Dashboard.html`**.
- **Theme:** light page / dark charts (the user's chosen finance look), instant (animation-off) Chart.js.
- No new trade logic — the actionable tickets are the **adversarially-audited** Macro+COT engine's TAKE trades shown
  verbatim; Module 1 is a faithful re-mapping of the audited endo into the skill's Big-Four format.

## Data provenance
US fundamentals = your 2026 Excel workbooks (the folder is US-rich; it now also has EU sentiment + China PMI +
updated COT/commodity-price/volatility files, available for a future cross-country extension). Positioning = live
CFTC COT. Prices/technicals = live Yahoo. The FX layer is COT-led because the Excel is US-only for the Big-Four (no
relative-endo FX bias) — stated openly.

## Caveats
Snapshot decision-support, **not a backtest** — no performance claim. US-only macro; FX COT-led. Account/risk
illustrative. **Not investment advice.**

## Related
[[2026 Trading System — Operating Manual]] (the full map / start-here) · [[Macro + COT Trade Signals]] · [[PTM Endo Scorecard (2026 Excel Data)]] · [[Dynamic Macro Panel]] · [[Macro Indicators Hub]] · [[PFTM Full Trading System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
