---
title: FX Endogenous-Exogenous Framework
category: fx
type: domain
data_asof: 2017-08
summary: "The two-stage FX method: score domestic drivers into an endogenous total, relative drivers into an exogenous total, then resolve into a long/short bias (worked AUD/USD resolves short)."
tags: [global-macro, fx, endogenous, exogenous, scoring, balance-of-payments, aud-usd]
data_vintage: "1960–2017 underlying series; US endo scorecard ~2017, AUD/USD exo scorecard ~Q1 2015"
sources: 7
updated: 2026-07-25
---

# FX Endogenous-Exogenous Framework

**What it is & why it matters** — This is the heart of the Global Macros FX strategy: a two-stage, scorecard-driven method for forming a directional bias on any currency pair. First each country is scored *endogenously* — its own domestic macro drivers (surveys, money supply, rates, inflation, employment, sovereign balance sheet) are each rated as Increasing or Decreasing the inflationary/growth impulse, and summed into a single endogenous score and "state". Then the two countries are compared *exogenously* — relative GDP, relative balance of payments, interest-rate differentials/carry, and relative stock-market wealth are scored on a cross-country basis to produce an exo score. The endo and exo scores combine into a fundamental predisposition (long/short bias) for the pair. The whole point, per the strategy's own ReadME, is to "quantify and classify data through historical quantitative analysis" so that the trade bias is systematic and stratified rather than left to "personal and subjective economic interpretation."

## Key datasets & files
| File | What's in it | Date range | Notable charts |
|---|---|---|---|
| `USA_Endogenous_Driver_Analysis.xlsx` | The full US endo scorecard ("US Endo' Score") plus one driver sheet each: ISM, NMI, UMCSI, PermitsSA, M2, IR%, CPIAUCSL/CPILFESL, PPIFGS/PPILFE, NFP, Govt, T10%, CBBS; Cycles (recession dating); Sources | Series 1939–2017; scorecard ~2017 vintage | ISM PMI vs GDP, M2 vs GDP YoY, Effective Fed Funds vs GDP, Debt/GDP, CB balance sheet % GDP |
| `Exogenous_AUD_USD.xls` | The AUD/USD exo scorecard ("AUD_USD Exo' Score") + Relative_GDP, BOPs_US/AUS/Relative, Trade_Analysis, TA1_IronOre, "IR Diffs & Carry", "Stock Returns" | GDP 1974–2017; BOP reserves 1960–; iron ore & carry 2006–Feb 2015 | Iron ore vs AUDUSD, IR-differential carry rollover, relative GDP growth |
| `Endo_Exo_Analysis_USD_AUD.xlsx` | The combiner sheet ("AUDUSD_Endo_Exo") — pulls US endo, AUS endo, both exo scores and resolves them into a USD/AUD and AUD/USD total bias with interpretation notes | ~2015–2017 | Scorecard summary block |
| `Balance of Payment/Balance_of_Payments_US.xls` | BEA U.S. International Transactions (current account, financial account, reserves) | 1960–2013 annual + quarterly SA/NSA | (data tables) |
| `Balance of Payment/Balance_of_Payments_AUS.xlsx` | ABS Australian balance of payments (Index, Data1) | to ~2014 | (data tables) |
| `Updated Market Data/Endogenous_Driver_Analysis.xlsx` | An updated/refreshed endo workbook (file is corrupted in this archive — `BadZipFile`; superseded by the 2017 USA workbook) | — | — |
| `AUTOMATED ENDO TEMPLATE/ReadME!!! .docx` (+ videos) | Author's explanation of the automated endo/exo template and "Exo Combined" tool; methodology rationale | — | — |

## Charts & key trends

### Endogenous scoring — how each US driver is rated (scorecard ~2017)
Each driver gets a **Score I/D** in the range −10…+10 (the "G" column shows the ±10 scale; "+" = inflationary/growth-positive, "−" = deflationary). Drivers are grouped, sub-totalled, and rolled up into one number on a sliding scale of **−150 to +160** (full scale 310). The US scorecard as captured reads **+36 = "Inflationary overall"**, with the note that "most indicators outside CA [central bank] action are normal to deflationary."

