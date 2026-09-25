---
title: "Central Banks — Policy Rates, Balance Sheets & the Global Stance"
category: central-banks
type: live-read
data_asof: 2026-09-24
summary: "Live global policy state: funds holding 3.88% (DFF 09-22) in the new 3.75-4.00% range, ECB 2.50% (09-24), BoE 3.73 / RBA 4.35; the strip re-priced UP again - peak 4.84% Nov-2027, ~96bp more; Fed B/S -24.7% off peak."
tags: ["central-banks", "monetary-policy", "rates", "fed", "ecb", "boe", "rba"]
updated: 2026-09-25
data_vintage: "EFFR/DFF to 2026-09-22 (range 3.75-4.00% since 2026-09-17) · ECB to 2026-09-24 · RBA to 2026-08 · BoE to 2026-06 (feed's latest) · world rate to 2026-08 · Fed B/S 2026-09-16 · implied path to 2028-02 (ZQ strip re-read from Explorer build vhash eb2c482311b9, asof 2026-09-24) · breakevens 2026-09-23 FRED/deck, 2026-09-24 Explorer · FOMC hawk-dove to 2026-09"
sources: 6
---

# Central Banks — Policy Rates, Balance Sheets & the Global Stance

Gliner devotes his longest institutional chapter (Ch 11) to central banks, on the argument that they are the single largest exogenous force on all four product groups. This page is the **live state**; the mechanics are in [[Monetary Policy Tools, Transmission & Communication]].

## Where policy sits right now

*Re-verified 2026-09-24; supersedes the 2026-09-19 readings, which are listed in [[log]] and kept inline below as supersession notes. No policy rate moved this week: the hike of 2026-09-17 has been carried at 3.88% every day through 2026-09-22, and what changed is the market's path around it.*

| Central bank | Policy rate | As of | Series |
|---|---|---|---|
| Federal Reserve (EFFR / DFF) | **3.88%** (target range **3.75–4.00%**) | 2026-09-22 | FRED `DFF` (`macro_pack.json` `DFF.latest`); range `DFEDTARL` / `DFEDTARU` |
| ECB (deposit facility) | **2.50%** | 2026-09-24 | `GLOB:ECB` (FRED `ECBDFR`) |
| Bank of England (Bank Rate) | **3.73%** | 2026-06 | `UK:IR` |
| RBA (cash rate) | **4.35%** | 2026-08 | `AU:RBA` |
| **World, GDP-weighted** | **4.62%** | 2026-08 | `WORLD:WRATE` |

**Both major central banks tightened in the week the energy shock peaked, and both have since held.** The FOMC raised the target range 25bp to **3.75–4.00%**, effective 2026-09-17 (FRED `DFEDTARL` 3.50→3.75, `DFEDTARU` 3.75→4.00) — the **first hike of the cycle**; daily funds (`DFF`) has printed **3.88%** every day from 2026-09-18 through **2026-09-22**, against 3.63% through 2026-09-16. The monthly `FEDFUNDS` average is still **3.63%** (August 2026) and will not show the move until the September print — several desk outputs still anchor to that monthly series and therefore still read "3.63%, on hold" (see the dashboard note in [[Business Cycle Dashboard - Live (June 2026)]]). The ECB's deposit facility rate is **2.50%**, raised from 2.25% effective 2026-09-16 and unchanged through **2026-09-24** — the newest observation of `GLOB:ECB` in the Explorer catalogue re-read this session, which prints 2.25% through 2026-09-13 and 2.50% at 2026-09-20 and 2026-09-24 (this supersedes the 2026-09-23 as-of first recorded in this refresh; the level is unchanged).

