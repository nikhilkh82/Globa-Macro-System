---
title: Million Dollar Traders — 5-Step Global Macro (July 2026)
category: synthesis
type: strategy-system
data_asof: 2026-09-24
summary: "Lex van Dam's 5-Step course as a rules-based macro system on 16 instruments; the FULL system re-run 2026-09-24 loses harder (−1.9%/yr, PF 0.94); gated-Turtle core +0.7% vs SPX 8.7% — no edge."
tags: [global-macro, lex-van-dam, 5-step-trading, turtle, trend-following, backtest, indexes, commodities, fx, honest, audited]
data_vintage: "LIVE — Yahoo daily + FRED + local ISM. 1990-01-02 → 2026-09-24, both variants (mdt_latest.json FULL and mdt_turtle.json CORE, each meta.asof 2026-09-24)"
sources: "Adapted from Lex van Dam's 'Million Dollar Traders' / 5-Step-Trading course (raw/Million Dollar Traders Course)"
updated: 2026-09-25
---

# Million Dollar Traders — 5-Step Global Macro (July 2026)

**What it is & why it matters** — A systematic reconstruction of **Lex van Dam's 5-Step-Trading course** (the "Million Dollar Traders" hedge-fund manager) as a **complete global-macro trading system on indexes, commodities and FX majors** — the sixth strategy engine, and the one where the adversarial audit mattered most: it **flipped the verdict**, and per this project's no-fabrication rule we report the flip. Every rule was extracted from the course's own files with citations: the 11 model spreadsheets (ISM→S&P returns model, real-rates→gold, oil↔USD, yield-curve→cycle, seasonality, **LVDTA position-sizing algorithm**) and the Technical-Strategies/Gold/FX workbooks (Turtle mechanics, ADX switch, Bollinger fade, Turtle Soup, Ichimoku ladder). Artifacts in project-root `million dollar traders/` (live trade dashboard), engine `tools/build_mdt.py`.

## The architecture — 5 steps → a machine
| Step | Course concept | Systematized as |
|---|---|---|
| 1 · Idea Generation | the indicator library + models | **Macro gates**: ISM SD-band (US equities; the course's own forward-return band table), real-rates→**gold**, USD-momentum→**oil**, carry/haven→**FX** (risk regime from ISM) |
| 2 · Fundamental Analysis | spreadsheet models | Regime strip: each model's live expected-return read; yield-curve nowcast as context (the course's curve model is contemporaneous — honestly not traded) |
| 3 · Chart Analysis | Technical Strategies workbooks | **Turtle 20/55 breakout** (skip-if-winner, 55d fallback, 2×ATR stop, 10/20d trail, ½-ATR pyramiding to 4 units — App M verbatim), 5/20 SMA gold sleeve, Bollinger(20,2) fade in ADX<20, Turtle Soup reclaim |
| 4 · Psychology | discipline chapters | Mechanized: close-wait execution, skip-filter, ADX trend/range switch, MACD confirmation |
| 5 · Risk Management | LVDTA algorithm | Turtle unit sizing (risk%×equity÷stop), **LVDTA fractional-Kelly** f=[W−(1−W)/R]×0.25 clamped 0.25–2% (spreadsheet cell G39), 12-unit portfolio cap, seasonality size modifier |

