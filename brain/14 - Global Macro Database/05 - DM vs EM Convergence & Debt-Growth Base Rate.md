---
title: DM vs EM Convergence & Debt-Growth Base Rate
category: gmd
type: deep-dive
data_asof: 2026-06
summary: "GDP-weighted DM↔EM convergence (DM debt 71→102%, EM 45→75%, + IMF tail to 2029) and the debt→forward-5y-growth base rate (3.57% → 2.77% across 197 countries)."
tags: [global-macro, gmd, debt, convergence, allocation]
data_vintage: "GMD v2026_06 (current release; cross-country macro to 2024, IMF projections to 2030)"
sources: "Global Macro Database — Müller, Xu, Lehbib & Chen (2025), NBER WP 33714"
updated: 2026-07-03
---

# DM vs EM Convergence & Debt-Growth Base Rate

A strategic-allocation page on two related facts the GMD makes visible: developed-market public debt is **converging up** toward levels once considered emerging-market, and across 197 countries higher starting debt maps to **lower forward real growth**. Together they reframe the DM-vs-EM "quality" gap and set a quantitative prior for long-horizon return assumptions.

## 1. The convergence: DM debt is rising to EM levels

GDP-weighted public debt/GDP, with DM = "High income" economies and EM = everything else (P6, 1995 → 2024):

| Bloc | 1995 | 2024 | Change |
|---|---|---|---|
| **DM** (High income) | 71.4% | **102.1%** | +30.7 pp |
| **EM** (rest) | 45.2% | **74.6%** | +29.4 pp |
| **DM − EM gap** | 26.2 pp | **27.5 pp** | roughly stable |

Two things stand out. First, **DM is converging upward** — at **102.1%** the developed bloc now sits where the historically-EM range used to be; the 2024 EM aggregate of **74.6%** is itself above where DM stood in 1995 (**71.4%**). Both blocs added roughly **+29–31 pp** of debt/GDP over three decades, so the level gap (~27 pp) is broadly intact while the entire distribution has shifted right. Second, the series **extend forward with IMF projections to 2029**, and the projection tail does not bend the trajectory back down — the directional read is more debt, not less.

The implication for the old "DM = safe, EM = fragile" allocation reflex: the *level* distinction is eroding. A DM sovereign carrying **102%** debt/GDP is not categorically distant from an EM sovereign at **75%**. What still separates them is composition and capacity — local-currency funding, deep domestic bond markets, reserve-currency status, and proven historical debt capacity (see the G7 own-history percentiles in [[01 - Where Today Sits vs History (US & G7 Percentiles)]]) — not the headline ratio.

## 2. The base rate: more debt, less forward growth

The pooled debt → forward-growth relationship (P7) is the quantitative spine of this page. Each country-year is matched to its **exact year+5 real GDP**, annualized, across **197 countries** and **n = 13,374** observations:

| Starting public debt/GDP | Mean annualized forward 5y real growth |
|---|---|
| **< 30%** | **3.57%** |
| **30–60%** | **3.37%** |
| **60–90%** | **2.91%** |
| **90–120%** | **2.99%** |
| **> 120%** | **2.77%** |

The gradient is near-monotone and decisive: **growth declines as starting debt rises**, with a **clear break above 60%**. Moving from the lowest bucket (**3.57%**) to the 60–90% bucket (**2.91%**) costs roughly **0.7 pp** of annualized real growth sustained over five years — a large compounding gap. Above 90% the curve flattens into a low-growth plateau (**~2.8–3.0%**), and the **>120% cell is the least robust** — it lands at **2.77%** in the base specification but ranges **~2.7–3.0%** under alternative match conventions, so treat it as "low and uncertain" rather than a precise point.

This is a **base rate, not a forecast** — it is an unconditional cross-country prior, not a country-specific prediction, and it says nothing about causation (high debt and slow growth can be jointly driven by demographics, prior crises, or institutional weakness). Used correctly it disciplines long-horizon return assumptions: a sovereign sitting in the top buckets today should not be penciled in for low-debt-economy trend growth.

### Where the big names sit
Per P7, **the US (122%) and Japan (236%) sit in the top buckets today** — the US straddles the 90–120% / >120% boundary, Japan is deep in the >120% tail. Both therefore inhabit the **~3.0% (or lower) forward-growth** cohort on this base rate. That is the link back to rates: a structurally lower real-growth prior at high debt is exactly the backdrop against which [[Government Bond Yields]] term premia, r-star debates, and debt-sustainability arithmetic get argued.

## 3. Tying the two together

The convergence (Section 1) is *pushing the major developed economies into the low-growth buckets* of the base rate (Section 2). In 1995 the DM bloc at **71.4%** sat near the 60–90% band (~2.91% prior); by 2024 at **102.1%** it sits in the 90–120% band (~2.99%) and individual names like the US and Japan are at or beyond the **>120%** frontier. The cross-section is telling you that the developed world has been migrating along its own downward-sloping debt-growth curve — and the IMF projection tail to 2029 keeps it there. EM, meanwhile, has moved from the **<30%/30–60%** zone in 1995 toward the **60–90%** zone in 2024, shedding part of its historical growth-premium edge from the debt side.

## What it means for positioning

- **Re-anchor long-horizon DM growth lower.** With DM at **102.1%** debt/GDP, the appropriate forward-5y real-growth prior is the **~3.0%** bucket, not the **3.4–3.6%** of low-debt economies. Build that into strategic SAA return assumptions for DM equities and into real-rate / term-premium expectations for [[Government Bond Yields]].
- **The DM-vs-EM "quality" trade is narrower than the reflex.** A 26 pp level gap that is roughly stable while both blocs shift right means the discriminator is **capacity and composition**, not the ratio. Differentiate within EM by funding structure and within DM by proven debt capacity — don't price the blocs as categorically different on debt level alone.
- **Use the gradient, not the corner.** The robust signal is the **decline through 60–90%**; the **>120%** cell is fragile (~2.7–3.0%). For Japan-type tails, lean on country-specific structure (domestic ownership, FX denomination) rather than the noisy top-bucket point estimate.
- **It's a prior, not a timing tool.** This calibrates strategic allocation and scenario growth assumptions; it does not generate tactical entries. Pair it with the live regime read in [[Macro Regime - Live (June 2026)]] for timing.

See also the [Global Macro Database Dashboard](Global%20Macro%20Database%20Dashboard.html) for the interactive convergence and debt-growth views, and [[00 - GMD Overview & Structural Edge]] for the dataset's structural edge over the FRED-based system.

## Sources & method
Global Macro Database (Müller, Xu, Lehbib & Chen 2025, NBER WP 33714) — 240+ countries, 1086–2030 incl. IMF projections, 158 variables, accessed via the official `global_macro_data` Python package `gmd()`. Convergence series (P6, GDP-weighted, DM = "High income") and the pooled debt → forward-5y real-growth base rate (P7, 197 countries, n = 13,374, each country-year matched to its exact year+5 real GDP) were computed from raw GMD by `tools/build_gmd_analysis.py` and independently re-verified (55/56 metrics exact-match, 0 mismatches).

*Educational; not investment advice.*
