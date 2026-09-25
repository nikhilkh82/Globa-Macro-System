---
title: Macro + COT Trade Signals
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "Turns 2026-Excel endo x live CFTC COT x Yahoo technicals into directional trades; 2026-09-19 book (COT as of 15 Sep): 3 TAKE (WTI, Dow longs; USD/JPY short), 10 WATCH, 2 STAND-ASIDE; endo inputs predate the Fed hike."
tags: [global-macro, strategy, trades, cot, positioning, endo, fx, indexes, commodities, excel-data, decision-support]
data_vintage: "ENDO: your 2026 Excel workbooks · COT: live CFTC (weekly) · prices: live Yahoo daily"
sources: 2
updated: 2026-09-19
---

# Macro + COT Trade Signals — Indexes · FX · Commodities

Turns the **trend-aware ENDO scores** (from your 2026 Excel data) plus **live CFTC COT positioning** into **actual
directional trades** across indexes, FX pairs and commodities. Built 2026-06-25 at the user's request ("update the
trading system based on these scores with COT to take actual trades").

> **Decision-support / education only — NOT investment advice.** Account ($100k) and risk %s are illustrative.

## Outputs (`Macro COT Trades/`)
- **[PFTM Trade Console](../../Macro%20COT%20Trades/PFTM%20Trade%20Console.html)** — one unified dashboard that walks **ALL the steps to take an actual trade**, per instrument: a single decision-funnel card showing every gate (Macro Regime → Macro Bias → COT Positioning → Technical Trigger → Sizing → Trade Ticket) with ✓/✗ pass-fail, plus a COT crowdedness chart, a conviction bar, correlation-cluster warnings, and TAKE/WATCH/stand-aside filters. The one surface to *see how a trade was arrived at*. Builder `tools/pftm_console_report.py` (reads this engine's `macrocot_latest.json`).
- `Macro COT Trades Dashboard.html` — the per-trade engine dashboard (COT table + trade cards). `macrocot_latest.json` — the engine output. `tools/macro_cot_trades.py` (engine) + `tools/build_macro_cot.py` (orchestrator).
- **`COT Cross-Check.html`** — validates the engine's **live-CFTC** COT z-scores against the user's own **10-yr Excel COT** workbooks (13.1 FX/Index 2013→2026 + 13 Metals/Energy). 2026-07-01: **7/11 agree closely** (EUR/JPY/NASDAQ/Gold/Silver/Copper/CHF — engine z ≈ your z), the 4 gaps explained by the Excel being ~1–2 wks behind live (notably **WTI**: your 06-16 neutral → live extreme-short = the swing that turned WTI contrarian-long). `tools/cot_excel.py` + `cot_excel_report.py`. **Read-only validation — the audited engine still runs on live CFTC.**

## How a trade is formed
1. **ENDO → macro bias** (the trend-aware US endo, [[PTM Endo Scorecard (2026 Excel Data)]]):
   - **Equity indexes** ← growth axis (LONG if growth>0.4), **trimmed** when inflation is high *and* re-accelerating (late-cycle).
   - **Oil / Copper** ← demand = 0.6·growth + 0.6·inflation (LONG in reflation).
   - **Gold / Silver** ← 0.5·inflation + a real-rate term (**LONG when the Fed is easing into rising inflation → real rates fall**).
   - **FX** ← **COT-positioning-led** with a USD risk-tilt (US-only endo can't give a *relative*-endo FX bias — stated openly).
2. **COT overlay** (live CFTC net-spec, z / percentile / 13-week change / weekly flip):
   - **confirm** (specs aligned, not crowded) → full conviction · **crowded** (aligned but ≥90th/≤10th pctile) → *reduce* (reversal risk)
   - **contrarian-support** (specs extreme *against*) → confirm · **divergent** (mildly opposed) → reduce / await a flip · a 🔁 flip toward the bias times the entry.
3. **Technicals** (Yahoo daily ATR/EMA/Keltner) set **entry / stop (2×ATR) / target (2R)**; **conviction** sets the risk
   (HIGH 1.0% / MED 0.6% / LOW 0.3% of $100k). **TAKE** = conviction ≥ MEDIUM (a live trade); WATCH = macro edge
   awaiting conviction/COT; STAND-ASIDE = no macro edge. Notional sized off the *displayed* stop; margin = notional/leverage.

## Live read — 2026-09-19 (current)
*Engine build `macrocot_latest.json` as_of **2026-09-19**, generated 2026-09-19 15:36 (file written 15:39). COT tables
as of **2026-09-15**. Prices are Yahoo daily closes (the Dow's 51,682.64 is its 18 Sep close). Supersedes the
2026-09-11 rebuilt read below (2 TAKE / 11 WATCH / 2 STAND-ASIDE, COT as of 2026-09-01), which stays as the dated record.*

**Regime (engine):** Mildly Inflationary · Reflation / Overheating (growth +0.56, inflation +0.89 and rising; real rates
not falling; endo total +12.9, 10 rising / 9 falling). **Book: 3 TAKE (2 long / 1 short), 10 WATCH, 2 STAND-ASIDE; gross
margin $4,823 (4.8%), gross risk $3,000.**

> **⚠ The ENDO layer has not caught up with this week.** The regime figures above match the 2026-09-11 read digit for
> digit. The 2.8 workbooks behind `Endo Excel/endoexcel_latest.json` (rebuilt 2026-09-19 15:47, same values) have not
> absorbed the mid-September releases: CPI, core CPI, PPI and retail sales still end at July, industrial production at
> June, and the Fed Funds row reads 3.63, before the hike. The engine does not yet see that the Fed raised 25bp to
> 3.75-4.00% (effective 17 Sep; EFFR 3.88%) and the ECB raised its deposit rate to 2.50% (effective 16 Sep), while WTI
> rose to $107.02 and Brent to $130.80 (15 Sep) and August PPI ran +9.85% y/y. The hike does not change the
> precious-metals call, because "real rates not falling" already held; 10Y TIPS real yield +2.61% (17 Sep). This
> trend-aware endo is a separate model from the Excel-template US Endogenous scorecard, which reads +19 today.

- **TAKE (3), all HIGH-conviction at 2.0 R:R with 2×ATR stops; every ticket enters at the last price:**
  - **USD/JPY short** (conv 2.17): entry 156.855, stop 160.8016, target 148.9618, margin $1,325, risk $1,000. New since
    the 09-11 read: it entered the book at MEDIUM in the 09-12 build and is HIGH today. Positioning-led: JPY specs net
    +22% of OI, 13-week change +51.0, z +1.27 (84th percentile, from z +0.56 / 68th in the 09-12 to 09-18 builds); the
    cross-country endo divergence (+7.5) confirms. ⚠ The technicals do not: RANGE trend, trigger "pullback to mid
    (EMA20)", `aligned = false`.
  - **WTI Crude long** (conv 2.07): entry 100.30, stop 91.11, target 118.67, margin $1,092, risk $1,000. Macro demand
    +0.87 (reflation); daily trend UP, mid-channel, `aligned = true`; COT is contrarian support, with specs extreme short
    at z -1.48 (8th percentile) and a weekly flip flagged. The engine price is the Yahoo front-month future (CL=F) and
    sits below FRED's WTI spot of $107.02 on 15 Sep; the series and dates differ, so the gap is not a verified price move.
  - **Dow Jones long** (conv 2.06): entry 51,682.64, stop 50,608.57, target 53,830.78, margin $2,406, risk $1,000. Growth
    axis +0.56 (risk-on); COT confirms (z +0.14, 55th percentile, from +0.39 / 66th on 09-11). ⚠ The daily trend is now
    DOWN (RANGE on 09-11) and the setup is still `aligned = false`.
- **WATCH (10), all LOW conviction:** Natural Gas long (1.07), S&P 500 long (1.06), NASDAQ 100 long (1.06), AUD/USD short
  (1.00), NZD/USD long (0.62), Copper long (0.57, COT crowded at the 96th percentile), USD/CHF short (0.49), GBP/USD long
  (0.31), EUR/USD short (0.30), USD/CAD short (0.30). Natural Gas, S&P 500 and NASDAQ 100 are `divergent` (COT mildly
  opposed, awaiting a flip). Against 09-11: USD/CAD flipped from long (1.09) to short, because CAD specs are building
  long off a net-short book (-10% OI, 13-week change +16.5), and it is reduced because the endo divergence (-1.4)
  opposes. AUD/USD rose from 0.30 to 1.00 because its endo divergence (-2.2) now confirms. Three pairs are reduced
  (GBP/USD, EUR/USD, USD/CAD), against four on 09-11. Across the seven FX names, five lean short USD (USD/JPY, NZD/USD,
  USD/CHF, GBP/USD, USD/CAD) and two lean long USD (AUD/USD, EUR/USD).
- **STAND-ASIDE (2):** Gold and Silver, NEUTRAL (inflation +0.89, real rates not falling). Gold is still crowded long at
  z +1.75 (99th percentile); Silver z +0.34 (60th).
- **COT Cross-Check (`cotexcel_latest.json`, rebuilt 2026-09-19 15:39):** 5 of 12 markets agree with your Excel COT,
  2 partial, 5 diverge. Your Excel COT ends 2026-08-25 for FX and indexes, 2026-09-01 for metals and WTI, and
  2026-08-04 for Natural Gas; the tool attributes each divergence to positioning moving since the Excel snapshot. Two
  of the three TAKEs are among the diverging names: USD/JPY (Excel z -0.44 vs live +1.27) and WTI (Excel +0.08 vs
  live -1.48).
- **⚠ Flag vs the 2026-09-11 read below:** the book went from 2 to 3 TAKEs with no change in the macro inputs. The new
  ticket comes entirely from the FX leg (COT positioning plus the cross-country endo divergence). Gross risk rose from
  $2,000 to $3,000 and gross margin from $4,215 to $4,823.

## Live read — 2026-09-11, rebuilt engine
*Engine build `macrocot_latest.json` as_of **2026-09-11**, generated 2026-09-11 09:17, after the ENDO feed was repaired
(`tools/xl_macro.py` now resolves the workbooks with `find_wb`; 19 of 19 drivers scored). COT tables as of 2026-09-01.
Supersedes the degraded build below (generated 2026-09-10 13:11), which stays as the dated record of the failure.*

**Regime:** Mildly Inflationary · Reflation / Overheating (growth +0.56, inflation +0.89 and rising; real rates not falling; endo total +12.9, 10 rising / 9
falling). **Book: 2 TAKE (2 long / 0 short), 11 WATCH, 2 STAND-ASIDE; gross margin $4,215 (4.2%), gross risk $2,000.**

- **TAKE (2), both HIGH-conviction longs at 2.0 R:R with 2×ATR stops:**
  - **WTI Crude long** (conv 2.07): entry 96.72, stop 88.97, target 112.23, margin $1,247, risk $1,000. Macro demand +0.87
    (reflation); daily trend UP with a breakout above the upper Keltner; COT is contrarian support, with specs extreme
    short at z -1.51 (7th percentile). The last price (102.94) is already above the entry level, so the ticket assumes a
    pullback fill; see [[Chart Room]] for the distance.
  - **Dow Jones long** (conv 2.06): entry 52,064.10, stop 51,187.12, target 53,818.07, margin $2,968, risk $1,000. Macro growth axis
    +0.56 (risk-on); COT confirms (z +0.39, 66th percentile). ⚠ The technical trigger opposes the long: price is breaking
    below the lower Keltner in a RANGE trend, and the engine marks the setup `aligned = false`.
- **WATCH (11), all LOW conviction:** USD/CAD long (1.09), Natural Gas long (1.07), S&P 500 long (1.06), NASDAQ 100 long (1.06), USD/JPY short (0.96), NZD/USD long (0.57), Copper long (0.57, COT crowded at the 99th percentile), USD/CHF short (0.49), EUR/USD short (0.30), GBP/USD long (0.30), AUD/USD short (0.30).
  The seven FX pairs are the same USD-theme `positioning-led` list as the degraded build; 4 of them (USD/CAD, EUR/USD, GBP/USD, AUD/USD) are
  reduced because the cross-country endo divergence opposes the positioning direction. The equity and commodity longs
  are back on the list because the macro bias is back.
- **STAND-ASIDE (2):** Gold and Silver, NEUTRAL. Inflation +0.89 with real rates not falling gives no precious-metals
  edge. Gold is crowded long at z +1.66 (99th percentile) with no bias to act on.
- **⚠ Flag vs the degraded build below:** its 0 TAKE / 7 WATCH / 8 STAND-ASIDE book and "Strongly Inflationary" label
  were artefacts of the blank ENDO input, not a regime change. Against the 2026-07-01 snapshot (11 TAKE / 3 WATCH, gross
  margin $16,714) this book is far smaller: the inflation axis is +0.89 against +2.01 then, and only two names clear
  MEDIUM conviction.

## Live read — 2026-09-11
*Engine build `macrocot_latest.json` as_of **2026-09-11** (generated 2026-09-10 13:11; COT tables as-of 2026-09-01). Supersedes the 2026-07-01 snapshot below (11 TAKE / 3 WATCH, gross margin $16,714) as the latest read; that snapshot is kept unchanged as the dated record.*

> **⚠ DEGRADED BUILD — the ENDO macro layer is blank, so this book is NOT a market read.** The engine's regime block
> reads growth **+0.00**, inflation **+0.00**, endo total **0**, rising **0** / falling **0** (inflation not rising,
> real rates not falling), yet labels the state **"Strongly Inflationary"**. That label comes from the state formula
> running on an all-zero input. It is not an inflation signal. Upstream, `Endo Excel/endoexcel_latest.json`
> (generated 2026-09-08 09:44) has **no indicator scored, and every row reports `src: missing file`**. This is the
> moved-workbook failure mode: 2.8 workbooks must be resolved with `tools/xlfind.find_wb`. Until the ENDO feed is
> repaired and the suite re-run, treat the macro gate as *unknown*, not *neutral*.

**Regime (as printed):** Strongly Inflationary · Reflation / Overheating (growth +0.00, inflation +0.00; real rates not
falling). **Book: 0 TAKE (0 long / 0 short), 7 WATCH, 8 STAND-ASIDE; gross margin $0 (0.0%), gross risk $0.**

- **WATCH (7). All are FX, LOW conviction, `positioning-led` and USD-theme:** USD/CAD long, USD/JPY short,
  NZD/USD long, USD/CHF short, EUR/USD short, GBP/USD long, AUD/USD short. FX survives because that leg is COT-led
  (plus the cross-country endo divergence) and does not depend on the blank US axes. None reaches MEDIUM, so there
  is no live ticket. The USD cluster partly nets off: 3 long-USD (USD/CAD, EUR/USD, AUD/USD) against 4 short-USD
  (USD/JPY, NZD/USD, USD/CHF, GBP/USD).
- **STAND-ASIDE (8). Every index and commodity:** S&P 500, NASDAQ 100, Dow Jones, Gold, Silver, WTI Crude, Copper,
  Natural Gas. All are NEUTRAL with the rationale "growth axis +0.00 ~flat" / "inflation +0.00" / "demand +0.00
  ~flat". They stand aside because the bias input is zero, not because the macro read is flat.
- **COT extremes that have no macro bias to act on:** Gold z +1.66 (p99) and Copper z +1.93 (p99) are crowded-long.
  WTI z -1.51 (p7) is extreme-short. The overlay has nothing to confirm, trim or fade until the ENDO bias returns.
- **⚠ Flag vs the 2026-07-01 headline below:** this build neither confirms nor refutes the "11 TAKE, 10 long, one USD
  bet split five ways" read. The drop to 0 TAKE comes from an input failure, not a regime change. Re-verify once
  the ENDO feed is fixed.

## Current book (snapshot 2026-07-01 — the live dashboards are the source of truth)
> *This book is regenerated every refresh (`refresh_2026_suite.ps1`); the specific tickets/levels change with live
> COT + prices. Treat the numbers below as a dated snapshot — open the [Macro COT Trades Dashboard] / [PFTM Trade
> Console] for the current state.*

**Regime:** Mildly Inflationary · Reflation / Overheating (growth +0.64, inflation **+2.01** & rising; **real rates
falling**). **11 TAKE (10 long / 1 short), 3 WATCH; gross margin $16,714 (16.7% of the illustrative account).**
HIGH conviction: **Silver, WTI Crude** (both long).

- **Why the book jumped 5 → 11:** positioning went **broadly extreme-short** — WTI (p6), NASDAQ (p9), NZD (p4), GBP
  (p5), USD/CAD-CAD (p6), USD/CHF (p13) all sit at/near the ≤10th percentile → the engine's **contrarian-support /
  fade-the-crowd** logic fires long across FX & indexes. **USD/CAD flipped LONG → SHORT** (fading extreme-short CAD
  specs). Gold (p95) and Copper (p97) are **crowded** (aligned + extreme) → conviction trimmed, not blocked.
- **⚠ Concentration is the real risk (the skill's non-negotiable rule):** 5 of the 11 TAKEs share the **USD** theme
  (USD/CHF, NZD/USD, GBP/USD, USD/CAD, USD/JPY) — that's essentially **one USD bet split five ways**. Plus real-rate
  (Silver+Gold) and global-growth (WTI+Copper) pairs. So "11 trades" is really ~**4 distinct bets**; per the skill,
  **take the single largest-divergence leg per cluster**, don't stack all five. 10-long / 1-short is very
  one-directional — size accordingly.
- **The COT overlay still does real work:** crowded (Gold/Copper) trims; extreme-opposed (WTI/NASDAQ/NZD/GBP)
  confirms; the audited sign logic (crowded vs contrarian keyed on z+percentile agreement; FX pair-inversion) is
  unchanged from the [audit](#audit).

## Audit (up front, lean — 6 agents, 3 lenses → refuter → synthesis) → SOUND_WITH_FIXES
**The high-stakes signs are all correct:** `cot_signs_ok: true`, `fx_inversion_ok: true`, `levels_ok: true` — *"no
backwards trades."* COT confirm/crowded/contrarian-support map to the right (bias × spec-direction × extremity)
combinations; the FX pair-inversion (long JPY-future → long USD/JPY) is applied exactly once; entry/stop/target
geometry and risk-based sizing are correct. **Two LOW convention fixes applied:**
- **L1-1:** the percentile arm of "extreme" now must agree with the z-sign (so a skewed distribution can't mislabel
  crowded vs contrarian). Didn't bite any current TAKE; fixed for robustness.
- **FX-ride-level:** the "ride the build" FX path now references the absolute net-spec *level*, not just its 13-week
  *direction* — a still-net-short book merely de-grossing is an **inflection** (reduced conviction), not a confirmed
  trend. This is what demoted NZD/GBP/CHF from TAKE to WATCH.

## Caveats
Snapshot decision-support, **not a backtest** — no performance/edge claim. The macro layer is US-only endo; the FX
layer is therefore COT-led (no relative-endo FX bias). COT is weekly (Tue-as-of, published Fri — a few days lagged).
Account/risk/leverage illustrative. **Not investment advice.**

## Related
[[PTM Endo Scorecard (2026 Excel Data)]] · [[PFTM Full Trading System]] · [[PFTM Global-Macro Execution Strategy]] · [[PTM Global-Macro Dashboard (Endo + Exo)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]] · Not investment advice.
