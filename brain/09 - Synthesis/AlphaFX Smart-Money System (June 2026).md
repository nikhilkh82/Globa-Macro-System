---
title: AlphaFX Smart-Money System (June 2026)
category: synthesis
type: strategy-system
data_asof: 2026-09-24
summary: "Systematic SMC/ICT FX reversal strategy (10 majors, daily, 2000–2026): re-run 2026-09-24 gives +0.034R/trade, PF 1.05, CI [−0.06,+0.13] spanning zero — and the random control now also pays, so the null hardens."
tags: [global-macro, forex, smart-money, smc, ict, price-action, backtest, honest-negative]
data_vintage: "LIVE — free Yahoo daily FX OHLC, 2000-01-03 → 2026-09-24 (alphafx_latest.json meta.start/meta.end, run asof 2026-09-24)"
sources: "Adapted from the AlphaFx Global 'Advanced Forex Mastery' (SMC/ICT) course"
updated: 2026-09-25
---

# AlphaFX Smart-Money System (June 2026)

**What it is & why it matters** — A systematic, deterministic reconstruction of the **AlphaFx "Advanced Forex Mastery"** course — a **Smart-Money-Concepts (SMC / ICT)** price-action method (liquidity sweeps, order blocks, fair-value-gaps, premium/discount structure, Wyckoff). It adds a **price-action / liquidity reversal** lens to the project's FX toolkit, which is otherwise top-down (macro **trend + carry + endo/exo**). The honest punchline up front: this is a **rigorously look-ahead-clean research harness** that returns an **honest negative result** — on free daily data the SMC edge is *tiny and not statistically significant*, and on the **2026-09-24 re-run it is no longer clearly better than a fair random control**. That finding is itself valuable: it guards against deploying the curve-fit SMC backtests that flood retail FX.

## The course → rules (the four pillars)
The video curriculum (liquidity, order blocks/mitigation, inefficiency, advanced market structure, Wyckoff, sessions, divergence, R:R) was codified into four **strictly causal** daily-bar pillars (a swing pivot is usable only `k=3` bars after it prints):

| # | Pillar (course concept) | Deterministic daily rule |
|---|---|---|
| 1 | **Structure** (BOS/CHoCH) | state machine over confirmed swings sets the only allowed direction — fade *with* the trend |
| 2 | **Liquidity sweep** (stop-hunt) | grab a prior swing's liquidity then close back inside with a confirming body (≥0.1·ATR penetration + reclaim) |
| 3 | **Premium/Discount** (location) | longs only in the discount half, shorts only in the premium half of the dealing range |
| 4 | **Inefficiency / FVG** (confluence) | an unfilled displacement-grade fair-value-gap in the trade direction |

**Exit (Lecturer 3, R:R):** stop beyond the swept swing (swing ∓ 0.5·ATR), target **2R**, 20-day time-stop, same-bar ties resolved **stop-first** (conservative). Event-driven, decision at `close[t]`, fill at `open[t+1]`.

## Result — honest
**851 trades** across 10 FX majors, **2000-01-03 → 2026-09-24** (`meta.start` / `meta.end`, run `meta.asof` 2026-09-24), 0.5% risk/trade (`meta.params.risk_pct`):

| Metric | Core (3-pillar) | Fair random control | 4-pillar (FVG) |
|---|---|---|---|
| Trades | 851 | 826 | 35 |
| Win % | 35.5 | 42.7 | 42.9 |
| Expectancy | **+0.034R** | +0.019R | +0.304R |
| Profit factor | 1.05 | 1.04 | 1.55 |

*Source keys: `stats.*`, `baseline.*`, `byfvg.with_fvg.*` in `alphafx smc/alphafx_latest.json` (asof 2026-09-24). The whole R-stream is **+29.1R** (`stats.totR`); compounded at 0.5% risk that is a **monthly Sharpe 0.14, +0.5%/yr, max drawdown −18.1%** (`monthly.sharpe / .ann / .maxdd`) — i.e. the "edge" is invisible at the equity-curve level.*

