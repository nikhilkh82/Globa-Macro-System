---
title: Cross-Country Endo & Divergence Backtest
category: pftm-system
type: strategy-system
data_asof: 2026-09-24
summary: "7-economy point-in-time endo scorecard (live FRED + PMIs, staleness-guarded) plus an FX-divergence backtest 2002-2026: Sharpe 0.37, IC +0.059, not significant alone, wired as a ±0.4 tilt; 2026-09-24 JP top, US negative."
tags: [global-macro, endo, cross-country, fx, divergence, backtest, interactive, staleness-guard, decision-support]
data_vintage: "live FRED (staleness-guarded) + 2026 Excel PMIs, rebuilt 2026-09-24 · backtest 2002-05→2026-02 monthly (284 months)"
sources: 1
updated: 2026-09-25
---

# Cross-Country Endo — US · UK · EZ · JP · AU · CA · CN — & the Divergence Backtest

The skill file's **multi-economy scorecard** finally built honestly, plus the thing the user asked for confidence
from: a **walk-forward backtest of the endo-divergence FX trade**. Built 2026-07-03 ("continue to build more
interactive charts with global macros, [7-country] endo, to take actual trades with backtesting results").

> **Decision-support / education only — NOT investment advice.**

## Engine (`tools/cc_endo.py` → `CC Endo/cc_endo_latest.json`)
- **7 economies**, each from the **audited per-country FRED id set** (endo_scores.py lineage: CPI [US=BLS CPIAUCSL;
  others OECD], unemployment, 3m rate, 10Y, M3; China: CPI/3m/discount/M3 — no free unemployment/10Y) **plus the 2026
  Excel PMIs** (Services PMI US/UK/EZ/JP/AU; official China PMI).
- **Balance of Payments driver (added 2026-07-03):** monthly trade balance per economy (US `BOPGSTB`; others
  `XTNTVA01*M667S`, current to **2026-05/06/07** on the 2026-09-24 rebuild (`last_obs`: US 2026-07; UK/JP/AU/CA/CN
  2026-06; the EZ/DE proxy 2026-05, the oldest leg on the board) — they were at 2026-03/04 when the driver was
  added; **EZ uses Germany as proxy** — the EZ aggregate ended 2022), scored as
  the balance's z vs its own history, direction +1 (**surplus/improving = structural currency demand**), axis
  "external". This is the PTM *exogenous* trade-flow leg — it moved the board with correct economics: the US trade
  deficit now weighs on USD (+2.6→+0.5), the UK deficit drags GBP (→−2.0), surplus economies gain (CA +2.4, CN +0.9).
  **Updated 2026-09-24 (supersedes the driver scores implied above):** the external leg has become the loudest driver
  on the board and has partly *inverted* the July story. It now reads **US −10.0** (the floor, `BOPGSTB` 2026-07),
  **CA +9.05**, **CN +6.83**, **EZ/DE +3.92**, **AU +1.31**, **JP −6.23**, **UK −8.47**. Japan flipping to a *negative*
  external score while still leading the board is the notable change: JP's +3.15 is now carried by its rates and
  unemployment drivers (3M rate +10.0, 10Y +6.07, unemployment +5.84) *against* its trade drag, not by the
  surplus-vs-deficit logic that made it the top pick in July. Canada is the one economy where the original
  surplus story still does the work.
  The dashboard has a **Balance-of-Payments panel** (per-economy balance, surplus/deficit state, pattern, score bar).
- **Point-in-time**: every driver scored as an expanding z (month i vs history through i, ±2σ×5 → ±10); country endo =
  mean of live drivers (60% level + 40% 6-month trend for the current read; patterns labeled).
- **Staleness guard (sign-critical):** any series >9 months old is flagged and **scored 0** — stale foreign CPI (the
  folder-37 lesson) can never set a trade. On the 2026-09-24 rebuild it is still 2–3 stale series per country
  (`n_stale`: US 2, UK 2, EZ 2, JP 2, CA 2, AU 3, CN 3), all visibly flagged and all scoring 0. The recurring
  casualties are **OECD M3** (last obs 2023-10/11 for every economy, 2018-12 for China) and one CPI or unemployment
  series per country: **UK CPI 2025-03, AU CPI 2025-03, CA CPI 2025-03, CN CPI 2025-04, JP CPI 2021-06, EZ
  unemployment 2023-01, US unemployment 2025-09**. Two consequences worth naming: **Japan's endo contains no
  inflation signal at all** (its CPI series died in 2021 and M3 in 2023), and **Australia has no Services PMI
  coverage after 2014-10** — the AU sheet of `34. Global Services PMI.xlsx` holds 49 observations, 2010-10 → 2014-10
  (last value 43.6), so that driver has been guard-zeroed for years and AU runs on four live drivers (`n_live` 4).
  That is a source-coverage gap, not a 2026 deterioration. US CPI is the exception — `CPIAUCSL` is
  live at **+3.35% YoY (2026-08)**, scoring +2.88.
- **Current read — 2026-09-24** (`cc_endo_latest.json`, `generated` 2026-09-24 16:09, `as_of` 2026-09-24;
  **supersedes the 2026-07-03 read below**, which is kept as the record): **Japan +3.15 (strongest) · CA +3.06 ·
  CN +1.22 · AU +1.12 · EZ +0.79 · US −0.68 · UK −1.02 (weakest)** → top divergence **JP over UK (Δ4.17)**,
  then CA over UK (Δ4.08), JP over US (Δ3.83), CA over US (Δ3.74). The pair at the top is the same, but the
  **board has compressed and the US has crossed to negative**: US +0.5 → **−0.68** (its trade-balance driver now
  scores the −10 floor) and JP +4.0 → +3.15, so the headline spread narrows 6.1 → 4.17. Canada has closed almost
  all of the gap to Japan (+2.4 → +3.06) and is now effectively co-leader. Note this engine's US endo is **not**
  the Excel endo template's US score (+19, "Mildly Inflationary", `scores_cache.json` 2026-09-24): different
  driver sets, different scaling — see [[PTM Endo Scorecard (2026 Excel Data)]].
- **Current read (2026-07-03, BoP-inclusive): Japan +4.0 (strongest) · CA +2.4 · CN +0.9 · US +0.5 · AU +0.2 ·
  EZ +0.1 · UK −2.0 (weakest)** → top divergence **JP over UK (Δ6.1)** — the classic surplus-vs-deficit pair.
- **FRED gotcha (cost an hour):** the OECD series need **2-letter** country codes (`IR3TIB01USM156N`) — the 3-letter
  variants 400. US CPI must be `CPIAUCSL` (the OECD US series lags ~12mo).

## Interactive dashboard (`CC Endo/CC Endo Dashboard.html`)
Country-picker **endo-history overlay** (7 point-in-time monthly lines, toggle chips, hover crosshair), current-endo
bar, the **FX divergence matrix** (strongest-over-weakest, the skill's rule), per-country driver cards with pattern +
staleness flags, and the **backtest panel** (equity curves vs carry + the stats table + the honest verdict).
Light page / dark wells / ← Main Dashboard. On the Main Dashboard as "Cross-Country Endo (7 economies)".
Re-exported from the payloads above, so the panels show the **2026-09-24** read and the re-run backtest — the
dashboard's own header reads *as of 2026-09-24*, though the file on disk was last written 2026-09-25, re-rendering
that same payload.

## The backtest (`tools/cc_backtest.py` → `cc_backtest_latest.json`) — the honest result
EUR/GBP/JPY/AUD/CAD vs USD, **2002-05→2026-02 (284 months)**, walk-forward: signal = relative endo (foreign − US) from
the PIT histories, **lagged 1 month**; FX excess return = spot + 3m-carry; dollar-neutral cross-sectional weights.
| Signal | Ann. ret | Sharpe | NW-t | Max DD | x-sec IC | IC t (NW) | Halves |
|---|---|---|---|---|---|---|---|
| **Endo divergence (incl. BoP)** | +1.5% | 0.37 | 1.78 | −12.0% | +0.059 | 1.81 | 0.44 / 0.29 |
| Carry (benchmark) | +2.0% | 0.48 | 2.28 | −17.7% | +0.113 | 3.62 | — |
*(post-audit, BoP-inclusive numbers — the signal re-tested after every driver change so tested = deployed. Adding
BoP slightly softened the IC but made the halves more consistent; the verdict is unchanged, reported as-is.)*

*Re-run **2026-09-24** (`cc_backtest_latest.json`, `generated` 2026-09-24 16:09) — supersedes the 2026-07-03 run.
The **window is identical** (`span` 2002-05..2026-02, `n_months` 284). That end date is not a hard-coded cap — the
axis is `set.intersection` over the five FX excess-return series, so the shortest of them still stops at 2026-02 and
the ragged edge has not advanced. What moved is therefore the re-scored endo history, not new months. **Sharpe 0.35 → 0.37, NW-t 1.67 → 1.78, second half 0.25 → 0.29**; the IC is
unchanged at **+0.059** and its NW t-stat is flat at **1.82 → 1.81**. The carry benchmark is unchanged to every
decimal (0.48 / 2.28 / +0.113 / 3.62). The signal got marginally better-behaved and **no threshold was crossed** —
the auto-verdict is still NOT SIGNIFICANT.*
- **Verdict (auto-set by thresholds, not narrative): NOT SIGNIFICANT as a standalone timer** — suggestive (positive
  both halves, IC t ≈ 2) but below the both-t≥2 bar. **Use as a bias/tilt layered with carry & COT** — which is
  exactly how it's wired into the trade engine.
- **Harness validation:** the same machinery reproduces the Brain's known carry result (folders 26/34: IC ~0.08–0.11,
  t ~3) — so the null-ish divergence number is credible, not a broken harness.
- Honesty (the payload's own `honesty` field, re-read 2026-09-24): revised (**not** point-in-time-vintage) FRED data;
  a 5-currency panel, i.e. a small cross-section; the signal lagged 1 month for publication — adequate for
  CPI/rates/PMI, but OECD M3, harmonized unemployment and the trade balance publish ~1–2 months after the reference
  month, so those drivers may carry up to ~1 month of residual look-ahead historically and are simply *absent* from
  the newest month on the live ragged edge; quarterly series re-keyed to quarter-end; excess returns = spot +
  3m-carry. **Both the IC and the portfolio t-stats are Newey-West(6)** — the earlier "iid IC-t" note on this page
  was stale, superseded by audit fix STATS-3 below.

## Trade-engine integration (`macro_cot_trades.py` — audited)
Per FX pair, **div = endo(foreign) − endo(US)**; |div| ≥ 1.0: sets the foreign-currency direction when COT is silent
(conv ≥0.8), **+0.4 conviction when it agrees** with positioning, **−0.4 when it opposes**. The existing audited
pair-inversion maps currency→pair. FX finally has a *fundamental* leg (it was COT-led only), sized as a tilt in
line with the backtest evidence.

**What the 2026-09-24 board implies for the USD pairs.** Taking `endo(foreign) − endo(US)` off the current read
(US −0.68) for the five traded currencies: **JPY +3.83, CAD +3.74, AUD +1.80, EUR +1.47** all clear the
|div| ≥ 1.0 gate, but **GBP is now −0.34 and drops below it** — in July, UK −2.0 against US +0.5 gave a −2.5
divergence that was comfortably trade-setting. The change is driven as much by the **US falling to −0.68** as by
anything in the UK. So four of the five pairs now tilt the *same* way (foreign over USD) and the fifth goes silent:
the cross-sectional information in the FX leg is thinner than the headline JP-over-UK spread suggests. (CN is
scored +1.22 but CNY is not in the traded panel.) Caveat on these figures: they are computed off the current
level+trend `endo` values shown above, whereas the deployed tilt reads the latest common month of the
point-in-time `hist` series (audit fix STATS-2/L2-3) — treat them as indicative of the board, not as the engine's
exact inputs.

## Audit (up front, lean — 12 agents, 3 lenses → refuter → synthesis) → fixes applied & re-run
**Signs verified correct end-to-end** (USD/JPY & USD/CAD invert exactly once in both tilt and backtest), but the
audit caught a **genuine look-ahead and two honesty gaps — all fixed before publication:**
- **L2-1 (MED, look-ahead):** FRED keys quarterly series to the quarter-START month, so AU CPI entered the backtest
  2–3 months before the ABS published it. **Fixed:** quarterly series auto-detected and re-keyed to quarter-end.
- **STATS-2/L2-3 (MED, tested≠deployed):** the live FX tilt was computed from the *level+trend current endo* — a
  variant the backtest never tested. **Fixed:** the tilt now reads the latest common month of the SAME point-in-time
  `hist` series the backtest validated.
- **STATS-1 (MED):** the auto-verdict couldn't distinguish "null" from "significantly wrong-signed". **Fixed:**
  three-way verdict (POSITIVE / NEGATIVE-do-not-use / NOT SIGNIFICANT).
- **STATS-3/4 (LOW):** IC t-stat now Newey-West(6) like the portfolio t (the iid IC-t 2.03 was overstated);
  annualization now geometric; M3/unemployment publication-lag caveat added to the honesty note.
The pipeline was re-run after the fixes; the numbers on the dashboard are the corrected ones.

## Related
[[Global Macro Trading Dashboard]] · [[Macro + COT Trade Signals]] · [[Global Macro Hedge Fund Strategy (Memo)]] · [[PTM Endo Scorecard (2026 Excel Data)]] · [[2026 Trading System — Operating Manual]] · [[the-dv01-both-legs-flattener-bug]]
