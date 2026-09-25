---
title: Macro Demand-Based Rates System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Equal-weight US aggregate-demand score → 5y duration and a DV01-neutral 2s10s flattener, 1998–2026 — a null corrected from a DV01 construction-bug artifact (curve IC +0.236 → +0.029); retracts 'macro times the curve'."
tags: [global-macro, strategy, fixed-income, rates, curve, demand, null-result, construction-bug, corrected, backtest]
data_vintage: "LIVE (FRED demand indicators + DGS2/5/10, 1998-03→2026-08) — engine re-run 2026-09-24 16:14"
sources: 1
updated: 2026-09-24
---

# Macro Demand-Based Rates Strategies

**Live dashboard:** [Demand Rates Dashboard](../../Demand%20Rates/Demand%20Rates%20Dashboard.html)

A free-data port of the Macrosynergy **"Macro demand-based rates strategies"** notebook. An equal-weight US **aggregate-demand score** is tested against two rates trades: **duration** (5y) and a **DV01-neutral 2s10s flattener**. Built 2026-06-23; **corrected the same day after an adversarial audit (see below).**

> **⚠️ Corrected from a strong-positive headline to a NULL.** The first version reported a robust, highly-significant curve result. A 22-agent adversarial audit (verdict **RESULT_INVALID**, independently reproduced on FRED data) found it was an artifact of a **DV01-construction bug** — both flattener legs were weighted by the 10y annuity, over-levering the 2y leg ~4.5×. Built correctly, the result is a null. Research/education only.

## Provenance — what we adapted
The notebook's thesis: aggregate **demand** pressures interest rates — under credible inflation targeting, excess demand should be **negatively** related to duration returns and **positively** related to **curve-flattening** returns. An equal-weight demand score is claimed to have "highly significant" predictive power. We kept that construction on free US FRED data.

## How it works
- **Aggregate-demand score** (FRED, YoY, point-in-time expanding-z, equal-weight, lagged 1m; **+ = excess demand**): real retail sales (RRSFS), real PCE (PCEC96), durable-goods orders (DGORDER), industrial production (INDPRO), payrolls (PAYEMS), consumer credit (TOTALSL).
- **Targets:** synthetic 5y Treasury total return (DGS5) for **duration**; a **DV01-neutral** 2s10s flattener from DGS2/DGS10 — `flat = (−A₁₀·Δy10 + A₂·Δy2)/100`, **each leg weighted by its own annuity** (the bug fix; see [[the-dv01-both-legs-flattener-bug]]).
- **Tests:** IC with **HAC (Newey-West, L=12)** t-stats; a leg decomposition (2y vs 10y); a jackknife dropping the 5 most-influential months; sub-samples; vol-targeted strategies. Walk-forward.

## The bug and the correction
The original "DV01-weighted 2s10s flattener" was `flat = −A₁₀·Δ(y10−y2) = −A₁₀·Δy10 + A₁₀·Δy2` — it applied the **10-year annuity (~7.9) to the 2y leg** instead of the 2y annuity (~1.9), over-weighting the front end by ~4.5×. Because demand → curve works *through the front end* (excess demand → Fed hikes the 2y), that mis-weighting turned the trade into an over-levered short-2y position and **manufactured the predictability**. The audit independently re-ran on FRED data and confirmed the corrected DV01-neutral result.

## Result — 1998-03 → 2026-08 (n=342)  *(corrected, DV01-neutral)*
| Component (demand → next-month return) | IC | HAC t | |
|---|---|---|---|
| Duration (5y level) | −0.094 | −1.51 | right sign, weak |
| **DV01-neutral 2s10s flattener** | **+0.029** | **+0.66** | **null** |
| Short-2y leg (front-end) | +0.183 | +2.63 | the lone flicker — a *level* bet |
| Long-10y leg | −0.016 | −0.33 | no signal |

