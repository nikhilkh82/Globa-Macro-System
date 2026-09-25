---
title: Treasury Macro-Trend System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: Tzotchev robust trend on synthetic Treasury TR (10y duration + DV01-neutral 2s10s) with a macro shortfall overlay, 1993–2026 — curve result retracted after the DV01 bug (IC −0.042); directional trend weak (0.49 vs 0.54).
tags: [global-macro, strategy, rates, treasuries, trend-following, curve, macro-overlay, null-result, construction-bug, corrected, backtest]
data_vintage: "LIVE (FRED yields + macro, 1993-03→2026-08) — engine re-run 2026-09-24 16:25"
sources: 1
updated: 2026-09-24
---

# Macro-Enhanced Treasury Trend Following

A free-data port of the Macrosynergy **"U.S. Treasuries and macro-enhanced trend following"** notebook: a Tzotchev robust trend on US Treasury total returns (**directional 10y duration** and **2s10s curve**), **macro-enhanced** by a "shortfall" composite (inflation/growth/labor/credit/sentiment below potential → bullish bonds). Built 2026-06-23; **the curve result was corrected the same day after an adversarial audit (see below).**

> **⚠️ The "macro helps the curve" result is RETRACTED.** It was an artifact of a DV01-construction bug (the 2s10s steepener weighted both legs by the 10y annuity, over-levering the 2y leg ~4.5×). Built correctly, the curve trend and the macro-on-curve effect are both insignificant. The honest finding: trend is at best weak in Treasuries, and macro adds nothing significant on the level *or* the curve. Research/education only.

## Provenance — what we adapted
Same structure as the [[Robust Equity Trend System]] (folder 25) but for bonds: a robust trend on bond returns, modified by macro "shortfall" scores (economic weakness → bullish bonds), tested both **directional** and on the **curve**. We rebuilt it on free US data (FRED yields + macro), keeping the Tzotchev robust trend and the never-flip macro modifier.

## How it works
- **Targets (synthetic total returns from FRED yields):** 10y duration TR = carry − duration·Δy; 2s10s **steepener** TR = **DV01-neutral** `(A₁₀·Δy10 − A₂·Δy2)/100`, **each leg on its own annuity** (the audit fix; the prior version wrongly used A₁₀ on both legs — see [[the-dv01-both-legs-flattener-bug]]).
- **Robust trend (Tzotchev):** avg over lookbacks {3,6,12,24}m of `2·Φ(mean/std·√N)−1`, on each target's own past returns.
- **Macro shortfall composite (FRED, point-in-time expanding-z, lagged 1m):** −(CPI YoY−2), −INDPRO YoY, UNRATE, Baa credit spread (`BAA10Y`), −UMich sentiment. **+ = weak economy = bullish bonds.**
- **Three signals each:** trend · macro-modified trend (never-flip sigmoid `C=2/(1+e^{−2·macro})`) · pure-macro (the shortfall z itself). Position = signal × forward return, vol-targeted to 8%. Walk-forward (signals ≤ t).
- **Significance:** time-series IC with a **Newey-West (HAC) t-stat** — serial-correlation-robust, since the trend signal is heavily autocorrelated.

## Outputs (`Treasury Trend/`)
- **`Treasury Trend Dashboard.html`** — light theme, Chart.js inlined: side-by-side growth-of-100 for directional and curve (trend / macro-modified / pure-macro / buy-and-hold), with performance tables.
- **`Treasury Trend Note <date>.md`** + **`treasurytrend_latest.json`**.
Tools: `tools/treasury_trend.py` · `treasury_trend_report.py` · `build_treasury_trend.py`.

## Result — 1993-03 → 2026-08 (n=402, vol-target 8%)
### Directional (10y duration)
| Strategy | Sharpe | CAGR | Vol | MaxDD | IC (HAC t) |
|---|---|---|---|---|---|
| Bond trend | 0.49 | 4.08% | 9.0% | −18.0% | 0.051 (t 1.1) |
| Macro-modified trend | 0.33 | 2.65% | 9.3% | −19.6% | −0.002 (t −0.05) |
| Pure macro (shortfall) | −0.11 | −1.76% | 10.9% | −61.3% | −0.064 (t −1.49) |
| Buy & hold 10y | **0.54** | 3.84% | 7.4% | −27.4% | — |

*Vintage: engine **re-run 2026-09-24 16:25** (`treasurytrend_latest.json`, `as_of` 2026-09-24 / `generated` 2026-09-24 16:25) and every figure that **existed on 2026-09-08** — Sharpe, CAGR, MaxDD, `ic_trend`/`ic_pure` and their t-statistics — is **unchanged**, re-checked cell by cell against the payload, with `Treasury Trend Note 2026-09-24.md` byte-identical to the 2026-09-08 and 2026-09-16 notes apart from its title line. The rest of both tables is **new here, not unchanged**: the whole Vol column (directional 9.0 / 9.3 / 10.9 / 7.4, curve 7.7 / 7.5 / 9.9 / 6.2), the "Buy & hold 2s10s steepener" row (`curve.perf_bh`) and `ic_modified` (−0.002, t −0.05 / −0.012, t −0.26) were first surfaced on this page on 2026-09-24 and have no 2026-09-08 counterpart to be compared against. The backtest still ends at the last **completed** month, **2026-08** (n=402), so no new return months entered the sample and the window did not move; that on its own would **not** guarantee unmoved figures — these engines re-pull revised FRED data, and the sibling [[Managed-Futures Trend System]] did drift on an unmoved window this pass — so the figures were re-checked rather than assumed. (Supersedes the earlier "metrics refreshed 2026-09-08" provenance note; the June-2026 figures remain superseded.) The audit verdicts below are unchanged and still refer to the original adversarial review. CAGR/Vol/MaxDD columns added 2026-09-24 from `directional.perf_trend/perf_modified/perf_pure/perf_bh`.*