| Group | Driver (code) | Rate captured | Score I/D | State note |
|---|---|---|---|---|
| Leading surveys | ISM Manufacturing | 58.8 | +8 | Growing/faster, GDP 3–4% |
| | NMI Services | 55.3 | +5 | Growing slower, possible Apr-17 peak |
| | UMCSI consumer sentiment | 96.8 | −5 | Highly bullish but slowing, Jan-17 peak? |
| | Building Permits | 1,230k | +3 | Sideways since 2013 |
| **Leading sub-total** | | | **+11** (of ±40) | Mild inflation, GDP 2–3%; deflationary threats from peaked surveys |
| Money supply | M2 (weekly % chg) | 2.89% | 0 | Normal M2 growth ≈ GDP 2%; 2× 30%+ prints = crisis correlation |
| Interest rates | Fed benchmark | 0.87% | 0 | Historically low + anomaly, ≈3% GDP |
| Inflation | CPI all-items | 0.40% m/m | +4 | Inflationary (oil) |
| | CPI core | 0.14% | 0 | Stable 12m |
| | PPI all | 0.46% | +2 | Inflationary (oil) |
| | PPI core | 0.12% | +4 | Half normal rate, in range |
| **Inflation sub-total** | | | **+10** (of ±40) | Oil-driven deflation in all-items; Fed acting via M2 crisis prints |
| Employment | NFP (12m rolling %) | 20.1% | +4 | Normal; possible jobs-growth peak |
| Balance sheets / sovereign | Govt Debt/GDP | 102.5% | +10 | 100%+ historical default zone, no choice but to continue |
| | Surplus/Deficit % GDP | −2.74% | +3 | Deficit clawed back, still inflationary |
| | Interest/GDP | 1.29% | −5 | Mildly deflationary, manageable |
| | Liquidity (cover) | 13.2 | +7 | Mildly inflationary |
| | US 10y Treasury | 2.14% | +7 | Absolute level very inflationary |
| | CB balance sheet % GDP | 25.35% | +3 | Mild inflation, more room |
| **Sovereign/CA sub-total** | | | **+25** (of ±50) | CA action very inflationary; Fed sponsoring govt debt via low rates + QE |
| **TOTAL US ENDO** | | | **+36** (scale −150…+160) | **Inflationary overall** |

The scorecard pairs the raw **State** (Growing/Faster, Sideways, etc.) with a forward **Comment** that maps the reading to expected GDP and Fed action — e.g. CPI 0.40% "predicts Fed action." The `Cycles` sheet anchors interpretation in the historical recession record: 10 US GDP contractions 1953–2009 averaging **11.1 months** long (longest 18m in 2007–09), used to gauge where in the cycle the indicators sit.

### Exogenous scoring — the cross-country (relative) layer (AUD/USD scorecard ~Q1 2015)
The exo scorecard scores **four relative drivers**, each on a ±10 scale, summed on a **−40 to +40** scale (full scale 80). The AUD/USD exo card reads **−14** (deflationary for AUD/USD → short-AUD bias):

| Exo driver | Score (±10) | Source basis |
|---|---|---|
| Relative GDP growth (US vs AUS) | −2 | IMF/World Bank GDP series |
| Relative balance of payments | −6 | BEA (US) vs ABS (AUS) BOP |
| Interest-rate differentials & carry | −4 | Fed Funds vs RBA interbank |
| Stock-market returns / relative wealth | −2 | AUDUSD vs ^AXJO returns |
| **TOTAL AUD/USD EXO** | **−14** (scale −40…+40) | Net deflationary for AUD |

