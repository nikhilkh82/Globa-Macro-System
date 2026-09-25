---
title: Cross-System Synthesis — What Works
category: synthesis
type: deep-dive
data_asof: 2026-06
summary: "Capstone meta-analysis of the 17 audited Strategy Lab systems: risk premia survive (carry, trend crisis-alpha, HF replication, risk parity); macro-timing of level/curve/sectors/direction is null; 2 'wins' overturned."
tags: [synthesis, capstone, meta-analysis, risk-premia, macro-timing, efficient-markets, methodology, scorecard]
data_vintage: "aggregates audited builds, folders 17–34 (2026-06)"
updated: 2026-06-24
---

# Cross-System Synthesis — What Works

A capstone meta-analysis of every backtested strategy system in the Brain (folders 17–34): seventeen free-data, point-in-time, walk-forward, **adversarially-audited** replications of published quant / Macrosynergy strategies. The interactive [Strategy Scorecard](../../Synthesis/Strategy%20Scorecard.html) ranks them all. This page distils what the whole exercise actually showed.

> **The one-line finding: risk premia survive; macro-timing does not.** Every robust positive is a *risk premium you get paid to bear*. Every attempt to *time* markets from lagged public macro is a null. The market is efficient with respect to lagged public macroeconomic data — you are compensated for bearing risk, not for forecasting it from information everyone already has.

## The scorecard — 5 positive, 1 marginal, 8 null, 2 corrected, 1 support
### What worked (robust positives — and *why* they work)
| System | Asset | What it is | Why it pays |
|---|---|---|---|
| FX carry ([[FX Signals System (Common Sense vs ML)]] 26 + [[FX Carry-Valuation System]] 34) | FX G10 | long high-rate / short low-rate | the **carry risk premium** — compensation for crash risk; IC ~0.08–0.09, t ≈ 3.5 (folder 26) / ≈ 2.9 (folder 34, iid SE — modestly lower under autocorrelation), significant in **two independent builds** |
| Managed-futures trend ([[Managed-Futures Trend System]] 19) | multi-asset | diversified TSMOM | the **trend premium as crisis-alpha** — −0.23 equity corr, +2.7% in the worst-decile equity months |
| Hedge-fund replication ([[Hedge-Fund Replication System]] 21) | multi-asset | 5-ETF linear clone | liquid multi-strat HF return is mostly **factor beta** — replicable (OOS corr 0.82), so mostly no 2&20 |
| Risk parity ([[Macro-Aware Risk Parity System]] 24) | eq/duration | inverse-vol + defensive macro overlay | **diversification** (RP Sharpe 0.62); the macro overlay only earns as 2022 *insurance* |

**The pattern:** all four are **premia / structural exposures** (carry, trend-as-insurance, factor beta, diversification) — things you are *paid to hold or bear*, not forecasts.

