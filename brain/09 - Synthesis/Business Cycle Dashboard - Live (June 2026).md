---
title: Business Cycle Dashboard - Live (June 2026)
category: synthesis
type: live-read
data_asof: 2026-09-24
summary: "Live Leading/Coincident/Lagging + liquidity monitor (27 FRED/ISM signals); 2026-09-24: the cycle builders re-ran and filled 12 stale rows while the shock that justified the hike unwound (WTI $96.41, off $10.61)."
tags: [global-macro, synthesis, business-cycle, leading-coincident-lagging, high-frequency, liquidity, alt-data, live, fred, cross-asset]
data_vintage: "LIVE — 2026-09-24 read: the cycle builders were re-run today (Monthly Report/Business Cycle Dashboard.html + the xlsx/docx exports, all stamped asof 2026-09-24, 16:56–16:57), on tools/macro_pack.json (16:04) and scores_cache.json (16:15); the FED:FFIMP, GLOB:ECB and Explorer breakeven rows re-read from the Workbook Explorer catalogue at vhash eb2c482311b9 / asof 2026-09-24; stacked above the 2026-09-19 read, the 2026-08-15 correction banner and the superseded 19-Jun-2026 snapshot"
sources: FRED live (user key) + raw/2.3 Current Data (ISM)
updated: 2026-09-25
---

# Business Cycle Dashboard - Live (June 2026)

**What it is** — A live, institutional Leading / Coincident / Lagging business-cycle monitor, with a fourth **Alternative & High-Frequency** block (real-time pulse & liquidity). It classifies the current US macro regime to inform asset allocation. This is the **business-cycle-framework** complement to the endo/exo read in [[Macro Regime - Live (June 2026)]] — same data backbone (FRED), different lens. Data pulled via `tools/build_cycle_dashboard.py`; synthesis adversarially verified by a 3-lens panel.

## Live read — 2026-09-24 (current) — Regime: Tightening Held, Energy Shock Unwinding

*This is the newest read. It supersedes the 2026-09-19 read below and, through it, the 2026-08-15 correction banner and the 19-Jun-2026 snapshot — all kept verbatim as dated records; do not trade from them. Every figure below carries its own observation date.*

**Two things changed since 19 September, and they point opposite ways.** First, **the dashboard builders were finally re-run.** `build_cycle_dashboard.py`, `build_cycle_html.py` and `build_cycle_exports.py` all produced output today: `Monthly Report/Business Cycle Dashboard.html` (asof **2026-09-24**, written 16:57) and `Global Macro Brain/10 - Global Macro Dashboard/Global Macro Dashboard - Data 2026-09-24.xlsx` / `- Brief 2026-09-24.docx` (16:56). That closes most of the "not re-verified" list the 19 September read had to carry: **Building Permits, Consumer Confidence, Capacity Utilization, Real Personal Income, Unit Labor Costs, C&I Loans, Average Duration of Unemployment, Atlanta Fed GDPNow, NFCI, WEI and the TGA/ON-RRP legs of Net Liquidity all have live prints again**, several of them for the first time since the 19 June snapshot. Second, **the trigger for the hike has unwound**: WTI is **$96.41** and Brent **$114.89** (22 Sep), −$10.61 and −$15.91 from the 15 Sep prints that this page called the energy shock. The policy setting has not moved with it — funds has printed 3.88% every day through 22 Sep, and the market has *added* to the path it prices.

**⚠️ The rebuilt HTML's regime banner is still wrong, and it is wrong by construction.** The banner and the "Regime" KPI in `Monthly Report/Business Cycle Dashboard.html` are **hard-coded editorial strings** in `tools/build_cycle_html.py` (the `KPIS` list and the `<div class="banner">` literal), so today's rebuild re-emitted *"Regime: Late-Cycle Reflation"* on top of entirely current numbers. Its Fed-Funds KPI reads **3.63%, "−170bps from 5.33% peak, on hold"** because `fed_path` anchors to the monthly `FEDFUNDS` series, which will not show the hike until the September average publishes. The same applies to several row trend labels — the UMich row prints **55.2 vs 49.5** and still tags it *"Bearish"*; the payrolls row still prints a hard-coded *"3mo-avg +188k"* against an actual 3-month average of **+71k**. **What *is* live in that file:** every `latest`/`prev` number, the four signal tables, the charts, and the signal-breadth gauge, which is recomputed from the rows and returns **5 Bullish / 9 Bearish / 10 Neutral / 3 N-A** — the same counts as before, arrived at honestly. Read the numbers, ignore the banner, and treat this page as the regime call until the label is parameterised.

### Leading Indicators (next 3–6 months)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Fed policy rate (target range) | 3.75–4.00%; funds **3.88%** (22 Sep, `DFF`) | 3.88% (17 Sep) | → held every day since the hike | Bear (tight, now static) |
| Market-implied policy path | peak **4.84%** Nov-2027 (`FED:FFIMP`, re-read this session) | peak 4.68% Oct-2027 (19 Sep strip) | ▲ +16bp higher, one month later | Bear (more tightening priced) |
| ECB deposit facility rate | 2.50% (24 Sep, `GLOB:ECB`) | 2.50% (20 Sep) | → held | Bear (global tightening) |
| Yield Curve 10Y–2Y | **+0.26** (23 Sep) | +0.25 (18 Sep); low +0.20 (21 Sep) | ▲ flattening stopped, widened 2 sessions | Neutral |
| Yield Curve 10Y–3M | **+0.92** (23 Sep) | +0.87 (18 Sep) | ▲ +12bp on 23 Sep alone | Neutral→Bull |
| Building Permits (SAAR) | 1,394k (Aug); **+3.49% YoY** | 1,433k (Jul) | ▼ −39k MoM, but positive YoY | Bear (level), improving |
| Housing Starts (SAAR) | 1,275k (Aug); −1.24% YoY | 1,309k (Jul) | ▼ −34k MoM | Bear |
| Initial Claims | 196k (wk of 12 Sep); 4-wk avg 203.25k | 206k (5 Sep) | ▼ lowest of the four weeks | Bull (no layoff wave) |
| Consumer Confidence (UMich proxy) | **55.2** (Jul) | 49.5 (Jun) | ▲ +5.7 — first re-verification since the June snapshot | Bull (proxy) |
| M2 Money Supply (YoY) | **+5.66%** (Aug) | +5.41% (Jul) | ▲ accelerating | Bull (liquidity) |
| ISM Mfg PMI (headline) | 54.0 | 52.7 | → unchanged; local workbook vintage, not re-sourced | Bull (low-confidence) |

