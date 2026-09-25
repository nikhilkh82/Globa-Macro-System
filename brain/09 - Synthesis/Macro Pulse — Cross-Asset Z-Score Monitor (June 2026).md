---
title: Macro Pulse — Cross-Asset Z-Score Monitor (June 2026)
category: synthesis
type: strategy-system
data_asof: 2026-09-24
summary: "Vol-adjusted 'dominant variable' z-monitor over 7 macro instruments; the 2026-09-23 board reads US10Y +3.4σ (rates up). Abnormal moves still mostly don't predict; the VIX→SPY edge stays non-robust (Bonferroni p 0.103)."
tags: [global-macro, cross-asset, z-score, dominant-variable, regime, monitor, honest-negative]
data_vintage: "LIVE — free Yahoo daily, 2000-08-23 → 2026-09-23 (macro_pulse_latest.json meta.start/meta.end, run asof 2026-09-24)"
sources: "Adapted from the Global-Macro-Intelligence-Dashboard (Streamlit) — the 'dominant variable' concept"
updated: 2026-09-25
---

# Macro Pulse — Cross-Asset Z-Score Monitor (June 2026)

**What it is & why it matters** — A systematic extension of the open-source **Global-Macro-Intelligence-Dashboard**'s one good idea: the **"dominant variable"** — which of 7 macro instruments (US10Y, US3M, DXY, Oil, SPY, QQQ, VIX) is moving most abnormally *relative to its own volatility* (a z-score, not a raw %). Each instrument maps to a macro driver (VIX=Fear, DXY=Liquidity, Oil=Fear/real-yields, US10Y=Growth/Rates…), so the board answers "**what's driving markets right now**, vol-adjusted." My additions: **data-driven point-in-time z-scores** (trailing realized vol, no look-ahead) instead of the source's hardcoded vols, and the question the source never asks — **is that abnormal move actually tradable?** Honest answer up front: **the monitor is the keeper; the trading signal is mostly a null.** (The source's Gemini AI narratives + scraped Edward Jones reports are dropped — not free or auditable.)

## The 7 instruments → macro drivers
| Instrument | Driver | Tradable |
|---|---|---|
| US10Y (^TNX) | Growth / Rates | signal-only |
| US3M (^IRX) | Fed expectations (13-wk T-bill) | signal-only |
| DXY | Global liquidity | yes |
| Oil (WTI) | Fear / real yields | yes |
| SPY | Risk appetite | yes |
| QQQ | Growth / liquidity | yes |
| VIX | Fear | signal-only |

The **dominant variable** each day = largest |z| over a 60-day trailing window (`meta.window` 60, `meta.z_thresh` 2.0, `meta.horizon` 10). Across the whole 2000–2026 sample **Oil is dominant most often** (1,213 days), then US10Y (1,128) and DXY (1,126); SPY is dominant least (538) (`domfreq`).

## Live board — 2026-09-23

*Supersedes the June-2026 build's read of "DXY at +2.5σ → USD strength / tightening", which is no longer the dominant variable. Values are `board[]` / `dominant` in `macro pulse/macro_pulse_latest.json` (`meta.asof` 2026-09-24, `meta.end` 2026-09-23).*

| Instrument | Driver | z | 1-day | 1-week | Close |
|---|---|---|---|---|---|
| **US10Y (^TNX)** | **Growth / Rates** | **+3.41** | **+3.04%** | +2.36% | **5.11** |
| DXY | Global liquidity | +2.35 | +0.67% | +0.92% | 101.10 |
| US3M (^IRX) | Fed expectations | +1.41 | +1.16% | +1.72% | 4.03 |
| Oil (WTI) | Fear / real yields | −1.33 | −3.78% | **−7.90%** | 92.16 |
| SPY | Risk appetite | −1.12 | −0.74% | +1.82% | 767.81 |
| VIX | Fear | +0.35 | +2.08% | −8.07% | 15.18 |
| QQQ | Growth / liquidity | −0.08 | −0.04% | +5.18% | 741.21 |

**Dominant variable: US10Y at +3.41σ, up — regime read "Rates up / growth-or-inflation"** (`dominant.z`, `dominant.regime`). FRED corroborates it independently: the `T10Y3M` spread jumped **0.80 → 0.92pp between 09-22 and 09-23** and `T10Y2Y` 0.25 → 0.26pp (`tools/macro_pack.json`), which is what a one-day long-end selloff looks like; and the level is consistent — FRED's `DGS10` 4.96% on 09-22 grossed up by the board's +3.04% day gives 5.11, the board's own ^TNX print. Context: the **Fed hiked on 2026-09-16 to a 3.88% effective funds rate** (`macro_pack.json` `DFF`, 09-22), so the whole curve is repricing upward, not just the 10Y.

**Oil is off the mid-September spike.** FRED `DCOILWTICO` has WTI at **$96.41 on 09-22**, down from **$103.62 on 09-16** (`macro_pack.json` `DCOILWTICO.last5`), and the board's own Oil series is **92.16 on 09-23, −7.90% on the week**. The "Fear / real yields" instrument is now the *weakest* mover on the board, not the strongest.

**What is and isn't firing.** Two of the seven a-priori signals are live at |z| ≥ 2 on the board's own last bar, **2026-09-23** (`meta.end`; the run is `meta.asof` 2026-09-24) — **US10Y rate shock** (z +3.41) and **DXY surge** (z +2.35) — and both are, per the study below, the ones with essentially **zero** forward edge (+0.05pp and +0.01pp). The one signal with a positive edge, the VIX fear spike, is **not** firing (z +0.35). That is the monitor behaving exactly as the honest study says it should: it is telling you what is abnormal, and none of what is abnormal is tradable.

