---
title: "Indicator Register — Grant Handbook mapped to live series"
aliases: ["Indicator Register - Grant Handbook mapped to live series"]
category: indicators
type: reference
data_asof: 2026-08-15
summary: Every Grant Handbook indicator (22 US + 26 Canadian) mapped to a live series id with a coverage verdict — US 15/22 full, Canada 11/26 after the 2026-08-15 CA build; capacity utilization is IP double-counted (r +0.946).
tags: ["indicators", "register", "grant", "release-calendar", "coverage"]
updated: 2026-09-11
data_vintage: "catalog 2026-08-14 · book indicators from Grant Ch 11-12 · CU-vs-IP test re-measured on the 2026-09-11 catalog (re-sourced IP)"
sources: 3
---

# Indicator Register — Grant Handbook mapped to live series

Every indicator catalogued in **John Grant, _A Handbook of Economic Indicators_** (Ch 11 Canada, Ch 12 United States), mapped to the platform's live series. Grant organises by **release frequency**, and that order is preserved — it is the book's structural contribution: what arrives weekly, what monthly, what quarterly, and therefore what you can actually know at any moment.

Columns: the indicator as the book names it → the live series ID → coverage verdict. **Gaps are stated, not hidden.**

## United States (Ch 12) — 22 indicators

### Weekly

| Grant indicator | Live series | Coverage |
|---|---|---|
| Initial State Unemployment Insurance Claims | `USLEAD:CLAIMS` (+ `CLAIMS:CONT` continuing) | ✅ full, weekly to 2026-08 |

### Monthly

| Grant indicator | Live series | Coverage |
|---|---|---|
| Capacity Utilization (Industry Operating Rate) | `USLEAD:CAPU` | ✅ |
| Car Sales | `LEI:VEH` (total vehicle sales) | ✅ |
| Consumer Confidence Index (Conference Board) | `USCONF:AA`, `USCONF:RAW` (OECD composite) | ⚠️ **proxy** — the Conference Board index itself is licensed; OECD composite substituted |
| Consumer Credit (G19) | — | ❌ **no series** |
| Consumer Price Index | `US26:CPIAUCSL`, `US26:CPILFESL`, `INFL:CPIFOOD`, `INFL:CPIENER`, `LEI:RENTCPI` | ✅ headline, core + components |
| Durable Goods Orders | `DUR:TOTAL` + 8 components (`DUR:EXTRANS`, `EXDEF`, `MACH`, `COMP`, …) | ✅ richer than the book |
| Employment & Unemployment (Establishment) | `US26:NFP`, `PAYROLL:*` (10 sector splits), `LEI:AWH`, `LEI:AHE` | ✅ |
| Employment & Unemployment (Household Survey) | `USLEAD:UNEMP` | ✅ rate only — no participation/U-6 |
| Factory Orders | `DUR:TOTAL`, `LEI:NOCG`, `LEI:NOCAP` | ⚠️ **partial** — durable orders and LEI sub-aggregates, not the full factory-orders release |
| Federal Government Budget Balance | — | ❌ **no series** (`AU:GBAL`/`UK:DEFGDP` exist for those countries, not the US) |
| Help-Wanted Index | `LEI:HPW` (NY Fed labour-market tightness) | ⚠️ **substitute** — the Conference Board Help-Wanted Index is discontinued/licensed |
| Housing Starts | `HOUSING:STARTS`, `HOUSING:PERMITS`, `HOUSING:COMPL`, `US26:PermitsSA` | ✅ |
| Index of Industrial Production | `IPC:TOTAL` + 7 components (mfg, mining, utilities, business equipment, materials…) | ✅ |
| Index of Leading Indicators | `LEI:PROXY`, `LEI:PROXYXE` (desk composite from free components) | ⚠️ **reproduction** — the Conference Board LEI is licensed; see [[Conference Board LEI & Leading-Lagging Map]] |
| International Trade | `BOP:US` (+ 6 other countries) | ✅ balance only — no detailed import/export breakdown |
| Money Supply | `US26:M2` | ✅ M2 — **no M1, no monetary base, no reserves** |
| Personal Income | `LEI:RINC` (real personal income ex-transfers) | ⚠️ **partial** — the LEI component, not the full personal-income release |
| Producer Price Index | `US26:PPIFGS`, `US26:PPILFE`, `INFL:PPIACO` | ✅ |
| Purchasing Managers' Survey (ISM) | `US26:ISM`, `ISMC:*` (5 components), `US26:NMI`, `NMIC:*` (6) | ✅ far richer than the book |
| Retail Sales | `RETAIL:TOTAL` + 9 category splits, `USLEAD:RETX` | ✅ richer than the book |

