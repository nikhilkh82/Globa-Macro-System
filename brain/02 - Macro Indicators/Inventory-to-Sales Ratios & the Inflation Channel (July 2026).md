---
title: Inventory-to-Sales Ratios & the Inflation Channel
category: indicators
type: live-read
data_asof: 2026-09-19
summary: "Retail I/S leads core CPI by 5m (+2.0% held-out, sign-stable). Jul-26 retail I/S rose to 1.27, its first 3m rise since Oct-25: the destocking impulse behind Aug core firming (3m-ann 1.97% from 1.64%) has faded to ~zero."
tags: [global-macro, inventories, inventory-to-sales, inflation, cpi, lead-lag, destocking, restocking, honest-negative]
data_vintage: "I/S through Jul-2026 (Census via FRED, read from the Workbook Explorer vintage rebuilt 2026-09-19; Jun-2026 manufacturers revised 1.48 -> 1.47, Jul-2025 retail 1.29 -> 1.28); CPI through Aug-2026; the ADF and held-out econometrics are the 2026-07 engine run, not re-run since"
sources: 1
updated: 2026-09-19
---

# Inventory-to-Sales Ratios & the Inflation Channel

The inventory-to-sales (I/S) ratio divides the period's inventory value by the same period's sales — how many months of sales the shelf currently holds. Rising I/S means inventory is building faster than it sells (firms pull back on production and orders); falling I/S means demand is eating the shelf (the setup for a restocking cycle).

Live in the Explorer as **`LEI:ISRET`** (retailers), **`LEI:ISMFG`** (manufacturers), **`LEI:ISTOT`** (total business) — **415** monthly observations from Jan-1992 to Jul-2026, Census via FRED (414 at the Jun-2026 vintage).

**Current read (I/S Jul-2026 · prices Aug-2026; refreshed 2026-09-19):** retailers **1.27** · manufacturers **1.47** · total **1.30** — July is the first new Census print since the 2026-09-16 read, and it moves the leading leg: retail I/S rose **+0.02** in the month (1.25 → 1.27), taking its 3-month change to **+0.01**, the first positive 3-month change since Oct-2025. Manufacturers (**−0.02** over three months) and total (**0.00**) are flat to falling. The price readings are unchanged since the last read because August is still the latest CPI print: headline CPI **+3.35% YoY**, core CPI **+2.45% YoY** (Aug-2026), with core's **3-month annualised rate at 1.97%**, up from 1.64% in July.

