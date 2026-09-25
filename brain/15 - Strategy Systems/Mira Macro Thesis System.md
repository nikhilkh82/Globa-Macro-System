---
title: Mira Macro Thesis System
category: strategy-lab
type: live-read
data_asof: 2026-09-19
summary: "Turns the live US regime into a Mira-compliant research package (14-claim evidence log, six live falsifiers). 2026-09-19: thesis INTACT, 0/6 triggered, but its 'Fed on hold' clause lags the 17 Sep hike to 3.75-4.00%."
tags: [global-macro, strategy, mira, thesis-system, evidence-log, falsifiable, research-protocol]
data_vintage: "LIVE (FRED) + Brain endo + prediction-market odds"
sources: 1
updated: 2026-09-19
---

# Mira Macro Thesis System

An **evidence-tracked, falsifiable, refreshable macro thesis** generator that operationalizes the [Mira](../../raw/11.%20Strategies/Mira-main/) research protocol on the Global Macro Brain's live data. It turns the current US macro regime into a Mira-compliant **research package** — a thesis with a claim-classified evidence log, expectation map, explicit falsifiers, and refresh boundaries — and auto-evaluates whether the thesis still holds. Built 2026-06-22.

> **Research support, not investment advice.** Mira is a research discipline, not a trade bot or signal — and this adaptation preserves that boundary: it issues no positions, targets, or trades.

## Provenance — what we adapted
[Mira](../../raw/11.%20Strategies/Mira-main/) is an *agent-native investment-research protocol*: it constrains model output into **source-backed claims, explicit uncertainty, refresh conditions and falsifiers**, kept separate from trading. Its headline artifact is a "research package" (memo + evidence log + expectation map + thesis ledger + decision log) with a validated CSV schema and Python validators. Unlike the prior drops it is **not a quant strategy** — there is no signal to backtest. The faithful adaptation is to *run the protocol*: generate a real, refreshable macro research package on the Brain's live data, following Mira's schemas exactly.

## How it works
- **Thesis:** the live US regime as a falsifiable claim — *late-cycle reflation* (firm growth + sticky/re-accelerating inflation), derived from the Brain's data (endo score, CPI/PCE, payrolls, curve, credit, vol). The engine's statement still carries the clause "Fed on hold", which is no longer true of the policy rate — the Fed **raised 25bp to a 3.75–4.00% target range effective 2026-09-17** — because the policy row reads *monthly* `FEDFUNDS` (Aug-2026 3.63%), which cannot see a mid-September move; see the 2026-09-19 snapshot.
- **Evidence log (`evidence-log.csv`, Mira schema):** 14 claims, each classified by Mira's taxonomy — `reported_metric` (official BLS/BEA/Fed prints via FRED, authority **L2**), `market_pricing` (Treasuries/credit/VIX/FX/commodities), and one `derived_calculation` (the PTM endo score, **L6**, upstream FRED series cited) — with `verification_status`, `freshness_status`, `treatment`, `readiness_impact` per row.
- **Expectation map (`expectation-map.csv`):** what the thesis predicts vs consensus and how it's priced, with next checks.
- **Falsifiers (`must_refresh_if`):** six explicit disconfirming conditions (CPI YoY < 2.5%; curve < −0.5pp; HY OAS > 5pp; payrolls 3m < 0; Fed cut > 25bps; VIX > 30), each **evaluated live** → a **thesis_state** (`intact` / `weakening` / `broken`).
- **Refresh boundary:** `stale_after` ≈ next CPI/FOMC cycle; the package is unsafe to reuse past it or once a falsifier triggers.
- **Decision separation:** an `actionability-bridge.md` keeps it research-bound (`research_action_only_not_trade_instruction`); no sizing without user holdings/mandate/risk budget.

## Outputs (`Mira Thesis/<case-id>/` + dashboard)
A full 9-artifact Mira package — `investment-memo.md` (hero), `evidence-log.csv`, `expectation-map.csv`, `thesis-ledger.md`, `decision-log.csv`, `actionability-bridge.md`, `research-package-manifest.json`, `routing.json`, `README.md` — plus **`Mira Macro Thesis Dashboard.html`** (light theme: thesis-state banner, KPIs, falsifier monitor, expectation map, evidence-log table, refresh boundary).
Tools: `tools/mira_thesis.py` (engine + self-validator) · `mira_report.py` (dashboard) · `build_mira.py` (one command). Reuses `tools/fred.py`; cross-links the [[Prediction-Market Macro System]] (Fed odds) and the PTM endo score.

