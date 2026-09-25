# UK Endogenous Driver Analysis

A UK macroeconomic scorecard mirroring the **US Endogenous Driver Analysis**
file's logic and layout, populated with live UK data from ONS / FRED / Bank of
England and wired with live formulas so the overall SCORE auto-calculates.

## Files

| File | Purpose |
|---|---|
| `UK_Endogenous_Driver_Analysis.xlsx` | The workbook (21 sheets) — open this |
| `refresh_uk_data.py` | Re-pull all live series from ONS/FRED → `uk_data_cache.json` |
| `build_uk_workbook.py` | (Re)build the workbook from the cache |
| `uk_data_cache.json` | Cached raw series (resume/robustness) |

## Refresh flow (mirrors the US file)

```
refresh_uk_data.py   →   uk_data_cache.json   →   build_uk_workbook.py   →   .xlsx
(ONS + FRED fetch)        (cached series)         (dashboard + formulas)     (live SCORE)
```

```bash
py refresh_uk_data.py      # fetch latest UK data (resumes from cache)
py build_uk_workbook.py    # rebuild the workbook
```

## Layout — `UK Endo' Score` dashboard

Same structure as the US file (and the reference Google Sheet):

| Rows | Group | Drivers |
|---|---|---|
| 5–8 | Leading Indicators | Manufacturing PMI, Services PMI, Consumer Confidence, Housing Approvals |
| 12 | Money Supply | M4 Broad Money |
| 14 | Interest Rates | Bank of England Bank Rate |
| 16–19 | Inflation | CPI, Core CPI, PPI Output, PPI Input |
| 23 | Employment | Unemployment Rate |
| 26–31 | Balance Sheets | Debt/GDP, Deficit, Interest/GDP, Liquidity, 10Y Gilt, BoE Balance Sheet |
| 10/21/33 | — | Subtotals |
| 36–39 | — | High / Low / Full / Half scale |
| H38 | — | **OVERALL SCORE** (live) |

- **E (Rate)** = `LOOKUP(9.9E+307, <datasheet>!col)` — latest value
- **F (Score)** = `LOOKUP(rate, threshold_table, score_table)` — embedded ascending helper tables on each data sheet

## Data sources (all free, no API key)

| Driver | Source | Series | Frequency | Status |
|---|---|---|---|---|
| CPI / Core CPI | ONS | D7G7 / DKO8 (mm23) | Monthly | Live |
| PPI Output / Input | ONS | GB7S / GHIK (ppi) | Monthly | Live |
| Unemployment | ONS | MGSX (lms) | Monthly | Live |
| Earnings | ONS | KAC2 (emp) | Monthly | Live |
| Debt/GDP | ONS | A3PW (pusf, Maastricht) | Monthly | Live |
| PSND / Deficit | ONS | HF6X / J5II (pusf) | Monthly | Live |
| 10Y Gilt | FRED | IRLTLT01GBM156N | Monthly | Live* |
| Bank Rate | FRED | IRSTCI01GBM156N | Monthly | Live* |
| Consumer Confidence | FRED | CSCICP02GBM460S | Monthly | Live* |
| M4 Broad Money | FRED | MANMM101GBM189S | Monthly | Live* |
| Mfg / Services PMI | S&P Global / CIPS | — | Monthly | **Manual** |
| Housing Approvals | DLUHC | — | Monthly | **Manual** |
| Interest/GDP, Liquidity | Derived | — | — | **Manual** |
| BoE Balance Sheet | Bank of England | APEXLPMA | Weekly | **Manual** |

\* FRED was unreachable at initial build time, so these 4 series were seeded
with verified latest values; re-running `refresh_uk_data.py` (when FRED is
reachable) backfills full history automatically.

**Manual** cells carry a clear `MANUAL — paste current value` note in cell E1;
their score formulas are still wired, so pasting a value immediately computes
the score.

## Notes

- Scoring tables are UK-tuned and anchored to the reference UK values
  (e.g. CPI 2.8% → score 3, Debt/GDP 100% → 10, Bank Rate ~3.7% → 2).
- The **OVERALL SCORE** is a live formula — it recalculates on every data
  refresh and on open in Excel.
- `Cycles` sheet lists UK recessions; `Sources` sheet documents every series.
