---
title: Information State Changes System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: Monthly change in macro information (5 groups) → synthetic 5y Treasury duration, 1998–2026 — a null on the free-data proxy (IC −0.02, t −0.5); the premise needs point-in-time ALFRED vintages, so it is untested.
tags: [global-macro, strategy, fixed-income, information-changes, data-flow, null-result, vintage-limitation, backtest]
data_vintage: "LIVE (FRED DGS5 + macro, 1998→2026-08; engine re-run 2026-09-24 16:15)"
sources: 1
updated: 2026-09-24
---

# The Predictive Power of Information State Changes — Fixed Income

A free-data port of the Macrosynergy **"Macro information changes as systematic trading signals"** notebook. The signal is the monthly **change in macro information** — the flow of new data across growth, inflation, labour, financial and survey groups — predicting US Treasury duration returns. Built 2026-06-23.

> **A null on the free-data proxy — with a genuine data confound.** The information-state-change premise specifically requires point-in-time vintages, which free FRED data can't reproduce, so the null is partly an *inability to test the premise faithfully* rather than a clean rejection. Research/education only.

## Provenance — what we adapted
The notebook's thesis: it's the *change* in the information state (new releases + revisions, tracked with point-in-time **vintages** via JPMaQS) that moves fixed income — improving macro flow → duration sells off; deteriorating → duration rallies. We kept the construction (grouped, signed, normalized, smoothed information changes → a duration signal) on **free, revised** FRED data — which is the central limitation.

## How it works
- **Target:** synthetic 5y Treasury total return (FRED DGS5, carry − duration·Δy) — the duration leg (matching the notebook's 5y IRS target).
- **Information changes (5 groups, FRED, point-in-time z, winsorized ±3, 3m-smoothed, lagged 1m):** growth (Δ INDPRO + payrolls YoY), inflation (Δ CPI YoY), labour (Δ unemployment), financial (Δ Baa credit spread), surveys (Δ UMich). Each **signed for a long-duration position** (improving growth/inflation → short duration; rising unemployment / widening spread → long duration).
- **Composite** = mean of the group information-change z's (the long-duration signal). Walk-forward; HAC (Newey-West) t-stat.

## Outputs (`Info Changes/`)
- **`Info Changes Dashboard.html`** — light theme, Chart.js inlined: signal-vs-buy&hold-duration growth-of-100, a performance table, and a per-group IC bar.
- **`Info Changes Note <date>.md`** + **`infochanges_latest.json`**.
Tools: `tools/info_changes.py` · `info_changes_report.py` · `build_info_changes.py`.

## Result — 1998-06 → 2026-08 (n=339)
- **Core, packaging-independent evidence:** the composite information-change signal has ~zero predictive correlation with next-month duration — **IC −0.02 (HAC t −0.52), insignificant.**
- Its long/short PnL also earns nothing (Sharpe −0.09, CAGR −0.42%/yr, MaxDD −24.9%) vs buy-and-hold 5y duration (**Sharpe 0.69**, CAGR 2.99%/yr) — but that's *secondary*: a long/short signal forfeits the multi-decade duration bull whenever it goes short, so the IC is the cleaner test.

| Group (info-change → next-month duration) | IC | HAC t |
|---|---|---|
| Growth | −0.032 | −0.5 |
| Inflation | −0.078 | −1.3 |
| **Labour** | **+0.068** | **+1.2** |
| Financial | +0.015 | +0.4 |
| Surveys | −0.023 | −0.4 |

*Metrics re-verified 2026-09-24 against the re-run engine (`infochanges_latest.json`, generated 2026-09-24 16:15). **Every figure above and in the table is unchanged from the 2026-09-08 refresh** — the last complete month is still 2026-08, so the window (1998-06 → 2026-08, n=339), the composite IC (`ic` −0.02, `ic_t` −0.52) and all five group ICs re-ran identically; only the CAGR/MaxDD detail above was added from the payload. The June-2026 figures remain superseded, and the audit verdicts below are unchanged and still refer to the original adversarial review.*

Only **labour** (rising unemployment → long duration) is even directionally right, and it's still insignificant; the others are flat or weakly wrong-signed.

## Two honest, non-exclusive readings
1. **The free-data proxy can't test the premise fairly.** A true *information-state* change is the change in what was *known at the time* (point-in-time **vintages** — releases + revisions as they happened). Revised FRED data gives the change in *today's* data, not the real-time surprise; revisions smear out the very flow the signal needs. A faithful test needs vintages (FRED's **ALFRED**), so this null likely *understates* the notebook's signal.
2. **Or macro-information-flow simply may not time duration** at a monthly horizon — the null could be genuine. We can't distinguish (1) from (2) without the vintages, and asserting the notebook's edge *would* appear here would be over-claiming. Both readings are stated.

## Verdict
- **A null on the free-data proxy** (IC ~0, t −0.52), distinct from the other macro-timing nulls ([[Macro Sector Rotation System]], [[ML Macro-Direction Model]]) in that the premise *specifically* requires vintage data the free feed doesn't provide — a genuine confound, not an excuse, just an acknowledged inability to test faithfully.
- The honest takeaway: on this proxy, holding duration beat timing it; whether the notebook's vintage-based edge is real is **untested here** and would need ALFRED point-in-time data. The faint labour trace (weak economy → bonds rally) is the only economically-sensible signal that survives.

## Audit
Adversarially audited (2-lens). The **look-ahead / construction lens confirmed 0 issues** — no leak, no forward-smoothing, and **no sign/orientation bug masking a real signal** (the mixed-sign per-group ICs are noise, not a systematic flip); the result is mechanically sound. (The evaluation lens hit the session token limit mid-verification, so its framing flags weren't formally adjudicated — I proactively tightened the write-up to lead with the packaging-independent IC null and to present the vintage limitation as one of two non-exclusive readings rather than a definitive excuse.)

## Caveats
- **Revised (not point-in-time/vintage) data — the central limitation.** US-only (the notebook's local-global cross-country aggregation isn't reproduced); synthetic 5y TR excludes roll/convexity; vol-targeted; 1-month macro lag; 3m smoothing of information changes (per the notebook).

## Related
[[Treasury Macro-Trend System]] · [[Macro Curve-Trade Strategy]] · [[ML Macro-Direction Model]] · [[Macro Sector Rotation System]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
