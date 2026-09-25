---
title: Economic Surprises & Commodities System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "US growth surprises (expanding AR(1) residuals) → 8 commodity futures, 2000–2026 — a structured null: the broad basket is unpredicted (IC −0.03); only gold passes Bonferroni, negative and lag-fragile. Audited up front."
tags: [global-macro, strategy, commodities, surprises, growth, null-result, lag-fragile, audited-up-front, backtest]
data_vintage: "LIVE (FRED growth + Yahoo commodity futures, 2000→2026-08); engine re-run 2026-09-24 16:25"
sources: 1
updated: 2026-09-24
---

# Economic Surprises & Commodity Future Returns

A free-data port of the Macrosynergy **"Economic surprises and commodity futures returns"** notebook — the Brain's **first commodity coverage** and **first surprise-based signal**. Thesis: positive **growth surprises** (the unexpected component of activity releases) raise commodity demand and should predict positive commodity returns. Built 2026-06-24; **audited up front** (the [[the-dv01-both-legs-flattener-bug]] lesson).

> **A structured null.** On free, US-proxy growth surprises the demand thesis does not replicate: the broad commodity basket is unpredicted and timing on it loses to buy-and-hold. The only Bonferroni-passing link is **gold's negative (counter-cyclical) response** — but the audit found it **lag-fragile** (significant at lag 1 only), so it is suggestive, not robust. Research/education only.

