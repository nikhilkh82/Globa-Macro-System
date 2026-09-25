---
title: Prediction-Market Macro System
category: strategy-lab
type: live-read
data_asof: 2026-09-19
summary: "Live Polymarket crowd odds on macro catalysts as an event-risk read, plus a calibration study (ECE 5.25%); 2026-09-19: after the Fed's Sept hike, Oct 25bp hike priced 55.5%, P(Fed cut 2026) ≈ 4.55%, recession 8.5%"
tags: [global-macro, strategy, prediction-market, polymarket, calibration, event-risk, signals]
data_vintage: "LIVE (Polymarket Gamma + CLOB)"
sources: 1
updated: 2026-09-19
---

# Prediction-Market Macro System

A **prediction-market macro-signal & calibration system** adapting the [prediction-market-analysis](../../raw/11.%20Strategies/prediction-market-analysis-main/) project to live, free **Polymarket** data. It turns crowd-implied odds on macro catalysts (Fed path, recession, geopolitics) into a tradeable event-risk view, and recreates the source project's headline analysis — **calibration & the favorite-longshot bias** — on resolved markets. Built 2026-06-22.

> Research/education only — prediction-market odds are crowd estimates, not guarantees. See disclaimer.

## Provenance — what we adapted
The source ([jon-becker/prediction-market-analysis](../../raw/11.%20Strategies/prediction-market-analysis-main/)) is a research framework over the largest public **Polymarket + Kalshi** market/trade dataset (36 GiB), with analyses on **calibration**, **favorite-longshot bias**, and **who-wins/loses** (execution vs information). We don't have the 36 GiB trade set, but the **Polymarket Gamma + CLOB APIs are reachable** from this environment (like FRED/CFTC), so we rebuilt the two most useful pillars on **live data**:
1. a **macro signal** the source doesn't surface (crowd odds on macro catalysts → an event-risk read), and
2. a **market-level calibration / favorite-longshot study** (the source did it at trade level on the full dataset).
Kalshi's public settled feed here is sports-dominated and lacks clean categories, so Polymarket is the primary source.

## How it works
### 1. Macro signal (live, active markets)
Pull current Polymarket markets, keep the macro-relevant ones via a **word-boundary keyword** classifier across themes — **Fed / Rates, Inflation, Growth / Recession, Fiscal / Policy, Geopolitics, Markets** — above a $25k volume floor, read each market's implied probability (`outcomePrices[0]` = P(Yes); all 162 macro markets in the 2026-09-19 feed have Yes as their first outcome), and derive headline signals (e.g. **P(any Fed cut in 2026) = 1 − P("no cuts" market)**). Each theme carries an asset-implication note.

### 2. Calibration / favorite-longshot (resolved markets)
For a sample of cleanly-resolved high-volume binary markets, fetch the **CLOB price history**, take the market's **mean implied probability over its life excluding the final 3 days** (the forecast), and pair it with the **actual outcome** (the winner is read from that same token's settlement price — *not* the separately-ordered `outcomePrices` array). Bucket all positions by decile → calibration curve, **ECE / MCE / Brier** (all over one 1–99% population), and the win-rate-by-price that exposes the favorite-longshot bias.

## Outputs (`Prediction Market/`)
- **`Prediction Market Dashboard.html`** — self-contained, light theme, Chart.js inlined: headline-signal KPIs, macro read by theme, top-markets implied-probability bar, calibration grouped bar, calibration curve vs the 45° line, and a 45-row macro-markets table.
- **`Prediction Market Note <date>.md`** + **`predmkt_<date>.json`** (machine-readable).
Tools: `tools/predmkt.py` (client) · `tools/build_predmkt.py` (engine) · `tools/predmkt_report.py` (HTML+MD) · `tools/build_predmkt_all.py` (one command). Run: `python tools/build_predmkt_all.py`.

## Snapshot — 2026-09-19 (live, current)
*Supersedes the 2026-09-08 snapshot below (kept verbatim as the record). Source: `Prediction Market/predmkt_latest.json`, as_of 2026-09-19 (generated 14:24); macro backdrop from the FRED snapshot verified 2026-09-19. Volumes are the source's `vol` field in $.*