### What didn't — the macro-timing nulls
Every system that tried to **predict a market from lagged macro** was a null (doesn't beat passive on free, point-in-time, multiple-testing-corrected data):
- **Direction:** [[ML Macro-Direction Model]] (17, equity), [[Credit ML Classification System]] (29, credit) — accuracy ≈ the long base rate, *no skill*.
- **The level of rates / the curve:** [[Macro Curve-Trade Strategy]] (20), [[Treasury Macro-Trend System]] (28, curve leg), [[Information State Changes System]] (30) — nulls. *(Folder 28 is the lone **marginal** system: its directional-trend leg ≈ buy-and-hold, while its curve leg was retracted — see below.)*
- **Sectors:** [[Macro Sector Rotation System]] (27), [[Sectoral Macro-Trend System]] (32) — crushed by the equal-weight basket.
- **Equities (trend):** [[Robust Equity Trend System]] (25) — equity-only TSMOM is the weakest trend class.
- **Allocation timing:** [[Macro Regime Allocation Engine]] (23) — regime *switching* adds ~+0.02 Sharpe over a static blend.
- **Commodities:** [[Economic Surprises & Commodities System]] (33) — growth surprises don't time the complex.

### What the audit caught — corrected "positives"
Two results looked like wins and were **artifacts the adversarial audit overturned** — see [[the-dv01-both-legs-flattener-bug]]:
- [[Macro Demand-Based Rates System]] (31): a "strong" demand→curve result (t 4.48) was a **DV01 construction bug** (the 2y leg over-weighted ~4.5×). Corrected → null. The *same bug* had quietly inflated the curve legs of folders 20 and 28.
- [[Sectoral Macro-Trend System]] (32): an "energy works" narrow positive was **collinear, tail-driven, and failed multiple-testing** → fragile null.

## The five recurring lessons
1. **Markets are efficient with respect to lagged public macro.** Revised, public macro data doesn't time the level, curve, sector, or direction of US markets — across rates, equities, credit, commodities, FX. The information is already in the price. The premia that *do* pay (carry, trend) are compensation for risk, not forecasts.
2. **The bar is the passive premium, not zero.** For high-positive-base-rate single markets (credit, equities), "60% accuracy" or "positive Sharpe" can just be *being long*. The honest benchmark is the long base rate / buy-and-hold, and most "edges" don't clear it. (Cross-sectional, dollar-neutral books fix this by construction — which is partly why FX carry's cross-sectional IC is the cleanest positive.)
3. **ML adds nothing over the economic prior.** Three ML builds (17, 26, 29) all reduced to: ML ≈ the common-sense composite ≈ the base rate. ML can't learn alpha that isn't there; it mostly relearns the risk premium (or overfits noise).
4. **Construction correctness ≠ no look-ahead.** The DV01 bug passed every look-ahead and inline check because the leak wasn't temporal — it was a financial-engineering error in the instrument. A *strong* result needs a dedicated construction-correctness check, and **a deferred/inline audit is not a substitute for the formal adversarial one** — the audit caught a result-invalidating bug across three builds that inline checks all missed.
5. **A single significant t-stat is not enough.** The survivors needed to clear crisis-exclusion, multiple-testing (Bonferroni/BH), collinearity, *and* lag-stability. Gold's −3.14 (folder 33) was significant at *exactly* one lag; the sector-macro "winners" were two collinear measurements of one tail-driven signal. Robustness is multi-dimensional.

## The honest bottom line
A disciplined, free-data, point-in-time replication of ~15 distinct published macro/quant strategies (17 system builds) finds that **the durable sources of return are risk premia and diversification — carry, trend-as-crisis-alpha, factor beta, risk parity — not macro forecasting.** That is not a disappointing result; it is the *correct* one, and it matches decades of academic evidence. The value the macro adds is as a **regime read and a risk lens** (when to expect carry crashes, when the curve is cycle-stretched, what the cross-asset state is) — not as a monthly timing signal. The adversarial-audit discipline was the hero of the project: it converted three would-be "discoveries" into honest nulls and kept the scorecard truthful.

## Provenance & method
Each system: free data (FRED + Yahoo + BIS REER + CFTC COT), strictly point-in-time / walk-forward, vol-targeted where applicable, HAC (Newey-West) t-stats for autocorrelated signals, cross-sectional IC for dollar-neutral books, and an adversarial multi-agent audit (look-ahead + construction + evaluation + statistics lenses → per-finding refutation → synthesis). Caveats that recur: US-centric (per-country/global and EM data are stale or non-free on FRED), revised (not point-in-time vintage) data, and free-data proxies for paid quantamental indicators — each disclosed on its own page. Scorecard: `tools/synthesis_scorecard.py`.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[FX Signals System (Common Sense vs ML)]] · [[FX Carry-Valuation System]] · [[Managed-Futures Trend System]] · [[Hedge-Fund Replication System]] · [[Macro-Aware Risk Parity System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]] · [[Systematic Trading — Factors, Risk Premia & Risk Parity|Systematic Trading — factors, risk premia & risk parity]]
