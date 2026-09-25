---
title: PFTM Full Trading System
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "The complete Anton Kreil PFTM workflow on 2026 Excel + live prices/COT: scorecard, Gate Keeping, ATR rankings, Kelly-capped sizing; 2026-09-19 gate: 4 DEPLOY (commodity longs), 5 WATCH (Gold, long-USD FX), 3 STAND-ASIDE."
tags: [global-macro, strategy, pftm, anton-kreil, fx, indexes, commodities, gate-keeping, risk-management, kelly, position-sizing, excel-data, decision-support]
data_vintage: "MACRO: user 2026 Excel workbooks (2.8 Macro Indicators) · PRICES/ATR: live Yahoo · COT: live CFTC"
sources: 1
updated: 2026-09-19
---

# PFTM Full Trading System — Indexes · FX · Commodities

The complete **Anton Kreil "Professional Forex Trading Masterclass" (PFTM)** workflow, built faithfully from the
course's own Excel templates (the `.mp4` lessons are unwatchable, but every lesson ships an Excel sheet that *is*
its deliverable). It chains the macro scorecard into a disciplined, sized, gated trading process across **indexes,
FX pairs and commodities**, and — per the user's instruction — runs the **macro engine on the user's own
updated-to-2026 Excel data**. Built / extended 2026-06-25.

> **Decision-support / education only — NOT investment advice.** Account size, leverage and the Kelly/stats inputs
> are illustrative templates to replace with your own.

## The five-stage workflow (mapped to the course Excel sheets)
1. **Macro scorecard** (Drivers 1–10 → `Endogenous_Driver_Analysis`, `Endo_Exo_Analysis`) — the **endo** bias per
   country/instrument. Now scored from the user's **2026 Excel workbooks** (see [[PTM Endo Scorecard (2026 Excel Data)]]).
2. **Gate Keeping** (V22–24 *Deploying Capital*; `Price_Action_Watchlist`) — per instrument: **DEPLOY / WATCH /
   STAND-ASIDE**. DEPLOY = macro bias ≠ neutral **and** the daily technical is aligned; WATCH = macro edge but the
   technical hasn't triggered; STAND-ASIDE = no fundamental edge. Carries **entry / stop / target** (Keltner edge,
   2·ATR stop, 2R target).
3. **ATR Rankings** (V25 `ATR_Rankings`) — **1-year-average** daily/weekly/monthly ATR% for the tradable universe,
   ranked, with the course's **Avg-Commodity vs Avg-ex-Commodity** benchmark rows. Commodities run several× FX/index
   volatility, so equal-risk sizing means much smaller commodity notionals.
4. **Position sizing** (V26 `Exposure_Margin` + V27 `Kelly_Criterion`) — **fixed-fractional** (1% risk / displayed
   stop) as the floor; **Kelly** (f\* = W − (1−W)/R) as a **per-trade risk CEILING capped at 2%** (do-not-exceed);
   **margin = notional / leverage** (FX 30:1, Index 20:1, Commodity 10:1); aggregate exposure + correlation-theme caps.
5. **Self-Awareness Statistics** (V28 `Portfolio Performance Statistics`) — the discipline tracker: **Sharpe /
   Sortino / Calmar**, win-rate, profit factor, expectancy (R), and the empirical Kelly. A template to populate with
   your own fills.

## Outputs
- **`PFTM System/PFTM System Dashboard.html`** — the full system (regime → gate-keeping table → ATR rankings →
  sizing → self-awareness stats), light theme, Chart.js inlined. `tools/pftm_system.py` · `pftm_system_report.py` ·
  `build_pftm_system.py`. JSON: `pftmsystem_latest.json`.
- **`Endo Excel/PTM Endo Scorecard (2026 Excel Data).html`** — the macro core from the user's 2026 workbooks.
  `tools/xl_macro.py` · `xl_macro_report.py` · `build_endo_xl.py`. JSON: `endoexcel_latest.json`.
- Built on [[PTM Global-Macro Dashboard (Endo + Exo)]] (folder 36) and [[PFTM Global-Macro Execution Strategy]] (37).

