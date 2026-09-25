---
title: "The Four Product Groups & Cross-Asset Relationships"
category: framework
type: domain
data_asof: 2026-08
summary: "Gliner Ch 4 measured on platform data: USD is the cross-asset hinge (−0.46 equities, −0.50 copper), rates near-orthogonal to equities, and the CAD–WTI 'almost 80%' is +0.76 in levels, +0.36 in changes, −0.01 since 2015."
tags: ["framework", "cross-asset", "correlation", "risk-on-risk-off", "gliner"]
updated: 2026-08-13
data_vintage: "computed from the Explorer catalog, monthly, windows stated per pair"
sources: 10
---

# The Four Product Groups & Cross-Asset Relationships

Gliner Ch 4: every macro market reduces to **currencies, equities, fixed income, commodities**, and the edge is in knowing how they move *together*. This page states the book's claims and then **measures them on this platform's own data** — because several of the folklore correlations do not survive measurement.

## The four groups, as the book defines them

| Group | Book's representative set | Brain home |
|---|---|---|
| Currencies | USD, EUR, JPY, GBP, AUD, CAD, CHF, BRL, MXN, RUB | [[USD & G10 FX]] |
| Equities | S&P 500, Nasdaq, Euro Stoxx 50, Nikkei, Shanghai, Bovespa | [[Sector Analysis & Rotation]] |
| Fixed income | US, Germany, Italy, Japan, UK | [[Government Bond Yields]] |
| Commodities | Oil, gold, copper, corn | [[Commodities — Supply, Demand & the Cycle]] |

The book further splits currencies into **majors** (EUR/USD, GBP/USD, USD/JPY) and **commodity currencies** (AUD/USD, NZD/USD, USD/CAD, USD/BRL, USD/ZAR, USD/RUB, USD/CLP) — the second group being exporters whose currency is a levered play on their export complex.

## Measured cross-asset correlation

Monthly; prices as % change, rates/spreads as level differences; full common overlap (437–455 months for the long pairs — window stated where it is short):

|  | S&P 500 | VIX | USD | EUR/USD | USD/JPY | WTI | Copper | 10y yield |
|---|---|---|---|---|---|---|---|---|
| **S&P 500** | +1.00 | −0.53 | −0.46 | +0.17 | −0.00 | +0.14 | +0.29 | −0.05 |
| **VIX** | −0.53 | +1.00 | +0.43 | −0.22 | −0.13 | −0.15 | −0.24 | −0.06 |
| **USD (broad)** | −0.46 | +0.43 | +1.00 | −0.86 | +0.35 | −0.37 | −0.50 | +0.05 |
| **EUR/USD** | +0.17 | −0.22 | −0.86 | +1.00 | −0.31 | +0.15 | +0.33 | −0.16 |
| **WTI** | +0.14 | −0.15 | −0.37 | +0.15 | +0.03 | +1.00 | +0.25 | +0.24 |
| **Copper** | +0.29 | −0.24 | −0.50 | +0.33 | −0.06 | +0.25 | +1.00 | +0.18 |

Separately, **HY OAS change vs S&P 500: −0.74** — but on only **35 months** of overlap (the OAS series starts 2023-08), so it is quoted apart from the long-window figures rather than beside them.

## What survives measurement, and what does not

**Survives:**
- **Dollar as the cross-asset hinge.** USD is the most connected node in the matrix: −0.46 to equities, −0.50 to copper, −0.37 to WTI, +0.43 to VIX. The book's claim that the dollar sits on one side of most macro trades is borne out.
- **EUR/USD ≈ inverse dollar** at −0.86 — the euro is 57.6% of the DXY basket, so this is near-mechanical, and it means EUR/USD and DXY are *not* two independent positions.
- **Equity–vol inversion** at −0.53 over 437 months.
- **Credit as the equity twin** — HY OAS at −0.74 (short window).

**Does not survive:**
- **"Dr. Copper" as the growth bellwether.** Copper vs S&P 500 is **+0.29** — real, but far weaker than the reputation. Copper is a *supply-constrained industrial* as much as a growth signal, and the current data makes the point: copper at the 100th percentile of its history while iron ore is −7.8% on the year.
- **Risk-on/risk-off as a single factor.** If one factor drove everything, the off-diagonal magnitudes would be uniformly high. They are not: USD/JPY vs S&P 500 is **−0.00**, 2s10s vs equities **−0.08**, 10y yield vs equities **−0.05**. The rates complex is substantially *orthogonal* to the equity/vol/dollar cluster.

That last point is the operationally important one: it means **rates trades genuinely diversify an equity-risk book**, whereas stacking long-equity, short-dollar and long-copper is close to one position expressed three ways. This is exactly the correlation-cap logic enforced in [[Position Sizing, Unit Size & Volatility Adjustment]] — the trade engine flags correlated TAKEs sharing a theme (`risk`, `USD`, `real-rate`, `global-growth`) and sizes them as a single bet.

## Correlation is unstable — the book's warning, honoured

Gliner's Fig 4.5 makes the point that correlations break precisely when they matter (2008). This platform's own cointegration work reaches the same verdict from the other direction: **all four framework pairs FAIL cointegration on the full sample**, and EUR/USD vs the US–DE 10-year spread only recovers a relationship in a post-2003 subsample. See [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]].

Treat every number on this page as a **regime-conditional average**, not a constant.

## Testing the book's headline claim: CAD vs WTI

Gliner states *"Since 1996, the correlation of the Canadian dollar to WTI Crude Oil is almost 80 percent."* That is checkable. Using FRED `DEXCAUS` (inverted to USD-per-CAD, so it rises as CAD strengthens) and `DCOILWTICO`, monthly, **368 months from 1996-01 to 2026-08**:

| Form | Correlation |
|---|---|
| **Levels** (the form the book's number implies) | **+0.76** |
| **Monthly % changes** (the non-spurious form) | **+0.36** |

The book's figure reproduces — in levels. But two trending series will correlate in levels whether or not they are related, which is why every lead-lag test on this platform is run on differenced data. On changes, the real co-movement is **less than half** the advertised strength.

And it has decayed:

| Window | Levels r | Changes r |
|---|---|---|
| 1996–2007 | **+0.91** | +0.20 |
| 2008–2014 | +0.68 | **+0.60** |
| 2015–2026 | **−0.01** | +0.34 |

The levels relationship the claim rests on has **completely disappeared** in the past decade (−0.01), while the changes relationship persists at a moderate +0.34. Anyone trading CAD as an oil proxy on the strength of the 80% headline would be trading a relationship that stopped existing in the form quoted.

This is the single best illustration on this page of the book's own Ch 4 warning, and of why [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] tests stationarity before it tests relationships.

**Still untestable here:** the book's copper–Chilean-peso claim (~90%) — no CLP series on the platform, and no substitute is close enough to stand in for it honestly.

Related: [[USD & G10 FX]] · [[Commodities — Supply, Demand & the Cycle]] · [[Position Sizing, Unit Size & Volatility Adjustment]] · [[Econometrics Lab — Cointegration, Regimes & State-Space (July 2026)]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