**The energy trigger has since faded, and that is the week's real news for policy.** Both moves came as WTI rose through $105 and Brent through $130 ($107.02 / $130.80 on 2026-09-15). Crude has given most of that back: **WTI $96.41** and **Brent $114.89** on **2026-09-22** (`macro_pack.json` `DCOILWTICO` / `DCOILBRENTEU`), −$10.61 and −$15.91 from the 15 Sep prints, with the daily WTI path 103.62 (09-16) → 103.21 (09-17) → 101.44 (09-18) → 96.97 (09-21) → 96.41 (09-22). *(Supersedes the "$107.02 / $130.80" read carried here on 2026-09-19 as the live level; those remain the correct 15 Sep prints.)* The rest of the case for the hike is intact: August PPI **+9.85% y/y**, retail sales **+6.01% y/y**, payrolls **+162k**, initial claims **196k** (week of 2026-09-12) — all four from `macro_pack.json` (`PPIACO`, `RSAFS`, `PAYEMS`, `ICSA`). *(Source corrected within this refresh: the **+1.24% m/m** retail-sales companion this sentence used to carry is **not** in the pack — `RSAFS` holds a level, `latest_date` 2026-08-01, and a calendar-keyed `yoy_pct` 6.01 only, with no m/m field — it comes from the rebuilt `Monthly Report/Business Cycle Dashboard.html` (asof 2026-09-24), whose Coincident row "Retail Sales (total)" prints "+1.24% MoM / +6.01% YoY".)* Markets have absorbed the move and then some — **VIX 14.21** and **HY OAS 2.68** (both 2026-09-22, superseding 15.44 / 2.70 on 2026-09-17), IG **0.77**, CCC **10.75**: risk pricing is *easier* a week after the hike than the day before it. The one gauge that did not join is Chicago Fed **NFCI −0.555** (2026-09-18), a hair tighter than −0.557 on 2026-09-11 and still deeply loose — flat, not easing.

**The BoE leg still could not be re-verified to a fresher month**: its feed was rebuilt again today (2026-09-24) and its newest observation is *still* **2026-06**, so 3.73% stands as the latest available, not a September read — it is now a full quarter stale and is listed as unresolved. The RBA feed still runs to **2026-08** at **4.35%** (unchanged since the 2026-09-19 re-verification). Neither foreign rate is re-sourced beyond these feeds in this refresh.

