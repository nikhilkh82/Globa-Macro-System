---
title: "Systematic Trading — Factors, Risk Premia & Risk Parity"
category: strategy-lab
type: deep-dive
data_asof: 2026-06
summary: "Maps Gliner Ch 6's construction stack onto the lab's 20 systems: risk-premia harvesters (risk parity 0.69, HF replication, CTA, FX carry) survived, every macro-timer is NULL; its Sharpes predate the 2026-09-08 refresh."
tags: ["systematic", "factors", "risk-premia", "risk-parity", "gliner"]
updated: 2026-08-13
data_vintage: "17 tested systems, verdicts as of the latest scorecard run"
sources: 3
---

# Systematic Trading — Factors, Risk Premia & Risk Parity

Gliner Ch 6 gives the construction framework for a systematic macro model. This page maps that framework onto the **20 strategy systems** in this folder and states what the evidence says about each layer.

## The book's construction stack

1. **Assets / product groups** — define the tradeable universe first.
2. **Strategies** — the expression logic (trend, carry, value, mean-reversion).
3. **Factors** — the systematic drivers returns load on.
4. **Risk factors** — the exposures you are *paid* to bear versus those you carry by accident.
5. **Risk premia** — the compensated, persistent return sources.
6. **Risk parity** — allocate by risk contribution rather than capital.

The discipline the book insists on: separate the **premium** (compensated, persistent) from the **timing bet** (uncompensated, regime-dependent). Most systematic failures are timing bets misdescribed as premia.

## What this platform's evidence says

The Strategy Scorecard's headline verdict is exactly that separation, and it is blunt:

> **risk premia ✓ · macro-timing ✗**

Sorted by the book's taxonomy:

| Layer | Systems here | Verdict |
|---|---|---|
| **Risk premia** (compensated) | Macro-Aware Risk Parity (0.69) · Hedge-Fund Replication (0.65) · Managed Futures / CTA trend (0.55) · FX Signals carry (0.40) · FX Carry-Valuation (0.31) | **POSITIVE** — the premia harvesters are the systems that survived |
| **Macro timing** (uncompensated) | Macro Regime Allocation (0.69, NULL) · Macro Sector Rotation (0.01) · Information State Changes (−0.09) · Surprises→Commodities (−0.29) · ML Macro-Direction | **NULL** — predicting the macro turn did not pay |
| **Single-asset trend** | Treasury Macro-Trend (0.50, MARGINAL) · Robust Equity Trend (0.32, NULL) · Sectoral Macro-Trend (0.43, CORRECTED) | mixed — trend works in aggregate (CTA), weakly per-sleeve |
| **Cross-sectional / ML** | Credit ML (0.57, NULL) · AI Hedge-Fund Committee (SUPPORT) | unproven standalone |

**The pattern is the book's thesis, confirmed on this platform's own data**: the systems that harvest a persistent, compensated exposure (carry, trend-as-a-premium, risk-balanced beta) survived testing; the systems that try to *time* the macro cycle did not — including one (Macro Regime Allocation) whose raw Sharpe of 0.69 matched the best survivor but failed robustness.

## Risk parity — the one allocation rule that held up

Macro-Aware Risk Parity is a POSITIVE at 0.69, the highest surviving figure in the lab. The book's argument for why is mechanical rather than predictive: equal *risk* contribution avoids the concentration that capital-weighting hides — a 60/40 book is ~90% equity risk. Nothing about it requires forecasting the macro environment, which is precisely why it survives when the forecasting systems do not.

See [[Macro-Aware Risk Parity System]] and, for the correlation logic that makes risk-weighting necessary, [[The Four Product Groups & Cross-Asset Relationships]] — where the measured matrix shows the equity/vol/dollar/copper cluster moving as close to one factor while the rates complex is near-orthogonal.

## Method note

Every verdict above comes from tests documented in [[Cross-System Synthesis — What Works]], with the same standing rules used throughout this platform: point-in-time inputs, no look-ahead, out-of-sample where the sample allows, and **negative results published rather than deleted**. Two systems carry a CORRECTED verdict — the audit changed the conclusion, and the change is on the record.

Related: [[Cross-System Synthesis — What Works]] · [[Macro-Aware Risk Parity System]] · [[Managed-Futures Trend System]] · [[Performance & Risk Metrics — Sharpe, Sortino, Drawdown, VaR]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
