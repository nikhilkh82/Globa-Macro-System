---
title: Currency Collapse & Early-Warning Signatures
category: gmd
type: deep-dive
data_asof: 2026-06
summary: "The hyperinflation universe (107 episodes / 42 countries, M2~inflation 1:1) and the REER pre-currency-crisis overvaluation fingerprint (+7.8% vs +0.6% since 1960)."
tags: [global-macro, gmd, currency-crisis, hyperinflation, reer]
data_vintage: "GMD v2026_06 (current release; cross-country macro to 2024, IMF projections to 2030)"
sources: "Global Macro Database — Müller, Xu, Lehbib & Chen (2025), NBER WP 33714"
updated: 2026-07-03
---

# Currency Collapse & Early-Warning Signatures

The currency lens on the Global Macro Database: the full hyperinflation universe that FRED simply does not contain, the quantity-theory regularity that governs it, and the single most reliable pre-crisis early-warning signature — real-exchange-rate overvaluation. This page is the EM/frontier FX and duration tail-risk screen that overlays the FRED-based system.

## What this is

A standing reference for spotting currency blow-ups *before* they happen. It pairs (1) the historical population of monetary collapses with (2) a forward-looking overvaluation fingerprint you can run on live REER data, so the macro PM can size and hedge FX/duration tail risk in EM and frontier markets rather than discover it after the fact.

## The hyperinflation universe

GMD records **107 country-years across 42 countries** with inflation **>500%** — of which **68 cleared >1000%**. This is the catalogue of full monetary collapse: **Weimar Germany 1923, Serbia 1994, Hungary 1945, Zimbabwe, Venezuela, Bolivia 1985**, among others.

The structural point is one of *coverage*: **none of these episodes exist in FRED.** A US-centric data system is blind to the entire tail of the currency-risk distribution. The GMD's 240-country breadth is what makes a genuine currency-collapse screen possible at all — see [[00 - GMD Overview & Structural Edge]].

## The quantity-theory slope (M2 ≈ inflation, 1:1)

Inside the high-inflation regime, the mechanism is not mysterious. **Annual M2 growth and inflation track a ~1:1 quantity-theory slope** — print at X%, get roughly X% inflation. Once an economy enters this regime, money growth is the inflation forecast; there is no stable velocity offset to hide behind.

Decision-relevant implication: for a currency already in or approaching the high-inflation regime, **monitor M2 growth as the leading variable** — it is the cleanest single read on where prices (and the FX rate) are headed. The 1:1 relationship is what turns runaway money creation into a near-deterministic FX short.

## The early-warning signature: REER overvaluation

The forward-looking edge is the **currency-crisis early-warning signal**. Measuring the real effective exchange rate against its own trailing 5-year mean (since 1960):

| Window | REER vs trailing 5y mean |
|---|---|
| **Year *before* a currency crisis** | **+7.8%** |
| All other years | **+0.6%** |

In the year before a currency crisis the REER sits, on average, **+7.8% above its own 5-year trend versus just +0.6%** in normal years — a **~7.2-point overvaluation gap**. A currency that has drifted meaningfully rich to its own recent history is wearing the fingerprint of an impending crisis. This is a *relative-to-own-trend* signal, not a cross-country valuation call, which makes it portable across very different economies.

## How to use — the screening overlay

This page is the tail-risk overlay on the FRED signals, applied to EM/frontier FX and the duration that travels with it.

- **Screen 1 — overvaluation fingerprint.** Rank EM/frontier currencies by REER vs their own trailing 5-year mean. Anything sitting materially rich (toward and beyond the **+7.8%** pre-crisis average) is flagged for FX and local-currency-duration de-risking or hedging. The **+0.6%** baseline is the "no signal" reference.
- **Screen 2 — regime check.** Cross-reference flagged names against money growth. Where **M2 growth is accelerating**, the ~**1:1** slope says inflation (and FX depreciation) is coming — escalate the flag.
- **Tail catalogue.** Use the **107-episode / 42-country** hyperinflation population (**68 >1000%**) as the base-rate reminder that currency collapse is a recurring, cross-country phenomenon — not a once-a-century anomaly — and that it is invisible to any FRED-only process.
- **Duration linkage.** An overvalued REER plus accelerating M2 is a short-FX *and* short-local-duration signal; treat the two as a joint hedge.

Pair this overlay with the developed-market FX context in [[USD & G10 FX]], the broader breakdown of currency episodes in [[02 - Crisis Chronology (Banking, Currency, Sovereign)]], and the cross-sectional vulnerability screen in [[04 - Current Cross-Country Snapshot (Fragility & Twin Deficits)]]. For execution sizing, route flags through [[Risk Management]].

## What it means for positioning

A currency that is **>500%-inflation-bound** does not get there quietly — it telegraphs the move first through an **overvalued REER (+7.8% vs +0.6%)** and then validates it through **M2 growth running ~1:1 with inflation**. The PM edge is sequencing: the REER signal gives the *when* (overvaluation a year out), money growth gives the *confirmation*, and the 42-country / 107-episode catalogue gives the *base rate* for how badly these resolve. Position to be short the currency and its local duration before the regime flips, and size the tail using the historical population rather than the (silent) FRED record.

The interactive view of these series lives in the [Global Macro Database Dashboard](Global%20Macro%20Database%20Dashboard.html).

*Sources & method:* Global Macro Database (Müller, Xu, Lehbib & Chen 2025; NBER WP 33714); REER, M2 and inflation series computed from raw GMD by `tools/build_gmd_analysis.py` and independently re-verified. Hyperinflation counts and the ~1:1 M2–inflation slope are from fact block **P9**; the +7.8% / +0.6% pre-crisis REER signature is from fact block **P11**.

*Educational; not investment advice.*
