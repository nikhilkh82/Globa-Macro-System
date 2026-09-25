---
title: PTM Global-Macro Dashboard (Endo + Exo)
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "PTM two-stage method live on FRED + CFTC COT: ENDO = 20 US drivers to a +/-200 state + growth x inflation quadrant (2026-09-19 +20.5, Mildly Inflationary, Reflation/Overheating); EXO = COT + carry + USD + relative endo."
tags: [global-macro, ptm, endogenous, exogenous, scorecard, fx, cot, dashboard, live, decision-support]
data_vintage: "LIVE (FRED + CFTC COT, through Sep-2026)"
sources: 1
updated: 2026-09-19
---

# PTM Global-Macro Dashboard — Endogenous + Exogenous

An automated dashboard implementing the **Anton Kreil PTM "Global Macros" two-stage method** over the `raw/2. Macro Indicators/2.8 Updated Detailed Macro Indicators` set. The first stage of the [[PFTM Global-Macro Execution Strategy]] (folder 37). Built 2026-06-24.

> **ENDO = single-country inflationary/deflationary bias; EXO = relative (carry + relative-endo + COT positioning) FX bias.** Decision-support, not a backtested strategy — and not investment advice.

## How it works
- **ENDO (US domestic):** 20 drivers (leading surveys ISM/NMI/UMich/permits; growth & activity retail/IP/durables/GDP/housing; inflation CPI/core/PPI/PCE; money & rates M2/Fed Funds; employment NFP/unemployment/claims; sovereign debt-GDP/10Y) scored to **±10** — distribution drivers by z-score vs ~1998+ history capped ±2σ ×5; ISM/NMI vs the 50 line — direction-signed so **+ = inflationary**. Summed by category → total on a **±200** scale → state; split into a **growth axis × inflation axis → business-cycle quadrant**.
- **EXO (relative/positioning):** CFTC COT net-spec positioning (z + percentile + flip), 3m-rate carry, trade-weighted USD trend, and cross-country relative-endo → per-pair FX bias (`0.45·carry + 0.35·rel-endo + 0.20·COT`, contrarian at positioning extremes); a risk-on/off read; and an **equity-index & commodity directional read** (indexes = risk-on/off; Gold/Silver = real-rate sign; WTI = growth cycle — each with a COT-positioning overlay). The fully executable version (technicals + ATR stops + sizing) is in [[PFTM Global-Macro Execution Strategy]].