All gates **point-in-time**: ISM lagged one month, CPI lagged one month for its mid-month release, every course regression **refit expanding** (≥120 obs — the course's fitted coefficients are never applied to their own estimation period).

## The audit that flipped the verdict
A first draft showed **+3.6%/yr**. The adversarial audit traced that to two flattering artifacts and fixed both:
1. **Impossible-profit stop fills** — when price gapped past a stop, the engine filled *at the stop price*, which for gapped entries booked profits on trades that could only lose (a Bollinger short "stopped out" *below* its entry). Fix: stops fill at the worse of stop/open, and a setup whose entry opens beyond its own stop is **skipped as invalidated** (~330 fake trades removed).
2. **Sparse 21-day equity marks** — hid intra-month drawdown. Fix: daily mark-to-market.
Plus: provable same-bar stop-outs on Turtle-Soup fills (close beyond stop ⇒ stopped), the missing per-class cap on soup fills, and a stale-month gate fallback so live tickets use the latest *known* gate. Look-ahead scan of the gates (ISM lag, expanding regressions, seasonality-from-prior-years, prior-day channels, Kelly from closed trades only) came back clean.

## Results — honest, post-audit (1990–2026, daily MTM, costs excluded)
| | CAGR | Sharpe | MaxDD | Trades | Win% | PF |
|---|---|---|---|---|---|---|
| **FULL system** (all sleeves) | **−1.9%** | −0.08 | −95.7% | 4,342 | 26.1% | 0.94 |
| **CORE** (gated Turtle only) | **+0.7%** | 0.13 | −52.8% | 1,478 | 18.8% | 1.04 |
| S&P 500 buy & hold | **+8.7%** | **0.66** | −56.8% | — | — | — |

*Refreshed 2026-09-24 — **both rows.** `mdt_latest.json` (`meta.asof` 2026-09-24, `meta.end` 2026-09-24, `meta.variant` "full") supersedes the 2026-09-08 FULL figures: CAGR −1.3% → **−1.9%**, Sharpe −0.03 → **−0.08**, MaxDD −95.1% → **−95.7%**, 4,303 → **4,342** trades, win 26.2% → 26.1%, PF 0.95 → **0.94**. **The CORE row is on the same run:** `mdt_turtle.json` carries `meta.asof` **2026-09-24**, `meta.end` 2026-09-24, `meta.variant` "turtle" — it is a restricted-sleeve run of today's build, not an older build. It is written only by `python tools/build_mdt.py turtle`; the no-argument run that the refresh chain calls never produces it, so it had been stuck on the 2026-09-08 build until that variant was run explicitly at 17:04 today. Against the 2026-09-08 CORE figures: CAGR +0.8% → **+0.7%**, 1,481 → **1,478** trades, win 19.1% → **18.8%**; Sharpe 0.13, MaxDD −52.8% and PF 1.04 unchanged. S&P 500 buy & hold is unchanged at 8.7% / 0.66 / −56.8% (`spx.*`, identical in both payloads).*

*CORE (turtle-only) variant re-run 2026-09-08 on refreshed price history — it had not been rebuilt since 2026-07-04 because `mdt_data.py` was failing on a moved workbook path, so these figures moved across the whole backtest, not just the last three months.*

*Metrics refreshed 2026-09-08 from the rebuilt engine output; the June-2026 figures are superseded. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Only the Turtle trend sleeve survives honest pricing**, and on the 2026-09-24 FULL re-run it survives by less: **+$513,827** over 1,486 trades, down from +$620K (`sleeves.turtle.totpnl`). The **Bollinger fade is still the principal drag (−$931,680 over 2,334 trades**, 29.3% win), Turtle Soup is a bigger loser than before (**−$87,119** over 507 trades, was −$81K) and the SMA gold sleeve is flat (**−$3,359** over just 15 trades) (`sleeves.*`).
- **The course's own risk algorithm agrees**: the LVDTA Kelly formula pins the risk budget at the **0.25% floor** — `meta.kelly_now` is **0.25** against a `meta.risk0` of 1% — the sizing rule itself refuses to size up a no-edge system.
- **The best fold is still the macro-gated Turtle core in 2011–17, but it has dimmed on the refreshed run: +1.8%/yr, Sharpe 0.22** (was +3.8%/yr, Sharpe 0.41; `folds` in `mdt_turtle.json`, asof 2026-09-24; MaxDD −25.1%). The regime-gating idea retains *some* content in a trending decade, but at 0.22 it is no longer meaningfully a "bright spot", and no fold of either variant approaches buy-and-hold. This weakens the one point that had been in the gating idea's favour — the headline no-edge verdict is unaffected, indeed reinforced. On today's FULL re-run **every** fold is negative: 2003–10 **−4.8%** (Sharpe −0.42), 2011–17 **−0.3%** (0.03), 2018–26 **−3.1%** (−0.35, and the −95.7% drawdown sits in this last fold) (`folds` in `mdt_latest.json`).
- FX is net negative in both variants — **CORE FX turtle −$301,196 over 404 trades at 13.9% win** (`byclass.fx` in `mdt_turtle.json`, asof 2026-09-24) and **FULL FX −$171,536 over 1,258 trades at 24.4% win** (`byclass.fx` in `mdt_latest.json`, 2026-09-24). In the FULL run *every* asset class loses: index −$192,643, commodity −$144,152, FX −$171,536. This is consistent with [[AlphaFX Smart-Money System (June 2026)|the AlphaFX null result]], which on its own 2026-09-24 re-run also weakened: retail-course FX timing rules don't survive honest testing.

## Live regime & tickets — 2026-09-24

The dashboard's Step-1/Step-2 strip and Step-5 tickets, read from `mdt_latest.json` (`regime`, `tickets`, `meta.asof` 2026-09-24):

- **Every gate is risk-on.** ISM **54.6** → `ism_gate` 1 and `risk_on` true; the gold gate is 1 on a 5-year real rate of **0.95%** with a model expected return `gold_E` of **+14.45%**; the oil gate is 1 on USD momentum `usd_yoy` **−0.52%** with `oil_E` **+14.0%**. All three Step-1 gates — equities via ISM, gold via real rates, oil via USD momentum — are open at once, which is the maximum-exposure configuration the backtest above prices at roughly −1.9%/yr.
- **Curve nowcast ties out to FRED exactly.** `regime.curve_t10y2y` **+0.26pp** and `curve_t10y3m` **+0.92pp** are identical to `T10Y2Y` and `T10Y3M` for **2026-09-23** in `tools/macro_pack.json`, so the strip is keyed to the same observation day. Both are positive — an upward-sloping curve, and 10Y−3M has steepened from 0.80pp on 09-22 — following the **2026-09-16 Fed hike to a 3.88% effective funds rate** (`macro_pack.json` `DFF`, 09-22). The course's curve model is contemporaneous and, per Step 2 above, honestly not traded.
- **11 live tickets**, all sized off the pinned Kelly budget — **0.25–0.31% risk per unit**, rising to **0.75%** only for the one three-unit position: HOLD LONG SPX (Bollinger sleeve, entry 7,631.44, stop 7,501.23) and DJI (entry 51,882.53); turtle HOLD LONG GOLD at 4,400.00 (stop 4,204.93) and HOLD SHORT EURUSD in **3 units** (the only multi-unit position, 0.75% risk); BUY STOP on WTI (106.75), USDCAD (1.4105) and USDCHF (0.8262); SELL STOP on DAX (25,172.89), GBPUSD (1.3249), USDJPY (152.897) and AUDUSD (0.7033).
- **The oil ticket is stranded above the unwind.** The WTI BUY STOP at **106.75** sits ~11% above the latest cash print — FRED `DCOILWTICO` is **$96.41 on 09-22**, down from **$103.62 on 09-16** — so it is an untriggered breakout order, not a position, and it stays untriggered unless crude climbs back through its mid-September levels. The SPX Bollinger long, by contrast, is roughly **1% in profit** against FRED's `SP500` close of **7,706.03 on 09-23**.

## Honest read
Mechanized faithfully and priced honestly, the 5-Step course's signal stack **has no net edge on free daily OHLC data** — the always-on version loses outright (**−1.9%/yr on the 2026-09-24 re-run**, worse than the −1.3% booked on 2026-09-08, with every sleeve except the turtle and every asset class in the red), and the best-gated core is breakeven versus an S&P that compounds at 8.7%. That does *not* make the course worthless: what it genuinely teaches — and what this build keeps — is **process**: regime-gated selectivity, one uniform ATR risk unit, a self-correcting Kelly budget, portfolio caps, and anti-impulse mechanics. The dashboard runs that discipline live (regime strip → signals matrix → sized tickets). Contrast with the [[Trading System - Backtest (June 2026)|cross-asset trend system]], whose honest Sharpe ~0.69 needed vol-sized clusters and a bond sleeve — sizing and diversification, not extra signals, are where trend edges actually come from.

## See also
- Live dashboard (regime strip · 16-instrument signals matrix · trade tickets · audited evidence): `million dollar traders/Million Dollar Traders Dashboard.html`
- Sibling engines: [[Trading System - Backtest (June 2026)]] · [[AI Analyst Committee — Stock Selection (June 2026)]] · [[AlphaFX Smart-Money System (June 2026)]] · [[Macro Pulse — Cross-Asset Z-Score Monitor (June 2026)]] · [[Target-Beta Factor Portfolio (June 2026)]]
- Method kin: [[Leading Indicators]] (ISM), [[Average True Range (ATR)]], [[Risk Management]] (Kelly), [[Cyclical Commodities]], [[Technical Analysis & Price Action]]

*Educational; not investment advice. Every figure computed from real free data; the audit cut the headline and we published the cut.*
