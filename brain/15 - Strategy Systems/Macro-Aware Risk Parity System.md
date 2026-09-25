---
title: Macro-Aware Risk Parity System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Inverse-vol SPY/synthetic-10y risk parity with a defensive-only overheating overlay, 1996–2026 — positive-but-honest: risk parity is robust (0.62); the overlay (0.69) is 2022 insurance (−21.7% → −4.1%)."
tags: [global-macro, strategy, risk-parity, equity-duration, overheating, macro-overlay, positive-result, backtest]
data_vintage: "LIVE (SPY + synthetic 10y TR + FRED, 1996-05→2026-08; engine run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Macro-Aware Equity-Duration Risk Parity

A free-data port of the Macrosynergy **"Macro-aware risk parity"** notebook: classic inverse-vol **equity–duration risk parity**, vol-targeted, with a point-in-time **overheating** overlay that de-risks when the economy overheats — the regime that historically *breaks* risk parity (2022). Built 2026-06-23.

> **A positive-but-honest result:** risk parity itself is robust, and the overheating overlay is *purely defensive insurance* — it earns its keep in 2022 and costs only a small premium otherwise. Research/education only.

## Provenance — what we adapted
The source is a Macrosynergy quantamental notebook (paid JPMaQS, multi-country) studying the "Macro Factors of the Risk-Parity Trade." The thesis: risk parity thrived through the disinflationary *golden decades* but suffers when the economy overheats (rates rise, the equity-bond correlation flips positive, both legs fall together). The macro-aware idea: scale the risk-parity book by an **overheating / slack** score. We kept that idea and rebuilt it on free US data.

## How it works
- **Risk-parity book:** equity (SPY total return) vs **duration** (a synthetic 10y Treasury total return from FRED DGS10 = carry − duration·Δy). Inverse-vol weights from each leg's trailing 36-month vol, vol-targeted to 10%.
- **Overheating composite (FRED, point-in-time z, ≥36m, lagged 1m):** average of z-scored CPI YoY, capacity utilisation (TCU), industrial-production YoY, wage growth (AHETPI), and inverse-unemployment. High = overheating.
- **Defensive overlay:** exposure = clip(**0.25, 1.0**, 1 − 0.5·overheat_z) — it only ever *reduces* the book when overheating is high; it **never levers above the vanilla book**. (A symmetric version that levered into "slack" added uncompensated risk — the audit caught this; the defensive cap is both more faithful to the thesis and cleaner.)
- **Walk-forward:** weights & overheating z from data ≤ t; macro lagged 1 month; the book earns t→t+1; ends at the last completed month.

## Outputs (`Risk Parity/`)
- **`Risk Parity Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (macro-aware vs vanilla vs 60/40, log), the **overheating-exposure-over-time** line (visibly cutting risk in 2022), a benchmark table, and the 2022 cushion KPI.
- **`Risk Parity Note <date>.md`** + **`riskparity_latest.json`**.
Tools: `tools/risk_parity.py` · `risk_parity_report.py` · `build_risk_parity.py`.

## Result — 1996-05 → 2026-08 (n=364 monthly, vol-targeted 10%)
| Strategy | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| **Macro-aware risk parity** | **0.69** | 7.08% | 7.0% | −18.9% |
| Vanilla risk parity | 0.62 | 7.22% | 8.2% | −22.3% |
| 60/40 (equity/duration) | 0.64 | 8.07% | 9.3% | −29.5% |
| All-equity (SPY) | 0.57 | 10.34% | 15.3% | −50.8% |

*Metrics re-verified 2026-09-24 against `Risk Parity/riskparity_latest.json` (engine run `generated` 2026-09-24 16:25, data through 2026-08). Every Sharpe/CAGR/MaxDD above is unchanged from the 2026-09-08 refresh — the completed-month window is still n=364 ending 2026-08 — and the vol / 60-40 / SPY cells previously left blank are now filled from `perf_rpm`, `perf_rp`, `p6040` and `peq`. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Full-sample overlay edge +0.07 Sharpe** (0.62 → 0.69), MaxDD −22.3% → −18.9%.
- **The benefit is the 2022 overheating episode:** vanilla risk parity lost **−21.7%** in 2022 (equities + duration sold off together); the overlay, having de-risked on the overheating signal, lost only **−4.1%**.
- **Ex-2022 it is near-neutral — a small insurance premium, not uncompensated risk:** macro-aware 0.73 (**7.1% vol**, MaxDD −18.9%) vs vanilla 0.77 (**7.8% vol**, MaxDD −20.5%) → −0.04 Sharpe (`overlay_edge_ex2022`) but at **lower** vol and a slightly **shallower** drawdown. The cost is a touch of return given up by occasionally de-risking, not extra risk.
- **Current read — 2026-09-24 run:** the overheating composite sits at **+0.17 z** (`current_overheat`), so the defensive overlay holds the book at **0.91×** exposure (`current_exposure`) — consistent with the clip(0.25, 1.0, 1 − 0.5·z) rule above, and only a token de-risk. The overlay is close to dormant right now; nothing like the deep cut it took in 2022.

## Verdict
- **Risk parity itself is a robust diversified book** (Sharpe 0.62, ahead of all-equity 0.57, ~matching 60/40 0.64) — the equity/duration risk balance works.
- **The macro-aware overlay is purely defensive overheating insurance:** spectacular in 2022 (−21.7% → −4.1%, full-sample MaxDD −22.3% → −18.9%), near-neutral otherwise (a small premium paid at *lower* vol). The +0.07 full-sample Sharpe is honestly 2022-concentrated — not a free all-weather edge, but unlike a symmetric tilt it **never adds uncompensated risk**. A more *positive* result than the timing nulls ([[Macro Regime Allocation Engine]], [[Macro Curve-Trade Strategy]]) because it's defensive insurance against a real, documented failure mode rather than a return-timing claim.

## Audit
Adversarially audited (2-lens: look-ahead + 2022-concentration honesty). **No look-ahead leak** (causality clean). The substantive catch (medium): the original *symmetric* overlay levered up to 1.5× into "slack," which ex-2022 ran **hotter** (8.7% vs 7.8% vol) for a *lower* Sharpe — uncompensated risk, and the "−0.04 ex-2022" understated it. **Fix:** made the overlay **purely defensive** (cap 1.0×) — now ex-2022 it runs *lower* vol with a slightly better drawdown, so the −0.03 is a genuine small premium. Also surfaced the ex-2022 vol/MaxDD (the MaxDD improvement is likewise 2022-concentrated). The audit improved the *design*, not just the disclosure.

## Caveats
- The synthetic 10y Treasury TR excludes roll-down/convexity; US-only; revised (not vintage) FRED data; the overheating composite is predefined (not fitted); 1-month macro lag approximates release timing.

## Related
[[Systematic Trading — Factors, Risk Premia & Risk Parity]] · [[Managed-Futures Trend System]] · [[Macro Regime Allocation Engine]] · [[Hedge-Fund Replication System]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