- Bond trend works modestly (Sharpe 0.49, IC 0.051) but barely beats **holding** the 10y (0.54) — the disinflation bull made buy-and-hold strong.
- **The macro overlay subtracts (−0.16 Sharpe), but that's the modifier injecting noise — not a real signal:** the pure-macro directional IC −0.064 (HAC t −1.49) is **statistically insignificant** (CI straddles zero). Lagged macro adds nothing to an already-good price trend on the level.

### Curve (2s10s steepener) — *corrected, DV01-neutral*
| Strategy | Sharpe | CAGR | Vol | MaxDD | IC (HAC t) |
|---|---|---|---|---|---|
| Curve trend | −0.12 | −1.22% | 7.7% | −50.7% | −0.042 (t −0.96) |
| Macro-modified curve | −0.03 | −0.51% | 7.5% | −48.2% | −0.012 (t −0.26) |
| Pure macro (shortfall) | 0.13 | 0.79% | 9.9% | −42.3% | 0.063 (t 1.84) |
| Buy & hold 2s10s steepener | −0.03 | −0.36% | 6.2% | −38.1% | — |

- **The curve result is RETRACTED.** The prior "curve trend IC 0.166 / pure-macro IC 0.152 / HAC t 4.0" was a real t-stat computed on a **mis-constructed** steepener (the 2y leg over-weighted ~4.5× by using A₁₀ instead of A₂). Built DV01-neutral, the curve trend is **insignificant** (IC −0.042, t −0.96) and the pure-macro steepener IC +0.063 is insignificant too — its HAC t is **1.84** (`curve.ic_pure_t`, surfaced here 2026-09-24), below the 1.96 two-sided threshold, so the null stands; it is the closest any curve component comes to significance and should be re-checked on the next re-run.
- So **macro does not help the curve after all** — the "weak economy → Fed easing → predictable steepening" edge was an artifact of the construction bug, not a real Fed-reaction-function link.

## Live signal — 2026-09-24
*From the 2026-09-24 16:25 engine run (`treasurytrend_latest.json`, `generated` 2026-09-24 16:25). The run is fresh, but the shortfall composite's inputs are **monthly** FRED series lagged 1m and still end at **2026-08**, so the z below is a **pre-hike macro read**: it does not yet reflect the 2026-09-16 Fed hike or the September rates move noted below.*

- **Macro shortfall composite: z = −0.02** (`current_macro_shortfall`) — essentially **neutral**, a hair on the "economy at potential" side. Since **+ = weak economy = bullish bonds**, this is a flat macro view: the never-flip modifier `C = 2/(1+e^{−2·macro})` sits at ~0.98, so it is neither amplifying nor damping the price trend. Given the directional overlay subtracts 0.16 Sharpe in-sample, a neutral macro read is the benign case.
- **Market context the signal has not yet digested** (from `tools/macro_pack.json`, read 2026-09-24): 10Y **4.96%** and 2Y **4.71%** (both 09-22), 2s10s **+0.26pp** (09-23), daily fed funds **3.88%** (09-22) after the 2026-09-16 hike. The curve is positively sloped but nearly flat, and the front end has repriced hardest — the configuration in which this page's retracted "macro times the curve" claim would once have fired. It does not fire now: the DV01-neutral curve trend is a null (IC −0.042, t −0.96).
- **The first read reflecting post-hike macro data arrives with the September monthly prints** — re-running the engine does not advance it, because the shortfall inputs still end 2026-08. Either way, no live curve or duration position is implied by this page.

## Verdict
- **Trend-following is, at best, weak in Treasuries.** Directional bond trend (0.49) barely matches buy-and-hold 10y (0.54) and is insignificant (IC 0.051, t 1.1); the curve trend is now insignificant too. (The multi-asset CTA [[Managed-Futures Trend System]] is the stronger trend story.)
- **Macro enhancement adds nothing significant — level OR curve.** The prior "macro is asset-specific: helps the curve, not the level" lesson is **withdrawn** — the curve edge was a DV01 artifact. Honest position: on free revised US data, lagged macro reliably times **neither** the level **nor** a properly DV01-neutral curve shape.

## Audit
Originally a 2-lens audit (look-ahead + significance) confirmed no leak and correctly replaced the iid IC t-stat with a **Newey-West HAC t** — but it did **not** catch that the underlying steepener was mis-constructed, so the HAC t 4.0 was a valid statistic on a **fabricated** series. The **2026-06-23 cross-build audit** (22 agents, on the related [[Macro Demand-Based Rates System]]) found the **DV01-both-legs bug** and flagged that the related curve builds shared it. Re-checked here: confirmed the same bug, fixed it (each leg on its own annuity), and the curve result collapsed to insignificance. The directional (10y duration) result does not use the curve construction and is unchanged. See [[the-dv01-both-legs-flattener-bug]]. **Lesson: a look-ahead audit that passes does not certify the financial-engineering correctness of the instrument construction.**

## Caveats
- Synthetic TR excludes roll-down/convexity; **2s10s steepener now DV01-neutral (audit-corrected)**; US-only time series; vol-targeted 8%; revised (not vintage) FRED data; the shortfall composite is predefined (not fitted); 1-month macro lag.

## Related
[[the-dv01-both-legs-flattener-bug]] · [[Managed-Futures Trend System]] · [[Macro Curve-Trade Strategy]] · [[Macro Demand-Based Rates System]] · [[Robust Equity Trend System]] · [[Macro-Aware Risk Parity System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