### Coincident Indicators (current state)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Industrial Production | +1.42% YoY / +0.02% MoM (Aug) | +1.13% YoY (Jul) | ▲ firming | Bull (modest) |
| Capacity Utilization | **76.27%** (latest print, today's rebuild) | 76.33% | → flat, below the ~79–80% norm | Neutral (slack) |
| Nonfarm Payrolls | +162k (Aug); 3mo-avg **+71k** | +21k (Jul), +31k (Jun) | ▲ rebound off a very weak base | Neutral→Bull |
| Retail Sales | +1.24% MoM / +6.01% YoY (Aug) | +5.03% YoY (Jul) | ▲ accelerating in nominal terms | Bull (nominal; CPI +3.35%) |
| Real Pers. Income (less transfers) | **+0.19% MoM / −0.38% YoY** (latest print, today's rebuild) | −0.00% YoY | ▼ YoY back below zero, MoM rising | Bear (the June "key crack", reopened at the margin) |
| Atlanta Fed GDPNow | **+5.08%** (current Q) | +1.54% | ▲▲ firmed hard | Neutral (composition-sensitive) |
| Real GDP (GDPC1) | +1.48% QoQ annualised / +2.10% YoY (Q2-26) | — | → modest | Neutral |

### Lagging Indicators (confirmation)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| CPI Headline | +3.35% YoY / +0.40% MoM (Aug); 3m ann. +0.18% | +3.30% YoY (Jul) | ▲ YoY a touch firmer; 3m pace near zero | Neutral (mixed) |
| Core CPI | +2.45% YoY / +0.29% MoM (Aug); 3m ann. 1.97% | +2.47% YoY (Jul); 3m ann. 1.64% | ▼ YoY easing; 3m up but still sub-2% | Neutral |
| Core PCE | +3.34% YoY (Jul); 3m ann. 3.05% | — (**still no Aug print** after today's re-pull) | → sticky, ~0.9pp above core CPI | Bear |
| Headline PCE | +3.70% YoY (Jul) | +3.72% YoY (Jun) | → above CPI | Bear |
| PPI — all commodities | +9.85% YoY / +0.96% MoM (Aug) | +8.70% YoY (Jul) | ▲▲ accelerating — but the barrel behind it has since fallen | Bear (pipeline, peaking?) |
| Unemployment U-3 | 4.10% (Aug); participation 61.6% | 4.10% (Jul) | → flat | Neutral→Bull |
| Avg Duration of Unemployment | **26.3 wks** | 24.9 wks | ▲ +1.4 wks | Bear (hiring freeze under a flat U-3) |
| Unit Labor Costs (QoQ ann.) | **+1.17%** | prior Q | → moderate | Neutral |
| C&I Loans | **+9.80% YoY / +1.57% MoM** | +8.67% YoY | ▲ expanding | Neutral (no credit stress) |

### Table 4 — High-Frequency & Liquidity Monitors (real-time pulse & liquidity)
| Indicator | Latest Print | Previous Print | Delta/Trend | Regime Signal | Data Frequency |
|---|---|---|---|---|---|
| Fed Balance Sheet (WALCL) | $6,746,548m (16 Sep) | $6,740,619m (9 Sep) | → **no newer print** in today's pack | Neutral (no drain) | Weekly |
| Central Bank Net Liquidity¹² | **$5.75T** | $5.90T | ▼ −$142bn WoW — **re-verified for the first time since June** | Bearish (drain, RRP buffer ~$0) | Weekly |
| Financial Conditions (NFCI) | **−0.555** (18 Sep) | −0.557 (11 Sep) | → flat, deeply loose | Bullish (no systemic stress) | Weekly |
| Real-Time Activity (WEI) | **3.07** | 3.73 | ▼ off the prior week, still ~3% pace | Bullish (firm) | Weekly |
| Credit — IG OAS | 0.77% (22 Sep) | 0.78% (17 Sep) | ▼ tighter | Bullish (no stress) | Daily |
| Credit — HY OAS | 2.68% (22 Sep) | 2.70% (17 Sep) | ▼ tighter | Bullish | Daily |
| Credit — CCC & lower OAS | 10.75% (22 Sep) | 10.76% (17 Sep) | ▼ tail calm | Bullish | Daily |
| Equity Vol (VIX) | **14.21** (22 Sep) | 15.44 (17 Sep) | ▼ lower again post-hike | Bullish | Daily |
| Equities | S&P 500 7,706.03 (23 Sep) **+15.76% YoY** · NASDAQ 26,936.04 **+19.33%** · Dow 51,511.59 **+11.27%** (both 23 Sep) | S&P 7,637.76 (17 Sep) | ▲ new highs on the week (S&P 7,764.70 on 21 Sep) | Bullish | Daily |
| Treasury yields | 2Y 4.71 · 10Y 4.96 · 3M 4.16 (22 Sep) | 2Y 4.67 · 10Y 4.94 · 3M 4.12 (17 Sep) | ▲ +4 / +2 / +4bp | Neutral→Bear | Daily |
| 10Y TIPS real yield | +2.63% (22 Sep) | +2.61% (17 Sep) | ▲ restrictive real rate held | Neutral | Daily |
| 30y Mortgage Rate | 6.95% (17 Sep) | 6.76% (10 Sep) | ▲ +19bp WoW; **no newer print** | Bear (housing) | Weekly |
| Energy | **WTI $96.41 · Brent $114.89** (22 Sep); +53.1% / +71.8% YoY | WTI $107.02 · Brent $130.80 (15 Sep) | ▼▼ **the spike has unwound** | Bearish, but easing | Daily |
| Inflation expectations | 5y breakeven 2.34% (`T5YIE`, 23 Sep) · 10y 2.35% (deck `swaps.bei_now.b10`, same vintage); Explorer `INFEXP:BE5`/`BE10` both **2.33% (24 Sep)** | 5y 2.31% (18 Sep) | ▲ +2–3bp *while* crude fell — not tracking the barrel | Neutral (anchored) | Daily / weekly |
| Gas & metals | Henry Hub $2.963/MMBtu (Jul-26, IMF monthly), −10.5% YoY · Copper $13,543/mt (Jul-26, IMF), +38.6% YoY | — | split — gas soft, copper surging | Mixed | Monthly |
| Broad USD Index¹¹ | **119.51** (18 Sep), −0.12% YoY · EUR/USD 1.1464 · USD/JPY 156.87 · AUD/USD 0.7111 (18 Sep) | 118.21 (11 Sep), −1.45% YoY | ▲ **dollar turned up**, +1.1% in a week | Neutral→Bear (for EM/commodities) | Weekly (lagged) |
| Inventories / sales | 1.30 (Jul) | — | → flat | Neutral | Monthly |

¹¹ FRED's H.10 publishes with a lag; **18 Sep is the latest available print** and no newer FX read is claimed here.
¹² Net Liquidity = `WALCL − WDTGAL − RRPONTSYD`, as computed by `build_cycle_html.py` in today's rebuild. The builder aligns the three series by *last observation* rather than by date, and its WALCL leg is the 16 Sep print; the "WoW" delta is between the two most recent observations of each. Quote it as the builder's composite, not as a dated triple.

**Scorecard cross-check** (`scores_cache.json`, rebuilt **2026-09-24 16:15** with Excel closed, so the endo/exo templates recalculated rather than being read stale). The FRED-backed **US Endogenous** template still scores **+19, "Mildly Inflationary"** — Leading Surveys −4, Money Supply −2, Interest Rates +2, Inflation +4, Employment −2, Sovereign & Balance Sheet +21 — and the **AUD/USD Exogenous** template still reads **+2, "NEUTRAL AUD/USD"** (Relative GDP Growth −2, Relative Balance of Payments +4, Rate Differential/Carry −2, Relative Equity Returns +2). **Both are unchanged from the 2026-09-19 read and are therefore re-verified, not restated** — the AUD/USD exo score is **+2, flipped in sign from −2**, and that flip has now survived a recalculation done with Excel closed rather than a cache read. Verified twice this session: `scores_cache.json` (written 16:15) and the Scorecards sheet of today's `Global Macro Dashboard - Data 2026-09-24.xlsx`, which carries the identical six endo categories, ENDO TOTAL 19 / "Mildly Inflationary", the four exo drivers and EXO TOTAL 2 / "NEUTRAL AUD/USD". Note these are the *template* engines. The Workbook Explorer's separate **card** engine computes different numbers on the same names — `wb_explorer.json` `scorecards` reads **US +36, AU +24, UK +27** and an **AUD/USD exo card of −4.0**. **Two of those four are path artefacts, not economics, and each for its own reason — both traced on disk this session, so neither is a second opinion:**

- **AU +24 is provisional, and it is not Australian disinflation.** `xlfind.find_wb` resolves `27. AUS_Endogenous_Driver_Analysis_New 2026.xlsx` to a thin **119,688-byte** copy sitting in the `2.8` root, instead of the curated **772,878-byte** copy in `15. Endogenous Score/` (both files confirmed on disk and `find_wb()` called this session — it returns the root copy). The thin copy sources M3 and CPI from retired FRED series, so both drivers are guarded to zero: `scorecards.endo[AU]` shows "M3 Money Supply (YoY %)" rate 4.631, score **0.0**, state **STALE**, and "Consumer Price Index (YoY %)" rate 2.402, score **0.0**, state **STALE**. The curated workbook reads **+34** — see [[Australia Endogenous Driver Analysis (July 2026)]] for the driver-by-driver bridge — so **+24 is not comparable with the US +36 and UK +27 beside it**.
- **The −4.0 AUD/USD exo card is computed from the OLDER of two copies of `39. Exogenous_AUD_USD.xlsx`.** Calling `find_wb` on it this session printed the loader's duplicate warning — *"subfolder copy NEWER than top-level … still reading the top-level copy"* — because the `16. Exogenous Score/` copy (822,790 bytes, 2026-09-07) is newer than the top-level one it actually reads (822,708 bytes, 2026-07-18). So the card is not a current read of that template either; the FRED-backed exo *template*, recalculated at 16:15 today, separately reads **+2, "NEUTRAL"** (above).

The user has chosen to leave both stray files in place for now. See [[PTM Endo Scorecard (2026 Excel Data)]].

**Conflicting-signal synthesis.** The leading block has improved at the margin: the curve stopped flattening and re-steepened, permits are positive year-over-year, claims fell to 196k, M2 accelerated to +5.66% and consumer sentiment jumped to 55.2. Coincident data are firm to hot — IP firming, retail sales +6.01% YoY, GDPNow at +5.08% — with **one genuine crack: real personal income less transfers is back below zero year-over-year (−0.38%)**, the same signal the June snapshot named as decisive and the first time it has been re-verified since. Lagging inflation is still two-tier (core CPI +2.45% against PPI +9.85%, core PCE 3.34%), but the pipeline's driver is now falling. The highest-conviction read is therefore **a cost-push impulse that is already fading into a policy setting that has not faded with it**: the Fed hiked into a $107 barrel, the barrel is $96, and the strip prices another ~96bp on top (re-read this session; the strip firmed ~2bp at the peak after the first write-up of this section). That is a *tightening-overshoot* risk, not the demand exhaustion the June snapshot feared and not the disinflation the August banner recorded. Markets have voted: credit tighter, VIX 14.21, equities at new highs.

**Cross-asset read** (supersedes the 2026-09-19 cross-asset read below, which was written into a live energy spike). The inflation-beneficiary trade has *already paid and is now rolling*: crude is off ~10% from its peak, gold fell 8.65% in a month and silver 6.78% (see [[Global Macro Trading Deck (July 2026)]]), while copper holds at the 99th percentile. Duration is being asked to absorb a 3.88% funds rate and a 4.84% priced peak with headline PCE at 3.70% — 10Y 4.96%, 10Y real +2.63% — and the rates-vol gauge (MOVE 95.45, 96.8th percentile) says that repricing is live, not settled. Credit is priced for calm (HY 2.68%) on data that now *postdates* the hike, which is a stronger statement than a week ago. Rate-sensitive housing still faces a **6.95%** mortgage against starts −2.6% MoM. The dollar has turned up (+1.1% in a week), which is the cleanest expression of the widening rate path and the main new headwind for EM and commodity exposure. Internal monitor — macro/asset-class level, not investment advice.

**Not re-verified in this read.** **ISM Mfg / New Orders** (the builder reads the maintained `raw/2.3 Current Data` workbook, still a Jun-2026 vintage — 54.0 / 52.7 is carried, not re-sourced); **`DHHNGSP` daily Henry Hub** (the IMF monthly is quoted instead); **Global Shipping (BDI/SCFI)**, **card-spend / TSA throughput** and the **earnings-transcript tracker**, all off the free pipeline. The **Fed Tracker** NLP block in §5 remains *Awaiting*: `fed_tracker.py` still needs the 17-Sep FOMC statement text, which has not been filed, and `fed_tracker_latest.json` was absent again in today's build. The desk's lexicon-scored `FED:HAWK` index — a different instrument — reads **70 for 2026-09**, and is documented in [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]].

## Live read — 2026-09-19 — Regime: Policy Tightening into an Energy Shock

> **SUPERSEDED by the 2026-09-24 read above** (added 2026-09-24). Kept verbatim as a dated record — including the "this is the newest read" wording below, which was true when written. Its energy levels (WTI $107.02 / Brent $130.80, 15 Sep) and its market prints (VIX 15.44, HY 2.70, 2Y 4.67 / 10Y 4.94, 17–18 Sep) are correct for their dates and are no longer current; its "not re-verified in this read" list has largely been closed by today's builder run.

*This is the newest read. It supersedes the 2026-08-15 correction banner below and, through it, the 19-Jun-2026 snapshot — both are kept verbatim as dated records; do not trade from them. Every figure below carries its own observation date, and the readings this section replaces are listed in [[log]]. The dashboard builders were **not** re-run for this read — see "Not re-verified in this read" at the end of the section.*

**Headline — both major central banks tightened in the same week the energy shock re-intensified.** The Fed **raised 25bp to a 3.75–4.00% target range, effective 17 Sep 2026** — the *first hike of the cycle*, and the outright reversal of the "easing cycle paused / hawkish hold" read that has stood on this page since June. EFFR printed **3.88%** on 17 Sep (3.63% through 16 Sep; monthly FEDFUNDS 3.63% in Jun, Jul and Aug). The **ECB deposit facility rate went 2.25% → 2.50%, effective 16 Sep** — its second move. The trigger sits in the goods pipeline, not yet in the consumer basket: **WTI $107.02** and **Brent $130.80** (15 Sep; +68.1% and +92.7% y/y), with **PPI all-commodities +9.85% y/y** in August (Jul +8.70%; +0.96% m/m). Demand is firm, not fading — **retail sales +1.24% m/m**, **payrolls +162k**, **initial claims 196k**. Core CPI is still only **+2.45% y/y**; its 3-month annualised pace **turned up to 1.97% from 1.64% in July**, but remains below both the y/y rate and 2% — a turn off a low base, not a re-acceleration.

### Leading Indicators (next 3–6 months)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Fed policy rate (target range) | 3.75–4.00% (eff. 17 Sep); EFFR 3.88% (17 Sep) | 3.50–3.75%; EFFR 3.63% (through 16 Sep) | ▲ +25bp — first hike of the cycle | Bear (tightening) |
| ECB deposit facility rate | 2.50% (eff. 16 Sep) | 2.25% | ▲ +25bp — second move | Bear (global tightening) |
| Yield Curve 10Y–2Y | +0.25 (18 Sep) | +0.33 (15 Sep) | ▼ flattened 8bp, still positive | Bear (momentum) |
| Yield Curve 10Y–3M | +0.87 (18 Sep) | +0.89 (15 Sep) | → little changed, comfortably positive | Neutral |
| Housing Starts (SAAR) | 1,275k (Aug); −2.6% MoM; −1.24% YoY | Jul: −8.59% YoY | ▼ level still falling, but the YoY drag narrowed sharply | Bear (level), improving |
| Initial Claims | 196k (wk of 12 Sep); 4-wk avg 203.25k | 206k (5 Sep), 207k (29 Aug), 204k (22 Aug) | ▼ lowest of the four weeks | Bull (no layoff wave) |
| M2 Money Supply (YoY) | +5.41% (Jul) | — | → still expanding; YoY rate eased from the +5.53% Aug-15 read | Bull (liquidity) |

**How the curve actually moved** — the week was not a single bear-flattening, and the front end did **not** rise on the hike. 10Y–2Y went +0.33 (15 Sep) → +0.27 (16) → +0.27 (17) → +0.25 (18). The **16 Sep leg was a bear-flattening** (2Y +7bp to 4.74, 10Y +1bp to 5.01). On **hike day, 17 Sep, both yields fell 7bp together — a parallel rally, with 2s10s unchanged at +0.27** (2Y 4.67, 10Y 4.94). The final 2bp of flattening on 18 Sep cannot be attributed, because no 18-Sep yield levels were published. Net 15 → 17 Sep: **2Y unchanged, 10Y −6bp**.

### Coincident Indicators (current state)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Industrial Production | +1.42% YoY / +0.02% MoM (Aug) | +1.13% YoY (Jul) | ▲ firming | Bull (modest) |
| Nonfarm Payrolls | +162k (Aug); 3mo-avg +71k | +21k (Jul), +31k (Jun) | ▲ sharp August rebound off a very weak base | Neutral→Bull |
| Retail Sales | +1.24% MoM / +6.01% YoY (Aug) | +5.03% YoY (Jul) | ▲ accelerating in nominal terms | Bull (nominal; CPI +3.35%) |
| Real GDP (GDPC1) | +1.48% QoQ annualised / +2.10% YoY (Q2-26) | — | → modest | Neutral |

### Lagging Indicators (confirmation)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| CPI Headline | +3.35% YoY / +0.40% MoM (Aug); 3m annualised +0.18% | +3.30% YoY (Jul); 3m annualised +0.49% | ▲ YoY a touch firmer; 3m pace near zero | Neutral (mixed) |
| Core CPI | +2.45% YoY / +0.29% MoM (Aug, firmest MoM since April); 3m annualised 1.97% | +2.47% YoY (Jul); 3m annualised 1.64% (Jun 2.29%, May 3.17%) | ▼ YoY easing; 3m pace turned **up from 1.64%**, still below 2% | Neutral |
| Core PCE | +3.34% YoY (Jul); 3m annualised 3.05% | — (no Aug print yet) | → sticky, ~1pp above core CPI | Bear |
| Headline PCE | +3.70% YoY (Jul) | — | → above CPI | Bear |
| PPI — all commodities | +9.85% YoY / +0.96% MoM (Aug) | +8.70% YoY (Jul) | ▲▲ accelerating | Bear (pipeline) |
| Unemployment U-3 | 4.10% (Aug); participation 61.6% | — | → low | Neutral→Bull |

### Table 4 — High-Frequency & Liquidity Monitors (real-time pulse & liquidity)
| Indicator | Latest Print | Previous Print | Delta/Trend | Regime Signal | Data Frequency |
|---|---|---|---|---|---|
| Fed Balance Sheet (WALCL)¹⁰ | $6,746,548m (16 Sep) | $6,740,619m (9 Sep); $6,737,204m (2 Sep) | ▲ higher for a second straight week (+$5.9bn WoW) | Neutral (no drain) | Weekly |
| Credit — IG OAS | 0.78% (17 Sep) | 0.80% (15 Sep) → 0.78% (16 Sep) | ▼ retraced on 16 Sep, **unchanged on hike day** | Bullish (no stress) | Daily |
| Credit — HY OAS | 2.70% (17 Sep) | 2.76% (15 Sep) → 2.70% (16 Sep) | ▼ same pattern | Bullish | Daily |
| Credit — CCC & lower OAS | 10.76% (17 Sep) | 10.85% (15 Sep) → 10.76% (16 Sep) | ▼ same pattern | Bullish (tail calm) | Daily |
| Equity Vol (VIX) | 15.44 (17 Sep) | 17.71 (16 Sep); 17.20 (15); 17.10 (14) | ▼ **fell on hike day** | Bullish | Daily |
| Equities | S&P 500 7,637.76 (17 Sep), +15.7% YoY · NASDAQ 26,522.55 (18 Sep), +18.0% YoY · Dow 51,682.64 (18 Sep), +12.0% YoY | — | ▲ broad YoY gains | Bullish | Daily |
| Treasury yields | 2Y 4.67 · 10Y 4.94 · 3M 4.12 (17 Sep) | 2Y 4.67 · 10Y 5.00 · 3M 4.11 (15 Sep) | → 2Y unchanged, 10Y −6bp net | Neutral | Daily |
| 10Y TIPS real yield | +2.61% (17 Sep) | +2.68% (16 Sep); +2.60% (14 Sep) | ▼ off the 16-Sep high | Neutral (restrictive real) | Daily |
| 30y Mortgage Rate | 6.95% (17 Sep) | 6.76% (10 Sep) | ▲ +19bp WoW | Bear (housing) | Weekly |
| Energy | WTI $107.02 · Brent $130.80 (15 Sep) | WTI $97.26 · Brent $109.51 (9 Sep); WTI $102.42 (14 Sep) | ▲▲ +68.1% / +92.7% YoY | Bearish (cost shock) | Daily |
| Gas & metals | Henry Hub $2.97 (15 Sep), −1.0% YoY · Copper $13,543/mt (Jul-26, IMF monthly), +38.6% YoY | — | split — gas flat, copper surging | Mixed | Daily / Monthly |
| Broad USD Index¹¹ | 118.21 (11 Sep), −1.45% YoY · EUR/USD 1.1600 · USD/JPY 153.71 · AUD/USD 0.717 (11 Sep) | — | → softer YoY | Neutral | Weekly (lagged) |

¹⁰ Only the **WALCL leg** of Net Liquidity was re-verified. TGA and ON RRP were not, so the `WALCL − WDTGAL − RRPONTSYD` Net Liquidity figure is **not restated** in this read — the June-vintage row in the snapshot below stands as a dated record, not as a current claim.
¹¹ FRED's H.10 publishes with a lag; **11 Sep is the latest available print** and no newer FX read is claimed here.

**Scorecard cross-check** (`scores_cache.json`, rebuilt 2026-09-19 15:33). The FRED-backed **US Endogenous** template scores **+19, "Mildly Inflationary"**, up from **+9, "Neutral / Balanced"** on 2026-09-09. The move is almost entirely **Inflation +4 (was −12)** on top of a standing **Sovereign & Balance Sheet +21**, against **Leading Surveys −4 (was +2)**, Money Supply −2, Interest Rates +2, Employment −2. The **AUD/USD Exogenous** template reads **+2, "NEUTRAL AUD/USD"** (was −2). Both agree with the read above: inflation pressure re-entering through the supply/pipeline channel while the forward-survey block softens. See [[PTM Endo Scorecard (2026 Excel Data)]].

**Conflicting-signal synthesis.** The leading block is split — the curve flattened and housing starts fell again, but claims at 196k and M2 at +5.41% YoY point the other way; the decisive leading change is the **policy rate itself**, tightening for the first time this cycle. Coincident data are firm across the board (IP, retail sales, the August payroll rebound). Lagging inflation is **two-tier**: consumer inflation is contained (core CPI +2.45% YoY, 3m 1.97%) while producer inflation is not (PPI +9.85% YoY) and core PCE is still 3.34%. The highest-conviction read is therefore **a cost-push impulse being met with pre-emptive tightening while demand is still firm** — neither the late-cycle demand exhaustion the June snapshot feared nor the disinflation the August banner recorded. Markets absorbed the move: credit had already retraced on **16 Sep**, the day *before* the hike took effect (HY 2.70, CCC 10.76), spreads were **unchanged on hike day**, and VIX *fell* to 15.44.

**Cross-asset read** (supersedes the June "Cross-asset implications" book below, which was written for an easing Fed). The Fed is tightening, not easing, and the shock is cost-push: the move in inflation-beneficiary real assets has already largely happened (Brent +92.7%, WTI +68.1%, copper +38.6% YoY). Duration is being asked to absorb a 3.75–4.00% policy rate with headline PCE at 3.70% and PPI at +9.85% (10Y 4.94%, 10Y real +2.61%). Credit is priced for calm (HY OAS 2.70%) on data that *predates* the hike. Rate-sensitive housing now faces a **6.95%** 30-year mortgage against starts already −2.6% MoM. Internal monitor — macro/asset-class level, not investment advice.

**Not re-verified in this read (unchanged — see the dated sections below).** The Business Cycle Dashboard builders (`build_cycle_dashboard.py`, `build_cycle_html.py` and the exports) were **deliberately not re-run** on 2026-09-19 because they hard-code a regime label, so `Monthly Report/Business Cycle Dashboard.html` — its regime banner, KPI strip and the 5/9/10/3 signal-breadth counts quoted in the banner below — still carries the earlier vintage. **Treat that HTML as stale until it is rebuilt with the regime label parameterised.** Also not re-verified today, and therefore left at their last-dated prints: **ISM Mfg / New Orders**, **Building Permits**, **Consumer Confidence (UMich proxy)**, **Capacity Utilization**, **Real Personal Income less transfers**, **Average Duration of Unemployment**, **Unit Labor Costs**, **C&I Loans Outstanding**, **Atlanta Fed GDPNow**, **NFCI**, **WEI**, and the **TGA / ON RRP** legs of Net Liquidity. The **Fed Tracker** NLP block in §5 remains *Awaiting*: `fed_tracker.py` needs the 17-Sep FOMC statement text, which has not been filed.

> ## ⚠️ SUPERSEDED — the regime call below has INVERTED (re-verified against FRED, 2026-08-15)
>
> This page is a **19 June 2026 snapshot**. It is kept as a dated record; do not trade from it. Its headline call — *"Late-Cycle Reflation: growth firm while inflation re-accelerates"* — no longer holds, and the page's own self-declared **highest-conviction pillar reversed outright**.
>
> | Pillar | This page (Jun 19) | Verified today (Aug 15) | Status |
> |---|---|---|---|
> | CPI headline YoY | +4.27%, "re-accelerating" | **+3.30%** (Jul), prior +3.46%; Jun MoM **−0.42%** | **Reversed** — disinflating |
> | Core CPI YoY | +2.96% | **+2.47%** (Jul) | Reversed |
> | Core PCE YoY | 3.29% "sticky" | **+3.29%** (Jun), easing from +3.42% | Rolling over |
> | Payrolls 3mo-avg | +188k | **+20k**; Jul outright **−23k**; May revised 172k→**63k** | Momentum collapsed |
> | 10s2s | +27bps, "re-flattening" | **+51bps** | Steepened, not flattened |
> | Real personal income | −1.04% YoY — "the decisive crack" | **rising** — two straight monthly gains | Crack closed |
>
> **But the growth side is genuinely two-sided, and this correction does not claim a downturn.** Against the weak hiring pace: **U-3 fell to 4.1%** (from 4.3%), **initial claims 199k** (4-wk, falling), Atlanta Fed **GDPNow Q3 +4.31%**, **M2 +5.53% YoY**. That is a *slowing hiring pace without rising joblessness* — not a contraction. What is unambiguous is the **inflation reversal**, and that alone flips the derived book below: short duration, TIPS-over-nominals and hawkish-hold were positioned for re-acceleration that did not happen.
>
> **A calculation bug also inflated the original prints.** The CPI figures on this page were overstated at source, independent of the two months that have passed — see the note under the Inflation table. Corrected in `tools/build_cycle_dashboard.py` on 2026-08-15.
>
> **To refresh:** `python tools/build_cycle_dashboard.py` (now date-matched), then rewrite the regime call from the new prints.
>
> **Interactive version.** A self-contained Chart.js dashboard renders this page at `Monthly Report/Business Cycle Dashboard.html` — regime banner, KPI strip, four color-coded signal tables, a signal-breadth diffusion gauge, and trend charts (Net Liquidity, NFCI, 10s2s, CPI vs Core PCE). Build: `python tools/build_cycle_html.py`. Current breadth: 5 Bullish / 9 Bearish / 10 Neutral / 3 N-A.

## Executive summary (AS OF 2026-06-19 — SUPERSEDED, see banner) — Regime: Late-Cycle Reflation
Coincident growth remains firm-to-accelerating (ISM Mfg 54.0, GDPNow +3.0%, payrolls +188k 3mo-avg) while inflation **re-accelerates** (CPI +4.27% YoY, Core PCE sticky 3.29%, M2 YoY +4.72%). The slowdown is a **forward risk confined to leading indicators** — Housing Starts −215k, sentiment 49.8, 10s2s re-flattening to +27bps, unemployment duration up to 26 wks — **not yet in the hard data**. The decisive crack is **contracting real personal income (−1.04% YoY)** beneath inflation-flattered nominal spending.

*Signal convention: **Bull** = expansionary/risk-supportive · **Bear** = contractionary/cautionary or hawkish-inflationary · **Neutral** = mixed. Level and delta weighted together.*

### Leading Indicators (next 3–6 months)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Yield Curve 10Y–2Y | +27 bps (Jun 18) | +54 bps (~1mo) | ▼ flattening 27bps, positive | Bear (momentum) |
| ISM Mfg PMI (headline)¹ | 54.0 (May) | 52.7 (Apr) | ▲ +1.3 | Bull (low-conf)¹ |
| Building Permits (SAAR) | 1,413k (May) | 1,423k (Apr) | ▼ −10k | Bear |
| Housing Starts (SAAR) | 1,177k (May) | 1,392k (Apr) | ▼▼ −215k (−15.4%) | Bear (strong) |
| Initial Claims (4wk MA) | 223.3k (Jun 13) | 219.3k | ▲ +4k | Neutral→Bear |
| Consumer Confidence² | UMich 49.8 (Apr) *(latest print since: 44.8 — 0.1st pctl of 73y)* | 53.3 (Mar) | ▼ −3.5 | Bear (proxy)² |
| M2 Money Supply (YoY) | +4.72% (Apr) | +4.58% (Mar) | ▲ accelerating | Bull (liquidity) |

¹ ISM **New Orders** sub-index not captured (Awaiting); headline substituted — low-confidence, and conflicts with the housing collapse. See [[Leading Indicators]].
² Conference Board CC is proprietary (unavailable); **UMich shown as FRED proxy**; latest hard print April.

### Coincident Indicators (current state)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| Industrial Production | +1.67% YoY / +0.14% MoM (May) | +1.37% YoY | ▲ firming | Bull (modest) |
| Capacity Utilization | 76.17% (May) | 76.13% | → flat, below ~79–80% | Neutral (slack) |
| Nonfarm Payrolls | +172k (May); 3mo-avg +188k | — | ▼ solid, decelerating | Neutral→Bull |
| Retail Sales (control proxy)³ | +0.88% MoM / +6.88% YoY (May) | +4.79% YoY | ▲ nominal; real ≈ +2.6% | Neutral (flattered) |
| Real Personal Income (less transfers) | −0.44% MoM / −1.04% YoY (Apr) | −0.58% YoY | ▼ contracting | Bear (key crack) |
| Atlanta Fed GDPNow | +3.04% (curr. Q) | +1.24% est | ▲ firmed | Neutral (noisy)⁴ |
| Real GDP (GDPC1) | ~+1.6% annualized (Q1-26) | prior Q | → modest | Neutral |

³ True Control Group not isolated on FRED; total + ex-auto shown. Real consumption soft after CPI deflation. See [[Coincident Indicators]].
⁴ Early-quarter GDPNow is composition-sensitive and diverges from hard GDP ~+1.6% — low-confidence.

### Lagging Indicators (confirmation)
| Indicator | Latest | Previous | Delta/Trend | Signal |
|---|---|---|---|---|
| CPI Headline | +4.27% YoY / +0.47% MoM (May) | +3.95% YoY | ▲ re-accelerating | Bear (hot) |
| Core CPI | +2.96% YoY / +0.21% MoM (May) | +2.99% YoY | ▼ easing | Neutral |
| Core PCE | +3.29% YoY / +0.24% MoM (Apr) | +3.24% YoY | ▲ sticky | Bear |
| Unemployment U-3 | 4.30% (May) | 4.30% (Apr) | → flat | Neutral (masks duration⁵) |
| Unit Labor Costs (NFB) | ~+1.8% annualized (Q1) | prior Q | → moderate | Neutral |
| C&I Loans Outstanding | +8.12% YoY / +0.80% MoM (May) | +7.68% YoY | ▲ expanding | Neutral (no stress)⁶ |
| Avg Duration of Unemployment | 26.0 wks (May) | 24.4 wks | ▲ +1.6 wks | Bear (hiring freeze) |

> **⚠️ These CPI prints were overstated at source — calculation bug, fixed 2026-08-15.** FRED carries a **null 2025-10** observation for CPIAUCSL and CPILFESL. `tools/build_cycle_dashboard.py` computed YoY as a *positional* `o[-1]/o[-13]`, and because the fetch layer drops nulls that lookback silently reached back **13 months**, comparing May-26 against **Apr-25**. Date-matched, the correct figures for this vintage were **CPI +4.17%** (not +4.27%) and **prev +3.78%** (not +3.95%). The bug inflated every YoY on any series with a data gap, always in the direction of *more* inflation. Now computed by calendar-date match, with missing months reported instead of absorbed silently.


⁵ Flat U-3 + rising duration = labor softening beneath a stable headline.
⁶ Strong C&I this late-cycle is often defensive/inventory financing and itself lagging — Neutral, not Bull.

### Table 4 — High-Frequency & Liquidity Monitors (real-time pulse & liquidity)
| Indicator | Latest Print | Previous Print | Delta/Trend | Regime Signal | Data Frequency |
|---|---|---|---|---|---|
| Central Bank Net Liquidity⁷ | $5.77T (Jun 17) | $5.92T (Jun 10) | ▼ −$151B WoW | Bearish (drain; buffer gone) | Weekly |
| Financial Conditions (Chicago Fed NFCI) | −0.51 (Jun 12) | −0.51 | → flat, **loose** (sub-zero) | Bullish (no systemic stress) | Weekly |
| Real-Time Activity (WEI)⁸ | 3.10 (Jun 13) | 2.90 | ▲ +0.20, ~3% pace | Bullish (firm) | Weekly |
| Global Shipping (BDI / SCFI) | Awaiting⁹ | — | — | N/A | Daily (BDI) / Weekly (SCFI) |
| Real-Time Consumer Spend (card / TSA) | Awaiting⁹ | — | — | N/A | Daily |
| Corporate Pulse (transcript mentions) | Awaiting⁹ | — | — | N/A | Quarterly (earnings) |

⁷ Net Liquidity = Fed Balance Sheet (WALCL $6.74T) − TGA ($957B, rebuilding) − ON RRP (~$0, drained). The **exhausted RRP buffer** means further TGA builds now hit bank reserves directly — a sharper liquidity headwind. See [[M2 Money Supply & Liquidity]].
⁸ WEI (Lewis-Mertens-Stock) scaled to ~YoY real activity; firm ~3%, corroborates GDPNow. FRED proxy for the real-time pulse.
⁹ Not on FRED / free pipeline — requires paid/alt feeds: shipping = Baltic Exchange & Shanghai Shipping Exchange; card spend = BofA/JPM/Opportunity Insights; TSA throughput = tsa.gov (daily); corporate-transcript NLP = bigdata.com / AlphaSense. The vault's `bigdata.com` integration could source the transcript-mention tracker on request.

**Alt-data read:** real-time activity (WEI ~3%) and financial conditions (NFCI −0.51, loose) corroborate firm *current* growth with no systemic stress — but **Central Bank Net Liquidity is draining (−$151B WoW) with the ON RRP buffer now exhausted**, a forward liquidity headwind that aligns with (not against) the leading-indicator cracks.

**Conflicting-signal synthesis:** Leading indicators flag a *forward* slowdown, but coincident labor/output are resilient and lagging inflation is hot — a mixed signal. The economy is **not slowing yet**; the leading edge is cracking while inflation re-accelerates. Highest-conviction read is the **inflation re-acceleration** (CPI/PCE + M2 agree); growth direction is two-sided and lower-conviction.

## 5. Central Bank NLP & Sentiment Analysis (The Fed Tracker) — data-derived block AS OF 2026-06-19, SUPERSEDED (see the 2026-09-19 Live read)
A deterministic NLP module that grades FOMC text (Statement / Minutes / Press Conference) for policy lean. Run `python tools/fed_tracker.py <current.txt> [previous.txt]`; it writes `fed_tracker_latest.json`, which the HTML dashboard auto-ingests.

| Output | Method | Current state |
|---|---|---|
| **Hawkish/Dovish Score** | Weighted hawk/dove lexicon → `10·tanh(net/8)`, scale **−10 (max dovish) … +10 (max hawkish)** | **Awaiting latest FOMC text** |
| **Delta from Previous** | Phrase-level diff vs prior statement — *emerged* vs *dropped* tracked phrases + score change | **Awaiting** (needs 2 texts) |
| **Forward Guidance / Terminal Bias** | Score→bias heuristic, anchored to the **real Fed Funds path** | **19-Jun-2026 vintage — SUPERSEDED. Current: Fed raised 25bp to 3.75–4.00%, eff. 2026-09-17 (EFFR 3.88%); ECB deposit rate 2.50%, eff. 2026-09-16 — see the Live read above.** |
| **Keyword Mention Tracker** | Frequency of high-impact terms (`disinflation`, `resilient`, `pain`, `balance sheet`, `two-sided risks`, `restrictive`, `elevated`, …) | **Awaiting text** |

**Data-derived forward guidance (no transcript needed):** Fed Funds **3.63%** (May 2026), **−170bps** from the 5.33% peak, **held flat Jan–May 2026** (easing cycle paused). With CPI re-accelerating to **+4.27% YoY** and Core PCE sticky at **3.29%**, the easing path has **stalled and the bias skews hawkish** — real policy rate is positive but inflation is re-accelerating, raising the risk of a hawkish hold / fewer cuts than the dot-plot implied. *This is the quantitative complement to the (awaiting) text NLP.*

### FOMC NLP Analysis — tear-sheet (output format)
When a statement (and the prior) is supplied, `fed_tracker.py` emits a **FOMC NLP Analysis** block:
- **Hawk/Dove Score:** `[-10 … +10]` + terminal-rate bias
- **Tone Delta:** one sentence on how tone changed vs the last meeting
- **Key Phrase Additions/Deletions:** exact quoted sentences (➕ added / ➖ removed)
- **Keyword Frequency Changes:** e.g. *"Disinflation" 3x (up from 0x); "Restrictive" 0x (down from 2x)*
- **Policy Implication:** one sentence for rate markets & the yield curve

> **Validated on an illustrative sample** (not a live read): a dovish statement vs a hawkish prior →
> Score **−9.9**; Tone Delta *"more dovish (+8.8 → −9.9)"*; additions incl. *"…in light of the progress on disinflation, the Committee decided to reduce the target range…"*; Keyword changes: Disinflation 3x (up from 0x), Restrictive 0x (down from 2x), Elevated 1x (down from 2x); Policy Implication *"Dovish tilt — aggressive front-end rally and bull-steepening."* Feed a real transcript to populate the live read.

## Cross-asset implications (AS OF 2026-06-19 — SUPERSEDED, see the 2026-09-19 Live read)
- **Equities** — Moderate net exposure; tilt to **inflation-beneficiary cyclicals/value (energy, materials, financials)** over both long-duration growth *and* classic bond-proxy defensives (which lag in reflation with firm growth + expanding credit + an easing Fed). Underweight rate-sensitive housing/homebuilders. See [[Sector Analysis & Rotation]], [[Portfolio Management]].
- **Fixed Income** — Short-to-neutral duration; re-accelerating CPI + sticky Core PCE cap duration extension. Favor front-end/cash and TIPS over nominals (real 10Y ≈ +2.2%). Curve positive but re-flattening — watch for late-cycle re-inversion. See [[Yield Curve & Recession Signals]], [[Government Bond Yields]].
- **FX & Commodities** — Long real assets (energy, copper, precious metals; gold/silver positioning crowded long per [[Commitment of Traders (COT)]]). USD mixed-to-soft (Fed easing vs sticky inflation); respect a hawkish-surprise squeeze given low vol. See [[Cyclical Commodities]], [[USD & G10 FX]].

## Data provenance & caveats
- Live FRED via the user's registered key (`tools/build_cycle_dashboard.py`), except **ISM** (maintained `raw/2.3 Current Data`). Fetched 2026-06-19.
- **Section 4 FRED-derived:** Central Bank Net Liquidity = `WALCL − WDTGAL − RRPONTSYD`; Financial Conditions = `NFCI`/`ANFCI`; real-time pulse = `WEI`.
- **Awaiting / unavailable (free sources):** ISM **New Orders** sub-index and **Conference Board** Consumer Confidence (UMich proxy); plus Section 4's **shipping (BDI/SCFI)**, **card-spend & TSA throughput**, and **earnings-transcript mention tracker** — all proprietary/alt-data, off the free FRED pipeline. UMich/PCE/income carry a one-month release lag.
- Synthesis adversarially verified (3-lens panel: regime classifier, signal auditor, cross-asset adversary) — relabeled from "slowdown" to "reflation" (coincident not yet slowing), nominal prints haircut to real, defensive equity tilt revised toward inflation-beneficiary cyclicals.
- Internal hedge-fund monitor — macro/asset-class level, not investment advice.

## See also
- [[Macro Regime - Live (June 2026)]] (endo/exo lens) · [[Macro Regime Snapshot]] (historical)
- [[Leading Indicators]] · [[Coincident Indicators]] · [[The Global Macros Framework]]
- [[Yield Curve & Recession Signals]] · [[M2 Money Supply & Liquidity]] · [[Cyclical Commodities]] · [[Commitment of Traders (COT)]]
- [[Global Macro Brain]] · [[index]] · [[log]]
