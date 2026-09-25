---
title: "Monetary Policy Tools, Transmission & Communication"
category: central-banks
type: domain
data_asof: 2026-08-13
summary: "Mechanics behind the live central-bank page: mandates, five tools, impossible trinity, ZLB/QE, Taylor-rule parameter fragility (1.9pp spread), and the FOMC hawk-dove index at 80 (a stance descriptor, not a predictor)."
tags: ["central-banks", "monetary-policy", "qe", "taylor-rule", "fomc", "communication"]
updated: 2026-08-13
data_vintage: "concepts from Gliner Ch 11 · live index values to 2026-08"
sources: 4
---

# Monetary Policy Tools, Transmission & Communication

The mechanics behind [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]]. Structure follows Gliner Ch 11.

## Mandates — they are not the same

The book stresses that the objective function differs by institution, so identical data produces different reactions:

- **Federal Reserve** — dual mandate: maximum employment *and* price stability (plus moderate long-term rates).
- **ECB** — price stability is the *primary* objective; everything else is subordinate to it.
- **Bank of England** — price stability, and subject to that, support for the government's growth and employment objectives.
- **Swiss National Bank** — price stability with explicit attention to the exchange rate.

Practical consequence: a growth shock moves the Fed's reaction function more than the ECB's. The euro-area leg of any policy-divergence trade should be modelled as more inflation-reactive and less growth-reactive.

## The five tools

1. **Reserve ratio** — the fraction of deposits banks must hold. Blunt, rarely used in DM.
2. **Policy interest rate** — the primary lever. Live: [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]].
3. **Open market operations** — buying/selling securities to steer the rate to target; includes repo/reverse-repo and the discount window.
4. **Currency intervention** — *sterilized* (offsetting operations leave the monetary base unchanged) vs *unsterilized* (base changes, i.e. genuine easing/tightening). The distinction is the whole question of whether an intervention is credible.
5. **Quantitative easing** — asset purchases once the policy rate is at the floor.

## The impossible trinity

A country can have at most **two** of: free capital movement, a fixed exchange rate, an independent monetary policy. This is the structural lens for every currency-regime trade in Ch 7 — a peg under capital mobility means the central bank has surrendered its rate policy, and the peg is the thing that eventually breaks. See [[USD & G10 FX]].

## Zero lower bound, liquidity trap, QE

At the floor the rate tool is exhausted; policy shifts to the balance sheet and to expectations. This platform observes the *unwind* of that phase rather than the phase itself: the Fed balance sheet is **−24.7% off its April-2022 peak** (`US26:CBBS`). Money supply is tracked at [[M2 Money Supply & Liquidity]] (`US26:M2`, **$23,155bn** at 2026-06).

## The Taylor rule as a benchmark

> **i = r\* + π + 0.5(π − π\*) + 1.0(u\* − u)**

Computed live in the companion page. The honest caveat belongs here: **the rule's answer is dominated by two unobservable parameters**, r\* and u\*. On current data the plausible range spans **4.33%–6.23%** — a 1.9pp spread produced entirely by parameter choice, against an actual policy rate of 3.63%. Quote the rule as a *direction* (policy is easier than the benchmark) rather than a level, and never as a forecast.

## Reading communication — statements, minutes, hawks and doves

Gliner's framing: the statement is the deliberate signal, the minutes are the distribution of views behind it, and the hawk/dove axis is the compression of both into something tradeable.

This platform implements that compression as **`FED:HAWK`** — a lexicon-scored index over every FOMC statement, 0–100, currently **80 (July 2026)**, up from a stable 60 through H1.

Two disclosures the index carries by construction:

- It is a **desk reproduction** built from a documented hawk/dove lexicon — not the proprietary embedding index it parallels. Where the two disagree, this one is tuned against the statement text, not against the vendor's output.
- It is a **stance descriptor, not a predictor**. Correlation with *trailing* policy change is **+0.36**; with *forward* policy change only **+0.15**. Use it to characterise the current regime, not to anticipate the next move.

## Transmission — what actually moves

The chain the book describes (policy rate → money-market rates → the curve → credit → the real economy → FX) is only partly observable here:

| Link | Observable? | Series |
|---|---|---|
| Policy rate → front end | yes | `RATES:UST3M`, `RATES:UST2Y` |
| Front end → long end | yes | `LEI:T10Y2`, `LEI:T10FF`, `RATES:UST10Y` |
| Curve → credit | yes | `RATES:BBBSPRD`, `RATES:BAA10Y`, `GLOB:HYOAS` |
| Policy → bank funding stress | **no** | LIBOR-OIS / repo: no feed |
| Policy → inflation expectations | yes | `INFEXP:BE5` 2.21%, `INFEXP:BE10` 2.24% (2026-08-13) |
| Policy → FX | partial | `GLOB:DXYB`, `GLOB:EURUSD`, `GLOB:USDJPY` |

Note the expectations row: 5y and 10y breakevens at **2.21%/2.24%** sit close to target even while core PCE runs **+3.29%**. The market is pricing the overshoot as transitory — that gap between realised and expected inflation is the live tension in the current regime.

Related: [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]] · [[M2 Money Supply & Liquidity]] · [[Yield Curve & Recession Signals]] · [[Macro Signal Stack — Leading-Lagging Econometrics Framework (July 2026)]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