- **The margin over the fair random control has all but closed.** The control (identical swing-anchored stops, only the entries randomised) was *flat* on the June-2026 run (−0.001R, PF 1.00); on the 2026-09-24 run it **earns +0.019R at PF 1.04** (`baseline.avgR` / `baseline.pf`), so the SMC entries beat random by only **≈0.015R** rather than ≈0.048R. The strategy's own bootstrap **95% CI on expectancy is [−0.060, +0.127]R — it includes zero**, and P(≤0) has risen to **0.236** (`significance.avgR_ci`, `significance.p_le0`). **The edge is not statistically significant, and is now less distinguishable from random entry than it was in June.**
- The eye-catching **4-pillar FVG "confluence" result (PF 1.55) is still small-sample noise** — on 35 trades its CI is [−0.143, +0.800] and the permutation test gives **p = 0.107** (`significance.fvg_ci`, `significance.fvg_p`), so it remains indistinguishable from a random 35-trade draw. It is *not* evidence the course's "stack your confluences" claim works.
- **After spreads/slippage the strategy is plausibly break-even**, and at +0.034R the cushion is thinner than June's +0.047R. Long/short remain broadly symmetric — long 436 trades at +0.045R (PF 1.07), short 415 at +0.022R (PF 1.04) (`perdir.long/.short`) — so the small edge is at least not a one-sided USD artefact.
- **The total is two pairs, not a method.** Of the +29.1R, **USDCHF alone supplies +23.1R** (57 trades, +0.405R, PF 1.80) and GBPUSD +13.0R, while **EURGBP subtracts −18.0R** (113 trades, −0.160R, PF 0.77) and AUDUSD −7.6R (`perpair.*.totR`). A result that concentrated in one cross is the signature of noise, not of a structural edge.

> **Re-run 2026-09-24 — digits refreshed, headline verdict unchanged, one supporting claim flagged.** The engine was rebuilt today (`alphafx smc/alphafx_latest.json`, `meta.asof` 2026-09-24) over 2000-01-03 → 2026-09-24 (`meta.start`/`meta.end`) with **851 trades**, 11 more than the 840 this page carried from the June run. The window label needs care: the page previously described that run as a 2003 start, which cannot be reconciled with an 11-trade increase — `monthly.cumR` puts ~3.4% of the sample's gross R before 2003, i.e. tens of trades, so either the June run already started in 2000 and the old label was wrong, or the overlap lost trades an unchanged deterministic engine cannot lose. Treat the June→September comparison as like-for-like on the digits only; the window discrepancy is unresolved. The null verdict is **unchanged and harder**: expectancy +0.047R → **+0.034R**, PF 1.07 → **1.05**, P(≤0) 0.16 → **0.236**. **Flagged for re-audit:** the June audit's supporting finding that "the SMC signal beats a fair random control" no longer holds cleanly — the control has moved from −0.001R/PF 1.00 to **+0.019R/PF 1.04**, leaving a ≈0.015R gap that the bootstrap CI cannot separate from zero. This weakens a *sub-claim* of the audit below; it does not reverse its conclusion, and the audit's own text is left as the record it is. **No setup fires today** — all ten pairs carry `sweep: 0` and `signal: "—"` in `setups[]` (dated 2026-09-24).

> **Adversarially audited (2026-06-21).** The engine is **look-ahead-clean to the strongest standard** — every signal column recomputed on a *truncated price prefix* `df[0:t+1]` matched the full-series value on every sampled bar (the gold-standard test that most SMC backtests fail: swing pivots are exposed only `k` bars after they print, entries fill at the next open, stop/ATR are known at the decision bar). The audit's sobering economic findings — fair control is flat, edge insignificant, FVG result is noise, ~break-even after costs — are **incorporated above and on the dashboard**, not hidden. A data-hygiene fix (clamping 278 Yahoo print-glitch opens into their bar) is applied.

## What this teaches
The disciplined version of an honest answer: **Smart-Money-Concepts, mechanised on daily bars, is not a robust standalone edge.** Where practitioners claim SMC pays is in **intraday execution, session timing (London/NY killzones) and discretionary context** — none of which free daily data can test, and all of which are far more prone to over-fitting and hindsight. This harness is the rigorous null check: it shows the *structural* SMC concepts, applied mechanically and honestly, do not by themselves clear the bar of statistical significance. **The refreshed sample moved the result the wrong way, not the right one** — the 2026-09-24 re-run adds three months at the end (the run spans 2000-01-03 → 2026-09-24; whether June’s run shared that start is unresolved — see the block above) and the outcome is expectancy down (+0.047R → +0.034R), P(≤0) up (0.16 → 0.236), and the random control now paying about as well. That is exactly what a no-edge process looks like as its sample grows. Useful as a falsification tool and a foundation to extend (intraday data, order-block zones, the divergence pillar), not as a deployable system.

## See also
- Dashboard (performance, the honest value-checks, live setups): open `alphafx smc/AlphaFX Smart-Money Dashboard.html`.
- Sibling strategies: [[Trading System - Backtest (June 2026)]] (cross-asset trend+carry), [[AI Analyst Committee — Stock Selection (June 2026)]] (single-stock). The project's macro FX engine: [[USD & G10 FX]], [[FX Endogenous-Exogenous Framework]]. Risk discipline: [[Risk Management]]. Price-action lineage: [[Technical Analysis & Price Action]].

*Educational; not investment advice. Every figure is computed from free data and reproducible — no fabricated performance, and the negative result is reported as honestly as a positive one would be.*