*Vintage: engine **re-run 2026-09-24 16:14** (`demandrates_latest.json`, `as_of` 2026-09-24) and every figure above is **unchanged** from the 2026-09-08 verification **except** the long-10y leg's HAC t, which is **−0.33** (`ic_leg10_t`) against the **−0.32** previously printed. The backtest still ends at the last **completed** month, **2026-08** (n=342), so no new return months entered the sample and the window did not move — but that alone does **not** hold the figures still: the engine re-pulls revised FRED data, which is where the −0.32 → −0.33 came from (`ic_leg10` itself is unchanged at −0.016, and the sibling [[Managed-Futures Trend System]] drifted on an unmoved window this pass too). (Supersedes the earlier "metrics refreshed 2026-09-08" provenance note.) The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Demand → a properly DV01-neutral curve shape is a null** (IC +0.029, t 0.66); all three sub-samples are insignificant — 1998–07 −0.025 (t −0.38), 2008–15 +0.080 (t 1.16), 2016–26 +0.035 (t 0.45) (`subsamples[].ic_flat` / `.t_flat`, sub-sample t-stats surfaced 2026-09-24).
- **The level (5y duration) is weak** (IC −0.094, t −1.51), right-signed; the demand-timed short-duration book (0.63) doesn't beat holding the 5y (0.70). The demand-timed **flattener** book is flatly dead: Sharpe **0.00**, CAGR **−0.33%**, MaxDD **−31.5%** (`perf_flattener`) versus a static always-on flattener at Sharpe **0.00**, CAGR **−0.19%**, MaxDD **−26.7%** (`perf_flat_static`) — timing the curve with demand does not beat not timing it.
- **The only full-sample component with a t-stat is the short-2y front-end leg** (IC +0.183, t 2.63) — but that's a front-end *level/direction* bet (excess demand → Fed hikes the 2y), **not** curve timing, and it shares the GFC concentration: the flattener jackknife dropping the 5 most-influential months (all 2008–09) gives IC +0.02 (t 0.49). The 10y leg carries no signal.
- **⚠️ Flagged 2026-09-24, verdict unchanged, needs re-audit:** the *sub-sample* duration ICs (`subsamples[].ic_dur` / `.t_dur`, surfaced for the first time this pass) are 1998–07 **−0.141 (t −2.04)**, 2008–15 −0.020 (t −0.24), 2016–26 −0.091 (t −1.06). The 1998–07 duration t passes |2| — the only *sub-period* statistic on this page that does, alongside the full-sample short-2y leg above. This does **not** overturn the full-sample duration null (IC −0.094, t −1.51), and the verdict below is **unchanged**; but a single significant early sub-sample inside an otherwise-null series is exactly the pattern that produced this build's retracted headline, so it is flagged for the next formal audit rather than written up as an edge.

## Live signal — 2026-09-24
*From the 2026-09-24 16:14 engine run (`demandrates_latest.json`).*

- **Aggregate-demand z = −0.08** (`cur_demand`) — marginally **below** potential. The engine's own reading: *"weak demand → long duration / steepen"* (`cur_view`). It is a near-zero score, so the implied tilt is nominal rather than a conviction position.
- **Read this against the market, not instead of it** (`tools/macro_pack.json`, read 2026-09-24): the Fed **hiked** on 2026-09-16 and daily fed funds is **3.88%** (09-22), with 10Y **4.96%** / 2Y **4.71%** (09-22) and 2s10s **+0.26pp** (09-23). A mildly-negative demand score pointing at "long duration / steepen" is therefore leaning **against** a tightening Fed — precisely the configuration where this build's measured ICs say it has no reliable edge (duration IC −0.094 t −1.51; flattener IC +0.029 t 0.66).
- **No position is implied.** The page's verdict is a null; the live score is published for monitoring and consistency with the dashboard, not as a signal to trade.

## Verdict
- **A null, corrected from a construction-bug artifact.** On free revised US data, the aggregate-demand score predicts **neither** the rates **level** (5y duration, weak) **nor** a properly DV01-neutral curve **shape** (null). The earlier "strong flattener" was an over-levered short-2y position created by the bug.
- **This retracts the cross-build "macro times the curve's shape, not the level" thesis.** All three curve builds shared the same DV01 error: [[Macro Curve-Trade Strategy]] was already a null (its IC fell 0.12 → 0.076 after the fix — conclusion unchanged), and [[Treasury Macro-Trend System]]'s curve result is likewise retracted once the steepener is built DV01-neutral (curve trend IC −0.042, t −0.96 — corrected 2026-09-24 from the −0.044 / −0.99 quoted here previously, read directly from that build's `curve.ic_trend` / `curve.ic_trend_t` rather than carried across). The honest position: **lagged macro does not reliably time US rates — level or shape — on free revised data.** Rates are largely efficiently priced w.r.t. lagged macro.

## Audit
**Adversarially audited (22 agents, 3 lenses → per-finding adversarial refutation → synthesis).** Verdict **RESULT_INVALID**: 6/6 flagged findings confirmed. The headline finding — the DV01-both-legs bug — was independently reproduced on live FRED data (IC +0.236/t4.48 → +0.029/t0.66). The walk-forward design (point-in-time z, 1-month macro lag, returns earned t→t+1) was confirmed **clean — no look-ahead**; the defect was financial-engineering construction, not leakage. **Key process lesson:** this build's inline self-checks (sub-sample, base-rate, concentration, look-ahead) all *passed* because they were downstream of the buggy target — they were **not** a substitute for the formal audit. Never publish a strong result on inline checks alone. See [[the-dv01-both-legs-flattener-bug]].

## Caveats
- **Revised (not point-in-time/vintage) data;** US-only; synthetic 5y TR / DV01 flattener exclude roll & convexity; vol-targeted; 1-month macro lag.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[Macro Curve-Trade Strategy]] · [[Treasury Macro-Trend System]] · [[Information State Changes System]] · [[ML Macro-Direction Model]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
