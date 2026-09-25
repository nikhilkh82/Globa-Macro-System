---
title: Target-Beta Factor Portfolio (June 2026)
category: synthesis
type: strategy-system
data_asof: 2026-09-24
summary: "Weekly Markowitz long/short over 12 macro ETFs solved to a target β (FF3 ρ/Σ): the dial still works (realized β −0.50…+1.39, CAGR −1.9%→+12.0%), β=0 neutral at +3.9%; β=−1 18% feasible; no book beats SPY Sharpe."
tags: [global-macro, portfolio-optimization, factor-model, fama-french, target-beta, long-short, etf, market-neutral]
data_vintage: "LIVE — free Yahoo + Ken French FF3 daily, 2007-01-12 → 2026-07-31 (4,918 days; tbeta_latest.json meta.start/meta.end/n_days). Solver run asof 2026-09-24; the price history it was solved on still ends 2026-07-31."
sources: "Adapted from the FE630 (Stevens FE) 'Long/Short Global Macro with Target Beta' final project"
updated: 2026-09-24
---

# Target-Beta Factor Portfolio (June 2026)

**What it is & why it matters** — A free-data reconstruction (extended to 2026) of the FE630 *"Long/Short Global Macro with Target β using the Fama-French 3-factor model"* project. It adds the one capability the rest of the system lacked: **explicit portfolio optimization with a target market β** — a Markowitz long/short book over **12 global-macro ETFs** that is solved, every week, to a *chosen* market-beta. It is the **risk-targeting / portfolio-construction pillar**, distinct from the trend, committee, SMC and z-score engines. The Fama-French factors are **free** (Ken French), so the whole thing runs on free data.

## Method
Per weekly rebalance, for each ETF estimate its **FF3 loadings** → a factor-model **expected return ρ** (window-mean factor premia) and **covariance Σ = B·Ωf·Bᵀ + D**, plus its **CAPM β vs SPY**; then solve

> max ρᵀw − γ·wᵀΣw − λ·(w−wₚ)ᵀΣ(w−wₚ)  **s.t. βᵀw = β_target**, Σw = 1, gross ≤ 200%, −1 ≤ wᵢ ≤ 1

swept over **target β ∈ {−1, −0.5, 0, 0.5, 1, 1.5}**, 2007–2026, benchmarked vs SPY. Strictly causal (estimation windows end at the rebalance day; weights apply the next day). Run parameters from `meta`: expected-return window **90d** (`rp`), covariance window **120d** (`vp`), rebalance every **5 trading days** (`rebal`), 12-ETF universe (`univ`).

## Results — re-run 2026-09-24 (data through 2026-07-31)

*The 19-minute SLSQP sweep **timed out on 2026-09-16** and the page's figures had been carried from the 2026-06-21 build. It completed today: `tbeta_latest.json` `meta.asof` = **2026-09-24**. Note the window it solved on — `meta.start` 2007-01-12 → **`meta.end` 2026-07-31**, 4,918 trading days — so this refresh absorbs the drift up to end-July 2026, and the two months since are **not yet in the sweep**. The June-2026 figures are superseded by the table below.*

| Target β | Realized β | CAGR | Vol | Sharpe | MaxDD | Feasible | Turnover |
|---|---|---|---|---|---|---|---|
| −1.0 | −0.57 | +0.1% | 22.7% | 0.05 | −77.8% | **18%** | 0.023 |
| −0.5 | −0.50 | −1.9% | 18.8% | −0.09 | −76.4% | 96% | 0.100 |
| **0.0** | **−0.05** | **+3.9%** | **17.7%** | **0.22** | −54.6% | 99% | 0.137 |
| +0.5 | +0.42 | +7.6% | 19.3% | 0.40 | −28.3% | 99% | 0.150 |
| +1.0 | +0.91 | +9.7% | 24.3% | 0.44 | −39.5% | 99% | 0.147 |
| +1.5 | +1.39 | +12.0% | 31.2% | 0.47 | −56.5% | 99% | 0.127 |
| SPY | 1.0 | +10.7% | 19.8% | 0.54 | −55.2% | — | — |

*Keys: `by_beta.<target>.realized_beta / .ann / .vol / .sharpe / .maxdd / .feas / .turnover`, `spy.*`. Every β book lost between 0.3 and 1.4 points of CAGR versus the June read (β=0: +4.9% → **+3.9%**; β=+1.0: +10.1% → **+9.7%**; β=−1.0: +1.5% → **+0.1%**), while SPY gained (+10.6% → **+10.7%**) — so the gap between the dial and the benchmark **widened** on this re-solve.*

