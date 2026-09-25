---
title: "Position Sizing, Unit Size & Volatility Adjustment"
category: portfolio-risk
type: live-read
data_asof: 2026-09-19
summary: "Gliner Ch 2's sizing rules mapped to the live engine: conviction→risk% (HIGH 1.0/MED 0.6/LOW 0.3), stop 2×ATR, target 2R, leverage caps FX 30×/Index 20×/Cmdty 10×; 2026-09-19 book: 3 TAKE, all HIGH, gross risk 3.0%."
tags: ["risk", "position-sizing", "atr", "volatility", "correlation", "gliner"]
updated: 2026-09-19
data_vintage: "engine parameters live (tools/macro_cot_trades.py) · book from macrocot_latest.json 2026-09-19 run (CFTC positions as of 2026-09-15) · rules from Gliner Ch 2"
sources: 3
---

# Position Sizing, Unit Size & Volatility Adjustment

Gliner Ch 2 argues that sizing — not idea generation — is what separates surviving macro books from dead ones. This page states the book's rules and then documents **exactly how this platform implements them**, with the live parameters.

## The book's rules

1. **Unit size** — define a standard trade unit first, then express every position as a multiple of it. Without a unit, "conviction" silently becomes "whatever felt right that morning."
2. **Volatility-adjust the size** — a position in a 30%-vol asset and one in a 6%-vol asset are not the same trade at the same notional. Size to *risk*, not to notional.
3. **Risk/reward before entry** — know the target and the stop before the ticket, or the trade has no defined loss.
4. **Correlation** — correlated positions are one position. Aggregate exposure by theme, not by ticker.
5. **Gap risk** — stops do not protect against a gap. Assets that gap (EM, pegged FX, single commodities on weather/OPEC headlines) need smaller units than their measured volatility suggests.
6. **Take losses** — the discipline that makes all of the above real.

## How this platform implements them

From the live trade engine (`tools/macro_cot_trades.py`, values as configured now):

| Rule | Implementation |
|---|---|
| Unit size | Risk-based: **conviction → % of account risked**. HIGH **1.0%**, MEDIUM **0.6%**, LOW **0.3%** of a $100,000 illustrative account. |
| Volatility adjustment | Stop distance = **2 × ATR** (daily). Size = risk$ ÷ stop distance, so **higher-vol assets automatically get smaller notional**. This is the book's rule 2, mechanised. |
| Risk/reward | Target = **2R** (twice the stop distance). Every TAKE carries entry / stop / target / R:R before it is published. |
| Correlation | TAKEs are tagged by theme (`risk`, `USD`, `real-rate`, `global-growth`, `natgas`) and **clusters of >1 TAKE sharing a theme are flagged on the dashboard** as one correlated bet. |
| Leverage caps | FX **30×**, Index **20×**, Commodity **10×** — applied when converting risk-sized notional to margin. |
| Gap risk | Partially handled: natural gas is given **its own theme** rather than being pooled into energy, precisely because it is weather/storage-driven and idiosyncratic. |

