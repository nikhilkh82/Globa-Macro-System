---
title: Macro Insights
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "Hidden-signal radar over the audited Explorer catalog (60 concepts): extremes, turns, divergences, composite, cycle clock, analogs, corr shifts, seasonality; Sep-2026 S&P +4.5s, services re-accelerating, UMich 1.4 pctl."
tags: [global-macro, dashboards, patterns, turning-points, divergences, leading-indicators, extremes, 2026-excel]
data_vintage: "computed from the audited Workbook Explorer catalog (2026 workbooks + live FRED retail)"
sources: 1
updated: 2026-09-19
---

# Macro Insights — patterns, turns & divergences

**`Macro Insights/Macro Insights.html`** (tools: `macro_insights.py` → `macro_insights.json` →
`macro_insights_report.py`). Built for: *"appropriate patterns and trends … hidden insights and useful data
visualization for taking actions."* Analytics computed ON TOP of the audited [[2026 Workbook Explorer]] catalog
(456 series in the 2026-09-19 build) — a curated, dedup'd universe of 60 concepts (no cross-group duplicates, no
STALE series).
*Superseded 2026-09-19: 287 series (as stated on this page through 2026-09-11).*
*Superseded 2026-09-11: ~61 concepts (as of 2026-07-17).*

> Decision-support / education only — **NOT investment advice**.

## The eight analytic passes (historical set added 2026-07-17)
5. **Cycle clock** — every fresh indicator as (level-z, Δz6m) on a four-quadrant scatter (Expansion / Slowing /
   Deteriorating / Recovering) with quadrant counts.
6. **Historical analogs** — 14-indicator z-vector distance vs every past month (≥10 shared dims, ≥12m apart,
   last 24m excluded): similarity history charted vs recessions + top-5 analog months with **forward 6/12m
   outcomes for S&P/WTI/unemployment/Fed Funds**. Labeled honestly: *five rhymes are not statistics* — current
   top analogs (anchor month 2026-08, 13 dims populated; Fed Funds is the missing one because its catalogue series
   ends at Jun-2026): 2024-06 (66.5), 2006-05 (66.0), **2007-10 (66.0)**, 1992-02 (60.2), 2014-05 (58.1). Their
   outcomes diverge wildly, which is itself the point (tells you what to watch, not what happens): S&P +12m after them
   +13.6% / +17.1% / −37.1% / +7.1% / +9.9%.
   *Superseded 2026-09-19: top analogs (12 dims) 2024-06 (64.7), 2007-10 (64.4), 2006-05 (64.2), 1992-02 (58.3),
   2021-11 (56.9); S&P +12m after them +13.6% / −37.1% / +17.1% / +7.1% / −10.7% (as of the 2026-09-10 build).*
   *Superseded 2026-09-11: top analogs 2024-06 (71), 2007-11 (66), 1992-02, 2006-08, 1977-01 (as of 2026-07-17).*
   *Pending (2026-09-11): the analogs above use workbook 12's spliced IP for the "IP YoY" dimension. A dry run of
   `macro_insights.py` on the re-sourced catalogue (vhash 4206c88b8f57) populates 13 dimensions, because IP now
   reaches July. Its top five are 2024-06 (66.5), 2006-05 (65.9), 2007-10 (65.8), 1992-02 (60.1) and 2014-05 (57.9).
   The dashboard shows them after its next refresh (see* Data integrity *in [[2026 Workbook Explorer]]).*
   *Resolved 2026-09-19: the rebuilt dashboard (`macro_insights.json` 2026-09-19 15:47) runs on the re-sourced IP. The
   top-five list at the head of this pass is the shipped build's; the dry-run scores in the note above came in
   marginally lower (2006-05 65.9 vs 66.0, 2007-10 65.8 vs 66.0, 1992-02 60.1 vs 60.2, 2014-05 57.9 vs 58.1).*
7. **Correlation regime shifts** — pairs with ≥240m history whose recent-36m corr moved ≥0.6 from the long-run:
   currently (6 pairs) construction payrolls vs total IP (+0.68→−0.80), private payrolls vs continuing claims
   (−0.63→+0.80), Euro-area industry vs consumer confidence (+0.60→−0.81), NFP vs IP-Mfg (+0.73→−0.67),
   capacity utilization vs mfg payrolls (+0.76→−0.34), durables orders vs S&P 500 (+0.53→−0.46) — rolling-corr charts.
   *Superseded 2026-09-19: construction payrolls vs IP-Mfg (+0.69→−0.79), NFP vs total IP (+0.76→−0.66) and
   **PPI vs Core CPI decoupled (+0.49→−0.78)** (as of the 2026-09-10 build). PPI vs Core CPI dropped out because the
   catalogue's Core CPI has no Oct-2025 print, which leaves 9 contiguous YoY months against the 36 this pass needs. That
   is a data-gap exclusion, not a measured re-coupling.*
   *Superseded 2026-09-11: NFP vs continuing claims (−0.64→+0.81), PPI vs Core CPI (+0.50→−0.83) (as of 2026-07-17).*
   *Pending (2026-09-11): both IP pairs above use the spliced IP series. In the same dry run on the re-sourced
   catalogue they become construction payrolls vs total IP (+0.68→−0.80) and NFP vs IP-Mfg (+0.73→−0.67); no
   other pair moves between the two catalogues. Pass 3 also gains a divergence the splice had hidden: IP-Mfg vs
   durables ex-transport (corr 0.89). The dashboard shows these after its next refresh.*
   *Resolved 2026-09-19: the rebuilt dashboard shows both IP pairs above, and IP-Mfg vs durables ex-transport is on
   the divergence radar (corr +0.89, gap 1.03σ).*