*(2026-09-19 — supersedes the 2026-09-16 readings — I/S through Jun-2026: retailers 1.25 · manufacturers 1.48 · total 1.30 — recorded inline here. Two changes. First, the July release revised June manufacturers from 1.48 to **1.47**, so the manufacturers' 3-month change to Jun-2026 is **−0.04**, not −0.03. It also revised Jul-2025 retail from 1.29 to 1.28, which is what makes Oct-2025's retail 3-month change +0.01; on the 2026-09-16 vintage the last positive one was Jun-2025. Second, and more important, the retail leg — the one that carries the core-CPI signal — has stopped falling. On the 5-month lead, July's retail reading maps onto **Dec-2026** core CPI, and on the channel's own terms a rising retail ratio precedes softer, not firmer, core momentum. It is one month of a first-print ratio, and this page withdrew the 2026-09-08 read for over-reading exactly that kind of wobble: read it as the destocking impulse having faded to roughly zero, not as a confirmed reversal, until the August I/S print confirms or revises it. The energy figure in the 2026-09-16 scoring section below is also dated: WTI was $107.02 on 2026-09-15, +68.1% y/y. The 2026-09-16 note below is kept as that read's record.)*

*(Supersedes the price side of the 2026-09-08 read, which had CPI +3.30% YoY through Jul-2026. It also **withdraws that read's conclusion.** Two corrections. First, "inventories are building slightly at the total and manufacturer level" over-read a one-month wobble: on the stationary 3-month-change form this page insists on, all three ratios are still falling in the three months to Jun-2026 — retail **−0.01**, manufacturers **−0.03**, total **−0.02**. Destocking has slowed, not reversed. Second, "headline CPI decelerates … easing, not intensifying" did not survive August: core CPI momentum firmed. The direction of the channel is intact; what has weakened is the size of the impulse still in the pipe.)*

## What the August CPI did to the channel — 2026-09-16

The August CPI is the first genuine out-of-sample observation this page has received since the channel was estimated, so it is worth scoring explicitly rather than folding into the numbers above.

**The prior.** Falling retail I/S precedes firmer **core** CPI by about 5 months, sign-stable, ~+2.0% held-out error reduction.

**What the leading leg did.** Retail I/S fell through the whole first half: 1.28 (Jan-26) → 1.27 → 1.26 → 1.26 → 1.26 → **1.25** (Jun-26), with the 3-month change negative in every one of those months. On a 5-month lead that maps Jan-26's decline onto **Jun-26** core CPI and Mar-26's onto **Aug-26**.

**What landed.** Core CPI's 3-month annualised rate went **1.64% (Jul) → 1.97% (Aug)**, with August core up **+0.29% m/m**. On the momentum measure the sign is **confirmed**, at roughly the predicted timing.

**Where it did not confirm.** Core CPI *year-over-year* did not firm — it went 2.57% (Jun) → 2.47% (Jul) → **2.45% (Aug)**, still drifting down on base effects. The channel is a statement about the *change* in core inflation, and the YoY level is the wrong instrument to score it with; but a reader who only watches YoY would have recorded this month as a miss, and that disagreement should be visible rather than smoothed away.

**What this does to the forward read.** Nothing yet, and deliberately so. One observation against a 14-origin held-out window does not upgrade a prior — it is consistent with it. The more useful signal is in the leading leg: the destocking impulse is **fading**. The manufacturers' 3-month change has shrunk from −0.06 (Apr-26) to −0.03 (Jun-26), total from −0.05 to −0.02. On the same 5-month lead, the inflation impulse arriving in **late 2026 and early 2027 is smaller than the one that has just landed** — the channel points the same way, with less force.

**Do not read this into headline CPI.** Headline's own 3-month annualised rate is **+0.18%**, because June fell 0.42% m/m; headline YoY is +3.35% only because of energy — WTI is up ~52% YoY. The inventory channel does not speak to energy, which is exactly why the headline version of this test was fragile in the first place.

> **Data-quality note (2026-09-16).** `CPIAUCSL` and `CPILFESL` are **missing an Oct-2025 observation** on FRED. Any YoY computed by stepping back 12 *observations* in the series instead of 12 *calendar months* therefore returns a 13-month change: for Aug-2026 that mis-prints headline as +3.71% (vs Jul-2025) instead of **+3.35%** (vs Aug-2025), and core as +2.76% instead of **+2.45%**. Every CPI YoY on this page is computed against the same calendar month of the prior year and was checked against the raw FRED observations today. The 3-month annualised figures are unaffected — the last three months have no gap.

## The standard narrative

The widely-taught sequencing — and the one attached to the MacroMicro CPI-vs-I/S chart — runs: after a crisis, policy support revives consumption; **retail I/S falls first** (essentials sell through), **manufacturing I/S follows** as demand works upstream, and once the **restocking cycle** begins, **inflation rises**. The 2000 and 2008 episodes are the cited evidence.

This page tests that story with the desk's audited engines rather than repeating it. *(Every estimate in the table below — the ADF statistics, the correlations, the held-out gains — is the **2026-07 engine run** and has not been re-run since; only the data readings above (refreshed 2026-09-19) and the scoring section (2026-09-16) have been refreshed since.)*

## What the data actually supports

**First, the levels are not usable.** ADF on the I/S levels: retailers **−1.49**, manufacturers **−2.12** — both fail to reject a unit root at the 5% critical value (−2.88). Correlating I/S *levels* against CPI is therefore a spurious-regression trap, and it shows: an unconstrained lead-lag scan on levels returns its "best" lead pinned exactly at the scan boundary (18m and 24m), the signature of shared drift rather than a real lead. **All results below are computed on stationary 3-month-change forms.**

| Claim tested | Stationary correlation | Held-out OOS test (ADL vs AR baseline) | Verdict |
|---|---|---|---|
| Retail I/S turns **before** manufacturing I/S | r **+0.59** at a **1-month** lead (n=409) | selection window +3.2% → **held-out −0.9%**, relation **FRAGILE** | **Does NOT survive.** Real co-movement, no forecast value |
| I/S predicts **headline CPI** | dMFG leads CPI YoY by 9m, r **−0.25** | retail I/S, 5m lead, **+2.3%** held-out, pred-corr +0.51, but **FRAGILE** | Marginal, unstable |
| I/S predicts **core CPI** | — | retail I/S, **5m lead**, **+2.0%** held-out gain, pred-corr **+0.31**, **STABLE** | **Survives** — the one durable link |

**The sequencing half of the narrative fails the honest test.** Retail and manufacturing I/S changes genuinely move together (r = 0.59 at a one-month lead), but that co-movement adds *nothing* to forecasting manufacturing I/S beyond its own persistence: it scored +3.2% on the selection window and **−0.9% on the held-out window**, and its sign is not stable across half-samples. That gap between selection and held-out performance is exactly the winner's curse the nested evaluation exists to catch.

**The inflation half survives, modestly.** Retail I/S leads **core** CPI by about 5 months with a genuine ~2% out-of-sample error reduction and, importantly, a **sign-stable** relationship across half-samples. The direction matches the narrative: falling I/S (destocking into firm demand) precedes firmer core inflation. The headline-CPI version is fragile — unsurprising, since headline carries energy noise the inventory channel does not speak to.

**Caveat, stated plainly:** the held-out window is only **14 origins**. These are low-power tests. A ~2% RMSE improvement is a real but small edge, and it is one input among many — in the Explorer's full leader tournament for core CPI, retail I/S competes against ~20 other leaders and does *not* win (UMich sentiment led at −5% held-out as of the 2026-07 run; the tournament was not re-run on 2026-09-16 or 2026-09-19).

## How to use it

- Read I/S **in changes, never levels** — the levels are unit-rooted and will manufacture false relationships.
- Treat the retail→core-CPI link as a **5-month directional prior**, sized small, not a timing signal.
- Score it on **core CPI momentum (3m annualised), not core CPI YoY** — August 2026 is the worked example of the two disagreeing, and YoY base effects will keep them disagreeing for several more months.
- Read the **size** of the I/S change, not just its sign: the 3-month declines shrank from Apr-2026, and in Jul-2026 the retail change turned positive (**+0.01**), so the prior currently argues for a *smaller* inflation impulse into Dec-2026 than the one that landed in August — from the retail leg, on July's first print, close to none; no I/S print yet maps onto 2027 (Aug-2026 I/S maps to Jan-2027).
- Do **not** trade the retail→manufacturing sequencing story; it is descriptive, not predictive.
- Both I/S ratios are now in the Explorer's **relation-chip leader pool**, so their held-out performance against every lagging target is recomputed automatically on each data vintage — if the relationship strengthens, the chips will show it without anyone re-running this analysis.

## Related

[[Leading Indicators]] · [[Coincident Indicators]] · [[Lagging Indicators]] · [[Conference Board LEI & Leading-Lagging Map]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] · [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] · [[2026 Workbook Explorer]]