## Does an abnormal move predict? — the honest study
For seven a-priori signals, the forward 10-day return after a **|z| ≥ 2** shock vs the unconditional baseline (`study[]`, re-run asof 2026-09-24 on data through 2026-09-23):

| Signal | → | n | fwd-10d | edge (pp) | t | hit |
|---|---|---|---|---|---|---|
| SPY abnormal down (z≤−2) | SPY | 237 | +0.08% | **−0.20** | +0.29 | 54.9% |
| SPY abnormal up (z≥+2) | SPY | 153 | −0.24% | −0.53 | −0.61 | 56.2% |
| QQQ abnormal down | QQQ | 239 | +0.22% | −0.15 | +0.69 | 56.1% |
| **VIX fear spike (z≥+2)** | **SPY** | **277** | **+0.55%** | **+0.27** | **+2.44** | **61.4%** |
| DXY surge | SPY | 191 | +0.29% | +0.01 | +1.27 | 58.6% |
| US10Y rate shock | SPY | 217 | +0.33% | +0.05 | +1.55 | 62.7% |
| Oil abnormal move | Oil | 390 | −1.04% | −1.43 | −1.29 | 51.5% |

*Three months of extra data (June → September 2026) added 0–2 observations per signal and moved nothing material: every edge sign, the ranking and the one-positive-signal conclusion are unchanged.*

- **Most "abnormal move → reversion" bets do not work** — same-asset dip-buying (SPY/QQQ/Oil) shows ~zero or negative edge, |t| ≤ 1.3. The eye-catching "dominant variable" is *not* a forward-return signal.
- The **one** signal with a positive, a-priori-plausible edge is the canonical **"buy the fear"** — a VIX spike → SPY (+0.55% fwd-10d, raw **t = 2.44**, 61.4% hit over 277 signals).

## The one tradable edge — VIX-fear dip-buy (a defensive overlay)
Long SPY for the 10 days after a VIX fear-spike, else cash:

| | Overlay | SPY buy & hold |
|---|---|---|
| CAGR | 4.1% | 6.5% |
| Sharpe | 0.37 | 0.42 |
| Max drawdown | **−34.8%** | −56.5% |
| Days in market | 32.2% | 100% |

*`strategy.ann / .sharpe / .maxdd / .pct_in_mkt` and `strategy.spy_bh.*`, asof 2026-09-24; 277 signals fired over the sample (`strategy.n_signals`).*

It **trails buy-and-hold on return** (in cash roughly two-thirds of the time) but cuts the **drawdown by ~22 points** — a *defensive risk-reducer*, not an alpha engine.

> **Refreshed 2026-09-24 — the multiplicity caveat stands, marginally softer.** Re-run on data through 2026-09-23 (`meta.end`), the block-bootstrap per-day edge vs off-market is **+4.1bps, CI [0.6, 10.9], p = 0.068** (`strategy.edge_bps / .ci_bps / .p_le_base`), and the VIX signal's raw t is **2.44**, p_raw **0.0147**, **Bonferroni ×7 p = 0.103** (`multiplicity.*`). The payload's own note still reads: "VIX-fear is the only positive-edge signal and is a priori plausible, but after Bonferroni (×7) and the 10-day window overlap it is NOT multiplicity-robust." These figures supersede the June-2026 versions quoted in the audit record below (+4.2bps, CI [0.4, 10.8], p = 0.071; Bonferroni 0.106) — the audit's text itself is left as written, and **its verdict is unchanged**.

> **Adversarially audited (2026-06-21).** **Look-ahead-clean** — the z-score was manually recomputed from the trailing window and matched to 1e-9; the strategy enters strictly after the signal bar; the forward-return targets are never fed back. But the audit (rightly) **deflated the VIX edge**: with **7 signals tested**, Bonferroni ×7 takes its p from 0.015 to **0.106 — not multiplicity-robust**; the 10-day window overlap inflates the t (Newey-West ≈ 2.1); and the effect is concentrated in 2009–2016. **Fixes applied:** a **block bootstrap** (the per-day edge vs *off-market* is +4.2bps, CI [0.4, 10.8], p = 0.071), an explicit **Bonferroni disclosure**, and the mislabelled `US2Y` corrected to **US3M** (^IRX is the 13-week T-bill). Wording softened from "significant" to "directionally plausible, not multiplicity-robust."

## What this teaches
Two honest lessons. **(1)** The vol-adjusted cross-asset z monitor is a **genuinely useful live tool** — it tells you, in one glance, what's abnormal across the macro complex and the implied regime. Keep it. The 2026-09-23 board is a clean demonstration: it puts the post-hike long-end selloff (US10Y +3.41σ) and the oil unwind (−7.90% on the week) on the same vol-adjusted scale, which a table of raw percentage moves would not. **(2)** The abnormal move *itself* is **not a forward-return signal** — buying because something moved a lot is, on this evidence, not an edge. The lone exception (buy SPY into a VIX spike) is economically sensible and directionally real, but statistically thin once you count the seven shots taken. A monitor worth watching; a trading edge worth only a cautious, defensive tilt.

## See also
- Dashboard (live board + the honest study + the overlay): open `macro pulse/Macro Pulse Dashboard.html`.
- Sibling strategies: [[Trading System - Backtest (June 2026)]], [[AI Analyst Committee — Stock Selection (June 2026)]], [[AlphaFX Smart-Money System (June 2026)]]. Live regime cockpit: [[Analyst System — Live Cockpit (June 2026)]]. Vol context: [[VIX & Implied Volatility]]. Cross-asset regime: [[Macro Regime - Live (June 2026)]].

*Educational; not investment advice. Every figure is computed from free data and reproducible — and the multiple-testing caveat is reported as plainly as the headline t-stat.*