## Live read — 2026-09-19 (current)
*Supersedes "Live read — 2026-09-11" below, which stays as the dated record. One vintage this time: the regime header,
gate, entries and sizing all come from builds run 2026-09-19 (`pftmsystem_latest.json` 15:36, `ptmstrategy_latest.json`
15:35, Excel endo `endoexcel_latest.json` 15:47), with ATR re-fetched from Yahoo at the 15:36 build. The macro backdrop
line is the verified FRED/ECB snapshot for 19 Sep, not a dashboard output.*
- **Macro backdrop: both major central banks tightened in the same week the energy shock re-intensified.** The Fed's
  first hike of the cycle, +25bp to **3.75–4.00%** (effective 17 Sep; EFFR 3.88% on 17 Sep, 3.63% through 16 Sep), and
  the ECB's second move, deposit rate **2.25% → 2.50%** (effective 16 Sep), came as WTI rose to $107.02 and Brent to
  $130.80 (15 Sep), with August PPI at +9.85% y/y. Demand is firm, not fading: retail sales +1.24% m/m and payrolls
  +162k (Aug), claims 196k (week of 12 Sep). Core CPI is still only +2.45% y/y (Aug); its 3-month annualised pace turned
  up to 1.97% from 1.64% in July but remains below 2%, while core PCE is +3.34% (Jul). The curve flattened (10Y–2Y +0.33
  on 15 Sep → +0.25 on 18 Sep), and markets absorbed the hike: credit had already retraced on 16 Sep (HY OAS 2.70, CCC
  10.76) and VIX fell to 15.44 on hike day.
- **Regime (2026 Excel endo, rebuilt today): Mildly Inflationary · Reflation / Overheating**, endo +12.9/±190 (level
  +9.2), 19/19 drivers (10 rising, 9 falling), growth axis +0.56, inflation axis +0.89: identical to 2026-09-11, because
  the workbooks it reads have not yet taken in the August CPI/PPI prints or the hike (see driver prints). Risk regime
  **NEUTRAL** (2026-09-11: RISK-ON); the live-FRED PTM engine reads equities "neutral / mixed" (global-growth score 0.0).
  The FRED-backed US Endogenous template, recalculated today, carries the same label: +19 'Mildly Inflationary' (was +9
  'Neutral / Balanced' on 2026-09-09), with Inflation at +4 (was −12).
