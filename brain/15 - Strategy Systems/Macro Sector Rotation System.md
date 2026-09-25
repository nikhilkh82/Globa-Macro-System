---
title: Macro Sector Rotation System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Predefined (not fitted) sector × macro-factor sensitivity matrix, dollar-neutral over 9 SPDR sectors, 2002–2026 — a clean null: IC ≈ 0, long-short Sharpe 0.02 vs 0.74 for the equal-weight basket."
tags: [global-macro, strategy, sector-rotation, equity-sectors, macro-factors, null-result, backtest]
data_vintage: "LIVE (9 SPDR sectors + FRED, 2002-03→2026-08; engine run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Macro Sector Rotation

A free-data port of the Macrosynergy **"Sectoral equity factors"** notebook: allocate *across* equity sectors within a country using macro factors. Different sectors have different macro sensitivities — financials like rising rates, energy likes inflation, tech/discretionary like growth but dislike duration, utilities/staples are defensive bond-proxies. Built 2026-06-23.

> **A clean, well-cross-checked null:** macro-driven monthly sector rotation has *no* cross-sectional predictive power and is comprehensively beaten by simply holding the sector basket. Research/education only.

## Provenance — what we adapted
The source studies how macro trends drive sectoral equity indices and tests cross-sector allocation strategies (paid JPMaQS quantamental factors). We rebuild the core on **free US data**: a **predefined economic sector × macro-factor sensitivity matrix** (the key honesty guard — *not fitted* to the sample) scored against point-in-time FRED macro factors, run as a cross-sectional dollar-neutral rotation across the 9 SPDR sectors.

## How it works
- **Sectors:** the 9 classic SPDR ETFs — XLF (Financials), XLE (Energy), XLB (Materials), XLI (Industrials), XLK (Technology), XLY (Discretionary), XLP (Staples), XLV (Health Care), XLU (Utilities), Yahoo monthly total returns.
- **Macro factors (FRED, point-in-time expanding-z ≥36m, lagged 1m):** growth (INDPRO YoY), inflation (CPI YoY), rising-rates (DGS10 12-month change), risk-on (−Baa credit spread `BAA10Y`).
- **Predefined sensitivity matrix** (economic priors, **not fitted**): e.g. XLF rates_up +1.0, XLE inflation +1.0, XLU rates_up −1.0, XLP growth −0.7. Sector score = Σ_factor SENS·macro_z.
- **Strategy:** demean scores cross-sectionally (dollar-neutral), gross-normalise, earn t→t+1; vol-targeted to 10%. Walk-forward (macro ≤ t). Benchmark = equal-weight sector basket.

## Outputs (`Sector Rotation/`)
- **`Sector Rotation Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (rotation vs equal-weight basket, log), a performance + current-macro table, and the current sector-tilt bar.
- **`Sector Rotation Note <date>.md`** + **`sectorrot_latest.json`**.
Tools: `tools/sector_rotation.py` · `sector_rotation_report.py` · `build_sector_rotation.py`.

## Result — 2002-03 → 2026-08 (n=293, 9 sectors)
| Strategy | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| Macro sector rotation (long-short) | **0.02** | −0.34% | 11.1% | −38.6% |
| Equal-weight sector basket | **0.74** | 10.1% | 14.5% | −49.1% |

*Metrics re-verified 2026-09-24 against `Sector Rotation/sectorrot_latest.json` (engine run `generated` 2026-09-24 16:25, data through 2026-08). This supersedes the 2026-09-08 refresh, which superseded the June-2026 figures; the null is unchanged (long-short Sharpe 0.03 → 0.02). The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **The macro-factor rotation has no cross-sectional predictive power: IC −0.001 (t −0.05)**, and the long-short book earns essentially nothing (Sharpe 0.02).
- **It is *vastly* beaten by passively holding the 9 sectors equal-weight (Sharpe 0.74, CAGR 10.1%)** — the rotation adds no cross-sectional alpha over the basket. (These are different objects — a market-neutral alpha vs equity beta — but the honest point stands: the macro tilt produced no harvestable cross-sectional edge.)
- **This is genuine, not a mis-specified matrix:** even plain **sector 12-month momentum is weak** (IC 0.022, t 0.78) — monthly cross-sectional sector returns are simply hard to predict from lagged macro (or their own trend). The current tilt is economically *sensible*, it just hasn't *predicted*.

## Current macro read & tilt
As of the **2026-09-24** engine run (`as_of`, macro through 2026-08) the matrix leans **cyclical** — LONG XLF **+0.97** / XLI **+0.70** / XLE **+0.54** (financials, industrials, energy), SHORT the defensive bond-proxies XLU **−1.45** / XLP **−1.02** / XLV **−0.71** (`cur_tilt`). The tilt is driven by the risk-on factor (`cur_macro.risk_on` **+1.11** z) with rising-rates **+0.50** and inflation **+0.43**; **growth is essentially flat at +0.09 z**, so this is a credit/rates-led cyclical lean rather than a growth-led one. Economically coherent as a *regime read*; historically without a measurable forward edge.

## Verdict
- **Macro-driven monthly sector rotation is a clean null** (IC ~0, Sharpe ~0), beaten comprehensively by the passive sector basket. Sector relative returns are dominated by idiosyncratic / flow / valuation forces that lagged macro factors don't capture at a monthly horizon.
- The exercise's value is a **regime read** (*which* sectors the current macro favours), not a return-timing strategy — the same recurring Brain lesson as [[Macro Regime Allocation Engine]] and [[Robust Equity Trend System]]: mechanical macro timing rarely beats holding the asset.

## Audit
Adversarially audited (2-lens: look-ahead/implementation + null-honesty) → **3 flagged, 0 confirmed — the cleanest audit of the run.** No look-ahead, no implementation bug artificially killing the signal (the sensitivity matrix is correctly signed, the cross-sectional IC and walk-forward are sound), and the null framing is fair. The null is genuine.

## Caveats
- The sensitivity matrix is **predefined from priors, not fitted** (deliberate — fitting it in-sample would be data-mining); US SPDR sectors (USD total return); vol-targeted 10%; revised (not vintage) FRED data; 1-month macro lag. **Free-data note:** FRED's `BAMLH0A0HYM2` (HY OAS) truncates to ~3 years — used `BAA10Y` (Baa credit spread) for the long-history risk factor.

## Related
[[Macro Regime Allocation Engine]] · [[Robust Equity Trend System]] · [[Macro Curve-Trade Strategy]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