## Current read (Sep-2026)
- **US ENDO ≈ +20.5/±200 → "Mildly Inflationary"; quadrant "Reflation / Overheating"** (engine build 2026-09-19 15:33; growth axis +0.77, inflation axis +1.40; inflation the dominant category at +12.9 — PCE +5.3 (headline PCE 3.70%, Jul), PPI +5.1 (Aug PPI +9.85% y/y), CPI +2.3 (3.35%, Aug), core CPI +0.2 (2.45%); restrictive rates a drag, Money & Rates −4.3 (Fed Funds −3.2, M2 −1.1); high sovereign debt, Govt Debt/GDP 122.59% scoring +7.0, netted by the 10Y's −4.4 to Sovereign +2.6; Employment +5.1 (unemployment 4.1% +3.8, claims 196k +2.3, payrolls −1.0); Growth & Activity +4.1 (durable goods +4.1); Leading Surveys +0.1, with U. Michigan sentiment scoring −9.1). Cross-check: the FRED-backed Excel endo template, recalculated 2026-09-19, reads +19 "Mildly Inflationary" (`scores_cache.json`; it was +9 "Neutral / Balanced" on 2026-09-09) — label and total now agree, though not the mix (template: Sovereign & BS +21, Inflation +4; engine: Inflation +12.9, Sovereign +2.6). ISM 54.0 / NMI 54.5 still supply +4.0 / +4.5 (= +8.5 of the +20.5) and are the fixed May-2026 web readings noted under Data approach, so the state still leans on stale survey inputs. The Fed Funds driver is monthly FEDFUNDS for Aug-2026 (3.63%), which predates the Fed's first hike of the cycle — +25bp to a 3.75–4.00% target range, effective 17 Sep (EFFR 3.88% that day) — so Money & Rates does not yet score the hike.
- **EXO:** risk **NEUTRAL** (flipped from RISK-ON; 0 net risk points — Baa–10Y spread 1.44, z −1.35, risk-on, cancelled by S&P COT z −0.57, risk-off; VIX COT z −0.43 neutral); FX leans by carry + relative-endo + positioning (e.g. EUR/USD short-EUR on negative carry: carry −1.79, score −39; USD/JPY LONG USD +61, USD/CAD LONG USD +29, AUD/USD LONG AUD +20, GBP/USD NEUTRAL 0). No FX COT lean is at an extreme; the only COT extreme is Gold crowded long (z +1.75, 99th pctile) — 10Y T-Note (z −1.33) and WTI (z −1.48, 8th pctile) are back inside the ±1.5 crowding threshold. Indexes (S&P 500, NASDAQ 100, Dow) read NEUTRAL on the neutral risk read; Gold/Silver LONG on the engine's 0.47% real rate (3m rate 3.82% − CPI 3.35%; LONG below 0.5%, so borderline — a short-rate measure, not the 10Y TIPS real yield of +2.61% on 17 Sep). Like the Fed Funds driver, that 3m rate is a monthly pre-hike reading (FRED IR3TIB01USM156N, Aug-2026); the 3-month Treasury rate was 4.12% on 17 Sep, so a post-hike front end lifts the real rate above the engine's 0.5% LONG threshold and would flip the Gold/Silver read to SHORT. Cross-country endo bars rank the major economies' debasement bias: Japan +40 (Strongly Inflationary) > US +17 > Eurozone +15 (Inflationary) > UK +13 > Australia +10 > Canada +9 (Mildly Inflationary) > Asia (JP/CN/KR/IN) −15 > China −58 (Deflationary).

*Superseded 2026-09-19: the 2026-09-08 build readings this read replaces (US ENDO +13.9, growth/inflation axes +0.33/+1.24, Inflation +11.6, Growth & Activity −0.7, Employment +4.9, Leading Surveys −0.2; the "+31" template cross-check; EXO RISK-ON on 2 points; indexes LONG; 10Y T-Note and WTI crowded short; FX pair scores and cross-country bars), which are listed in [[log]]. The 2026-09-11 flag on that read, unchanged:*

*Flag 2026-09-11: that template cross-check was made against the old +33 read; the 2026-09-08 total of +13.9 is under half of +31, so only the state label still agrees (magnitude not re-verified). ISM 54.0 / NMI 54.5 still supply +4.0 / +4.5 (= +8.5 of the +13.9) and are the fixed May-2026 web readings noted under Data approach, so the state leans on stale survey inputs.*

*Superseded 2026-09-11: US ENDO ≈ +33/±200 "Mildly Inflationary", quadrant "Reflation / Overheating"; EXO risk NEUTRAL (as of 2026-06-24).*

## Outputs (`PTM Macro/`)
- **`PTM Macro Dashboard.html`** — light theme, Chart.js inlined: endo gauge + category bar + business-cycle quadrant scatter + cross-country endo bars + COT-positioning bars + driver & FX-pair tables.
- **`PTM Macro Note <date>.md`** + **`ptmmacro_latest.json`**. Tools: `tools/ptm_macro.py` · `ptm_macro_report.py` · `build_ptm_macro.py`.

## Data approach
The **2.8 folder is the indicator spec + PTM scoring structure**; the data is pulled **live (FRED + CFTC COT)** so it is continuous and current to Sep-2026 — several folder files are course-era (the COT files run 2013–2017) or locked, so live data is both more faithful to "updated to 2026" and far more robust than parsing the heterogeneous workbooks. ISM/NMI are not on FRED → web-sourced May-2026 diffusion readings. The distribution scoring is a **continuous re-derivation** (z×5; level−50) of the endo template's stepped ZTAB/LVLTAB lookup, so engine scores won't equal the Excel scorecard cell-for-cell.

## Audit
**Audited (lean, 12 agents, 8/8 confirmed) → SOUND_WITH_FIXES; all fixes applied.** Confirmed: EXO pair sign-logic correct. Fixes applied: (ENDO-1, HIGH) the 10-Year yield was signed +1 while Fed Funds was −1 for the same nominal-rate-level move → **10Y re-signed −1** (a higher rate level = tighter conditions = disinflationary, consistent with Fed Funds); (L3-1, MED) corrected the COT-vintage framing ("end 2013" → **"2013–2017"**); (EXO-SIGN-1) removed a dead variable; (L3-3) resampled weekly jobless claims to monthly; documented the continuous-vs-stepped scoring divergence. Noted caveat: the growth-axis is boundary-marginal (one capped survey can nudge the quadrant).

## Caveats
- US-detailed (cross-country endo is a comparable cross-check, not the full per-country template); revised (not point-in-time vintage) FRED data; continuous re-derivation of the Excel scoring; decision-support only.

## Related
[[PFTM Global-Macro Execution Strategy]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]] · [[Cross-System Synthesis — What Works]]