- **Gate keeping (2026-09-19): 4 DEPLOY, 5 WATCH, 3 STAND-ASIDE.** DEPLOY: WTI, Copper, Silver and Natural Gas, all
  commodity longs with macro and daily technical aligned (trend UP). WATCH: **Gold long, down from DEPLOY on 2026-09-08**
  (daily trend now RANGE), plus the four long-USD FX trades (short GBP/USD, EUR/USD, AUD/USD; long USD/JPY), all RANGE
  and awaiting the trigger. STAND-ASIDE: S&P 500, NASDAQ 100, Dow (neutral bias; the Dow's daily trend is DOWN). The
  intervening 2026-09-16 build had Gold, Copper and Silver at WATCH; Copper and Silver have re-triggered since.
- **⚠ Cross-engine check:** the [[Macro + COT Trade Signals]] engine, rebuilt today (CFTC positions as of 2026-09-15),
  confirms only **WTI** among these DEPLOYs (HIGH-conviction TAKE; specs at the 8th percentile, a contrarian tailwind).
  It holds Copper at WATCH as crowded (96th percentile), Natural Gas at WATCH (COT mildly opposed), and stands aside on
  Gold and Silver (inflation +0.89 with real rates not falling). It also **opposes** this system on two rows: it takes
  **short USD/JPY** where the gate here watches long USD/JPY, and a **Dow long** where the gate stands aside.
- **Correlation caps (unchanged):** 4 trades share the long-USD theme, 3 global-growth (WTI, Copper, Natural Gas), 2
  real-rate (Gold, Silver). Each cluster is one correlated bet: cap combined risk and lead with one.
- **ATR rankings (1yr avg, daily, fetched 2026-09-19):** Natural Gas 7.8% · Silver 4.9% · WTI 4.1% · Gold 2.8% · Copper
  1.8% · NASDAQ 1.5% · Dow 1.1% · S&P 1.0%; **Avg-Commodity 4.26% vs Avg-ex-Commodity 0.85%** (≈5×).
- **Sizing (illustrative $100k, 1% / 2%-Kelly-cap; stops from today's gate):** gross margin **$21,069 (21.1% of
  account)** across 9 sized rows (4 DEPLOY + 5 WATCH), from ≈$22.7k. WTI long (DEPLOY): stop 8.83%, fixed-frac notional
  $11,320, Kelly ceiling $22,639 (2.0%), margin $1,132 at 10:1. Gold long (now WATCH): stop 4.79%, notional ≈$20.9k,
  ceiling ≈$41.7k. EUR/USD short (WATCH): stop 0.84%, notional ≈$119.5k, ceiling ≈$238.9k.
- **Self-awareness: unchanged illustrative template, NOT performance.** Kelly W 0.60, R 1.72 → f\* 0.367 (quarter-Kelly
  0.092); Sharpe 1.45, Sortino 2.27, Calmar 6.37, max DD −2.0%, CAGR 12.7% (n=24 weekly), all from the hard-coded
  demonstration path and example trade log in `pftm_system.py`, not from fills.
- **Driver prints (Excel endo, rebuilt today; unchanged from 2026-09-11):** CPI 3.3% YoY (Jul), Core 2.47% (Jul), PCE
  3.7% (Jul), PPI 5.51% (Jul), ISM mfg 54.62 (Aug) / svcs 54.1 (Jul), unemployment 4.1% (Aug), Fed Funds 3.63% (the
  pre-hike rate), 10Y 4.78%, M2 +5.41% (Jul), claims 206k, U-Mich 51.7 (Aug). **They lag the verified data:** August CPI
  is +3.35% and core +2.45%; claims were 196k (week of 12 Sep); the Fed target is now 3.75–4.00% (EFFR 3.88%, 17 Sep);
  the 10Y was 4.94% (17 Sep). The workbook's July PPI (5.51%) also disagrees with FRED's all-commodities July print
  (+8.70%; August +9.85%), unresolved. The +12.9 score therefore does not yet include the August inflation data or the hike.

## Live read — 2026-09-11
*Supersedes the "Current read (2026-06-25)" below, which stays as the dated record. Mixed vintages: the regime header is
`pftmsystem_latest.json` rebuilt 2026-09-11 09:16 on the repaired Excel endo (19 of 19 drivers); the gate, entries and
sizing come from `ptmstrategy_latest.json` (live-FRED macro, built 2026-09-08 09:31), so they are a 2026-09-08 read; the
ATR rankings were re-fetched from Yahoo at the 2026-09-11 build.*
- **Regime (rebuilt 2026 Excel endo): Mildly Inflationary · Reflation / Overheating**. Endo +12.9/±190 (level score
  +9.2), 19 drivers (10 rising, 9 falling); growth axis +0.56, inflation axis +0.89. Same label as June (+15.2 → +12.9,
  both axes a little softer). Risk regime **RISK-ON** (June: NEUTRAL).
- **The 2026-09-08 build's regime header was an artefact.** It printed `endo_state` "Strongly Inflationary" with
  `endo_total` 0 because the Excel endo loaded 0 of 19 drivers after the workbooks were moved. The 2026-09-11 rebuild
  carries the +12.9 read. The gate was never affected: its biases come from the live-FRED PTM engine, not the Excel endo.
- **Gate keeping (2026-09-08). Flag: the deployable book has flipped since June.** 5 **DEPLOY**, all commodity longs (Gold,
  WTI, Copper, Silver, plus newly listed Natural Gas; macro + daily technical aligned); 4 **WATCH**, all FX on a long-USD
  bias awaiting the trigger (short GBP/USD, EUR/USD, AUD/USD; long USD/JPY); 3 **STAND-ASIDE** (S&P 500, NASDAQ 100,
  Dow; neutral bias). June's two DEPLOYs (EUR/USD & GBP/USD shorts) are now WATCH (daily trend UP, against the short);
  June's four commodity WATCHes are now DEPLOY; AUD/USD and USD/JPY moved from STAND-ASIDE to WATCH.
- **⚠ Cross-engine check:** the [[Macro + COT Trade Signals]] engine, rebuilt 2026-09-11 on the Excel endo plus COT,
  takes only WTI Crude and Dow Jones longs and stands aside on Gold and Silver (inflation +0.89 with real rates not
  falling). The two engines read different macro inputs, so the Gold and Silver DEPLOYs here are not confirmed by the
  COT engine.
- **Correlation caps:** 4 trades share the long-USD theme, 3 global-growth (WTI, Copper, Natural Gas), 2 real-rate (Gold,
  Silver). Each cluster is one correlated bet: cap combined risk and lead with one.
- **ATR rankings (1yr avg, daily, fetched 2026-09-11):** Natural Gas 8.0% · Silver 5.0% · WTI 3.9% · Gold 2.1% · Copper 1.8%
  · NASDAQ 1.5% · Dow 1.1% · S&P 1.0%; **Avg-Commodity 4.17% vs Avg-ex-Commodity 0.85%** (≈5×). The higher commodity
  average is Natural Gas joining the basket; the four June commodities alone average ≈3.2%, below June's 3.61%.
- **Sizing (illustrative $100k, 1% / 2%-Kelly-cap; stops from the 2026-09-08 gate):** gross margin ≈$22.7k (22.7% of account) across 9 sized rows
  (5 DEPLOY + 4 WATCH), up from ≈$13k. Gold long (DEPLOY): stop 3.63%, fixed-frac notional ≈$27.6k, Kelly ceiling
  ≈$55.1k (2.0%), margin ≈$2.8k at 10:1. EUR/USD short (now WATCH): stop 0.83%, notional ≈$119.9k, ceiling ≈$239.7k.
- **Self-awareness: unchanged illustrative template, NOT new performance.** Kelly W 0.60, R 1.72 → f\* 0.367
  (quarter-Kelly 0.092); Sharpe 1.45, Sortino 2.27, Calmar 6.37, max DD −2.0%, CAGR 12.7% (n=24 weekly). Identical to
  June because they come from a hard-coded demonstration equity path and example trade log (n=20) in
  `pftm_system.py`, not from any fills.
- **Driver prints (rebuilt Excel; latest obs Jul–Sep 2026):** CPI 3.3% YoY, Core 2.47%, PCE 3.7%, PPI 5.51%, ISM mfg
  54.62 / svcs 54.1, unemployment 4.1%, Fed Funds 3.63%, 10Y 4.78%, M2 +5.41%, claims 206k, U-Mich 51.7. CPI, Core,
  PCE, unemployment and Fed Funds match the 2026-09-08 FRED snapshot. These supersede the June build-snapshot prints
  under Data provenance.

## Current read (2026-06-25)
- **Regime (from your 2026 Excel data): Mildly Inflationary · Reflation / Overheating** (endo +15.2/±190; growth
  axis +0.61, inflation axis +1.13). Risk regime NEUTRAL.
- **Gate keeping:** 2 **DEPLOY** (EUR/USD & GBP/USD shorts — macro + daily technical aligned), 4 **WATCH** (Gold,
  WTI, Copper, Silver long on macro but awaiting the technical trigger), 5 **STAND-ASIDE** (AUD/USD, USD/JPY,
  the three US indexes — neutral macro bias).
- **ATR rankings (1yr avg, daily):** Silver 5.2% · WTI 5.1% · Gold 2.1% · Copper 2.0% · NASDAQ 1.3% · S&P 1.0%;
  **Avg-Commodity 3.61% vs Avg-ex-Commodity 0.85%** (commodities ≈4× FX/index vol).
- **Sizing (illustrative $100k, 1% / 2%-Kelly-cap):** gross margin ≈$13k (≈13% of account). EUR/USD short: stop
  1.26%, fixed-frac notional ≈$79k, Kelly ceiling ≈$158k (2.0%).
- **Self-awareness (illustrative):** Kelly W 0.60, R 1.72 → f\* 0.367; Sharpe 1.45, Sortino 2.27, Calmar 6.37.

## Data provenance (honest)
- **Macro (endo): the user's 2026 Excel workbooks** in `raw/2. Macro Indicators/2.8 Updated Detailed Macro
  Indicators/` — 19 US drivers read live from the sheets (CPI 4.17% YoY, Core 2.82%, PCE 3.77%, PPI 13.1%, ISM
  mfg 54.0 / svcs 54.5 *(build snapshot; ISM mfg Jun-26 print: 53.3)*, unemployment 4.3%, Fed Funds 3.62%, 10Y 4.55%, M2 +5.4%, plus retail/IP/durables/permits/
  NFIB/claims/U-Mich/GDP). Cross-validates the live-FRED endo (same regime).
  *Note 2026-09-11: the driver prints above are the 2026-06-25 build snapshot; the rebuilt read (19/19 drivers, as of
  2026-09-11) is under "Live read — 2026-09-11 (current)".*
  *Note 2026-09-19: the latest rebuild is under "Live read — 2026-09-19 (current)"; its Excel driver prints are
  unchanged from 2026-09-11 and lag the verified August data.*

- **Prices / ATR / relative-FX / COT positioning: live** (Yahoo + CFTC). The folder's **price & volatility
  workbooks are 2013–2015 vintage** (the Comm-Float volatility sheets end Mar-2015; the FX/index COT analysis files
  are 2013), and the cross-country survey files (China/global PMI, ESI) are 2014–2021 — so only the **US
  macro-indicator** workbooks were updated to 2026. Using live market data there is the honest choice.

## Audit (up front, lean — 9 agents, 3 lenses → refuter → synthesis)
**Verdict: SOUND_WITH_FIXES.** The Kelly formula and the long/short stop–target **sign geometry** were verified
**correct**. Five findings confirmed and **all fixed**:
- **HIGH — sizing/stop ATR mismatch (L1-01):** the "1% risk" notional was sized off the Yahoo daily ATR while the
  *displayed* stop used a different (ptm_strategy) ATR, so the position wouldn't lose exactly 1% at the shown stop.
  **Fixed:** size off the actual displayed `(entry − stop)` distance, so a stop-out loses exactly 1%.
- **MED — Kelly notional was a 9.2× leverage multiple (L1-02):** `kelly_notional` reused the fixed-fractional
  formula with the 9.2% quarter-Kelly fraction → ≈$780k on a $100k account, nonsensical as a position size.
  **Fixed:** the Kelly column is now a per-trade **risk CEILING capped at 2%** (do-not-exceed), ≈2× the 1% floor.
- **LOW — Kelly fallback / empty-log handling (L1-03):** now returns `—` (not a silent mirror of the 1% number)
  when the trade log is empty or the edge is non-positive.
- **LOW — Sortino convention (L3-1):** downside deviation now uses the textbook RMS of `min(r,0)` over **all**
  periods (was the std of only-negative returns, which inflated Sortino 3.0 → corrected 2.27); rf=0 documented.
- **LOW — ATR window label (L3-2):** ATR rankings now use a **1-year window** per timeframe to match the template's
  "1yr Average" columns (was a fixed 14-period window mislabeled as a 1-yr average).

## Caveats
- Snapshot decision-support, not a backtest (no performance claim). Macro = US endo only (the rich data the user
  updated); relative-FX/exo and prices are live. Account/leverage/Kelly inputs illustrative. The endo z-scores use
  each series' full Excel history (incl. the high-inflation 1970s–80s), which can make current readings look low
  vs history. **Not investment advice.**

## Related
[[PTM Endo Scorecard (2026 Excel Data)]] · [[PTM Global-Macro Dashboard (Endo + Exo)]] · [[PFTM Global-Macro Execution Strategy]] · [[The Global Macros Framework]] · [[Cross-System Synthesis — What Works]] · [[the-dv01-both-legs-flattener-bug]] · [[Analyst System — Live Cockpit (June 2026)]]