The GDP-weighted world policy rate is a desk calculation (BIS policy rates × World Bank GDP weights, US and euro-area legs spliced live past the BIS publication lag — BIS's own last print is **2025-06**, so the recent tail carries the other 15 members forward and is approximate; hyperinflation members excluded above 60%). At **4.62%** it has been grinding *up* — 4.58% through February–May, 4.60% in June, **4.62% in July and August**. **Global policy is not easing** — and September's Fed and ECB hikes both land after the aggregate's last month.

## The market's implied path — a hiking path, not a cutting one

The desk reproduction of the CME FedWatch projection (`FED:FFIMP`, implied EFFR = 100 − 30-day fed funds future) prices, on the ZQ strip in the Explorer catalogue **re-read this session** (September is realized EFFR, not a future):

```
2026-09  3.88 (realized)   2026-10  3.895   2026-11  4.06   2026-12  4.205
2027-01  4.275   2027-04  4.57   2027-08  4.795  2027-10  4.82
2027-11  4.84 (peak)       2027-12  4.825  2028-01  4.795  2028-02  4.775
```

That is roughly **+96bp of further tightening priced on top of the hike already delivered** — peaking at **4.84% in November 2027** and barely drifting off after it. October is still priced flat (3.895%, inside the 3.75–4.00% range); the next 25bp bucket is reached in November (4.06%, implied range 4.00–4.25%) and the one after in January 2027 (4.275%, 4.25–4.50%). The target range implied at the end of the strip has been lifted a whole bucket to **4.75–5.00%** (`FED:FFLOWER` 4.75 / `FED:FFUPPER` 5.00 at 2028-02).

> **Within-refresh supersession.** This strip was first written from the 2026-09-24 rebuild as `2026-10 3.90 · 2026-11 4.065 · 2027-04 4.56 · 2027-08 4.78 · 2027-11 4.82 (peak) · 2027-12 4.77 · 2028-02 4.78`, *"roughly +94bp"*. The catalogue has since re-run (`wb_explorer.json`, `built` 2026-09-25T10:09:58, vhash `eb2c482311b9`) and the whole strip firmed a touch: the peak is **4.84%**, still November 2027, and the tail no longer falls away — 4.825 in Dec-2027 against the 4.77 first recorded. **The two supersession blocks below quote the 4.82% peak because that is what their comparison was made against; they are dated records and are not restated.** Measured against the same 2026-09-19 strip, the peak rose ~16bp, not ~14bp.

> **This supersedes the 2026-09-19 strip**, which read `2026-09 3.88 · 2026-10 3.895 · 2026-11 4.025 · 2026-12 4.165 · 2027-01 4.23 · 2027-04 4.49 · 2027-08 4.665 · 2027-10 4.68 (peak) · 2027-12 4.65 · 2028-02 4.62` — *"roughly +80bp of further tightening priced"*, end-of-strip range 4.50–4.75%. In five sessions with the policy rate itself unchanged, the market added **~14bp to the peak** (4.68% → 4.82%), pushed it a month later (Oct-2027 → Nov-2027) and lifted the terminal range a full 25bp bucket. This is the third consecutive re-pricing in the same direction on this page, and the first one that happened *after* the Fed delivered: the hike did not cap the path, it extended it.

> **This supersedes the 2026-09-15 strip**, which read `2026-09 3.63 · 2026-10 3.88 · 2026-12 4.11 · 2027-04 4.38 · 2027-08 4.55 · 2027-11 4.60 (peak) · 2027-12 4.57 · 2028-02 4.54` — *"roughly +95bp of tightening priced"* from a 3.63% EFFR, end-of-strip range 4.50–4.75%. The Fed has now delivered the first 25bp of that path, and the market did not read it as the end: the peak rose 8bp (4.60% → 4.68%) and arrived a month earlier, so measured from the pre-hike 3.63% the cycle priced to the peak is now ~105bp against ~97bp on 2026-09-15.

> **This supersedes the 2026-08-13 strip**, which read `2026-08 3.63 · 2026-12 3.83 · 2027-04 3.96 · 2027-08 3.99 · 2027-12 3.94` — *"roughly +35bp of tightening priced"*, peaking near 3.99%, end-of-strip range 3.75–4.00%. In five weeks the market has **roughly tripled the tightening it prices** and lifted the terminal range by three whole 25bp buckets. Nothing the Fed did caused this: the policy rate itself has not moved. The re-pricing is the market's, and it is the single largest change on this page.

The cash curve corroborates it: the 2-year is **4.71%** and the 10-year **4.96%** (2026-09-22, FRED `DGS2`/`DGS10` via `macro_pack.json`; supersedes 4.67% / 4.94% on 2026-09-17), with the 3-month at **4.16%**. A 2-year yield sitting ~83bp *above* the 3.88% funds rate is exactly the shape a hiking path implies, and it has widened, not narrowed, since the hike landed.

This matters for how the book's Chapter 9 expressions are framed: a market pricing substantial further tightening with a still **positively-sloped** 2s10s — **+0.26pp at 2026-09-23** (FRED `T10Y2Y`; +0.42pp on 2026-07-15, +0.48pp on 2026-08-13, +0.33pp on 2026-09-15 and +0.25pp on 2026-09-18) and 10y−3m at **+0.92pp** (2026-09-23; supersedes +0.87pp on 2026-09-18) — is a bear-flattener/steepener question, not a recession-inversion question. **The flattening has stopped and partly reversed:** 2s10s bottomed at **+0.20pp on 2026-09-21** and has widened for two sessions, while 10y−3m jumped **+12bp on 23 Sep alone** (0.80 → 0.92) on a day the desk's MOVE gauge printed **95.45**, **+14.25 against its own previous observation** — which is the 21 Sep close of 81.20, because the deck's raw MOVE feed has no 22 Sep row, so that is a two-session move and not a 23 Sep one (see [[Global Macro Trading Deck (July 2026)]]). Today's pack carries no 23 Sep yield *levels* — only the two spreads — so which leg moved is not attributed here. See [[Yield Curve & Recession Signals]].

## The balance sheet — far off peak, now flat

FRED `WALCL` (the `US26:CBBS` workbook series still ends 2026-09-02 in the 2026-09-24 build) — Fed total assets **$6,746,548m** at **2026-09-16**, against a peak of **$8,965,487m at 2022-04-13**: **−24.7% off peak**. *Re-verified 2026-09-24: this is the same weekly print as the 2026-09-19 read — H.4.1 has published no observation after 2026-09-16 in today's pack (`macro_pack.json` `WALCL.latest_date`), so the figure is unchanged rather than restated.* Seven weeks of essentially flat balance sheet — $6,748,567m at 2026-08-05 → $6,746,548m — with the last three weekly prints edging *up* (from $6,730,912m at 2026-08-26), so the unwind has stalled into a drift rather than an active drain: **the Fed raised the price of money without resuming the drain of its quantity**. The accumulated quantitative tightening remains the passive backdrop; the book's Chapter 11 QE tables describe the expansion phase, and this platform is watching the unwind.

**Where the tightening is actually transmitting.** The clean pass-through is in mortgages: the 30-year fixed is **6.95%** (2026-09-17, `MORTGAGE30US`), **+19bp in the hike week** and +30bp from 6.65% on 2026-08-20. Expectations have not moved with it — the **5-year breakeven is 2.34%** (2026-09-23, FRED `T5YIE` via `macro_pack.json`) and the **10-year 2.35%** (same vintage, `macro_deck.json` `swaps.bei_now.b10`). The 5-year has recovered **only 2–3bp of the 9bp it gave back into 2026-09-18**, not all of it: the Explorer's weekly `INFEXP:BE5` ran 2.40% (09-11) → **2.31% (09-18)** → **2.33% (09-24)**, still **7bp below** its 09-11 level, while FRED's daily `T5YIE` went 2.31% (09-18) → **2.34% (09-23)**, +3bp. *(Corrects "having recovered the 9bp … without going anywhere on net", which overstated the retracement; every print here recomputed this session from `wb_explorer.json` and `macro_pack.json`.)* The Explorer's weekly copies are one observation fresher and a hair lower — `INFEXP:BE5` and `INFEXP:BE10` **both 2.33% at 2026-09-24** — which does not change the reading: every tenor on every feed sits inside a 2.33–2.35% band. *(Attribution corrected within this refresh: the 2.35% ten-year is the deck's figure, not `INFEXP:BE10`'s, which has no 09-23 observation.)* So the hike is being priced as a *real*-rate tightening — 10y TIPS real **2.63%** (2026-09-22, `DFII10`) — against unchanged long-run inflation expectations, which is the transmission the Committee would want and the opposite of a credibility problem.

## Policy stance vs the Taylor rule — policy is easier than the rule

Taylor (1993), in the unemployment-gap form Gliner presents:

> **i = r\* + π + 0.5(π − π\*) + 1.0(u\* − u)**

Live inputs (re-verified 2026-09-24 against `macro_pack.json`): core PCE inflation **+3.34% YoY** (2026-07, FRED `PCEPILFE`; 3-month annualised **3.05%**), unemployment **4.1%** (2026-08, `UNRATE`), π\* = 2%. *Both inputs are unchanged from the 2026-09-19 read — core PCE is the slowest-arriving input here, still runs one month behind CPI, and **still has no August print** after today's full re-pull — so the table below is re-verified, not restated.*

| r\* assumption | u\* = 4.0% | u\* = 4.4% |
|---|---|---|
| Classic r\* = 2.0% | **5.91%** | **6.31%** |
| Low r\* = 0.5% | **4.41%** | **4.81%** |

*(Previous reading, 2026-08-13: 5.83 / 6.23 / 4.33 / 4.73. The five-basis-point rise in core PCE lifts every cell ~8bp — the rule's verdict is unchanged, only slightly firmer.)*

Against an actual funds rate of **3.88%** (2026-09-22, `DFF` — the hike's level, now four days old), every parameterisation still says policy is **easier than the rule prescribes** — by ~0.5pp on the most generous (low-r\*, tight-u\*) reading and ~2.4pp on the classic one (*supersedes ~0.8pp / ~2.7pp against the pre-hike 3.63%: the hike narrowed every gap by 25bp and closed none*). That is the honest reading of the arithmetic, not a forecast: the Taylor rule is a benchmark with contested parameters, and the r\* choice moves the answer by 1.5pp on its own.

## Stance vs communication — they currently agree

The desk's FOMC hawk-dove index (`FED:HAWK`, lexicon-scored statements, 0–100) jumped to **80 in July 2026** from a steady 60 through the first half. The **September statement** — the one that delivered the hike — scores **70** (`FED:HAWK` 2026-09, re-verified in the 2026-09-24 rebuild and unchanged): the Fed raised rates in *less* hawkish language than July's statement. The series holds the stance constant between meetings, so 70 is the current reading until the next statement.

Hawkish language, inflation above target, a market pricing further tightening, and a balance sheet held a quarter below its peak are a **coherent set** — the rare case where communication, pricing and the rule all point the same way. As of this refresh the coherence holds and the Fed has now *acted* on it, but the legs moved further apart: the strip now prices **~96bp more** on top of the hike (was ~80bp on 2026-09-19), while the statement stance eased a notch (80 → 70) and the trigger the hike was answering — crude — has fallen back roughly $11 on WTI. The one leg that is *not* tightening with the others is the balance sheet, which has drifted sideways-to-up for seven weeks.

Caveat carried from the hawk-dove index's own build: it is a *stance descriptor*, not a return predictor — its correlation with trailing policy changes (+0.36) far exceeds its correlation with forward ones (+0.15). Detail in [[Monetary Policy Tools, Transmission & Communication]].

The newest CPI print is **still August's** — re-verified 2026-09-24 and unchanged: headline **+3.35% YoY** and core **+2.45% YoY** (`macro_pack.json` `CPIAUCSL` 334.131 / `CPILFESL` 337.765 for 2026-08, calendar-keyed against 2025-08 — a strict 12-month change; the pack withholds any YoY whose base month is missing, which is why FRED's null 2025-10 cannot inflate these again). Both sit above the 2% target — headline still rising (July +3.30%), core barely moved (July +2.47%) — and core PCE, the Fed's own gauge, remains **+3.34%** (July); that is what the "inflation above target" leg of the coherent set rests on. The pipeline is hotter still: August PPI (all commodities) is **+9.85% y/y** (July +8.70%). The sub-annual picture is more mixed and is not this page's to adjudicate: core CPI's 3-month annualised pace turned up to **1.97%** from 1.64% in July (still below 2% and below the 2.45% y/y) — and headline's only **+0.18%** (June fell 0.42% m/m) despite August's +0.40% m/m. See [[Macro Regime Snapshot]] for the inflation read proper.

## What is not here

- **No CDS, no repo, no LIBOR-OIS.** The book's funding-stress toolkit (Ch 9) has no feed on this platform; bank-funding stress cannot be monitored here.
- **No ECB/BoJ balance sheets** — only the Fed's. Comparative QE analysis is not possible.
- **Reserve balances, TGA, RRP** are not broken out; only total assets.

Related: [[Monetary Policy Tools, Transmission & Communication]] · [[M2 Money Supply & Liquidity]] · [[Government Bond Yields]] · [[Yield Curve & Recession Signals]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