Supporting exo data:
- **Relative GDP** (`Relative_GDP`, 1974–2017): captures both countries' nominal GDP and YoY growth and the growth *differential*. By 2017 both grew ~2.2%, with AUD/USD having fallen from above parity (1.0424 in 2014) to **0.7848** — a large relative-wealth/terms-of-trade adjustment.
- **Trade analysis** (`Trade_Analysis`): Australia's export mix is **iron ore 22%, coal 18%, pet gas 5.5%, gold 5.4%, crude 4.5%**; top export markets China 29%, Japan 20%, South Korea 8.4%. This is why commodity demand (especially Chinese) is the dominant AUD exogenous driver.
- **Iron ore** (`TA1_IronOre`, Feb 2006–Feb 2015): iron ore spot **peaked at $197.12 in April 2008**, then collapsed to **$68 by Feb 2015**; AUDUSD tracked it, falling from ~0.88 (early-2015) toward the high-0.70s. Iron ore is treated as a leading proxy for the AUD.
- **IR differentials & carry** (`IR Diffs & Carry`, May 1976–Feb 2015): models the daily rollover on a $100k synthetic AUD/USD carry position. The RBA–Fed spread compressed to ~**2.17%** by Feb 2015 (RBA 2.275% vs Fed Funds ~0.11%) from much wider 1970s–80s levels — eroding the AUD carry advantage.
- **Relative BOP** (`BOPs_Relative`, 1960–): tracks year-on-year change in US vs Australian foreign reserves alongside AUD/USD, the FX expression of the balance-of-payments differential.

### Combining endo + exo into a bias (`AUDUSD_Endo_Exo`)
The combiner does **not** simply add scorecards, because deflation in Australia is *bullish* USD/AUD but *bearish* AUD/USD. As captured:
- US endo **+36** (inflationary, absolute USD purchasing-power loss) → **short USD** on an absolute basis; AUS endo **0**.
- Exo USD/AUD **−14** / AUD/USD **−14**.
- **Total USD/AUD score +22 (long-USD bias); Total AUD/USD −14 (short-AUD bias).**

The interpretation note states the resolution precisely: *"On an absolute basis the USD is losing its purchasing power. On a relative basis it is gaining purchasing power against the AUD because the AUD is losing more of its purchasing power than the USD."* Net fundamental predisposition: **short AUD/USD**. The notes also flag the dynamic risk — extreme AUD deflation invites aggressive RBA/CA easing, so AUD/USD (a leading indicator itself) "may have already moved," and if USD rises too far it becomes a deflationary threat to the US that the Fed may "manage lower." This is the "currency wars" framing: importing inflation via a weak currency.

## How it's used in the strategy
1. **Score each country's endo** independently (the −150…+160 card), tagging an inflation/growth **state**. A strongly positive score = absolute currency-debasement / inflationary regime; deeply negative = deflationary.
2. **Score the pair's exo** (−40…+40) from the four relative drivers — relative growth, relative BOP, rate-differential/carry, relative wealth.
3. **Resolve to a directional bias** via the combiner logic: absolute endo gives the base-currency view; the relative (exo) overlay flips the sign appropriately for the quote currency, yielding a **long/short fundamental predisposition** on the pair (here: short AUD/USD).
4. **Cross-check with leading/dynamic signals** — the dominant export commodity (iron ore for AUD) and the carry rollover act as faster-moving confirmations; because FX is itself a leading indicator, the trader checks whether the move has already happened before sizing.
5. **Feed the bias into idea generation and risk** — the fundamental predisposition sets *direction*; pair selection, sizing and stops then draw on [[Average True Range (ATR)]], [[Commitment of Traders (COT)]] positioning, and [[Risk Management]]. The author's "automated endo/exo template" mechanises steps 1–2 so any pair can be scored quickly.

**Live counterparts:** the two live sibling scorecards in this folder — [[Australia Endogenous Driver Analysis (July 2026)]] (AU **+34** of ±130, 13 drivers) and [[UK Endogenous Driver Analysis (July 2026)]] (UK **+29** of ±150, 15 drivers) — plus [[Endo-Exo Toolkit & Workflow]] (the workbook/variant registry) and [[2026 Workbook Explorer]] for the live cards: US endo **+36** of −150…+160 (17 drivers) and the **AUD/USD exogenous −4.0 of ±40** (low conviction), asof 2026-07-24. Cross-country z-scored reads sit in [[Cross-Country Endo & Divergence Backtest]].

## See also
- [[The Global Macros Framework]]
- [[Endo-Exo Toolkit & Workflow]]
- [[Trade Idea Generation Process]]
- [[USD & G10 FX]]
- [[GDP & Growth]]
- [[Leading Indicators]]
- [[M2 Money Supply & Liquidity]]
- [[Government Bond Yields]]
- [[Cyclical Commodities]]
- [[Commitment of Traders (COT)]]
- [[Macro Regime Snapshot]]
- [[Risk Management]]
- [[Glossary]]