### Quarterly

| Grant indicator | Live series | Coverage |
|---|---|---|
| Employment Cost Index | `LEI:ECI`, `LEI:ECIQ` | ✅ |
| National Income and Product Accounts | `US26:GDPPCT`, `GDPC:*` (GDP, PCE, investment, exports, imports, government) | ✅ |

**US scorecard: 15 of 22 fully covered, 5 partial/proxy, 2 absent.**

## Canada (Ch 11) — 26 indicators

The handbook is **Canada-first** — its longest chapter, and this platform originally carried two Canadian series. **On 2026-08-15 a live `CA` group was built to close the gap** (15 series, `tools/canada_data.py`), taking coverage from 1/26 to 11/26.

**Why not FRED:** FRED's Canadian series are OECD-sourced and largely **frozen** — CPI ends 2025-03, industrial production 2024-02, producer prices 2022-12, consumer confidence 2017-12 (checked 2026-08-15). Only 5 of 20 candidates were current. The live routes are the two official free APIs, both verified reachable from this environment:

- **Bank of Canada Valet** — policy rate, benchmark yields, USD/CAD, the full CPI family including the three BoC core measures. Daily series carry 2,400–6,400 observations.
- **Statistics Canada WDS** — Labour Force Survey, monthly real GDP, building permits, manufacturing sales.

Series that came back stale were dropped rather than shipped: StatCan housing starts (`v735319`, ends **2007**) and retail trade (`v52367097`, ends **2022**) are both excluded, which is why those two rows below still read ❌.

| Grant indicator (frequency) | Live series | Coverage |
|---|---|---|
| Bank of Canada Weekly Financial Statistics — rates, FX, monetary aggregates (weekly) | `CA:POLICY`, `CA:USDCAD`, `CA:G2Y`, `CA:G10Y`, `CA:GLONG` | ✅ the rate/FX core, **daily** rather than weekly. The **Monetary Conditions Index** itself was discontinued by the BoC and is absent |
| Average Hourly / Weekly Earnings (monthly) | — | ❌ |
| Building Permits (monthly) | `CA:PERMITS` | ✅ |
| Car Sales (monthly) | — | ❌ |
| Consumer Price Index (monthly) | `CA:CPI`, `CA:CPIYOY`, **`CA:CPITRIM`, `CA:CPIMED`, `CA:CPICOMMON`** | ✅ richer than the book — carries the three BoC core measures the handbook predates |
| Durable Goods Orders (monthly) | — | ❌ |
| Employment & Unemployment — Labour Force Survey (monthly) | `CA:UNE`, `CA:EMP` | ✅ |
| Federal Government Fiscal Position (monthly) | — | ❌ |
| Help-Wanted Index (monthly) | — | ❌ (discontinued in Canada as in the US) |
| Housing Starts (monthly) | — | ❌ StatCan `v735319` ends **2007** — excluded rather than shipped stale |
| Index of Leading Indicators (monthly) | — | ❌ (StatCan discontinued its composite leading index in 2012) |
| Industrial Product Price Index (monthly) | — | ❌ |
| Industrial Production (monthly) | `CA:MFGSALES` (manufacturing sales) | ⚠️ **partial proxy** — sales, not production |
| Merchandise Trade (monthly) | `BOP:CA` | ✅ |
| Money and Credit Aggregates (monthly) | — | ❌ |
| Raw Materials Price Index (monthly) | — | ❌ |
| Real GDP at Factor Cost (monthly) | **`CA:GDPM`** | ✅ monthly real GDP at basic prices — Grant's own headline Canadian series |
| Retail Trade (monthly) | — | ❌ StatCan `v52367097` ends **2022** — excluded |
| Balance of Payments (quarterly) | `BOP:CA` (trade balance only) | ⚠️ partial |
| Business Conditions Survey (quarterly) | — | ❌ |
| Capacity Utilization Rate (quarterly) | — | ❌ |
| Corporate Profits in the NIEA (quarterly) | — | ❌ |
| Financial Flow Accounts (quarterly) | — | ❌ |
| National Balance Sheet Accounts (quarterly) | — | ❌ |
| Quarterly Financial Statistics for Enterprises (quarterly) | — | ❌ |
| Environmental Indicators (annual) | — | ❌ |
| *(not in the book, but held here)* Manufacturing PMI | `PMI:CA` | ✅ |

