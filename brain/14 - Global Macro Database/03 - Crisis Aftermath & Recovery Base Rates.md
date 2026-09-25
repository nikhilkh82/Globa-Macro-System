---
title: Crisis Aftermath & Recovery Base Rates
category: gmd
type: deep-dive
data_asof: 2026-06
summary: "Empirical priors: the 345-episode banking-crisis real-GDP path (t−1=100 → 112.8 by t+5) and the 181-episode debt-at-default distribution (median 61%, IQR 32–94%) — 'no safe debt level'."
tags: [global-macro, gmd, crisis, base-rates, stress-testing]
data_vintage: "GMD v2026_06 (current release; cross-country macro to 2024, IMF projections to 2030)"
sources: "Global Macro Database — Müller, Xu, Lehbib & Chen (2025), NBER WP 33714"
updated: 2026-07-25
---

# Crisis Aftermath & Recovery Base Rates

What this is: two empirical priors built from the GMD crisis chronology — the median real-GDP path *after* a banking crisis (345 episodes) and the distribution of debt/GDP *at the moment of* sovereign default (181 episodes). Both are meant to be used as calibration anchors for stress scenarios, not as forecasts. See [[02 - Crisis Chronology (Banking, Currency, Sovereign)]] for the underlying flag counts and [[Risk Management]] for how these feed sizing.

## Why base rates beat intuition

When a macro PM stress-tests a book, the two questions that matter most are usually: *how deep and how long is the growth hit if the banking system breaks?* and *at what debt level does a sovereign actually default?* Memory and headlines bias both answers toward the tail (2008, Greece). The GMD chronology lets us replace that bias with the full cross-country, multi-century distribution — including all the un-newsworthy episodes that recovered quietly or never blew up. That is the whole point of a base rate: it includes the boring middle, not just the catastrophes you remember.

## Base rate 1 — Banking-crisis recovery path (345 episodes)

Real-GDP event study, every banking-crisis episode in the GMD chronology indexed so that the year before the crisis (t−1) equals 100. The series below is the **cross-country median** path:

| Horizon | rGDP index (t−1 = 100) | Cumulative vs t−1 |
|---|---|---|
| t−1 | **100.0** | — |
| t0 (crisis year) | **101.3** | +1.3% |
| t+1 | **102.3** | +2.3% |
| t+2 | **104.4** | +4.4% |
| t+3 | **106.7** | +6.7% |
| t+5 | **112.8** | +12.8% |
| t+6 | **115.9** | +15.9% |

What the median path actually says:

- **The typical banking crisis is not a catastrophe.** The median country never sees the GDP index dip below the pre-crisis level — output is still **101.3** in the crisis year itself and keeps grinding higher. The "scar" shows up as a *slower* trajectory, not an outright collapse, in the median case.
- **The scar is measurable but moderate.** By **t+6** the median economy is **+15.9%** above its pre-crisis level — real, but well short of a depression narrative.
- **The median hides a fat left tail.** Advanced-economy crises and the 2008 cohort specifically recover **more slowly** than this median. The 345-episode sample is dominated by smaller and emerging-market events that bounce back faster, so the median understates the pain of a GFC-style shock in a large developed economy. Treat the median as the *central* prior and the advanced-economy/2008 path as the *adverse* tail of the same distribution.

Positioning translation: a "banking crisis" stress node should not default to a 2008-shaped collapse. The empirical center of mass is a flat-to-slightly-positive growth path with a multi-year drag. Reserve the deep-drawdown scenario for the explicit advanced-economy tail, and size it as the tail it is.

## Base rate 2 — Debt/GDP at the point of default (181 episodes)

Across **181 sovereign-default episodes** in the GMD chronology, the distribution of public debt/GDP *at the moment of default*:

| Statistic | Debt/GDP at default |
|---|---|
| Median | **61%** |
| Interquartile range (25th–75th) | **32%–94%** |

The single most important takeaway for risk calibration: **there is no universal "safe" debt level.**

- A full quarter of defaults happened at debt/GDP **below 32%** — and many occurred **below 60%**, i.e. at levels a naïve screen would wave through as comfortable.
- Conversely, **many high-debt sovereigns never defaulted at all** — Japan carries **236.1%** today and the UK twice ran above **250%** (post-Napoleon and post-WWII) without defaulting (see [[02 - Crisis Chronology (Banking, Currency, Sovereign)]] and the G7 debt-capacity panel in [[00 - GMD Overview & Structural Edge]]).
- Default is therefore **not** a mechanical function of the debt ratio. It is driven by **willingness to pay, rollover/liquidity stress, and FX-denomination** of the debt. A 50%-debt sovereign borrowing in a foreign currency with a closing rollover window is more dangerous than a 200%-debt sovereign with its own central bank and a domestic investor base.

The practical consequence: debt/GDP is a **fragility input, not a default trigger.** Use it to rank vulnerability alongside currency denomination, maturity profile and external-financing need (the twin-deficit and fragility screens in [[04 - Current Cross-Country Snapshot (Fragility & Twin Deficits)]]), never as a standalone "this level is safe" rule.

## What it means for positioning

- **Calibrate the banking-crisis node from the median, stress it from the tail.** Base case: flat-to-modestly-positive rGDP with a slow grind-back (the 345-episode median). Adverse case: the slower advanced-economy / 2008 cohort path. Two distinct scenarios from one event study.
- **Stop pricing sovereign risk off a debt threshold.** The 61% median and the 32–94% IQR mean any "safe debt line" is false precision. Score sovereigns on FX-denomination, rollover need and willingness — debt ratio is one factor among several.
- **Feed both priors into sizing and scenario weights.** These are the empirical anchors for the stress book; the page that turns them into position limits is [[Risk Management]]. For the live-regime read of where today's stress sits, see [[Macro Regime - Live (June 2026)]].
- Explore the distributions interactively in the [Global Macro Database Dashboard](Global%20Macro%20Database%20Dashboard.html).

## Sources & method

Global Macro Database (Müller, Xu, Lehbib & Chen 2025; NBER WP 33714) — BankingCrisis and SovDebtCrisis chronology (Reinhart-Rogoff / Laeven-Valencia lineage), 240+ countries, 1086–2030. The 345-episode rGDP event study (P4) and the 181-episode debt-at-default distribution (P12) were both computed from raw GMD by `tools/build_gmd_analysis.py` and independently re-verified (55/56 metrics exact-match, 0 mismatches). See also [[index]] and [[log]].

*Educational; not investment advice.*
