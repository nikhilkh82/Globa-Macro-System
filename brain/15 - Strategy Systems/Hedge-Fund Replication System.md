---
title: Hedge-Fund Replication System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Hasanhodzic–Lo linear clone of QAI from 5 liquid ETFs (24-month rolling OLS), walk-forward 2011–2026 — a robust positive: OOS corr 0.87, R² 75%, and the investable factor sleeve beats QAI (Sharpe 0.43 vs 0.33)."
tags: [global-macro, strategy, hedge-fund-replication, alternative-beta, factor-investing, hasanhodzic-lo, positive-result, backtest]
data_vintage: "LIVE (Yahoo ETFs + FRED, 2009→2026-09; engine re-run 2026-09-24 16:15)"
sources: 1
updated: 2026-09-24
---

# Hedge-Fund Replication System — *Do you really need to pay 2&20?*

A free-data realisation of the **Hasanhodzic–Lo (2007) "linear clone"**: replicate a hedge-fund return stream with a rolling OLS regression on a handful of **liquid, investable factors**, and measure how much of the return a cheap clone captures out-of-sample. Built 2026-06-23.

> **A genuinely positive, robust result** — the contrast to the Brain's recent nulls. Liquid factors capture the great majority of a multi-strategy hedge fund's return; held directly they even *beat* it (the fund's wrapper is a net drag). Research/education only.

## Provenance — what we adapted
The source (`Hedge-Fund-replication-master`) bundles the **Hasanhodzic–Lo 2007** paper + a Payne–Tresl genetic-algorithm variant, with R scripts and a messy bundled CSV. We kept the *core idea* — a rolling linear clone on liquid factors — and rebuilt it cleanly on **free live data**, solving the one hard part (a free target) with an investable proxy.

## How it works
- **Target:** **QAI** (IQ Hedge Multi-Strategy Tracker ETF) — an investable, liquid multi-strategy hedge-fund proxy (monthly total return from Yahoo adjusted close, 2009→). A true HFRI/CS index needs paid data; QAI is the best free *investable* HF-beta proxy — and it's itself the heart of the "do you need 2&20?" question.
- **Factors (liquid ETFs):** SPY (equity), IEF (7–10y Treasuries), HYG (high-yield credit), DBC (commodities), UUP (US dollar).
- **Method:** monthly; for each month *t*, OLS betas are estimated on the **trailing 24 months strictly before *t***, then held to earn month-*t*'s factor returns — a **causal / walk-forward** clone. Two objects are reported: the **HL clone** (with the fitted constant — measures tracking) and the **investable factor sleeve** (ETF betas only; a constant isn't a tradable position). Both are charged a turnover cost (5 bps × factor-weight turnover).

## Outputs (`Hedge Fund Replication/`)
- **`Hedge Fund Replication Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (QAI vs HL clone vs investable sleeve), a performance table, current factor loadings, and the fee/cost disclosures.
- **`Hedge Fund Replication Note <date>.md`** + **`hfrep_latest.json`**.
Tools: `tools/hfrep.py` · `hfrep_report.py` · `build_hfrep.py`. Yahoo chart API for ETF total returns + `fred.py` for the T-bill.

## Result — out-of-sample, 2011-05 → 2026-09 (n=185 monthly)
| | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| QAI (hedge-fund proxy, net of fee) | 0.33 | 3.15% | 5.04% | −13.8% |
| HL linear clone (w/ fitted constant) | 0.18 | 2.34% | 4.73% | −10.9% |
| **Investable factor sleeve (no constant)** | **0.43** | **3.53%** | **4.66%** | **−9.1%** |

*Metrics refreshed 2026-09-24 from the re-run engine (`hfrep_latest.json`, generated 2026-09-24 16:15); the 2026-09-08 figures — which had themselves superseded the June-2026 ones — are now superseded in turn. The evaluation window (2011-05 → 2026-09, n=185) is unchanged, as are the Sharpe and Vol columns; what moved against the 2026-09-08 run is the CAGR column (QAI 3.19% → 3.15%, clone 2.37% → 2.34%, sleeve 3.56% → 3.53%) and `beta_to_target` (0.82 → 0.81). The MaxDD column, previously blank, is now filled from the payload. The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Correlation clone↔QAI 0.87 · OOS R² 74.9%** (in-sample on the *same window* 80.8% — a ~6pt overfit gap, modest).
- **HL tracking clone captures 74%** of the return (70% on a total-return basis), tracking error 2.52%/yr, clone β to QAI **0.81**.
- **The investable factor sleeve out-returns QAI** (CAGR 3.53% vs 3.15%, Sharpe 0.43 vs 0.33 — 112% of QAI's return captured) — holding QAI's *own* factor exposures directly beat QAI, because the fund's wrapper is a **−1.15%/yr net drag** (fee + frictions + the fitted constant that isn't tradable).

## Verdict
- **For liquid multi-strategy hedge-fund beta — mostly no, you don't need to pay 2&20.** Five cheap ETFs reproduce ~¾ of QAI's return variance out-of-sample; the tracking clone captures ~74% of the return, and the investable factor sleeve actually *beat* QAI at the same low fee. The classic Hasanhodzic–Lo result reproduces on free data.
- **Honest caveats:** (1) QAI is itself a *liquid HF-replication ETF* (already cheap beta), so this **understates** the difficulty of cloning a true high-alpha 2&20 fund; ~¼ of variance is unexplained — that residual is where genuine manager skill / idiosyncratic strategy would live. (2) The sleeve uses leverage (gross to **1.42×**) and shorts in **179/185 months**, so its higher Sharpe is not risk-matched. (3) Returns are net of 5 bps turnover (~1.4×/yr) but before financing on the short/levered legs; capture compares a costed clone to net-of-fee QAI.
- A clean counterpoint to the Brain's mechanical-alpha nulls ([[ML Macro-Direction Model]], [[Macro Curve-Trade Strategy]]): here the *systematic / fee-arbitrage* finding is real and robust, precisely because it claims **beta replication**, not alpha.

## Caveats / provenance notes
- QAI is an investable proxy, not a proprietary HFRI/CS index (free-data constraint).
- Yahoo adjusted-close total returns (dividends in); revised data; US ETFs; 24-month rolling window; 2009-inception → 24-month burn-in means the OOS sample starts 2011.
- Adversarially audited (2-lens workflow) → 5 medium/low items, all addressed: turnover cost now modelled; in-sample R² put on the same window as OOS (0.765 vs 0.665); the non-tradable intercept disclosed and the investable sleeve reported separately; "≈0 fee" language replaced with the honest gross/net + leverage/shorts disclosure; β-to-QAI reported as the computed 0.76. No headline number was wrong; the framing was made precise. *(Note added 2026-09-24, not a change to this record: the 0.765 / 0.665 and 0.76 digits are the June-2026 run's values. The live payload now reads `r2_insample` 0.808 vs `r2_oos` 0.749 and `beta_to_target` 0.81 — the figures in the Result section above. What this bullet records is the audit finding, not the digits.)*

## Related
[[Managed-Futures Trend System]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[ML Macro-Direction Model]] · [[Macro Curve-Trade Strategy]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
