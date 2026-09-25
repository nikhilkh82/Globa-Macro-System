---
title: The DV01 Flattener-Construction Bug
category: meta
type: meta
data_asof: 2026-06-23
summary: "The DV01 flattener-construction bug: a 2s10s curve trade must weight each leg by its own annuity; weighting both by the 10y annuity over-levers the 2y leg 4.0-4.6x and faked 'macro predicts the curve' in builds 20/28/31."
tags: [methodology, lesson, rates, curve, dv01, construction-bug, audit, correction]
updated: 2026-06-23
---

# The DV01 Flattener-Construction Bug — a cross-build correction

A methodology note recording a **construction error that faked "macro predicts the yield curve" across three builds** ([[Macro Curve-Trade Strategy]] · 20, [[Treasury Macro-Trend System]] · 28, [[Macro Demand-Based Rates System]] · 31), how it was caught, and how to build a curve trade correctly. Recorded 2026-06-23.

## The bug
A 2s10s curve-trade monthly return was written as `±A₁₀·Δ(y10 − y2)` with `A₁₀ = annuity(y10, 10)`. Algebraically that is `±A₁₀·Δy10 ∓ A₁₀·Δy2` — it applies the **~10-year annuity (~7.9) to the 2y leg as well**, over-weighting the front-end yield change by `A₁₀/A₂ ≈ 4.0–4.6×`. Because macro→curve signals work almost entirely through the **front end** (excess demand → the Fed hikes the 2y), this mis-weighting turns the "flattener" into a ~99% over-levered **short-2y** position and **mechanically manufactures predictability** the curve shape does not actually have.

## The correct DV01-neutral construction
Weight each leg by **its own annuity** `A(T,y) = (1 − e^{−yT})/y`:
- **Flattener** (long 10y duration + short 2y): `flat = (−A₁₀·Δy10 + A₂·Δy2) / 100`
- **Steepener** (short 10y + long 2y): `steep = ( A₁₀·Δy10 − A₂·Δy2) / 100`
- `A₁₀ = annuity(y10ₚ/100, 10)`, `A₂ = annuity(y2ₚ/100, 2)`.

Sanity: a flattener gains when y10 falls (`−A₁₀·Δy10 > 0`) or y2 rises (`+A₂·Δy2 > 0`). **Always decompose by leg** and report the 2y-leg IC vs the 10y-leg IC — if the "curve" signal is really just one leg, it is a level/direction bet, not a curve-shape trade.

## What it cost — the three corrections
The 22-agent adversarial audit of folder 31 caught it, independently reproduced the corrected null on FRED data, and verdict was **RESULT_INVALID**. Fixing it collapsed every "curve works" result:

| Build | Curve result before (buggy) | After (DV01-neutral) |
|---|---|---|
| [[Macro Demand-Based Rates System]] (31) | flattener IC 0.236 (t 4.48) | **IC 0.029 (t 0.66) — null** |
| [[Treasury Macro-Trend System]] (28) | curve trend IC 0.166 (t 4.0); pure-macro IC 0.152 | **curve trend IC −0.044 (t −0.99); pure-macro IC 0.063 — gone** |
| [[Macro Curve-Trade Strategy]] (20) | Pearson IC 0.12 | **IC 0.076 (t 1.55)** — was already a null, conclusion unchanged |

**Net honest finding:** on free revised US data, lagged macro reliably times **neither** the rates level **nor** a properly DV01-neutral curve shape. The earlier cross-build thesis *"macro times the curve's shape, not the level"* was a shared construction artifact and is **retracted**.

## The load-bearing process lesson
Folder 31's formal audit was initially **deferred** (a session limit), and in its place inline self-checks were run — sub-sample robustness, base-rate, concentration, look-ahead. They **all passed** while completely missing the bug, because they were all *downstream of the buggy target construction*. None examined the financial-engineering correctness of the DV01 weighting; the formal audit's dedicated construction lens expanded the algebra and re-ran on real data.

- **Inline checks are not a substitute for the formal multi-agent audit.** Never publish a backtest result on inline checks alone.
- **A strong/positive result deserves MORE scrutiny, not a deferred audit.** The instinct to "ship the win" is exactly when to slow down.
- **A passing look-ahead audit does not certify instrument construction.** Leak-free ≠ correctly built. Add a "construction correctness" lens for any synthetic instrument (curve trades, total returns, spreads, vol).

## Related
[[Macro Curve-Trade Strategy]] · [[Treasury Macro-Trend System]] · [[Macro Demand-Based Rates System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
