---
title: Global Macro Hedge Fund Strategy (Memo)
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "Hedge-fund-style strategy memo from the audited engine JSONs: Big-Four +3/±4, 1928-2026 bull/bear (June-26 closes, all 8 non-bear), 3 TAKE tickets (USD/JPY short; WTI, Dow longs); template prose still says Fed easing."
tags: [global-macro, strategy, memo, hedge-fund, pftm, skill-file, bull-bear, historical, patterns, indexes, fx, commodities, decision-support]
data_vintage: "2026 Excel workbooks (incl. Bull_Bear 1928→2026-06-26, the latest workbook row) · live CFTC COT (report 2026-09-15) · live prices"
sources: 1
updated: 2026-09-19
---

# Global Macro Hedge Fund Strategy — the written memo

The **detailed written strategy** the skill file describes — a hedge-fund-style memo composed from the audited engine
outputs, adding the one layer the dashboards didn't have: **historical market structure** from the user's own
`Bull_Bear_Markets_2026.xlsx` (daily index history to 1928). Built 2026-07-02 ("create a detailed Global Macro Hedge
fund strategy with updated data … with analysis of pattern, trends and historical movements").

> **Decision-support / education only — NOT investment advice.**

## Output
**`Global Macro Hedge Fund Strategy/Global Macro Hedge Fund Strategy.html`** — a seven-section memo (serif document
styling, dark chart wells, ← Main Dashboard link; also a Main-Dashboard card). `tools/hf_strategy_memo.py` +
`tools/bull_bear.py` + `build_hf_strategy.py`.

## Structure (the skill's four modules, written out)
- **Exec summary** — regime, positioning, historical context in three paragraphs.
- **I. Macro Regime** — Big-Four scorecard (+1/0/−1 per block from the trend-aware endo) + the 12 highest-impact
  drivers with **pattern labels** (Rising-accelerating / Rolling-over…), and the pattern read (real-rate compression;
  sentiment-vs-activity divergence).
  *Current (memo as of 2026-09-19, the macro-COT engine's as_of; HTML regenerated 2026-09-19 from the same-day engine
  JSONs — its own header reads 'As of 2026-09-19 · 3 TAKE'; the HTML's file modified-time only tracks the later
  dashboard re-themes, not a data rebuild; supersedes the 2026-09-11 readings, which are listed in [[log]]):
  Big-Four **+3/±4** (GDP +0 · CPI +1 · Rates +1 · Jobs +1, unchanged), scored from the 19-driver trend-aware endo;
  12-row driver table, latest obs 2026-04 → 2026-08.*
  *⚠ Re-check 2026-09-19 (regenerated memo) — the flag below still holds, and the template prose is now also wrong on
  policy. The exec summary's "the Fed easing into it", the pattern read's "Fed funds path points down" and the commodity
  paragraph's "the Fed easing into re-accelerating inflation (real rates falling)" are fixed text that now contradicts the
  Fed's first hike of the cycle — 25bp to a 3.75-4.00% target range, effective 2026-09-17 (EFFR 3.88% that day) — which the memo's own Rates block
  already reads as "Fed Funds ↑"; the 10Y TIPS real yield was 2.61% on 17 Sep (2.60% on 14 Sep), not falling.
  "Re-accelerating" fits headline and producer prices (CPI +3.35% y/y Aug; PPI all-commodities +9.85% Aug from +8.70% Jul),
  not core: core CPI is +2.45% y/y and its 3-month annualised pace turned up to 1.97% from 1.64% in July but is still
  below 2%. The driver table's PPI row (5.51, obs 2026-07, ↓ Rolling over) does not match FRED's all-commodities PPI
  (+8.70% Jul, +9.85% Aug, rising). COT on the 2026-09-15 CFTC report: S&P 500 at the 28th and Dow at the 55th
  percentile (29th / 66th in the flag below), NASDAQ 100 52nd — still not "extreme short"; Gold 99th and WTI 8th
  against the prose's "~95th" and "~6th". Gold and Silver are STAND-ASIDE ("real rates not falling") while the prose
  still has Silver carrying the real-rate theme.*
  *⚠ Flag 2026-09-11 — several memo sentences are fixed template prose in `tools/hf_strategy_memo.py`, not computed,
  and the memo's own computed fields contradict them. The "pattern read" says inflation is "rising and accelerating"
  with sentiment deteriorating, against PPI and PCE ↓ Rolling over, Core CPI ↓ Falling (accelerating), U. Michigan ↑
  Bottoming and NFIB ↑ Rising (accelerating). The exec summary prints "real rates falling" beside "(currently stable)" and
  calls index-futures specs "extreme short", against S&P 500 at the 29th and Dow at the 66th COT percentile. The
  commodity paragraph's Gold "~95th" and WTI "~6th" percentile compare with the engine's 99th and 7th. Trust the tables
  and tickets, not those sentences, until the template is made data-driven.*

- **II. Global Growth** — the 11-country PMI check (gate for risk-on & industrial commodities).
- **III. Historical Market Structure** — NEW: from the 1928→2026 file, per index: % off high, bull/bear state,
  distance to the −20% bear threshold, **historical bear count / median depth / median recovery** and CAGR.
  *Current (re-read 2026-09-19 from `bullbear_latest.json`, generated 2026-09-19 15:51; every figure unchanged from the
  2026-09-11 re-read): all 8 indexes in non-bear
  states — 5 BULL, 2 BULL (at/near highs: DJIA −0.2%, Eurostoxx 50 −1.6%), Nasdaq 100 −5.0% off high = PULLBACK
  (−15.8% to the bear line; a pullback-entry context); S&P 500 −3.4% off high; median S&P bear −33.5% (12 bears over
  98.5y), median recovery 646 days → the drawdown context that motivates conviction-scaled sizing. **Vintage: every
  index close is still dated 2026-06-26** — the latest row of `30. Bull_Bear_Markets_2026.xlsx`, which has not been
  extended; both September regenerations (11 and 19 Sep) re-read the same June rows, so this is a late-June market read,
  not a September one — FRED's S&P 500 closed 7,637.76 on 17 Sep, above the file's 7,609.8 running high.*
  *Superseded 2026-09-11: "all 8 indexes in bull regimes; NASDAQ −5%; median S&P bear −33.5% over ~2yrs" (as of
  2026-07-02) — figures unchanged on re-read; only the vintage qualification and source-exact labels are new.*
- **IV. Asset-Class Strategy** — indexes / FX majors / commodities: fundamental case × COT × technicals, with the
  live TAKE **tickets** (entry / 2·ATR stop / 2R target / size / risk) and watchlists.
  *Current (memo as of 2026-09-19, from the macro-COT engine generated 2026-09-19 15:36 on the 2026-09-15 CFTC report;
  supersedes the 2026-09-11 readings, which are listed in [[log]]): **3 TAKE tickets**, all HIGH-conviction at 2.0 R:R
  with 2×ATR stops: USD/JPY **short** (entry 156.855 · stop 160.80 · target 148.96 · size $39,744), WTI Crude long
  (entry 100.30 · stop 91.11 · target 118.67 · size $10,917) and Dow Jones long (entry 51,682.64, the 18 Sep close ·
  stop 50,608.57 · target 53,830.78 · size $48,119). Gross risk $3,000 (2 long / 1 short) on the illustrative $100,000
  account; no active correlation clusters. FX now has a TAKE-grade setup — USD/JPY, where the positioning trend (net +22%
  OI, 13-wk Δ +51.0, z +1.27) and the +7.5 endo divergence agree — plus a 6-pair watchlist, all positioning-led. The
  WTI entry is the engine's live price, below FRED spot WTI's $107.02 on 15 Sep; the USD/JPY entry 156.855 is
  likewise the engine's live quote — FRED's H.10 publishes with a lag and its last USD/JPY is 153.71 on 11 Sep.
  ⚠ The Dow long now sits against its daily technical trend, which reads DOWN (not aligned; trigger mid-channel) — a
  formal conflict with the playbook's "never enter against the daily technical trend". USD/JPY's trend reads RANGE
  (also not aligned); WTI's reads UP (aligned).*

- **V. Risk & Portfolio** — conviction sizing table, correlation clusters (one-bet rule), crowding rule, drawdown context.
- **VI. Execution Playbook** — the weekly cadence: refresh → regime check → funnel review → breakout/pullback entries → risk pass → journal.
- **VII. Provenance & honest limits** — snapshot-not-backtest, FX positioning-led (no foreign Big-Four data), COT validated vs the user's own workbooks.

## New tool: `tools/bull_bear.py`
Reads `Bull_Bear_Markets_2026.xlsx` (15 index sheets, S&P from 1928; newest-first rows) → per index: current
drawdown vs rolling high, −20% bear threshold, and **bear-episode statistics** (episodes = close < 80% of running
high until full recovery; count, median depth, days-to-trough/recover) → `bullbear_latest.json`. Wired into
`build_hf_strategy.py`; the memo regenerates from the latest JSONs.

## Related
[[Global Macro Trading Dashboard]] · [[Macro + COT Trade Signals]] · [[PTM Endo Scorecard (2026 Excel Data)]] · [[2026 Trading System — Operating Manual]] · [[The Global Macros Framework]] · Not investment advice.