## How it works
- **Growth-surprise composite (faithful to the notebook's ARMA-surprise):** for 4 independent US activity dimensions (industrial production, mfg new orders, durable-goods orders, payrolls — each 3m/3m annualised), the **expanding AR(1) residual** = actual − forecast(a + b·xₜ₋₁), fit point-in-time on history < t. The "news"/innovation. z-scored, averaged, lagged 1m. *(IPMAN dropped — 0.98-correlated with INDPRO; per audit F7.)*
- **Commodities (Yahoo continuous futures, monthly):** WTI, nat-gas, copper, silver, gold, corn, wheat, soybeans.
- **Tests:** per-commodity IC with **HAC (Newey-West) t**, crisis-excluded robustness, **Bonferroni** over 8 commodities, **gold lag-sensitivity** (lags 0–3), and a long/short surprise-timing overlay vs buy-and-hold.

## Outputs (`Surprise Commod/`)
- **`Surprise Commod Dashboard.html`** — light theme, Chart.js inlined: per-commodity IC (by group) and the timing overlay vs buy-and-hold, with a full diagnostics table.
- **`Surprise Commod Note <date>.md`** + **`surprisecommod_latest.json`**.
Tools: `tools/surprise_commod.py` · `surprise_commod_report.py` · `build_surprise_commod.py`.

## Result — 2000-12 → 2026-08 (n=222)
- **Growth surprise → broad commodity basket is a null: IC −0.031 (HAC t −0.40).** The "positive growth surprise → commodities up" thesis does **not** hold, and the long/short timing overlay (Sharpe −0.28; **realized vol 18.6%, ~2× its 10% target** — the trailing-vol scaler doesn't fully control tails) **destroys value** vs buy-and-hold (0.61). It loses throughout, not just one episode (ex-2020-05 Sharpe −0.25).

| Commodity | Group | IC | HAC t | p | ex-crisis IC | ex-crisis t |
|---|---|---|---|---|---|---|
| Nat Gas | energy | +0.093 | 1.89 | 0.059 | −0.004 | −0.06 |
| Copper | ind-metal | +0.089 | 0.77 | 0.44 | 0.007 | 0.10 |
| WTI Crude | energy | +0.002 | 0.01 | 0.99 | 0.134 | 1.67 |
| Wheat / Corn / Soybeans | ags | ~−0.03 to −0.07 | <0 | ns | more negative | — |
| **Gold** | precious | **−0.143** | **−3.2** | **0.0014*** | −0.106 | −2.04 |
| Silver | ind-metal | −0.147 | −1.78 | 0.076 | −0.046 | −0.72 |

*Metrics re-verified 2026-09-24 against `surprisecommod_latest.json` — **the engine was re-run today** (`as_of` 2026-09-24, `generated` 2026-09-24 16:25), on data still ending 2026-08. The headline statistics quoted above are unchanged from the 2026-09-08 refresh (`ic_basket` −0.031 / `ic_basket_t` −0.40, `perf_strategy.sharpe` −0.28 vs `perf_bh.sharpe` 0.61, window 2000-12 → 2026-08, n=222), but several table cells did move in today's run and are corrected here: gold's ex-crisis IC and t (−0.108 / −2.06 → **−0.106 / −2.04**, `per[]` sym `GC=F` `ic_ex` / `t_ex`, in both the table and the lag-fragility paragraph below); the gold lag table at lag 2 (−0.017 / −0.28 → **−0.015 / −0.25**) and lag 3's t (−0.40 → **−0.39**), from `gold_lags`; and Nat Gas's p and ex-crisis t (0.058 / −0.05 → **0.059 / −0.06**, `per[]` sym `NG=F` `p` 0.0586, `t_ex` −0.06). WTI's p-value, previously left blank, is now filled in from `per[]` sym `CL=F` `p` 0.9915. No conclusion moves with these digits — gold is still the only Bonferroni pass (`n_pass_bonferroni` 1) and still significant at lag 1 alone. The June-2026 figures remain superseded, and the audit verdicts below are unchanged and still refer to the original adversarial review.*

- **The growth-cyclicals behave as theory predicts only weakly, and not robustly:** copper and nat-gas are weakly positive full-sample but **vanish ex-crisis** (≈0) — the weak positive was the 2008/2020–22 episodes. Ags are weather-driven noise.
- **Gold is the one Bonferroni-passing link and it is NEGATIVE** (IC −0.143, t −3.2) — economically clean (a real-rate/safe-haven asset falls on positive growth surprises; the *opposite* of a demand story). **But it is lag-fragile (the audit's key finding):**

| Gold lag | IC | HAC t |
|---|---|---|
| lag 0 | −0.049 | −0.81 |
| **lag 1** | **−0.143** | **−3.2** |
| lag 2 | −0.015 | −0.25 |
| lag 3 | −0.021 | −0.39 |

Significance appears at **exactly lag 1** and collapses one month either side. A genuine monthly-persistent macro→price relationship should show a similar effect at adjacent lags; gold's does not. It *is* split-half/decade-stable (not a single-crisis fluke), but softens to t −2.04 ex-crisis. **Net: a suggestive but not robust counter-cyclical tendency — not a reliable signal.**

## Why the demand thesis fails here — the key caveat
**US growth surprises are a weak proxy for the GLOBAL growth the notebook aggregates.** Industrial commodities (copper, oil) are priced on global demand — above all China — which US activity surprises capture only partially. The notebook builds a multi-country (DM + EM) surprise panel; this rebuild has only the US, so the broad-basket null likely *understates* a true global-surprise → industrial-commodity link. A faithful test needs the global surprise panel.

## Verdict
- **A structured null — the Brain's first commodity coverage.** On free, US-proxy data, growth surprises do not predict the broad commodity complex, and timing on them loses to buy-and-hold. The only Bonferroni-passing signal is gold's counter-cyclicality, and even that is lag-fragile (suggestive, not robust).
- Dovetails with [[Sectoral Macro-Trend System]] (folder 32), where macro-cycle → *energy equities* was the one fragile flicker: the underlying commodity complex does not cleanly reward macro-surprise timing on US data.

## Audit
**Audited up front (61 agents, 3 lenses → adversarial verification → synthesis).** The **look-ahead/construction lens fully verified: construction is CLEAN** (the expanding AR(1)-surprise, 3m/3m transform, expanding-z and lag are all genuinely point-in-time — no leak). Confirmed findings applied: (F2) gold's significance is **lag-fragile** — now disclosed with the lag-sensitivity table; (F4) the strategy's "vol-targeted 10%" label was false (realizes 18.6%) and is relabelled a long/short overlay with realized-vol and ex-COVID Sharpe reported; (F6) the unused DBC fetch removed; (F7) IPMAN dropped (double-counted INDPRO); (F5) futures-roll bias kept disclosed. **Caveat on completeness:** the session token limit hit mid-run, so the **statistics-lens** (deeper multiple-testing / "is gold a real-rate/USD proxy" scrutiny) and **evaluation-lens** verifications, plus the synthesis, **did not complete** — gold's "is it just a real-rate proxy" question is therefore *not fully adjudicated*. The framing is hedged accordingly (gold = suggestive, lag-fragile, possibly a real-rate proxy). A full re-run of those lenses is a follow-up when the limit resets.

## Caveats
- **US growth surprises proxy the notebook's global panel** (the central limitation); commodity futures are **Yahoo continuous contracts** (non-roll-adjusted — injects roll discontinuities, worst for nat-gas/WTI); revised (not vintage) FRED data; the timing overlay realizes ~2× its vol target.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[Sectoral Macro-Trend System]] · [[Macro Curve-Trade Strategy]] · [[FX Signals System (Common Sense vs ML)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