**Canada scorecard: 11 of 26 covered (was 1), 2 partial, 13 absent.** What remains missing is genuinely missing: three of Grant's indicators were **discontinued by the agencies themselves** (Monetary Conditions Index, the StatCan composite leading index, the Help-Wanted Index), two are published but frozen in the free feeds (housing starts, retail trade), and the rest — earnings, car sales, IPPI/RMPI, the quarterly enterprise and balance-sheet accounts — would each need a specific StatCan vector that has not been located and verified.

Current Canadian read (2026-08): policy rate **2.25%**, 10y **3.62%**, unemployment **6.4%**, CPI **+2.8% YoY** with all three BoC core measures **below target** (trim 1.8, median 1.9, common 2.6).

## Two of Grant's claims, tested on this platform's data

The register is more useful if the book's analytical assertions are checked rather than repeated.

### "Capacity utilization contains no independent monthly information" — **CONFIRMED**

Grant: *"the only real monthly information is in the production data; the utilization rate is simply calculated from it"* — because short-run capital stock is essentially fixed.

Measured, monthly changes, **653 months**:

| Pair | r |
|---|---|
| Δ Capacity Utilization vs Δ IP total | **+0.946** |
| Δ Capacity Utilization vs Δ IP manufacturing | +0.898 |

*(Re-measured 2026-09-11 on the re-sourced IP series over the same 653 months: +0.946 total, +0.898 manufacturing.
The first readings, +0.907 and +0.869, used workbook 12's spliced IP: a fake −4.7% month at 2017-09 plus
older-vintage history, which understated the link. The verdict holds and is stronger. See* Data integrity *in
[[2026 Workbook Explorer]].)*

At +0.95 the two are the same signal. **Watching `USLEAD:CAPU` alongside `IPC:TOTAL` is double-counting** — it adds a second vote to a view already expressed. Treat CU as a level/pressure gauge for inflation framing, never as independent confirmation of an industrial-activity call.

### "Initial claims are not a good predictor of employment changes" — **SUPPORTED, once one month is removed**

Grant is explicitly sceptical: changes in initial claims are *"not strongly correlated with changes in unemployment or employment in the same month… not really a good predictor for this purpose."*

| Test | All months | Excluding 2020 |
|---|---|---|
| Δclaims vs Δunemployment, same month | −0.21 | **+0.16** |
| Δclaims vs Δunemployment, **1 month ahead** | **+0.88** | **+0.25** |
| Δclaims vs Δunemployment, 3 months ahead | −0.09 | — |

The full-sample **+0.88 is not a relationship — it is a single observation.** March 2020: claims +5,731,000 and unemployment +10.4pp the following month. That one pair, roughly fifty standard deviations out on both axes, dominates all 712 months. Strip 2020 and the honest number is **+0.25** — modest, and squarely consistent with Grant's scepticism.

This is the register's own cautionary tale: a spectacular correlation that appears at exactly one lag and nowhere else is nearly always one crisis, not a signal.

## How to use this register

Grant's sequencing logic (Ch 10) is that indicators answer different questions at different lags. In this platform's terms:

- **Weekly** (`USLEAD:CLAIMS`, `LEI:LMSI`, `GLOB:VIX`, `COT:*`) — the only genuinely current reads; everything else is history.
- **Monthly** — the workhorses. Surveys (ISM, UMich, NFIB) arrive first and are never revised; hard data (IP, retail, payrolls) arrive later and *are* revised.
- **Quarterly** (`GDPC:*`, `LEI:ECI`) — confirmation, not news. By the time GDP prints, the monthly series have already told the story.

Related: [[Leading Indicators]] · [[Coincident Indicators]] · [[Lagging Indicators]] · [[Conference Board LEI & Leading-Lagging Map]] · [[2026 Workbook Explorer]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
