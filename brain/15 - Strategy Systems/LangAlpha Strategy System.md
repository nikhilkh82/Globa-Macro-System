---
title: LangAlpha Strategy System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: Deterministic cross-asset RV engine (19 majors; trend/macro/carry/COT/value) ranking longs/shorts and 13 pair ideas — the audited point-in-time backtest still shows no cross-sectional edge (Sharpe −0.15, IC ≈ 0).
tags: [global-macro, strategy, langalpha, relative-value, cross-asset, signals]
data_vintage: "LIVE signals re-run 2026-09-24 (FRED + CFTC COT + PTM scorecards) · point-in-time backtest 2013-02→2026-05 (160 months), re-run 2026-09-24"
sources: 1
updated: 2026-09-25
---

# LangAlpha Strategy System

A **cross-asset relative-value signal engine** that adapts the [LangAlpha](../../raw/11.%20Strategies/LangAlpha-main/) idea-generation methodology to the Global Macro Brain's own live data. Built 2026-06-22. It turns the firehose of FRED + CFTC COT + the PTM endo/exo scorecards into a small, ranked set of **long/short trade ideas** with conviction, suggested sizing, an explicit thesis, and the conditions that would invalidate it — and it tracks how those signals evolve run-over-run.

> Research/education only — not investment advice. See the disclaimer at the foot of every generated note.

## Provenance — what we adapted, and what we didn't

[LangAlpha](../../raw/11.%20Strategies/LangAlpha-main/) (the open-source *Ginlix* platform) is a full production application: a LangGraph research agent with sandboxed Programmatic Tool Calling, MCP financial-data servers, a FastAPI backend, a React web workbench, Postgres/Redis, and Docker orchestration (1,895 files). Its headline deliverable is **AI-generated long/short pair-trade ideas calibrated to your book**, produced by an LLM that screens markets and compounds research in a persistent workspace.

