---
title: Sectoral Macro-Trend System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Specific macro-trend → sector links (export growth → energy, confidence → real estate, …) tested one by one on SPDR total returns 2002–2026 — a fragile null: only macro-cycle → Energy flickers, collinear or tail-driven."
tags: [global-macro, strategy, equities, sectors, macro-trends, null-result, fragile, multiple-testing, audited-up-front, backtest]
data_vintage: "LIVE (SPDR sector ETFs + FRED, 2002-11→2026-08; engine run 2026-09-24)"
sources: 1
updated: 2026-09-24
---

# Macro Trends & Sectoral Equity Performance

A free-data port of the Macrosynergy **"Macro trends and sectoral equity performance"** notebook. Where the [[Macro Sector Rotation System]] (folder 27) used a *generic* macro composite, this tests the notebook's **specific, economically-motivated macro-trend → sector links** (export growth → energy, consumer confidence → real estate, …) one by one. Built 2026-06-24; **audited up front** (the formal audit ran *before* publishing, per the [[the-dv01-both-legs-flattener-bug]] lesson).

> **A fragile null.** The audit (61 agents) returned **RESULT_OVERSTATED** and the result, corrected, is essentially a null: only **energy's** sensitivity to the demand/inflation cycle shows any signal, and it is too fragile to call an edge. The combined sector-selection strategy is insignificant and trails passive. Research/education only.

