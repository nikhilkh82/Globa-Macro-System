---
title: FX Carry-Valuation System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "G10-vs-USD carry + a PPP/REER valuation overlay, 2004–2026: carry is a genuine positive (IC +0.085, t 2.99, Sharpe 0.33) but REER valuation fails in G10, so adjusted carry dilutes to Sharpe 0.11 for a smaller drawdown."
tags: [global-macro, strategy, fx, carry, valuation, ppp, reer, positive-result, failed-enhancement, backtest]
data_vintage: "LIVE (FRED FX/rates + BIS REER, 2004-04→2026-08; engine re-run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Advanced FX Carry with Valuation Adjustment

A free-data port of the Macrosynergy **"Advanced FX carry strategies with valuation adjustment"** notebook. Tests whether adjusting FX carry by currency **over-/under-valuation** improves carry strategies, across a G10-vs-USD panel. Built 2026-06-24.

> **Carry works; the valuation overlay does NOT improve it here.** Carry is a genuine, significant FX signal (one of the Brain's few robust positives), but PPP/REER valuation didn't work in G10 over 2004–2026, so valuation-adjusted carry *dilutes* carry's return in exchange for a smaller drawdown — not the documented enhancement. Research/education only.

## How it works
- **Panel:** 9 G10 vs USD (EUR/GBP/AUD/NZD/JPY/CHF/CAD/SEK/NOK). FX excess return = spot (USD-per-foreign) + carry. Cross-sectional, dollar-neutral, vol-targeted 10%, walk-forward.
- **Carry** = cross-sectional z of the 3m rate differential (foreign − US). The base FX factor.
- **Valuation** = each currency's **BIS REER deviation from its own expanding (point-in-time) long-run mean** — a free PPP-overvaluation proxy (+ = over-valued/rich). **Value signal = −overvaluation** (long cheap / short rich, PPP reversion). *REER lagged 1 month for its publication lag (point-in-time).*
- **Valuation-adjusted carry** = carry_z − overvaluation_z (penalise carry in over-valued currencies, which are most carry-crash-prone).

## Outputs (`FX Carry Value/`)
- **`FX Carry Value Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 for carry vs valuation vs valuation-adjusted carry, a performance + cross-sectional-IC table, and the current tilt.
- **`FX Carry Value Note <date>.md`** + **`fxcarryvalue_latest.json`**.
Tools: `tools/fx_carry_value.py` · `fx_carry_value_report.py` · `build_fx_carry_value.py`.

## Result — 2004-04 → 2026-08 (n=268)
| Signal | Sharpe | Vol | MaxDD | x-sec IC | IC t |
|---|---|---|---|---|---|
| **Carry (3m rate diff)** | **0.33** | 10.0% | −32.1% | **+0.085** | **2.99** |
| Valuation (−REER overvaluation) | −0.26 | 8.9% | −46.4% | −0.05 | −1.94 |
| Valuation-adjusted carry | 0.11 | 7.8% | −21.7% | +0.021 | 1.04 |
| Passive long-foreign | −0.03 | 8.2% | −39.3% | — | — |

*Metrics re-verified 2026-09-24 against `FX Carry Value/fxcarryvalue_latest.json` (as_of 2026-09-24, generated 16:14); the 2026-09-08 figures — window through 2026-07, n=267, carry Sharpe 0.32 / IC 0.082 — are superseded. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Carry works (the real signal):** cross-sectional IC **+0.085 (t 2.99)**, Sharpe 0.33 — significant, **replicating [[FX Signals System (Common Sense vs ML)]]** (folder 26). High-rate currencies out-earn low-rate ones (the FX risk premium / policy subsidy). *The extra month of data (2026-08) nudged carry up, not down: the positive is unchanged in kind.*
- **PPP/REER valuation does NOT work in G10:** value-only IC **−0.05 (t −1.94)** — marginally *wrong*-signed. Cheap (under-valued) G10 currencies did not reliably revert; valuations stayed stretched for years. (Verified the sign directly: over-valued currencies had *higher*, not lower, subsequent returns — PPP-reversion genuinely failed, it's not a coding flip.)
- **So valuation-adjusted carry does NOT improve carry:** blending in a negative-IC value leg **dilutes** carry — Sharpe 0.33 → 0.11, IC 0.085 → 0.021 (insignificant). The **only** benefit is a smaller drawdown (−21.7% vs −32.1%, +10.4pp): the value tilt leans defensively away from over-valued high-yielders (softening carry crashes) — but it costs more return than it saves. *And part of that drawdown gap is still the leverage artifact the audit disclosed: on this run adj realizes **7.8%** vol against carry's **10.0%**, so it simply runs lighter.*

## Why this differs from the notebook — free-data limitations
- **No EM.** The notebook's carry+valuation works best in **emerging markets** (bigger carry, faster valuation reversion); this rebuild is G10-vs-USD only, where the valuation effect is weakest.
- **Nominal, not real, carry.** Per-country CPI is stale on FRED, so carry here is the nominal rate differential, not the notebook's inflation-adjusted *real* carry; and the valuation proxy is a simple REER-deviation, not the notebook's gap-adjusted PPP metric. Both weaken the specific enhancement.

## Verdict
- **A genuine positive (carry) with a failed enhancement (valuation) on free G10 data.** Carry is a real, significant FX signal — **confirmed across two independent builds** (this + [[FX Signals System (Common Sense vs ML)]]). But the notebook's valuation-adjustment does not improve it here: G10 PPP-reversion didn't pay over 2004–2026, so the overlay trades carry's return for a smaller drawdown. The documented enhancement likely needs **EM breadth** and **real carry** to appear.
- On *valuation* in G10: a defensive risk-reducer, not a return-enhancer, on this sample.

## Audit
**Audited up front — a lean audit (17 agents, 12/13 findings confirmed) completed and validated the build.** It confirmed the construction is **sound** (no DV01-style bug; walk-forward timing, FX inversions, carry lag, vol-target window all correct) and the **value-leg sign is genuine** (over-valued currencies had *higher* subsequent returns in G10, so PPP-reversion really fails — not a coding flip; nice mechanism note: currencies overshoot and persist). It independently flagged the **REER publication-lag** (month-t BIS REER isn't public until ~3 weeks into month t+1) — which I'd **already fixed proactively** (lagged 1 month; the audit confirms value stays negative, t ≈ −2.0, under the lag). Two **LOW** fixes applied: (1) the IC t-stat was mislabeled "HAC-style" — it's an **iid SE** over the monthly series, and carry is a slow signal so its true t is a bit under 2.89 (still significant; folder 26's full audit independently confirms carry); (2) part of the adj drawdown benefit is a **leverage artifact** (adj realizes ~7.9% vol vs carry ~9.9%), now disclosed. The earlier runs were throttled by the recurring session limit; this leaner audit was sized to complete within it.

## Caveats
- **G10-vs-USD only (no EM); nominal (not real) carry; REER-deviation (not gap-adjusted PPP);** revised (not point-in-time vintage) BIS REER on FRED; vol-targeted; IC t-stat is iid-SE (carry's effective N somewhat below 268).

## Related
[[FX Signals System (Common Sense vs ML)]] · [[the-dv01-both-legs-flattener-bug]] · [[Macro Curve-Trade Strategy]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