We did **not** stand up that platform (it needs Docker, cloud sandboxes, LLM keys, and hosted services that aren't available on this machine). Instead we extracted its *method* — multi-factor screen → ranked long/short ideas → conviction → risks → calibrate-to-book → track over time — and re-implemented it as a **deterministic, no-LLM, no-cloud engine** wired to the data we already have working ([[Endo-Exo Toolkit & Workflow]], the FRED dataset, and the [[Commitment of Traders (COT)]] feed). The LangAlpha `idea-generation` skill is equity single-name screening; our universe is macro/cross-asset, so the adaptation is a **cross-asset RV** engine rather than a stock screener.

## How it works

### 1. Instrument universe (19 — major indexes, FX majors, commodities)
The universe is the liquid macro "majors". Each instrument maps to a FRED price series, an optional CFTC COT contract, and a *direction transform* so that "bullish" always means the instrument as named:

| Class | Instruments |
|---|---|
| Equity indexes | S&P 500, Nasdaq 100, Dow Jones (US, daily) · DAX, Nikkei, FTSE (OECD monthly share-price indices) |
| FX majors | EUR/USD, GBP/USD, AUD/USD, NZD/USD, USD/JPY, USD/CHF, USD/CAD, broad USD (DXY) |
| Commodities | WTI, Brent, Natural gas, Copper, Gold |

FX pairs use conventional quoting (EUR/USD, GBP/USD, AUD/USD, NZD/USD have USD as quote → "up = long the pair"; USD/JPY, USD/CHF, USD/CAD have USD as base). CFTC futures are always the *foreign* currency vs USD, so for USD/x pairs COT-long-foreign is the opposite direction (handled by an `aligned=False` flag). Gold uses FRED `IR14270` (Import Price Index: Nonmonetary Gold, Dec-2024=100) as a spot proxy — the London bullion fixes were discontinued on FRED; scale-invariant z-scores make an index level fine. No free FRED price exists for **silver** or **Russell 2000**, and DAX/Nikkei/FTSE are monthly OECD indices (lagged). Brent/Copper and the international indexes have no COT (positioning renormalised out). *(Rates and credit are no longer tradeables — they still feed the macro-regime factor internally.)*

### 2. Five transparent factors (each bounded to −100…+100 via `tanh`)
- **Trend (34%)** — z-scored 6-month bullish return + position vs the long moving average.
- **Macro (26%)** — regime tilt from CPI level/acceleration, industrial-production YoY, the risk regime (VIX percentile + HY OAS direction), USD trend, and real-rate direction. FX uses a **per-currency strength model** (a pair tilt = base-currency strength − quote-currency strength), plus the **PTM endo** overlay (inflationary regime → +commodities, +broad USD).
- **Carry (15%)** — FX same-tenor (10Y) rate differential in the pair's direction (foreign − US for FOR/USD pairs; US − foreign for USD/FOR pairs). Non-FX instruments carry no carry factor (renormalised out).
- **Positioning (15%, contrarian)** — CFTC COT *Flip* z-score; crowded longs read bearish.
- **Value (10%, contrarian)** — multi-year mean-reversion; rich screens bearish.

The **composite** is the weighted blend over whatever factors are available (weights renormalise when a factor is missing).

### 3. Ideas
- **Directional screen** — every instrument ranked by composite; the top/bottom become candidate longs/shorts.
- **Relative-value pairs** — **thirteen** economically-linked pairs (the `PAIRS` list in `langalpha_strategy.py`: Gold vs S&P, Gold vs Copper, WTI vs Nat gas, Brent vs WTI, Nasdaq vs S&P, S&P vs Dow, S&P vs DAX, Nikkei vs DAX, EUR/USD vs GBP/USD, EUR/USD vs USD/JPY, USD/JPY vs USD/CHF, AUD/USD vs NZD/USD, AUD/USD vs broad USD); the engine goes **long the higher-composite leg, short the lower**, vol-balanced. Yield/spread legs are converted to a *price-equivalent* vol (via approximate duration) so a bond leg and an equity leg can be sized on the same footing; the pair's estimated vol uses the legs' realised correlation.
- **Conviction** (High/Med/Low) rises with the composite spread, factor agreement across the two legs, and positioning confirmation.
- **Thesis & risks** are auto-generated from which factors drive the spread and which disagree ("what would make this wrong").
- **Calibrate-to-book** — drop a `LangAlpha Strategy/book.json` of current exposures and each idea is flagged as adding-to / diversifying-against the book.

### 4. Compounding
Every run writes a snapshot (`history/<date>.json`) and appends `signals_history.csv`, so the dashboard plots each instrument's composite **over time** and the notes show the week-over-week conviction delta — the "research compounds" idea, made quantitative.

## Outputs (`LangAlpha Strategy/`)
- **`LangAlpha Strategy.html`** — self-contained interactive dashboard (light theme, Chart.js inlined → works offline): regime banner, ranked idea cards, directional long/short tables, composite-alpha bar, factor heatmap, and a **5-year point-in-time composite-history chart** (leaders vs laggards, computed monthly by re-running the model with data truncated to each past date).
- **`LangAlpha Ideas <date>.md`** — the strategy note (regime, ranked pairs, top-idea detail, directional screen, methodology). Latest: **`LangAlpha Ideas 2026-09-24.md`**.
- **`ideas_<date>.json`** — machine-readable (latest `ideas_2026-09-24.json`, `as_of` 2026-09-24).
- **`backtest.json`** / **`experiments.json`** — the Track-record panel's inputs; both re-run 2026-09-24 (see *Run it*).

## Run it
```
python tools/build_langalpha_strategy.py
```
Modules: `tools/langalpha_strategy.py` (engine) · `tools/langalpha_report.py` (HTML+MD) · `tools/build_langalpha_strategy.py` (orchestrator) · `tools/langalpha_backtest.py` (point-in-time backtest → `backtest.json`, rendered as the Track record panel) · `tools/langalpha_experiments.py` (factor-weighting variants → `experiments.json`). Reuses `tools/fred.py` + `tools/cot.py`.

**The last two are not in any refresh chain.** `build_langalpha_strategy.py` runs on the normal refresh and regenerates the signals, the ideas note and the dashboard; `langalpha_backtest.py` and `langalpha_experiments.py` must be invoked by hand. They were last run **2026-09-24** (before that, June) — if the Track-record panel ever looks frozen relative to the rest of the page, this is why.

## Snapshot — 2026-09-24 (live, 19 majors)
*Supersedes the 2026-06-22 snapshot below, which is kept as the record. Source: `LangAlpha Strategy/ideas_2026-09-24.json` (`as_of` 2026-09-24, `generated` 2026-09-24 16:18) and the companion note `LangAlpha Ideas 2026-09-24.md`.*

Regime: **risk-on** (`regime.risk_on` true), CPI YoY **+3.4%**, IndProd YoY **+1.4%**, VIX **28th percentile**, PTM endo **+19 (Mildly Inflationary)**, PTM exo **+2 — "NEUTRAL AUD/USD"**.

Both PTM overlays moved on this run, and both are read from a **recalculated** `scores_cache.json` (2026-09-24) — the Excel endo/exo templates were rebuilt and recalculated the same afternoon, so this is the first run since early September that is not re-using a frozen pair. Across the three preceding runs (`ideas_2026-09-07`, `09-08`, `09-16`) the overlay read **+9 / −2** every time; it now reads **+19 / +2**:
- **PTM endo +9 → +19**, and the state crosses back from **"Neutral / Balanced" to "Mildly Inflationary"** (it was +27 at the June snapshot below). The Excel category split behind it is Sovereign & BS **+21** carrying the whole score against Leading Surveys **−4**, Money **−2**, Employment **−2**, Rates **+2**, Inflation **+4**.
- **PTM exo has flipped sign: −2 → +2.** The label stays **"NEUTRAL AUD/USD"**, but the tilt no longer leans against the Aussie — it had read −2 on every run since 2026-07-23, and −6 / "SHORT AUD/USD" back in June. *(The Workbook Explorer's AUD/USD exo **card** is a different engine from this Excel template and disagrees in sign; it is also computed from the older of two copies of `39. Exogenous_AUD_USD.xlsx`. Do not reconcile the two numbers — see the Explorer's own page.)*

Composite dispersion is wider than in June, which ran **+68 to −15** (`ideas_2026-06-22.json`: WTI 68.4 at the top, EUR/USD −14.8 at the bottom); this run spans **+52 to −64** — the widening is entirely at the *bottom* of the book (Gold −64), while the top of the book is *lower* than June's (+52 vs WTI +68). Leaders: **WTI +52, S&P 500 +52, Brent +49, Nikkei +49, Copper +42, Nasdaq +42, FTSE +39, Dow +39, USD/CHF +37, DAX +35**. Laggards: **Gold −64, USD/CAD −6, EUR/USD −5**.

**The directional screen is no longer long-only.** June produced *zero* conviction shorts; the 2026-09-24 run names five longs (**WTI, S&P 500, Brent, Nikkei, Copper**) and one conviction short — **Gold**, at −64 with every factor against it (trend −42, macro −81, positioning −70, value −84). Gold's collapse is what drives the top of the pair book:

1. **LONG S&P 500 / SHORT Gold** — High (edge +116, 4/4 factors agree, pair vol 11.5%) — defensive haven vs risk equity.
2. **LONG Copper / SHORT Gold** — High (edge +106) — haven gold vs growth-cyclical copper.
3. **LONG WTI / SHORT Natural gas** — High (edge +32) — energy RV.

The June top idea (LONG Copper / SHORT Gold) survives, but has been displaced from first place and its edge is about 60% wider (+67 → +106; 66.6 → 106.1 in the JSONs, a ~59% increase — not a doubling). The pair that displaced it is not new either: **LONG S&P 500 / SHORT Gold was already June's #3 at +37** (`ideas_2026-06-22.json` `pairs[2]`, spread 36.9), so its edge has roughly *tripled* (+37 → +116) rather than appearing from nowhere — the June bullet below mis-lists #3 as S&P 500 / DAX, which was in fact that run's #10 at +22, and is left as written because that snapshot is a dated record.

**One caveat on the energy legs.** WTI and Brent screen 1st and 3rd on composite, and on a year-over-year view that is well earned (`macro_pack.json`: WTI **+53.1% YoY**, Brent **+71.8% YoY**). But crude has just come **off a mid-September spike**: `DCOILWTICO` prints **$103.62 on 2026-09-16 → $101.44 on 09-18 → $96.41 on 09-22**, with Brent at **$114.89** (09-22). The monthly trend factor is therefore reading a level that has already retraced ~7% inside a week. Treat "LONG WTI / SHORT Natural gas" and the energy end of the directional screen as momentum on a fading move until the next run re-scores it.

## Snapshot — 2026-06-22 (live, 19 majors)
Regime: **neutral risk**, CPI YoY +4.3%, VIX 62nd pctile, PTM endo **+27** (Mildly Inflationary). Broad global-equity bull (Nikkei +37, S&P +35, Nasdaq +28, FTSE +27, Dow +24, DAX +13), commodities bid (WTI +68, Copper +65, Brent +61), firm dollar (broad USD +18, USD/CHF +19, USD/JPY +14; EUR/USD −15 the main laggard). With almost everything positive, the directional screen is long-only (0 conviction shorts); the relative-value pairs still express both sides. Top pair ideas:

1. **LONG Copper / SHORT Gold** — High (edge +67) — reflation cyclical vs crowded-long haven.
2. **LONG WTI / SHORT Natural gas** — energy RV.
3. **LONG S&P 500 / SHORT DAX** — US vs Germany equity.

## Track record — backtest (point-in-time, audited)
`tools/langalpha_backtest.py` validates the composite **strictly point-in-time** (each month-end recomputes every composite using only data ≤ that date via the `_ASOF` truncation, with the monthly OECD/import-price series publication-lagged and the PTM endo overlay held out), then earns the next month's return. It runs a cross-sectional, inverse-vol, **dollar-neutral long/short** (long high-composite, short low) and a same-universe equal-risk long-only benchmark, monthly rebalance, 10bps turnover cost; plus each factor's information coefficient.

**Honest verdict (2013-02 → 2026-05, 160 months):** the cross-sectional long/short shows **no demonstrated edge** — net **Sharpe −0.15** (gross ≈ 0.00), and the composite IC is ≈ 0 (−0.002). Returns in this universe over the period came from **passive risk-parity beta** (long-only universe Sharpe **+0.86**; **+1.11** on the 2016+ window vs S&P **+0.91** at a third of the vol), not from cross-sectional selection. By factor, the **contrarian value (IC −0.024) and positioning (−0.018)** factors were mildly *counter*-productive; **carry (+0.028)** was the only mild positive; macro is faintly positive (+0.014) and trend ≈ 0 (−0.006).

*Re-run **2026-09-24** (`backtest.json`, `window` ["2013-02","2026-05"], 160 months) — supersedes the figures published with the 2026-06-22 build. **The verdict is unchanged and the headline numbers barely moved**: net Sharpe −0.15, gross −0.01, composite IC −0.002, long-only benchmark +0.86. What shifted is the matched-window comparison — the same-universe long-only book **+1.15 → +1.11** and the S&P comparator **+0.92 → +0.91** over `matched_spx_window` 2016-10→2026-05 (116 months). The "third of the vol" claim still holds exactly: the long-only book runs **4.6%** annualised vol against the S&P's **15.6%**, for a 5.2% CAGR against 13.8%.*

> **Why the window ends 2026-05 and not 2026-09.** This is *not* stale output — `backtest.json` and `experiments.json` were both re-run on 2026-09-24 (neither payload carries a date field of its own, so that stamp is their file mtimes: 2026-09-24 16:16 and 16:18). The end month is a **pinned constant** in the scripts (`end = "2026-05"` in both `langalpha_backtest.py` and `langalpha_experiments.py`), and the loop runs `range(len(axis) - 1)` so each month's composite earns the *following* month's return: the last book is formed at **2026-04** and earns the **2026-05** return. Neither script sits in any refresh chain, so they only move when run by hand — before 2026-09-24 they had not been re-run since June. To extend the track record to September, raise that constant; nothing else needs to change.

This is a **valuable null**, consistent with the rest of the book ([[Trading System - Backtest (June 2026)]], [[AlphaFX Smart-Money System (June 2026)]], [[Macro Pulse — Cross-Asset Z-Score Monitor (June 2026)]]): the engine is a transparent **regime / relative-value monitor and idea-surfacer**, not a proven alpha generator. The signs of the contrarian factors are not re-fit to this backtest (that would be in-sample overfitting) — the finding is disclosed, not optimised away.

**Factor-weighting experiments (`tools/langalpha_experiments.py`, IS<2020≤OOS; re-run 2026-09-24 → `experiments.json`).** One point-in-time factor pass; 7 principled re-weightings reweight the stored factors into a variant composite, each scored in-sample (2013-01→2019-12, 84 months) and out-of-sample (2020-01→2026-05, 76 months). Result: **every one of the seven is negative out-of-sample, and six of the seven are positive in-sample** — `trend_carry` IS Sharpe +0.33→OOS −0.20, `carry_tilt` +0.30→−0.32, `flip_contrarian` +0.30→−0.25, `carry_only` +0.28→−0.03, `no_contrarian` +0.25→−0.35, baseline +0.04→−0.32; **OOS IC is negative for all seven**. The seventh, `equal_weight`, is the exception that proves nothing: it is negative in *both* windows (−0.53→−0.29), so it never had an in-sample story to break. **No variant survives both windows** — the textbook overfitting signature. This is *why* the live model is deliberately not re-tuned: tilting toward the in-sample-best factors (carry, trend) is data-mining that does not generalise. (7 variants on one 76-month OOS — multiplicity-prone; shown in the dashboard's Track-record panel.)

*On the 2026-09-24 re-run the pattern held but the in-sample side softened: baseline IS **+0.07 → +0.04**, `trend_carry` **+0.34 → +0.33**, `flip_contrarian` **+0.31 → +0.30**, baseline OOS **−0.33 → −0.32**, and `flip_contrarian` OOS **−0.26 → −0.25** (that last digit was carried through unchecked when this note was first written and is corrected here against `experiments.json` `variants.flip_contrarian.oos_sharpe` = −0.25). The earlier "every variant is positive in-sample" wording no longer holds — `equal_weight` is now negative in-sample — so the claim above has been narrowed to six of seven rather than restated. The conclusion is unaffected.*

Adversarially audited by a 3-lens workflow which **fixed three real defects before this verdict** (a publication-lag look-ahead that had flattered the result; a not-truly-dollar-neutral book that added beta noise to the Sharpe; an unfair S&P comparator window) — the fixes left the null intact / made it more conservative. The dashboard's **Track record** panel shows the equity curves, the per-factor IC bar, and this metrics table.

## Caveats
- Deterministic factor model, **not** the LLM research agent — it surfaces candidates, not conclusions (same caveat as the source skill).
- **No demonstrated cross-sectional alpha** (see Track record) — use it as a monitor, not a black-box signal.
- Free-data limits: gold via an import-price proxy (monthly, lagged); **silver & Russell 2000 have no free FRED price** (omitted); DAX/Nikkei/FTSE are monthly OECD indices (lagged); no COT for Brent/Copper/international indexes; FX carry uses 10Y rate differentials.
- This is **live-markets data**, distinct from the vintage teaching corpus — keep separate from the historical wiki pages.

## Related
[[Endo-Exo Toolkit & Workflow]] · [[Macro Regime - Live (June 2026)]] · [[Commitment of Traders (COT)]] · [[Trade Idea Generation Process]] · [[The Global Macros Framework]]