8. **Seasonality** — monthly mean/hit-rate for NON-seasonally-adjusted market series only (S&P/WTI/Copper/
   Lumber/TWI; SA macro excluded by design), current+next month highlighted.

## The four core passes
1. **Extremes board** — every series' latest vs its FULL monthly history (z + percentile); ±σ bars, click-through.
2. **Turning points** — fresh 3m-vs-6m inflections (Rolling over / Bottoming / accelerating), ranked by Δz(6m);
   requires a **contiguous 13-month tail** (the gap-broken 24 PMI series (23 countries + global) can't fake a pattern).
3. **Divergence radar** — pairs with |corr| ≥ 0.6 over ≥48 overlapping months (YoY paths; point-diffs for
   negative-capable series) whose **last-6m paths gapped ≥1σ** in own-vol units (sign-flipped for anti-correlated
   pairs); one appearance per series; dual-line 36m charts.
4. **Leading composite** — mean z of 8 classic leaders (ISM New Orders, Permits, Claims⁻¹, 2s10s, BBB spread⁻¹,
   XHB, NFIB Leading, UMich Expectations), monthly 1986→, charted vs NBER recessions.

Every row/card **deep-links into the Workbook Explorer** (`#s=` hash) with the series preloaded — insight → full
interactive analysis in one click. Auto-written "what the data is saying" bullets state only what the numbers
support.

## Live read — 2026-09-19 (current)
*`macro_insights.json` generated 2026-09-19 15:47 on the rebuilt Explorer catalogue (`wb_explorer.json` built
2026-09-19T15:47:15, asof 2026-09-18, vhash 6d3783a9bace, 456 series) · universe 60 concepts (56 fresh) · 16 extremes ·
12 turns · 8 divergences · 6 corr-regime shifts · 5 seasonality series. Supersedes the 2026-09-11 read below as the
current read; that section is kept verbatim as a dated record.*
- **Hard-vs-soft split unchanged on the board**: S&P +4.49σ (100th pct, Aug), Copper +3.15σ (100th, Aug), PPI +2.78σ
  (99.9th, Jul), Durables total 99.5th / ex-Transport 100th (Jul), Retail headline 99.5th (Jul) with food services
  (100th) and motor vehicles (99.8th) now through Aug, M2, Core CPI & Core PCE 100th (Jul). On the other side, UMich
  headline 51.7 sits at the **1.4th pct** (z −2.27, Aug) and UMich Expectations at the 4.1th pct (z −1.84), both *Bottoming*.
- **Momentum still skews to acceleration**: of 56 fresh series, 23 *Rising (accelerating)* (24 on 2026-09-11),
  6 *Rolling over*, 5 *Falling (accelerating)*, 4 *Bottoming*. The biggest Δz(6m) moves are unchanged: Philly Fed +1.54,
  NFIB capex plans +1.13, ISM Services New Orders +0.79 (all *Rising (accelerating)*); housing completions −0.65
  *Falling (accelerating)*. Headline and Core CPI carry no pattern, because the catalogue's CPI series have no
  Oct-2025 print and their 13-month tails are not contiguous.
- **Divergence radar (8)**: Philly Fed vs Copper 3.12σ (corr +0.62), 2Y Treasury vs USD TWI 1.61σ (+0.64), ISM Mfg
  New Orders vs UK Services PMI 1.42σ (+0.74), NFIB hiring vs Euro-area Industry Confidence 1.41σ (+0.81), M2 vs 10y
  TIPS real yield 1.18σ (−0.66), Permits vs Starts 1.05σ (+0.74), 2s10s vs S&P 1.05σ (+0.65), IP-Mfg vs Durables
  ex-Transport 1.03σ (+0.89). Core CPI vs USD TWI (1.71σ on 2026-09-11) is off the radar for the same Oct-2025 hole:
  Core CPI has 9 contiguous YoY months, short of the 48 the radar needs, so its exit is not a measured convergence.
- **Leading composite +0.335σ (Jul-2026)**, unchanged: XHB +2.29 vs UMich Expectations −1.84 (BBB spread⁻¹ +0.98,
  Claims⁻¹ +0.60; ISM New Orders −0.18, 2s10s −0.13). Analogs and correlation shifts now run on the re-sourced IP
  (passes 6–7 above).
- **What the board cannot see yet**: its inputs are mostly Jun–Aug monthly prints (only the TIPS and credit-spread
  series carry a 4 Sep value), so they predate the week both major central banks tightened as the energy shock
  re-intensified. The Fed's first hike (to 3.75–4.00%, effective 17 Sep) and the ECB's second move (to 2.50%, effective
  16 Sep) came as WTI rose to $107.02 and Brent to $130.80 (15 Sep), with August PPI at +9.85% y/y. The catalogue's WTI
  stops at its 31 Aug print (85.76, *Rolling over*) because the commodity workbook was not updated past 2026-08-31, so
  treat that flag as out of date; its Fed Funds series ends at 3.63% (Jun-2026). Demand and labour were firm into
  September, not fading (August retail sales +1.24% m/m and payrolls +162k; initial claims 196k in the week of
  12 Sep), which sits on the hard side of the split. Core CPI is +2.45% y/y, its 3-month pace up to 1.97% from 1.64%
  but still below 2%; core PCE is 3.34% (Jul).

## Live read — 2026-09-11
*`macro_insights.json` generated 2026-09-10 13:10 · universe 60 concepts (56 fresh) · 16 extremes · 12 turns ·
8 divergences · 6 corr-regime shifts · 5 seasonality series. Supersedes the 2026-07 first-run findings below as the
current read; that section is kept verbatim as a dated record.*
- **Hard-vs-soft split still open, soft side lifting off the floor**: S&P +4.49σ (100th pct, Aug), Copper +3.15σ
  (100th, Aug), PPI +2.78σ (99.9th, Jul — just off its peak), Durables total 99.5th / ex-Transport 100th, Retail
  headline 99.5th, M2, Core CPI & Core PCE 100th — vs UMich headline 51.7 at the **1.4th pct** (z −2.27, Aug) and
  UMich Expectations at the 4.1th pct (z −1.84), both *Bottoming*.
- **Momentum skews to acceleration**: of 56 fresh series, 24 *Rising (accelerating)*, 6 *Rolling over*,
  5 *Falling (accelerating)*, 4 *Bottoming*. Biggest Δz(6m): Philly Fed +1.54, NFIB capex plans +1.13, ISM Services
  New Orders +0.79, NFIB hiring plans +0.56 (all *Rising (accelerating)*); ISM Services Business Activity (+0.32) and
  ISM Manufacturing (+0.33) also accelerating. Still weakening: UK Services PMI (Jun, 5.9th pct) and ISM Mfg New
  Orders (Aug), both *Falling (accelerating)*; WTI, Durables total, Lumber and USD TWI *Rolling over*.
- **Widest divergences** (8 on the radar): Philly Fed vs Copper 3.12σ (corr +0.62), Core CPI vs USD TWI 1.71σ
  (+0.62), ISM Mfg New Orders vs UK Services PMI 1.42σ (+0.74), NFIB hiring vs Euro-area Industry Confidence 1.41σ
  (+0.81) — none of the four 2026-07 pairs is still on the radar.
- **Leading composite +0.335σ (Jul-2026)**, up from +0.078 (May) and +0.194 (Jun); member dispersion still extreme:
  XHB +2.29 vs UMich Expectations −1.84 (BBB spread⁻¹ +0.98, Claims⁻¹ +0.60; ISM New Orders −0.18, 2s10s −0.13).

> **Flag — overturns part of the 2026-07 read below:** the *services momentum inflection* has reversed — Philly Fed,
> ISM Services New Orders & Business Activity (then *Rolling over*) and NFIB hiring plans (then *Bottoming*) are all now
> *Rising (accelerating)*; only UK services still *Falling (accelerating)*. UMich is off its all-time low (1.4th pct,
> *Bottoming*), and PPI is at the 99.9th pct, no longer the 100th.

## First-run findings (2026-07)
- **Hard-vs-soft split**: S&P +4.5σ, PPI at its **113-year 100th percentile**, Copper +2.9σ, Durables/Retail/M2
  at ~100th pct — while **UMich sentiment sits at its all-time low** (0.3rd pct). One side usually closes.
- **Services momentum inflection**: Philly Fed, ISM Services New Orders & Business Activity all *Rolling over*;
  UK services *Falling (accelerating)*; NFIB hiring plans *Bottoming* — while ISM manufacturing still accelerates.
- **Widest divergences** (36 contiguous months, window must end now — audit-hardened): Durables vs WTI (2.9σ),
  ISM Services Orders vs NFIB hiring (2.4σ), Private Payrolls vs USD TWI (2.2σ), ISM Orders vs Copper (2.0σ).
- **Leading composite +0.22σ (mildly positive)** with extreme member dispersion: XHB +2.3 vs UMich Exp −1.9.

## Related
[[2026 Workbook Explorer]] (the data + deep-link target) · [[Interactive Macro Charts]] · [[PTMI Trading Dashboard]]
(per-workbook patterns) · [[Global Macro Trading Dashboard]] (tickets) · [[Cross-Country Endo & Divergence Backtest]] ·
[[2026 Trading System — Operating Manual]]
