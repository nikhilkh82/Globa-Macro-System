---
title: FX Signals System (Common Sense vs ML)
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "G10-vs-USD dollar-neutral FX panel, 2000–2026: carry-only vs a common-sense composite vs walk-forward Ridge ML — carry works (Sharpe 0.41, IC t 3.61), common sense ≈ carry, and ML adds no measurable value over the prior."
tags: [global-macro, strategy, fx, carry, machine-learning, conceptual-parity, positive-result, backtest]
data_vintage: "LIVE (FRED FX + 3m rates, 2000-04→2026-08; engine re-run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# FX Signals — Common Sense vs Machine Learning

A free-data port of the Macrosynergy **"FX trading signals: common sense and machine learning"** notebook: a G10-vs-USD cross-sectional, dollar-neutral, vol-targeted strategy comparing **carry-only**, a **"common sense" conceptual-parity** composite (carry + trend + value), and a **walk-forward ML (Ridge)** combiner — against a passive long-foreign basket. Built 2026-06-23.

> **A positive result *and* a disciplined ML null:** FX carry works, a simple economic prior equals it, and machine learning adds *no measurable value* over that prior. Research/education only.

## Provenance — what we adapted
The source builds a large per-country quantamental factor set (external balances, inflation, growth, terms of trade…) and asks whether ML-learned FX signals beat a simple "common sense" conceptual-parity composite. Per-country CPI/IP are stale/absent on FRED, so we rebuild the **core comparison** on the FX factors that *are* free — **carry** (the dominant FX macro signal), **trend**, and a crude **value** proxy — and keep the headline question intact: *does ML beat the economic prior?*

## How it works
- **Panel:** 9 currencies vs USD (EUR/GBP/AUD/NZD/JPY/CHF/CAD/SEK/NOK), FRED FX spot normalised to USD-per-foreign + 3-month interbank rates.
- **FX excess return** = spot appreciation + carry `(foreign 3m − US 3m)/12`.
- **Factors** (cross-sectionally z-scored each month): **carry** (rate differential), **trend** (12-month excess-return momentum), **value** (5-year spot mean-reversion).
- **Three signals:** carry-only · **conceptual parity** = equal-weight mean of the 3 z's ("common sense") · **ML** = a walk-forward Ridge that *learns* the factor weights from pooled past (factor→forward-return) rows.
- **Portfolio:** demean the signal cross-sectionally (dollar-neutral), gross-normalise, earn t→t+1; vol-targeted to 10%. Walk-forward (factors & the Ridge fit from data < t).

## Outputs (`FX Signals/`)
- **`FX Signals Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (carry vs common sense vs ML vs passive, log), a benchmark table, and the per-month cross-sectional IC comparison.
- **`FX Signals Note <date>.md`** + **`fxsignals_latest.json`**.
Tools: `tools/fx_signals.py` · `fx_signals_report.py` · `build_fx_signals.py`.

## Result — 2000-04 → 2026-08 (n=304, 9 currencies)
| Strategy | Sharpe | MaxDD | X-sec IC (t) |
|---|---|---|---|
| Carry-only | **0.41** | −31.1% | 0.094 (t 3.61) |
| **Common sense (conceptual parity)** | 0.38 | −27.6% | 0.087 (t 3.34) |
| Machine learning (Ridge) | 0.28 | −30.9% | 0.069 (t 2.65) |
| Passive long-foreign basket | 0.07 | −43.2% | — |

*Metrics re-verified 2026-09-24 against `FX Signals/fxsignals_latest.json` (as_of 2026-09-24, generated 16:14); the 2026-09-08 figures — window through 2026-07, n=303, carry Sharpe 0.40 / IC 0.091 — are superseded. MaxDD, previously left blank, is now read from the payload. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **FX carry is the real, dominant factor** (Sharpe 0.41, cross-sectional IC 0.094, t 3.61) — and it crushes a passive long-foreign basket (0.07), so the edge is the *cross-sectional carry tilt*, not just owning foreign FX.
- **"Common sense" ≈ carry** (0.38, edge −0.03): equal-weighting carry with trend and value barely changes it — FX trend/value are weak; carry dominates the composite.
- **All three signals have individually-significant cross-sectional skill** (IC t 3.61 / 3.34 / 2.65 — including ML). But **ML adds no *measurable* value over the prior:** it's a touch lower on Sharpe (−0.10), and the gap is **within noise** (paired-t on monthly returns 1.38, on monthly IC 1.44 — both insignificant). ML neither beats nor clearly loses to common sense.
- **The drawdowns do not follow the Sharpes:** the common-sense composite has the shallowest MaxDD (−27.6%) and carry the deepest of the three active books (−31.1%) — the trend/value legs buy a little crash protection, which is the composite's only real contribution.

## Verdict
- **FX carry works (Sharpe 0.41, IC t 3.61) and a simple conceptual-parity composite is its equal** — a genuine, well-documented positive (with the usual carry caveat: it crashes in risk-off episodes).
- **Machine learning does not improve on the economic prior — there is no measurable value-add.** On a small, noisy, highly-correlated FX panel, *learning* factor weights captures nothing the simple equal-weight "common sense" prior didn't already have. The notebook's title is the finding: common sense ≈ ML. **Use ML to *test* priors, not to replace them.**

## Audit
Adversarially audited (2-lens: look-ahead/conventions + framing). **No look-ahead, and the FX inversions / carry sign / ML walk-forward are all correct** (verified by re-running the pipeline). Two medium framing fixes — and both made the writeup *fairer to ML*: (1) the original **pooled** IC was the wrong statistic for a dollar-neutral book and buried ML at 0.014 → switched to the **per-month cross-sectional IC** (carry 0.091/t3.5, cp 0.084/t3.2, **ML 0.066/t2.5 — significant**); (2) "ML loses/overfits" overstated an insignificant gap → reframed as "**ML adds no measurable value**" with the paired-t tests (1.4, insignificant) reported in-product. The Sharpe ordering (P&L) was always correct.

## Caveats
- Free-data scope: carry/trend/value only (per-country CPI/IP/external-balances are stale/absent on FRED, so the notebook's fuller quantamental macro panel isn't reproduced — disclosed); G10 vs USD; the value proxy is a crude spot mean-reversion; vol-targeted 10%; revised data.

## Related
[[Managed-Futures Trend System]] · [[ML Macro-Direction Model]] · [[Macro-Aware Risk Parity System]] · [[Robust Equity Trend System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