**Three findings:**
1. **The β dial still works** (for targets ≥ −0.5). Realized β tracks the target monotonically — **−0.50 / −0.05 / +0.42 / +0.91 / +1.39** against targets −0.5 / 0 / +0.5 / +1 / +1.5 — and return scales with it (−1.9% → +12.0%). You can genuinely set market exposure from ~−0.5 to +1.5. The higher-β books **no longer approach** SPY's Sharpe (0.47 at β=+1.5 and 0.44 at β=+1.0, against 0.54), so on this window *no* setting of the dial matches the benchmark risk-adjusted; the value is the *control*, not raw outperformance.
2. **The dial saturates at the negative end.** **β = −1 is only 18% feasible** (`by_beta.-1.0.feas` = 18.0, against 96–99% for every other target) — with a long-biased ETF universe under a 200% gross cap, a true −1 portfolio mostly cannot be formed, so the optimizer falls back to prior weights (turnover 0.023, a sixth of the others) and the realized β floors near **−0.57**. That row is illustrative only, and its CAGR has fallen to **+0.1%** with a **−77.8%** drawdown.
3. **The β = 0 sleeve is still genuinely market-neutral** (realized β **−0.05**, 99% feasible) and was strongly positive in the 2008 GFC (**+69.1%**) and the 2020 COVID crash (**+18.5%**) — **but that crisis P&L is a concentrated oil (USO) bet** the optimizer selected. The payload measures the concentration directly: average USO weight **+0.14 in the GFC and −0.17 in COVID** (`concentration.uso_gfc / .uso_covid`) — long oil into the 2008 commodity spike, short oil into the 2020 crash, exactly as described. The strip-USO counterfactual (gains falling to ~+24% / ~+3%) is **carried unchanged from the 2026-06-21 run** — today's payload reports the USO weights but not the ex-USO re-solve, so that pair of numbers has not been re-verified. So it is a real *low-correlation* sleeve, **not** a structural crisis hedge.

**Two further scenarios from the payload** (`scenarios[]`) that this page has not carried before: in the **2022 bear** the β=0 book returned **+1.2%** against SPY's **−17.7%** (the cleanest evidence for the neutrality claim), and across **2023–2026** it returned **+83.3%** against SPY's **+96.0%** — low-correlation, but paying for it in a bull market. The dial's failure mode is visible in the **2009–19 recovery**, where β=0 lost **−44.4%** while SPY made **+402.2%**.

**Window sensitivity.** The headline 90/120 configuration is *not* the flattering one: at β=+0.5 it gives Sharpe **0.40**, while r120/v120 gives **0.52** and r60/v120 **0.49** (`window_sens[]`). The spread across the five window pairs the payload tests (Sharpe 0.40–0.52, CAGR 7.6–10.0%) is a fair measure of how much of any single headline number is estimation noise — and it is wider than the gap between several of the β rows.

> **Re-solved 2026-09-24 — construction verdict unchanged, the α verdict gets worse.** The SLSQP sweep that timed out on 2026-09-16 completed today; every digit in the results table above is from `tbeta_latest.json` (`meta.asof` 2026-09-24, data through `meta.end` 2026-07-31). **Unchanged:** the β constraint still binds (realized β −0.50/−0.05/+0.42/+0.91/+1.39 against its targets), β=−1 is still the one infeasible corner (**18%**), and the β=0 crisis P&L is still an oil concentration — the June audit's two must-disclose findings both survive intact. **Changed, and flagged:** on the June run the top of the dial "approached SPY's Sharpe"; on this run it does not — **0.47 at β=+1.5 and 0.44 at β=+1.0 against SPY's 0.54**, with every β book's CAGR lower than June's and SPY's higher. That is a *degradation* of the factor-model α, not a reversal of the audit's conclusions, so the audit record below stands as written. The claim to watch on the next re-audit is whether a book whose Sharpe is uniformly below the benchmark's is still worth running for the β control alone.

> **Adversarially audited (2026-06-21): look-ahead-clean.** Verified causal (windows end at the rebalance day; the booked return uses the *old* weights; ρ/Σ/β estimated on past data only). The audit confirmed the factor-model Σ and the β constraint are correct (estimated portfolio β hits the target exactly when feasible) and that the **source-fixes are sound and material**: the original's ±2 bounds with only a tracking-variance penalty allow **unbounded gross leverage and blow up (110% vol)** — adding the standard **gross-leverage cap + total-variance risk aversion** (γ=8, which does *not* over-shrink to min-variance) and **window-mean ρ** (the source used a single last observation) are the right fixes. Two must-disclose findings — the **β=−1 infeasibility** and the **β=0 crisis P&L being a USO concentration** — are now surfaced on the dashboard, in the table (feasibility column), and above.

## What this teaches
**Beta-targeting is a working, valuable risk-control lever** — a clean way to dial portfolio market exposure and build a low-correlation sleeve, which the rest of the system can't do. But two honest lessons, and the 2026-09-24 re-solve sharpens the first: the factor-model **expected-return α is weak — on the refreshed window, negative.** Higher β does not merely fail to beat the market risk-adjusted; **every** target, including +1.0 and +1.5, now lands below SPY's 0.54 Sharpe, so you are paying optimization complexity to under-earn the index. Second, **"market-neutral" is not automatically "crisis hedge"** — whether a β=0 book protects in a crash depends entirely on what the optimizer happens to hold (here, oil, at an average +0.14 weight through the GFC), not on the beta constraint itself. The β=0 book's **+1.2% through the 2022 bear against SPY's −17.7%** is the honest version of the claim: reliable *de-correlation*, not reliable protection.

## See also
- Dashboard (the β dial, the spectrum, crisis behaviour, robustness): open `target beta/Target-Beta Portfolio Dashboard.html`.
- Sibling strategies: [[Trading System - Backtest (June 2026)]], [[AI Analyst Committee — Stock Selection (June 2026)]], [[AlphaFX Smart-Money System (June 2026)]], [[Macro Pulse — Cross-Asset Z-Score Monitor (June 2026)]]. Portfolio-construction theory: [[Portfolio Management]], [[Risk Management]].

*Educational; not investment advice. Every figure is computed from free data and reproducible — and the infeasibility / concentration caveats are reported as plainly as the headline beta dial.*
