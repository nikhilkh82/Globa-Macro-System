---
title: Macro Regime Allocation Engine
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Growth×inflation regime (FRED, lagged) → 4-quadrant ETF playbook + VIX>20 overlay, 2008–2026, all legs vol-matched — near-null: switching adds +0.02 Sharpe. Current call: Reflation, unchanged since 2026-06."
tags: [global-macro, strategy, regime, tactical-allocation, growth-inflation, vix-overlay, near-null, backtest]
data_vintage: "LIVE (FRED + Yahoo ETFs, 2008-07→2026-08; engine run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Macro Regime Allocation Engine

A free-data port of the rule-based core of **[adithya3670/macro-signal-engine](https://github.com/adithya3670-stack/macro-signal-engine)** — classify the **growth × inflation regime** from FRED, apply a *predefined* economic playbook across asset ETFs with a VIX de-risk overlay, and backtest walk-forward. Built 2026-06-23.

> **An honest near-null on regime *timing*** — when every leg is risk-matched, regime switching adds essentially nothing; the value is diversification / tail-control, not macro timing. Research/education only.

## Provenance — what we adapted
The source is a Flask macro-backtesting platform: a `RegimeStateEngine` (rule states — inflation>3%, growth>0, VIX>20 — plus a latent regime) feeding a `RotationalStrategy` (inverse-vol, vol-targeted, VIX-regime-filtered rotation). Its signal layer is a heavy **deep-learning ensemble** whose trained artifacts are excluded from the public repo. We kept the **reproducible rule-based core** and dropped the DL, so the result is fully transparent and free.

## How it works
- **Regime (FRED, point-in-time, 2-month publication lag):** growth = INDPRO YoY + payrolls YoY (>0 = up), inflation = CPI YoY (>3% = high, the source's threshold) → the classic 4-quadrant regime: **Goldilocks / Reflation / Stagflation / Deflation**.
- **Predefined playbook (macro theory, NOT fitted):** Goldilocks → equities+credit+bonds; Reflation → commodities+gold+equities; Stagflation → gold+commodities+cash; Deflation → long bonds+gold. A **VIX>20 overlay** moves half the risk-asset (SPY/HYG/DBC) weight to T-bills.
- **Walk-forward:** regime from macro ≤ t (lagged), the portfolio earns month t→t+1, ends at the last completed month. Asset menu = SPY/TLT/IEF/DBC/GLD/HYG + cash (T-bill).
- **Risk-matched evaluation:** *every* leg — regime, the static blend, 60/40, equal-weight — is vol-matched to 10% with the same causal trailing-vol target and the same VIX overlay, so Sharpe and MaxDD are like-for-like and the regime-switching effect is cleanly isolated.

## Outputs (`Macro Signal/`)
- **`Macro Signal Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (regime vs 60/40 vs static blend), a benchmark table, the regime-distribution bar, current allocation, and regime-conditional returns.
- **`Macro Signal Note <date>.md`** + **`macrosig_latest.json`**.
Tools: `tools/macro_signal.py` · `macro_signal_report.py` · `build_macro_signal.py`.

## Result — 2008-07 → 2026-08 (n=217 monthly, every leg vol-matched to 10%)
| Strategy | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| **Macro regime allocation** | **0.69** | 8.30% | 10.3% | **−15.6%** |
| Static blend (same assets, **no switching**) | 0.67 | 7.22% | 9.0% | −17.3% |
| 60/40 (SPY/IEF) | 0.78 | 9.27% | 10.3% | −20.7% |
| Equal-weight menu | 0.57 | 6.67% | 9.9% | −18.7% |
| All-equity (SPY, raw) | 0.74 | 12.35% | 15.6% | −41.8% |

*Metrics re-verified 2026-09-24 against `Macro Signal/macrosig_latest.json` (engine run `generated` 2026-09-24 16:21, data through 2026-08). Every Sharpe/CAGR/vol/MaxDD above is unchanged from the 2026-09-08 refresh — the sixteen extra days of data did not move the completed-month window (still n=217, ending 2026-08), and the 2026-09-16 run in between printed the same table. The SPY CAGR/vol cells previously left blank are filled from `pspy`. The audit verdicts below are unchanged and still refer to the original adversarial review.*

Regime distribution over the sample (`regime_dist`): Goldilocks 106, Deflation 52, Reflation 52, Stagflation 7.

**Current regime: `Reflation`** — and it is not new. The engine has classified Reflation since the **2026-06** return month (`regimes` / `labels`, `macrosig_latest.json`; the last transition in the series is 2026-05 Goldilocks → 2026-06 Reflation) and already printed it at the 2026-09-08 and 2026-09-16 runs — both `Macro Signal Note`s read "current regime **Reflation** (VIX 16.0)". 2026-09-24 (`as_of`) is the date this was re-verified, **not** the date of the call: nothing flipped today. What today's refresh corrects is this page's own **Goldilocks** line, which had been stale against the engine's own output since the 2026-09-08 refresh. The engine's VIX read is **16.0** (`current_vix`) — well below the >20 de-risk trigger — so the full Reflation playbook is on: **SPY 30% / DBC 30% / GLD 20% / HYG 20%** (`current_weights`). **The latest prints are not what turned it.** The classification turned at the 2026-06 return month (`regimes`), i.e. on macro from roughly **2026-04** under the engine's own 2-month publication lag. Today's calendar-keyed FRED prints do sit on the Reflation side of the rules — CPI YoY Aug-2026 **+3.35%**, Jul **+3.30%** (`CPIAUCSL.yoy_pct` / `prev_month_yoy_pct`, `tools/macro_pack.json`, `yoy_base_date` 2025-08-01), above the source's 3% "high inflation" line, with growth positive (INDPRO **+1.42%** YoY) — but they are not the input the engine classified on, and headline CPI YoY is decaying *toward* that threshold from above rather than crossing it (the vault's Macro Signal Stack page records **4.17%** for May-2026 against 3.35% in Aug).

**Three engines, three answers — stated, not harmonised.** This page's regime label is the lagged-FRED 4-quadrant classifier only. The endo/exo template (recalculated 2026-09-24 16:15) scores US endo **+19, "Mildly Inflationary"** (`scores_cache.json`); the Workbook Explorer's separate workbook engine card reads US **+36**, "Inflationary overall" (`Workbook Explorer/wb_explorer.json`, `asof` 2026-09-23). All three lean inflationary, which is the only thing they agree on — they run on different inputs and different scales, and none is a cross-check on the others. Do not read the +19/+36 scores as confirming "Reflation."

## Verdict
- **Regime *switching* adds essentially nothing.** At matched risk and with the identical VIX overlay, the regime allocation (0.69) barely beats a static blend of the same assets (0.67) — a clean **switching edge of +0.02 Sharpe**. The diversified menu + the VIX overlay, not the macro regime calls, do the work.
- **It trails a vol-matched 60/40 on risk-adjusted return** (0.69 vs 0.78).
- **Its one genuine, risk-matched edge is drawdown:** −15.6% MaxDD vs 60/40's −20.7% (and SPY's −42%) — but mostly the diversified menu + overlay (the static blend already reaches −17.3%); switching only tightens it modestly. **The honest value is diversification / tail-control, not macro timing** — consistent with the literature that regime-based tactical allocation rarely beats static diversified benchmarks out-of-sample once publication lags are respected. Same recurring Brain lesson as [[ML Macro-Direction Model]] and [[Macro Curve-Trade Strategy]].

## Audit
Adversarially audited (2-lens: look-ahead + evaluation honesty). The **load-bearing fix (HIGH):** the original applied the vol-target + VIX overlay **only to the strategy, not the benchmarks** — so the shallow drawdown over-credited the regime engine and the "switching edge" was confounded. Now **all legs are vol-matched with the same overlay**, isolating switching cleanly (the +0.02 result survives, and the drawdown comparison is fair). Also fixed: the partial current month is dropped (ends at the last completed month). The honest near-null held throughout — the audit *tightened* the framing rather than overturning it.

## Caveats
- US ETFs; 2-month macro lag approximates true release lags (INDPRO/payrolls are also revised); revised (not vintage) FRED data; Stagflation has only 7 months (per-regime reads are thin).
- The growth proxy sums INDPRO YoY + payrolls YoY (sign of the composite, not a calibrated index).

## Related
[[Managed-Futures Trend System]] · [[Macro Curve-Trade Strategy]] · [[ML Macro-Direction Model]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