## Validation — passes Mira's *own* validator
The generated package is checked two ways: (1) a built-in self-validator replicating Mira's evidence-log rules (PASS), and (2) **Mira's actual `scripts/validate_repo.py` run against the generated case → `0 errors, 0 warnings`.** Matching Mira's real schema (evidence-log columns/enums, manifest fields, routing fields, decision-log vocabulary, README refresh/disclaimer markers) is the strongest proof this is a faithful instantiation of the protocol, not a look-alike.

## Snapshot — 2026-09-19 (current; data as of 2026-09-19)
Supersedes the 2026-09-11 snapshot below. Source: `Mira Thesis/mira_latest.json` (as_of 2026-09-19, generated 2026-09-19 15:51) — the engine re-evaluated the same case, **`us-macro-regime-2026-09`**; prints cross-checked against the FRED snapshot verified 2026-09-19. The readings this replaces are listed in [[log]].

- **Thesis state: INTACT — 0 of 6 falsifiers triggered (0 major).** The statement itself, however, is now partly stale: it still reads "Fed on hold" while the Fed **raised 25bp to a 3.75–4.00% target range effective 2026-09-17** — the first hike of the cycle — with EFFR at **3.88%** (2026-09-17, from 3.63% through 16 Sep). The engine's policy row is *monthly* `FEDFUNDS` (Aug-2026 **3.63%**, 6m change **−0.01pp**), so the falsifier arithmetic is untouched but the thesis sentence needs re-cutting on the next run. The ECB moved the same week — deposit facility rate **2.25% → 2.50%**, effective 2026-09-16 — which the evidence log does not carry at all.
- **Inflation — still the nearest falsifier:** headline CPI **3.35% YoY** (Aug print; Jul 3.30%), leaving the 2.5% disinflation line **0.85pp** away. Core PCE **3.34% YoY** (Jul — no Aug print yet). Core CPI, which is *not* in Mira's evidence log, is **2.45% YoY** with a 3m-annualised rate of **1.97%**: it turned up from 1.64% in July but is still below both its own YoY rate and 2%, so the "core is cooler underneath" caveat stands, just weaker than a month ago. The loudest reflation print in the set is PPI all-commodities at **+9.85% YoY** (Aug, from +8.70% in Jul), alongside WTI's move to **$107.02** (Brent **$130.80**, 2026-09-15).
- **Growth / labour:** payrolls 3m-avg **+71.3k** (Aug; monthly 31k Jun → 21k Jul → 162k Aug), IndPro **+1.42% YoY** (Aug, up from +1.13% in Jul — the deceleration flagged on 2026-09-11 has reversed). Demand corroborates: retail sales **+1.24% m/m** (Aug) and initial claims **196k** (week of 12 Sep, 4-week average 203.25k), neither of them evidence-log rows. Falsifier (3m-avg < 0) not close.
- **Curve:** 10Y–3M **+0.87pp** (2026-09-18) — the same slope the last snapshot carried, still moving nowhere near the −0.5pp re-inversion falsifier. The flattening is in the belly: 10Y–2Y went **+0.33pp (15 Sep) → +0.25pp (18 Sep)**, a bear-flattening on 16 Sep (2Y +7bp to 4.74%, 10Y +1bp to 5.01%) and then a parallel 7bp rally in both legs on hike day (2s10s unchanged at +0.27pp); the last 2bp on 18 Sep cannot be attributed, as FRED has no 18 Sep yields yet. 10Y real (TIPS) **2.61%** (2026-09-17), up from 2.42% on 2026-09-03 (2.68% on 16 Sep).
- **Credit / vol:** HY OAS **2.70pp** (2026-09-17; threshold 5.0pp), VIX **15.44** (2026-09-17; threshold 30). The two legs moved on different days — credit retraced on 16 Sep (HY 2.76 → 2.70, CCC-and-lower 10.85 → 10.76), the day *before* the hike took effect, and was unchanged on hike day, while vol fell *on* hike day (17.71 on 16 Sep → 15.44 on 17 Sep).
- **Fed path pricing:** prediction markets now imply **0.045** odds of any 2026 cut (the evidence row rounds it to ~4%), down from 0.111. Note the asymmetry the protocol leaves open: the `Fed pivots to easing` falsifier fires only on a −25bp move, so the tightening that actually occurred cannot trigger it — a hike is thesis-*supporting* under this evidence log.
- **Other evidence rows:** M2 **+5.41% YoY** (Jul), WTI **$107.02** (2026-09-15, from $91.48 on 1 Sep), broad USD **−1.9%** over 6m (2026-09-11; H.10 publishes with a lag, so this is the freshest FX read), PTM endo score **+19 (Mildly Inflationary)**, up from +9 (Neutral / Balanced) — the scorecard's own swing came from Inflation (−12 → +4) against a weaker Leading Surveys (+2 → −4). 14 claims logged, all `verified` / `current`; built-in self-validator **PASS** (`validation: []`). Mira's external `validate_repo.py` result is still not recorded in the source for this case — the 0-errors run in *Validation* above refers to the June case.
- **Refresh boundary:** `stale_after` **2026-10-24** (was 2026-10-13); the six `must_refresh_if` conditions are unchanged.