- **The September hike happened — the crowd now leans toward a second one:** the Fed raised 25 bp to a **3.75–4.00%** target range, effective 2026-09-17 (EFFR 3.88% on 2026-09-17) — the first hike of the cycle — and the ECB raised its deposit rate 2.25% → **2.50%**, effective 2026-09-16. For the **October 28 FOMC** the crowd prices a 25 bp hike at **55.5%** ($1.7M), 50+ bp hike 0.95% ($1.3M), 25 bp cut 0.55% ($1.5M), 50+ bp cut 0.35% ($1.1M). The September-FOMC complex, "Fed rate hike in 2026?" and "Fed Rate Hike by October 2026 Meeting?" markets quoted on 2026-09-08 are no longer in the active feed.
- **Headline signals:** **P(any Fed cut in 2026) ≈ 4.55%** (derived as 1 − P("Will no Fed rate cuts happen in 2026?") with that market at 95.45%, $8.4M; was ≈ 7.4% on 2026-09-08) and **recession market 8.5%** ("US recession by end of 2026?", $2.0M; was 6.5%) — recession odds edged up but stay low, in line with demand that is firm, not fading (retail sales +1.24% m/m and payrolls +162k in Aug-2026; initial claims 196k, week of 12 Sep).
- **Backdrop (FRED, 2026-09-19 snapshot):** both major central banks tightened in the same week the energy shock re-intensified — WTI $107.02 and Brent $130.80 (2026-09-15), PPI all-commodities +9.85% y/y (Aug-2026). Headline CPI +3.35% y/y and core CPI +2.45% y/y (Aug-2026; core's 3-month annualised pace 1.97%), core PCE +3.34% y/y (Jul-2026); 2y 4.67% / 10y 4.94% (2026-09-17), 10Y–2Y +0.25 (2026-09-18), flattened from +0.33 (2026-09-15) — a bear-flattening on 16 Sep (2y +7 bp, 10y +1 bp), then a parallel 7 bp rally on hike day 17 Sep (2s10s unchanged); VIX fell 17.71 → 15.44 on 2026-09-17 and HY OAS tightened 2.76 → 2.70 on 2026-09-16, the day before the hike took effect (unchanged on 17 Sep), so equities and credit absorbed the hike.
- **Universe:** 162 macro markets across 4 active themes (was 153). Geopolitics 98 markets / $341.0M still dominates by volume; Markets 46 / $86.9M; Fed / Rates 17 / $58.6M (was 20 / $141.3M — the September-FOMC markets have left the feed); Growth / Recession 1 / $2.0M (the recession market alone).
- **Top geopolitics odds (oil / risk-relevant):** "Will the U.S. invade Iran before 2027?" **15.5%** ($67.0M, still the largest macro market; was 14.5%); "Will China invade Taiwan by end of 2026?" 3.95% ($42.3M); "Putin out as President of Russia by December 31, 2026?" 4.5% ($21.8M; was 7.5%); Strait of Hormuz traffic back to normal by September 30 **0.6%** ($9.1M), by October 31 6.5% ($0.7M) and by December 31 **17.5%** ($11.8M; was 24.5%) — the crowd now puts ~82.5% (1 − 17.5%) on Hormuz disruption persisting through year-end, consistent with Brent through $130. "Iran-Oman Hormuz Agreement by September 30?" trades at 8% ($0.7M). The by-September-15 leg still sits in the active feed at 0.05% ($2.5M) past its 2026-09-16 end date, i.e. effectively resolved No.
- **Calibration (320 markets, 372 positions, 1–99% range):** **ECE 5.25%**, MCE 15.88%, **Brier 0.1186** — identical to 2026-09-08 bucket for bucket (0–10%: implied 3.6% → resolved 1.1%, n 93; 90–100%: implied 96.4% → won 98.9%, n 93), consistent with the daily signal-only refresh reusing the stable calibration block rather than re-running it. Build health: degraded false, pages_failed 0, clob_empty 2, ambiguous_skipped 32.
- **What changed vs 2026-09-08:** the event-risk read moves from *hike risk* to *hike delivered, a second one slightly favoured* — September's coin-flip 25 bp hike (51.5%) was delivered, October's 25 bp hike is now 55.5%, P(cut) 7.4% → ≈ 4.55%, recession 6.5% → 8.5%; Hormuz normal-by-year-end 24.5% → 17.5%, U.S.-invade-Iran 14.5% → 15.5%; universe 153 → 162 markets; calibration unchanged (ECE 5.25%).

## Snapshot — 2026-09-08 (live)
*Supersedes the 2026-06-22 snapshot below (kept verbatim as the build record). Source: `Prediction Market/predmkt_latest.json`, as_of 2026-09-08 (generated 09:12); macro backdrop from the FRED snapshot verified 2026-09-08. Volumes are the source's `vol` field in $.*

- **Macro signal — the crowd has flipped from "no cuts" to "hikes":** **P(any Fed cut in 2026) ≈ 7.4%** (derived as 1 − P("Will no Fed rate cuts happen in 2026?") with that market at 92.65%, $8.2M; was ≈ 20% in June) and **recession market ≈ 6.5%** ("US recession by end of 2026?", $1.7M; was ≈ 12%). "Fed rate hike in 2026?" trades at **70.5%** ($8.8M) and "Fed Rate Hike by October 2026 Meeting?" at 61.5%.
- **September 16 FOMC (the deepest Fed/Rates complex by volume):** 25 bp hike **51.5%** ($19.2M), 50+ bp hike 0.55% ($13.9M), 25 bp cut 0.45% ($32.2M), 50+ bp cut 0.15% ($13.8M) — a coin-flip hike against essentially zero cut odds. Backdrop (FRED, 2026-09-08 snapshot): EFFR 3.63% (2026-09-03), headline CPI 3.3% YoY and core PCE 3.34% YoY (Jul 2026), 2y 4.34% / 10y 4.77% (2026-09-03).
- **Universe:** 153 macro markets across 4 active themes (was 157). Geopolitics 94 markets / $331.5M still dominates by volume; Fed / Rates 20 / $141.3M; Markets 38 / $77.6M; Growth / Recession 1 / $1.7M (the recession market alone).
- **Top geopolitics odds (oil / risk-relevant):** "Will the U.S. invade Iran before 2027?" **14.5%** ($64.9M, the largest macro market); "Will China invade Taiwan by end of 2026?" 3.75% ($41.0M); "Putin out as President of Russia by December 31, 2026?" 7.5% ($20.2M); Strait of Hormuz traffic back to normal by September 30 **2.15%** ($7.9M) and by December 31 **24.5%** ($10.5M) — the crowd puts ~75% (1 − 24.5%) on Hormuz disruption persisting through year-end. The by-August-31 leg still sits in the active feed at 0.05% ($18.1M) past its 2026-09-01 end date, i.e. effectively resolved No.
- **Calibration (320 markets, 372 positions, 1–99% range):** **ECE 5.25%**, MCE 15.88%, **Brier 0.1186** (June build snapshot: 4.1% / 17.6% / 0.114 on 370 positions — the calibration block has been re-run since June, not merely reused). Still **well-calibrated** with the same **mild favorite-longshot bias**: the 0–10% bucket (mean implied 3.6%, n 93) resolved **1.1%**; the 90–100% bucket (mean implied 96.4%, n 93) won **98.9%**. The MCE now lives in the thin middle: 40–50% (implied 44.5%) resolved 28.6% on n 14, 50–60% (55.5%) resolved 71.4% on n 14, 80–90% (85.5%) resolved 72.0% on n 25. Build health: degraded false, pages_failed 0, clob_empty 2, ambiguous_skipped 32.
- **What changed vs 2026-06-22:** the event-risk read moves from *higher-for-longer* to *hike risk* — P(cut) 20% → 7.4%, recession 12% → 6.5%, a 2026 hike priced 70.5% with September a coin-flip; universe 157 → 153 markets; ECE 4.1% → 5.25% on 370 → 372 positions, favorite-longshot tails unchanged (1.1% / 98.9%).

## Snapshot — 2026-06-22 (live)
- **Macro signal:** **P(any Fed cut in 2026) ≈ 20%** (hawkish / higher-for-longer — market leans toward *no* cuts), recession market ≈ 12%. 157 macro markets across 4 active themes (Fed/Rates, Geopolitics, Growth/Recession, Markets); Geopolitics dominates by volume (Iran/Russia/Taiwan conflict markets — oil/risk-relevant).
- **Calibration (320 markets, 370 positions, 1–99% range):** **ECE 4.1%**, MCE 17.6% (small mid-buckets), **Brier 0.114** — Polymarket is **well-calibrated**, with a **mild favorite-longshot bias**: longshots (1–10% priced) resolved only **1.1%** of the time (overpriced), while favorites (90–100% priced) won **98.9%** (underpriced). Mirrors the source project's finding.

## Caveats
- Crowd odds are estimates, not guarantees; thin/short-lived markets are noisy.
- **Market-level** calibration (mean life price), not the source's trade-level study (no 36 GiB trade set here); high-volume + decisively-resolved sample (a selection); the 1–99% population excludes near-certain positions so ECE reflects genuine mid-range skill.
- This is **live-markets data** — keep separate from the vintage teaching corpus.
- Adversarially audited (3-lens workflow) → **8 defects fixed before publishing** (most importantly an `outcomePrices`↔`clobTokenIds` ordering mismatch that had corrupted ~5.5% of the calibration sample). See the [[log]].

## Integration
Wired into the [[Analyst System — Live Cockpit (June 2026)|cockpit]] as **§7 "Event Risk — Crowd Odds (Polymarket)"** — headline KPIs (P(Fed cut), recession, calibration ECE) + a top-macro-markets table + drill-down. The cockpit's `refresh_analyst.ps1` runs `build_predmkt_all.py signal` (a **~2.5s signal-only** path, timed at the 2026-06-22 build, that reuses the stable calibration) so the panel stays current daily; re-run the full `build_predmkt_all.py` (no arg, ~3 min at the 2026-06-22 build) to refresh the calibration study itself.

## Related
[[Macro Regime - Live (June 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[LangAlpha Strategy System]] · [[Analyst System — Live Cockpit (June 2026)]] · [[The Global Macros Framework]]
