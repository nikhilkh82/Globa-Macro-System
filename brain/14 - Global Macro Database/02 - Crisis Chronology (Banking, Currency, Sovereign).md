---
title: Crisis Chronology (Banking, Currency, Sovereign)
category: gmd
type: deep-dive
data_asof: 2026-06
summary: "The Reinhart-Rogoff / Laeven-Valencia chronology: 362 banking + 547 currency + 278 sovereign crisis country-years; 1,117 distinct country-years 1800–2017; contagion years 1931/1992-94/2008."
tags: [global-macro, gmd, crisis-chronology, banking-crisis, contagion]
data_vintage: "GMD v2026_06 (current release; cross-country macro to 2024, IMF projections to 2030)"
sources: "Global Macro Database — Müller, Xu, Lehbib & Chen (2025), NBER WP 33714"
updated: 2026-07-03
---

# Crisis Chronology (Banking, Currency, Sovereign)

This is the hub page for GMD's financial-crisis dummies — the **BankingCrisis / CurrencyCrisis / SovDebtCrisis** flags in the Reinhart-Rogoff / Laeven-Valencia lineage — covering **1800–2017**. It is the single piece of the database that has no analogue in a FRED-based system: FRED has no crisis chronology at all. Use it to put any current stress episode in two-century context and to read contagion years off the historical tape.

## What this is

A per-year, per-country panel of three binary crisis flags. A given country-year can carry zero, one, two, or all three flags simultaneously. This page summarizes the totals, the worst contagion years, and the one distinction that trips up most readers: **sum-of-flags vs distinct country-years**.

## Headline totals (1800–2017)

| Crisis type | Country-years flagged |
|---|---|
| Banking | **362** |
| Currency | **547** |
| Sovereign-debt | **278** |
| **Sum of the three** | **1,187** |
| **Distinct country-years carrying ≥1 flag** | **1,117** |

The two bottom rows are different objects and must not be conflated.

- **362 + 547 + 278 = 1,187** is the *sum of flags*. It double- and triple-counts any year where a country was hit by more than one crisis type at once (a banking crisis that becomes a currency crisis that becomes a default — the classic twin/triple-crisis cascade).
- **1,117** is the count of *distinct country-years* that carry **at least one** flag. Because 1,117 < 1,187, we know that crisis types overlap in the same country-year roughly 70 times' worth of flags — i.e., compound crises are common, not rare. When you cite "how many crises," be explicit about which number you mean: the flag-sum (1,187) overstates the number of *episodes*; the distinct-count (1,117) is the cleaner measure of "how many country-years were in trouble."

## Worst years by sum-of-flags

Ranking years by the total number of crisis flags lit across all countries surfaces the contagion clusters:

| Year | Total flags | Note |
|---|---|---|
| **1994** | **35** | Worst single year on record (Tequila / EM FX wave) |
| **1992** | **33** | ERM crisis era |
| **2008** | **32** | **25 of which were banking** — the GFC signature |
| **1931** | **30** | Credit-Anstalt / interwar banking collapse |
| **1983** | **29** | LatAm debt-crisis aftermath |
| **1990** | **29** | |
| **1914** | **23** | WWI financial shutdown |

The **2008** row is the analytically important one: of its 32 total flags, **25 were banking crises** — the highest banking concentration in the table and the unmistakable fingerprint of a synchronized, advanced-economy-led banking event. Compare that to **1994** (35 flags but spread across banking + currency + sovereign in EM), which was a broader but shallower-per-type wave. High total ≠ high banking concentration.

## DM vs EM composition over time

Banking crises did not stay in one bloc. The chronology shows them **shifting between EM-dominated waves and advanced-economy episodes** — the two clearest advanced-economy clusters being **the 1930s** (interwar banking collapse, 1931) and **2008** (the GFC). Most other peak years (1992, 1994, 1983, 1990) are EM/FX-driven. The practical read: a banking-crisis signal is not inherently an "EM-only" risk — twice in this sample the epicenter was the developed core.

## How to use this for positioning

- **Read contagion years, not isolated flags.** The value of the chronology is the clustering. Years like 1994, 1992, 2008, 1931 show that crises arrive in correlated waves — when one flag lights in a vulnerable bloc, the base rate of others lighting nearby is elevated. This is the empirical backbone for cross-asset, cross-country correlation spikes in risk-off regimes (see [[Risk Management]]).
- **Banking concentration is the tell.** A year dominated by banking flags (2008: 25/32) signals a credit/solvency event with slow recovery; a year dominated by currency flags signals an FX/balance-of-payments event. The aftermath profiles differ — pair this page with the banking-crisis GDP event study in [[03 - Crisis Aftermath & Recovery Base Rates]] for the recovery scarring.
- **Always state your denominator.** When the desk asks "how many crises in year X," answer in distinct country-years (the 1,117 basis), and flag separately when a country is carrying a *compound* crisis — that overlap is where tail losses concentrate.
- For the current regime overlay, cross-reference [[Macro Regime - Live (June 2026)]] and the [Global Macro Database Dashboard](Global%20Macro%20Database%20Dashboard.html).

## Sibling pages

- [[00 - GMD Overview & Structural Edge]] — why the crisis chronology is one of GMD's four structural edges over FRED.
- [[01 - Where Today Sits vs History (US & G7 Percentiles)]] — debt levels that precede sovereign-default flags.
- [[03 - Crisis Aftermath & Recovery Base Rates]] — banking-crisis aftermath event study and debt-at-default distribution.

## Sources & method

Global Macro Database (Müller, Xu, Lehbib & Chen 2025; NBER WP 33714), BankingCrisis / CurrencyCrisis / SovDebtCrisis dummies, Reinhart-Rogoff / Laeven-Valencia lineage, 1800–2017. All counts computed from raw GMD by `tools/build_gmd_analysis.py` and independently re-verified (55/56 metrics exact-match, 0 mismatches). See [[index]] and [[log]] for vintage and ingest history.

*Educational; not investment advice.*