## Snapshot — 2026-09-11 (data as of 2026-09-08)
Supersedes the 2026-06-22 snapshot below. Source: `Mira Thesis/mira_latest.json` (as_of 2026-09-08, generated 2026-09-08 09:11) — the engine rolled to a new case, **`us-macro-regime-2026-09`**; prints cross-checked against the FRED snapshot verified 2026-09-08.

- **Thesis state: INTACT — 0 of 6 falsifiers triggered (0 major).** Statement unchanged: late-cycle reflation — still-firm growth, sticky inflation, Fed on hold. Same verdict as June, but the evidence has shifted (below).
- **Inflation — now the nearest falsifier:** headline CPI **3.3% YoY** (Jul-2026 print) vs the 4.3% quoted in the June snapshot; the 2.5% disinflation line is 0.8pp away, not 1.8pp. Core PCE **3.34% YoY** (Jul). The FRED path shows headline CPI peaking at 4.17% (May) then 3.46% (Jun) → 3.3% (Jul); core CPI, which is *not* in Mira's evidence log, is 2.47% YoY with a 1.64% 3m-annualised rate — the number most likely to push the thesis to `weakening` first.
- **Growth / labor:** payrolls 3m-avg **+71.3k** (Aug; monthly prints 21k Jul → 162k Aug per FRED), IndPro **+1.08% YoY** (Jul, decelerating from 1.53% in May). Falsifier (3m-avg < 0) not close.
- **Curve:** 10Y–3M **+0.87pp** (2026-09-04), steeper than June's +0.6pp and moving away from the −0.5pp re-inversion falsifier; 10Y real (TIPS) yield **2.42%** (2026-09-03).
- **Credit / vol:** HY OAS **2.65pp** (2026-09-03; ~unchanged vs June's ~2.6pp; threshold 5.0pp). VIX **14.32** (2026-09-03; down from ~18 in June; threshold 30).
- **Fed:** effective funds **3.63%** (Aug), 6m change **−0.01pp** (on hold; falsifier is −0.25pp). Prediction markets price ~**11%** odds of any 2026 cut (`fed_cut_odds` 0.111).
- **Other evidence rows:** M2 **+5.41% YoY** (Jul), WTI **$91.48** (2026-09-01), broad USD **+0.1%** over 6m (2026-08-28), PTM endo score **+9 (Neutral / Balanced)**. 14 claims logged, all `verified` / `current`; built-in self-validator **PASS** (`validation: []`; manifest `evidence_log_selfvalidation: pass`). Mira's external `validate_repo.py` result is not recorded in the source for this case — the 0-errors run in *Validation* above refers to the June case.
- **Refresh boundary:** `stale_after` **2026-10-13**; the six `must_refresh_if` conditions are unchanged.

## Snapshot — 2026-06-22 (live)
Thesis **INTACT (supported)** — **0 of 6 falsifiers triggered**: CPI 4.3% (hot), payrolls firm, 10Y-3M dis-inverted (+0.6pp), HY OAS tight (~2.6pp), Fed on hold, VIX calm (~18). The late-cycle-reflation overlay holds; nearest watch items are the inflation path and any Fed pivot. (Matches the Brain's [[Macro Regime - Live (June 2026)]] and [[Business Cycle Dashboard - Live (June 2026)]].)

## Caveats
- A **macro overlay**, not a single-name or sized call; revised (not vintage) FRED data; refresh on the next CPI/PCE/FOMC release.
- The thesis statement is a *framing* of the live regime, evidence-tracked and falsifiable — not a forecast or recommendation.

## Related
[[Macro Regime - Live (June 2026)]] · [[Business Cycle Dashboard - Live (June 2026)]] · [[Prediction-Market Macro System]] · [[Endo-Exo Toolkit & Workflow]] · [[Analyst System — Live Cockpit (June 2026)]]