## How it works
- **Sectors:** SPDR ETFs (Yahoo, **dividend-adjusted total return**), relative return = sector − equal-weight basket over a consistent 6-sector signal universe.
- **Specific links (FRED macro trend, point-in-time expanding-z, series-specific publication lag → that sector's next-month relative return):** export growth (BOPTEXP 6m mom, **lag 2**), producer inflation (PPIACO YoY), IP trend (INDPRO 6m mom), durable-goods (DGORDER YoY, **lag 2**), consumer confidence (UMCSENT 3m chg), financial conditions (NFCI inverted). Each tested with **HAC (Newey-West) t**, a **crisis-excluded** robustness check, and **Bonferroni/BH** multiple-testing.

## Outputs (`Sector Macro/`)
- **`Sector Macro Dashboard.html`** — light theme, Chart.js inlined: per-link IC (full vs crisis-excluded) and the combined market-neutral strategy curve, with a full diagnostics table.
- **`Sector Macro Note <date>.md`** + **`sectormacro_latest.json`**.
Tools: `tools/sector_macro.py` · `sector_macro_report.py` · `build_sector_macro.py`.

## Result — 2002-11 → 2026-08 (point-in-time, total return)
| Macro trend → sector | Sec | IC | HAC t | p | ex-crisis IC | ex-crisis t |
|---|---|---|---|---|---|---|
| Producer inflation → Energy | XLE | +0.175 | 3.16 | 0.0016 | 0.096 | 1.75 |
| Export growth → Energy | XLE | +0.152 | 2.31 | 0.0211 | 0.158 | 2.93 |
| Easy financial conditions → Financials | XLF | +0.117 | 1.41 | 0.157 | 0.072 | 0.84 |
| Consumer confidence → Real Estate | XLRE | +0.055 | 0.76 | 0.447 | −0.036 | −0.36 |
| …5 more | | ~0 / −ve | <1.7 | ns | | |

*Metrics re-verified 2026-09-24 against `Sector Macro/sectormacro_latest.json` (engine run `generated` 2026-09-24 16:25, data through 2026-08), read from `links[]` link by link. This supersedes the 2026-09-08 refresh, which superseded the June-2026 figures. Both Energy links are unchanged on IC and HAC t (0.175/3.16 and 0.152/2.31), and export-growth→Energy is unchanged on every column (ex-crisis 0.158/2.93); only the PPI→Energy ex-crisis tail shaved, IC 0.097 → 0.096 and t 1.76 → 1.75 — and that shave is **not** today's: `Sector Macro Note 2026-09-16.md` already printed 0.096 / 1.75, so it happened at the intervening 2026-09-16 run. The financial-conditions → Financials link weakened further (IC 0.120 → 0.117, HAC t 1.46 → 1.41, ex-crisis IC 0.08 → 0.072 and t 0.93 → 0.84) and the fragile null stands. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **At most ONE economically-sensible signal — the macro/inflation cycle → Energy — and it is fragile.** The only two nominal hits are both Energy and are **ρ 0.79 collinear** (one finding, not two).
- **No single version is robust on both axes:** producer-inflation→Energy survives multiple-testing (p 0.0016 < Bonferroni 0.0056 — the *only* one of the 9 links that does) **but is tail-driven** (ex-crisis t 1.75); export-growth→Energy is **robust to crisis exclusion** (ex-crisis t 2.93) **but fails Bonferroni** (p 0.0211). The one Bonferroni-survivor is the tail-fragile one.
- **The notebook's marquee link fails:** consumer confidence → real estate is a null (IC 0.055, t 0.76; *negative* ex-crisis) on the short XLRE sample (2015-12→2026-08, n=129).
- **Multiple testing:** the 9 links reuse only ~6 FRED series (several collinear), so effective independent tests ≈ 6; under the null ~0.4 clear |t|≥2 by chance. One fragile survivor is only weakly above noise.

## Combined sector-selection — insignificant, beaten by passive
- The combined dollar-neutral overlay (the 6 sectors carrying a link — `uni` = XLB/XLE/XLF/XLI/XLRE/XLY) is **insignificant**: cross-sectional IC **0.055 (HAC t 1.53)**, ex-crisis IC 0.064 (t **1.94**, still short of 2).
- Its market-neutral Sharpe is **0.47** (`perf_strategy.sharpe`; the right benchmark for a market-neutral book is **zero**), CAGR 3.9% at 9.0% vol, MaxDD −19.2%. For context, holding the equal-weight sector basket over the *same* 286 months earned **0.82** (`perf_ewbasket_match.sharpe`, CAGR 11.07%) — the macro overlay produces no sector-selection edge and badly trails passive.

## Verdict
- **A fragile null.** Only the **macro-cycle → Energy** link shows any signal on free US data, and it is not a robust, tradable edge (no point-in-time, multiple-testing-corrected, crisis-robust version survives; the two measurements are one collinear signal). The combined strategy is insignificant and trails passive.
- Sits with the project's broad macro-timing nulls (the generic-composite [[Macro Sector Rotation System]] was also a clean null). The value of testing *specific* links: it isolates **energy's** demand/inflation-cycle sensitivity as the one economically-real flicker — while showing it is not an edge.

## Audit
**Audited up front (61 agents, 3 lenses → adversarial verification → synthesis): verdict RESULT_OVERSTATED, 18/19 findings confirmed.** Crucially, **no construction/look-ahead fabrication** (unlike the DV01 case) — the timing/z/vol logic is clean. The downgrade came from fixing real issues the audit found *before* publication: (1) **dividends dropped** (price not total return → biased high-yield sectors) — fixed to adjusted close; (2) **trade/durable-goods data need a 2-month publication lag** to be point-in-time; (3) the two energy links are **collinear** (one finding); (4) PPI→Energy is a **2022-surge artifact**; (5) **neither survives multiple-testing** cleanly; (6) the strategy-vs-basket "beat" was an **unequal-window** illusion (basket actually wins); (7) **6-vs-11 sector universe** inconsistency. All applied. **This is the [[the-dv01-both-legs-flattener-bug]] lesson working as intended — the audit ran first and stopped an overstated "narrow positive" from being published as a finding.**

## Caveats
- **Revised (not point-in-time vintage) FRED data** — a real caveat for the headline significance; US-only; SPDR total returns; XLRE/XLC short histories (2015/2018); vol-targeted; 6 of 11 sectors carry signals.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[Macro Sector Rotation System]] · [[Robust Equity Trend System]] · [[Macro Curve-Trade Strategy]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
