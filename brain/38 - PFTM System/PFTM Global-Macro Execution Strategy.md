---
title: PFTM Global-Macro Execution Strategy
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "Executable 4-module PFTM playbook (Big-Four scorecard, FX divergence, Keltner/ATR trigger with alignment gate, 2xATR/1% risk); 2026-09-19: no FX trade (all four pairs RANGE), four commodity longs released, Gold waits."
tags: [global-macro, ptm, pftm, execution, scorecard, fx-divergence, keltner, atr, risk-management, dashboard, live]
data_vintage: "SNAPSHOT 2026-06-24 (FRED + Yahoo daily) — flipped by 2026-08-15; as of 2026-09-19 the FX bias (SHORT EUR/GBP) and the S&P spec short are back but un-triggered, and the commodity 'wait' has released; re-verified 2026-09-19 against ptmstrategy_latest.json (built 15:35, Yahoo closes through 18 Sep) + CFTC 2026-09-15"
sources: 1
updated: 2026-09-19
---

# PFTM Global-Macro Execution Strategy

> ### Worked examples re-verified — 2026-09-19 (current; supersedes the 2026-08-15 check below)
>
> The dashboard was rebuilt today. `PTM Strategy/ptmstrategy_latest.json` has `as_of` **2026-09-19** and was built at
> 15:35. Its prices are Yahoo daily closes through 18 Sep (the Dow's 51,682.64 is the 18 Sep close). The engine's regime
> line reads **Mildly Inflationary · Reflation / Overheating · risk NEUTRAL**. The three worked examples now stand as follows:
>
> | Example on page | Verified 2026-09-19 |
> |---|---|
> | **SHORT EUR / SHORT GBP**, "aligned daily downtrends" | **The bias is back, but the trigger is not.** Big-Four net: US **+2** (GDP −1, CPI +1, rates +1, employment +1), Eurozone **+1**, Japan **+1**, Australia **+1**, UK **0**. All four pairs now lean long USD: SHORT GBP (divergence −2), SHORT EUR and SHORT AUD (−1 each), and LONG USD/JPY (+1). All four daily trends read **RANGE**, so none passes the alignment gate. There is no FX trade, and the playbook says wait. EURUSD 1.1489 and GBPUSD 1.3394 sit below their 20d EMAs (1.1565 and 1.3488). The 2026-08-15 uptrends have faded but have not become downtrends. |
> | **S&P / NASDAQ specs "crowded short"** | **S&P specs are net short again, and NASDAQ specs are long.** The E-mini S&P net non-commercial position is **−100,461** (CFTC 2026-09-15; −24,425 on the week). That reverses the +11,280 long of 2026-08-11 and is a bigger short than the −37,592 of 2026-06-30. The COT engine (`Macro COT Trades/macrocot_latest.json`, built 15:36) ranks it at the 28th percentile and does not flag it as extreme. NASDAQ 100 E-mini is **+33,718 net long** (52nd percentile). The bias for all three indexes stays **NEUTRAL**, and the Dow's daily trend is DOWN. |
> | Gold/Silver/WTI/Copper LONG on macro but "technicals say wait" | **The gate has released three of the four, plus natural gas.** All five commodities are LONG on macro. WTI (CL=F front-month 100.30, 18 Sep close — not the $107 FRED spot of 15 Sep below), Copper (6.615), Silver (66.56) and Natural Gas (2.912) are in daily **UP** trends and aligned, so each is marked **✓ trade**. Gold (4,424.90) is in a RANGE, so it is marked **✗ wait**. |
>
> **Correlation:** the four executable longs cover two themes, not four separate trades. The global-growth theme is WTI +
> Copper + Natural Gas, led by WTI. For the real-rate theme, the executable leg is Silver, because the engine's lead leg,
> Gold, is itself on wait.
> **Input caveats in today's build:** the "real yield" of **0.47%** behind gold and silver is the US 3-month interbank rate
> (monthly OECD series `IR3TIB01USM156N`, 3.82%) minus August CPI y/y (3.35%). It is not the 10Y TIPS yield, which was
> 2.61% on 17 Sep. It sits just under the tool's **0.5%** cut-off for a gold LONG. The tool does not read the policy rate,
> so the Fed's 25bp hike to **3.75–4.00%** (effective 2026-09-17) is not an input. ISM is still the hard-coded May-2026
> **54.0**. The staleness guard zeroes four inputs: Japan CPI (last 2021-06), AU CPI (2025-01), UK CPI (2025-03) and
> Eurozone unemployment (2023-01). This tool still reads AU CPI from the FRED/OECD series, not the DBnomics re-source
> described in the Audit below.
> **Backdrop:** both major central banks tightened in the same week that the energy shock re-intensified. The Fed's first
> hike (to 3.75–4.00%, effective 17 Sep) and the ECB's second move (to 2.50%, effective 16 Sep) came as WTI rose to $107
> and Brent to $131 (FRED spot, 15 Sep), with August PPI at +9.85% y/y. Demand is firm, not fading: retail sales +1.24%
> m/m, payrolls +162k, claims 196k. Core CPI is still only +2.45% y/y. Its 3-month pace turned up to 1.97% from 1.64% but
> remains below 2%, while core PCE is 3.34% (Jul). The curve flattened (10Y-2Y +0.33 → +0.25). Markets absorbed the hike:
> credit had already retraced on 16 Sep (HY 2.70, CCC 10.76), and VIX fell to 15.4 on hike day.

> ### ⚠️ The worked examples below have all flipped — re-verified 2026-08-15
>
> The *method* on this page stands; the **illustrative positions do not**. Every one has reversed since 2026-06-24:
>
> | Example on page | Verified 2026-08-15 |
> |---|---|
> | **SHORT EUR / SHORT GBP**, "aligned daily downtrends" | **Both in uptrends.** EURUSD 1.1380 → 1.1573 (+1.70%), above a rising 20d EMA (1.1509); GBPUSD 1.3200 → 1.3536 (+2.54%), also above |
> | **S&P / NASDAQ specs "crowded short"** | **S&P half flipped sign.** E-mini S&P net non-commercial **+11,280 net LONG** (CFTC 2026-08-11), 91st pctile — was −37,592 on 2026-06-30 |
> | Gold/Silver/WTI/Copper LONG on macro but **"technicals say wait, they're pulling back"** | **All four broke out.** Gold 3990 → 4380 (+9.8%), Silver 58.05 → 64.99 (+12.0%), WTI 70.34 → 82.40 (+17.2%), Copper 5.943 → 6.600 (+11.1%) |
>
> The alignment gate that held the commodity book back is exactly what would have released it. Re-run the
> scorecard before quoting any position here.


The complete **Anton Kreil PFTM 4-module playbook** — from the user's `Global Macro Trading Strategy` skill file — made executable on live data. The execution layer on top of the [[PTM Global-Macro Dashboard (Endo + Exo)]] (folder 36). Built 2026-06-24. **Decision-support / education only — NOT investment advice.**

> **Top-down: score economies → trade the biggest fundamental divergence → enter only when the daily technical aligns → size for 1% risk with ATR stops and treat correlated pairs as one trade.**

## The four modules
1. **Big-Four scorecard** — US/EZ/UK/JP/AU scored **+1/0/−1** on GDP growth, CPI (inflation→hawkish→currency-supportive, per the skill file), short rates (higher = capital-attracting), and employment (falling unemployment = strong) → a **net economic-strength** score.
2. **Cross-asset matrix — FX, equity indexes AND commodities, all fully tradeable** (each with bias + technicals + ATR sizing + correlation): **FX divergence** (long strongest / short weakest economy; need real divergence, never +1 vs +1); **equity indexes** (S&P 500, NASDAQ 100, Dow — risk-on/off bias); **commodities** (Gold/Silver = real-rate sign; WTI/Copper = global-PMI demand + USD).
3. **Technical execution** — daily **ATR(14)**, **20-EMA**, **Keltner channels** (EMA ± 2·ATR), trend (HH/HL), and the entry **trigger** (breakout outside the Keltner / pullback to the mid) — with a **macro-alignment gate** ("fundamentals = what, technicals = when; only trade when aligned").
4. **Risk & sizing** — **2×ATR** stop, **1%** position sizing, and **correlation clustering** (long-USD pairs are one trade → keep only the largest-divergence pair).

## Current read (mid-2026)
- **Big-Four (net strength):** US **+1**, Japan **+1**, Australia **+1**, Eurozone **0**, UK **0** — modest, synchronized cycle.
- **FX:** **SHORT EUR** and **SHORT GBP** (= long USD), both with aligned daily downtrends; **USD/JPY and AUD/USD NEUTRAL** (no divergence).
- **Equity indexes (S&P/NASDAQ/Dow): NEUTRAL** (risk-on/off is mixed — marginal growth); note the COT shows S&P/NASDAQ specs *crowded short*.
- **Commodities: Gold/Silver/WTI/Copper all LONG on macro** (real yield −0.55% bullish gold; ISM > 50 industrial demand) — **but the daily technicals say "wait"** (they're pulling back), so the alignment gate holds them.
- **Correlation flags (across asset classes):** short-EUR + short-GBP = one *long-USD* trade; Gold + Silver = one *real-rate* trade; WTI + Copper = one *global-growth* trade → size each theme as ONE, lead with the highest-conviction leg.

## Outputs (`PTM Strategy/`)
- **`PTM Strategy Dashboard.html`** — light theme, Chart.js inlined: KPI strip, Big-Four scorecard heatmap + net-score bar, FX-divergence bar, FX + technical-trigger table, **equity-indexes table, commodities table**, and a **unified executable-trades table spanning FX + indexes + commodities** (stops / notional / correlation-theme), with cross-asset correlation warnings.
- **`PTM Strategy Note <date>.md`** + **`ptmstrategy_latest.json`**. Tools: `tools/ptm_strategy.py` · `ptm_strategy_report.py` · `build_ptm_strategy.py`.

## Audit
**Audited (lean, 11 agents, 7/7 confirmed) → SOUND_WITH_FIXES; all fixes applied.** Crucially, **every trade-direction sign was verified correct (no flipped trades)** — Big-Four directions, the FX divergence/alignment logic, and the ATR sizing (a 2-ATR move = exactly 1% of account) and correlation clustering all confirmed. Two **data-integrity bugs** were caught and fixed — exactly the high-stakes kind for a trade tool:
- **(L3-1, HIGH) stale foreign CPI:** the OECD-MEI CPI series are discontinued — **Japan CPI ends ~2021 (~5 years stale)**, UK ~2025; AU since **re-sourced CURRENT** via OECD/DBnomics (2026-Q1 = 4.05% YoY, fixed 2026-07-04) — yet Japan's CPI score had been driving the USD/JPY divergence. Added a **staleness guard**: any input older than 9 months is **flagged and scored 0** so stale data can never set a trade direction (the dashboard marks guarded cells). With it, USD/JPY correctly falls to **NEUTRAL** (the stale-data-manufactured divergence disappears).
- **(L3-2, HIGH) quarterly-YoY bug:** the YoY helper hard-coded a 12-step lag → a quarterly CPI was read as a 3-year change. Fixed with **frequency-aware** YoY + rate-series handling.
- **(L2-1, LOW)** the alignment gate marked zero-divergence (NEUTRAL) pairs as "aligned" → now **None** (undefined when there's no bias).

## Caveats
- US inputs current to Aug-2026 (CPI 3.35% y/y, U-3 4.1%); **free-FRED foreign CPI and EZ unemployment are lagged/discontinued** — today's build staleness-guards (scores 0) Japan CPI 2021-06, AU CPI 2025-01, UK CPI 2025-03 and Eurozone unemployment 2023-01; the DBnomics AU re-source noted in the Audit is not wired into this tool; ISM/PMI use web-sourced May-2026 readings; technicals are **daily** (the skill file's 4H entries are out of scope for a daily snapshot); position sizing is illustrative ($100k, 1%, 2×ATR). **Decision-support, not advice.**

## Related
[[PTM Global-Macro Dashboard (Endo + Exo)]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]] · [[Macro Regime Allocation Engine]] · [[Cross-System Synthesis — What Works]]