Current book state (2026-09-19 engine run, `Macro COT Trades/macrocot_latest.json`, CFTC positions as of 2026-09-15 — supersedes the 2026-09-16 run's 3 TAKE / $4,753 margin / $2,600 gross risk (2.6%) as this page carried them (the final 2026-09-16 engine note gives $4,771 margin), which in turn superseded the 2026-08-12 run's 6 TAKE / $10,257 margin / $4,400 gross risk; this page previously carried $10,274 for that run, a transposition of the engine note's $10,257): **3 TAKE** (2 long / 1 short), 10 WATCH, 2 STAND-ASIDE; **gross margin $4,823 (4.8% of account)**; **gross risk $3,000 (3.0%)**.

What moved since 2026-09-16 is one conviction, not the regime or the line-up: the **USD/JPY short was promoted MEDIUM → HIGH** ($600 → $1,000 of risk) on a stronger positioning trend in the new CFTC report — net +22% of OI (z +1.27, 84th percentile, 13-week change +51.0) against +2% (z +0.56, 68th) on the 2026-09-16 run — with the endo divergence still confirming at +7.5 (unchanged from the 2026-09-16 engine note). WTI Crude and the Dow Jones long are unchanged (HIGH, $1,000 each). The regime inputs are unchanged too (Reflation / Overheating, growth +0.56, inflation +0.89, real rates not falling) because the engine's ENDO input (`Endo Excel/endoexcel_latest.json`) scores the 2026 Excel workbooks, which have not been updated past the hike. The run read the 2026-09-16 build, and the 2026-09-19 15:47 rebuild carries identical figures, with its Fed funds driver still at 3.63%. So the regime side of this run does not yet reflect the Fed's first hike of the cycle (25bp to 3.75–4.00%, effective 2026-09-17).

Between 2026-08-12 and 2026-09-16, five of the six 2026-08-12 TAKEs came off the book, and **two different mechanisms** did it — the regime flip explains only part of the halving:

- **Regime.** Reflation / Overheating (growth +0.56, inflation +0.89, real rates *not* falling) on 2026-09-16, against Stagflation (growth −0.13, inflation +2.01, real rates falling) on 2026-08-12. Real rates no longer falling retired **Silver and Gold** outright — both are now STAND-ASIDE, because the precious-metals bias scores `0.5×inflation + (1.2 if real rates falling else −0.3)` — and the softer reflation demand score (+1.13 → +0.87) dropped **Natural Gas** just under the MEDIUM conviction cut-off, to LOW-conviction WATCH.
- **Positioning, not regime.** **USD/CAD** and **GBP/USD** fell to LOW WATCH on COT alone: the crowded 3rd-percentile CAD short normalised to the 34th (51st on 2026-09-19), and sterling's positioning trend inflected (net −18% of OI on 2026-09-16 but building long) with the endo divergence now *opposing* the positioning direction.

What survived: **WTI Crude carried over unchanged** — same HIGH conviction and the same $1,000 of risk as on 2026-08-12, so no risk was moved *into* it. The genuinely new risk is a **Dow Jones long** (HIGH, $1,000; STAND-ASIDE on 2026-08-12, promoted once the growth axis crossed the +0.4 equity threshold) and a **short USD/JPY** (MEDIUM, $600 on 2026-09-16, HIGH from 2026-09-19 as above; LOW-conviction WATCH on 2026-08-12, promoted on a confirmed positioning trend plus a confirming endo divergence of +1.2 as this page carried it (the 2026-09-16 engine outputs give +7.5)).

That 3.0% aggregate risk against 3 positions is the arithmetic of the table above working — three HIGH convictions at 1.0% each (WTI Crude, Dow Jones, USD/JPY short) = $3,000 (on 2026-09-16: two HIGH plus one MEDIUM at 0.6% = $2,600), and no single position can risk more than 1%. The correlation flag is what stops several 1% bets from being one large bet; on this run it is **silent**, because the three TAKEs sit in three different themes (`global-growth`, `risk`, `USD`). On 2026-08-12 it fired twice — Silver + Gold on `real-rate`, USD/CAD + GBP/USD on `USD`.

## The sizing formula, explicitly

```
risk$        = account × risk%(conviction)          e.g. $100,000 × 0.6% = $600
stop_distance = 2 × ATR(daily)                       in price terms
stop_frac    = |entry − stop| ÷ entry                as a fraction
size_notional = risk$ ÷ stop_frac
margin       = size_notional ÷ leverage(asset_class)
```

The property worth noting: **notional is an output, never an input**. The trader chooses conviction; volatility chooses the size.

## Where the book goes further than this platform

- **Position-sizing sheet / portfolio-level VaR budget** — the book runs sizing against a portfolio VaR and risk-utilisation budget. This platform sizes per-trade and *reports* gross risk, but does not optimise against a VaR limit. See [[Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR]].
- **Stress-testing** — no scenario-shock engine here.
- **Thematic trade construction** — the book treats a theme as a deliberately-constructed multi-leg expression; this platform only *detects* thematic overlap after the fact and warns.

Related: [[Risk Management]] · [[Portfolio Management]] · [[Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR]] · [[Average True Range (ATR)]] · [[The Four Product Groups & Cross-Asset Relationships]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
