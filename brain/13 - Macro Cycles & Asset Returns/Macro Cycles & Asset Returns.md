---
title: Macro Cycles & Asset Returns
category: cycles
type: dashboard-page
data_asof: 2026-09-19
summary: "Folder page for the FRED+Yahoo notebook recreating the Macrosynergy cyclical-strength → asset-returns study. 2026-09-19 re-run: pooling 6 countries lifts equity t from −0.44 (US) to −2.81, but the book earns Sharpe 0.06."
tags: [global-macro, macro-cycle, asset-returns, panel-regression, notebook, jpmaqs]
data_vintage: "FRED+Yahoo pull of the 2026-09-19 notebook re-execution: US monthly 1998→2026-08, 6-country panel 2001-01→2026-08 (see Build status 2026-09-19). The 2026-07-03 execution's figures are kept below as a record."
sources: 1
updated: 2026-09-19
---

# Macro Cycles & Asset Returns — folder 13

**What it is** — A runnable notebook (`.ipynb` + rendered `.html`) recreating the Macrosynergy/JPMaQS *cyclical-strength → asset-class returns* research on free FRED+Yahoo data: macro-cycle factors (excess growth / inflation / labour) → composite z-score signal → value-checks (panel regression, hit-rate, naive & cross-sectional PnL) for equity/bonds/FX/commodity. `tools/build_macro_cycles_notebook.py`.

**Key finding** (digits from the 2026-07-03 execution; the 2026-09-19 re-execution moves them slightly and leaves
the verdict unchanged, see *Build status — 2026-09-19*): a **6-country panel** (US/DE/UK/JP/CA/AU) demonstrates the breadth effect — pooling lifts the equity
signal from insignificant (**US-only t = −0.43**) to significant (**panel t = −2.77**), and the negative
(counter-cyclical) sign holds in every country. But breadth buys *statistical significance*, not *returns*: the
cross-sectional relative-value equity book that makes the panel tradable earns a Sharpe of **0.08** (0.3% annualised
over 305 months), and every single-country naive PnL is flat-to-negative. **This remains a null result in P&L terms.**

## Build status — 2026-09-19 (notebook re-executed; current)
Today's run of `tools/build_macro_cycles_notebook.py` **succeeded** — run under **Python 3.12**
(`C:\Users\nikhi\AppData\Local\Programs\Python\Python312\python.exe`, kernel 3.12.10), which has `nbformat` 5.10.4 +
`nbconvert`; the project's 3.14 interpreter still lacks `nbformat`, so the 2026-09-16 failure below recurs if the
builder is run with it. Both deliverables were rewritten at **2026-09-19 15:58** (cells executed 08:58:15–08:58:50
UTC) on a fresh FRED+Yahoo pull, so the US macro block now runs **1998 → 2026-08-31** and the 6-country panel
**2001-01-31 → 2026-08-31** (**1,848** country-months, all six countries kept). This supersedes the 2026-09-16 status
below, when the builder failed on `nbformat` and the data stopped at 2026-05-31. The 2026-07-03 execution's figures
further down are kept as a record and have not been rewritten — the section headed *What the current render actually
reports* describes the 2026-07-03 render, not today's. The Business Cycle Dashboard's `build_cycle_*` builders were
deliberately not run today because they hardcode a regime label. None of them writes into folder 13.

Same construction as before. Return samples are now **343 months** for equity / 10Y UST / WTI and **331** for EUR/USD.

| Figure | 2026-07-03 execution | 2026-09-19 re-execution |
|---|---|---|
| US equity t (single-country value-check) | −0.31 | −0.30 |
| US bonds / EUR/USD / WTI t | −0.47 / −1.19 / −1.10 | −0.51 / −1.18 / −1.05 |
| US naive PnL Sharpe (eq / bonds / FX / WTI) | −0.31 / 0.01 / −0.11 / −0.16 | −0.31 / 0.02 / −0.11 / −0.17 |
| Panel equity t (n) | **−2.77** (1,780) | **−2.81** (1,798) |
| Panel bonds 10Y t (n) | −2.92 (1,830) | −2.93 (1,848) |
| Panel FX vs USD t (n) | −1.73 (1,525) | −1.75 (1,540) |
| US-only equity t in the panel test (n) | **−0.43** (305) | **−0.44** (308) |
| Cross-sectional relative-value equity | Sharpe **0.08**, 0.3% ann., 305 months | Sharpe **0.06**, 0.1% ann., 308 months |
| Latest US Cyclical Strength z | 0.77 (2026-05-31) | 0.16 (2026-08-31, G factor only) |

**Verdict unchanged.** The breadth effect reproduces on the longer sample: pooled t is significant, single-country t
is not, and the per-country correlation is still negative in all six markets. The P&L is still null, and the
cross-sectional Sharpe slipped from 0.08 to 0.06. Per the note below, the re-run is not an edge.

**Regime read on this vintage.** The 0.16 print for 2026-08-31 is a one-factor reading: only G (+0.16) has an August
value. I is blank because core PCE has no August print yet, and L is also blank for August on this pull, so this is
not a regime turn. The last month with
all three factors is **2026-07-31: G +0.09, I +1.24, L +0.14, CS +0.49**. That is still the mildly reflationary,
late-cycle posture, and excess inflation drives it: the I factor is the point-in-time z-score of core PCE y/y minus
2%, and core PCE was +3.34% y/y in July. The notebook's macro data ends before September's policy moves, so none of
them is in this read. Both major central banks tightened as the energy shock re-intensified: the Fed made its first
hike, to 3.75-4.00% (effective 17 Sep), and the ECB moved to 2.50% (effective 16 Sep), as WTI rose to $107 and Brent
to $131 (15 Sep).

## Build status — 2026-09-16 (notebook NOT rebuilt)
Today's data-layer re-run did **not** refresh this folder. `tools/build_macro_cycles_notebook.py` **failed** with
`ModuleNotFoundError: nbformat` (the package is not installed; installing it needs the user's go-ahead), so the two
deliverables below are byte-unchanged since their **2026-07-03 17:37** execution and their macro data still stops at
**2026-05-31**. `data_asof` is therefore held at **2026-07-03** — the figures on this page were *read* today out of the
shipped `.ipynb`'s stored cell outputs, but nothing was re-pulled from FRED or Yahoo.

Do not confuse this builder with the three similarly-named `build_cycle_*` tools, which serve the **Business Cycle
Dashboard**, not this notebook: `build_cycle_dashboard.py` (prints the live Leading/Coincident/Lagging block) and
`build_cycle_html.py` (→ `Monthly Report/Business Cycle Dashboard.html`) both **succeeded** today, while
`build_cycle_exports.py` (→ `10 - Global Macro Dashboard/` xlsx+docx) **failed** on an `IndexError` raised when the
NFCI series came back empty inside the builder, even though FRED serves it. None of the three writes into folder 13.

## What the current render actually reports (2026-07-03 execution, figures read 2026-09-16)
Signal = the point-in-time expanding z-score composite **CS = mean(G growth, I excess inflation, L labour)**, lagged
one month against the next month's return. Return samples: **341 months** for equity / 10Y UST / WTI, **329** for
EUR/USD.

**Single country (US) — weak and insignificant, exactly as the conclusion says:**

| Asset | corr | β | t-stat | hit % | signal dir | PnL Sharpe | PnL CAGR % |
|---|---|---|---|---|---|---|---|
| Equity (S&P 500) | −0.018 | −0.081 | −0.31 | 55.1 | counter-cyclical | −0.31 | −5.6 |
| Bonds (10Y UST) | −0.028 | −0.060 | −0.47 | 50.3 | counter-cyclical | 0.01 | −0.2 |
| FX (EUR/USD) | −0.070 | −0.190 | −1.19 | 52.0 | counter-cyclical | −0.11 | −1.4 |
| Commodity (WTI) | −0.064 | −0.755 | −1.10 | 52.0 | counter-cyclical | −0.16 | −13.1 |

**Pooled 6-country panel** — 1,830 country-months, 2001-01-31 → 2026-05-31, HC1 robust errors:

| Target | Sample | n | corr | t-stat | hit % |
|---|---|---|---|---|---|
| Equity | Panel (6 countries) | 1,780 | −0.073 | **−2.77** | 52.1 |
| Bonds 10Y | Panel (6 countries) | 1,830 | −0.082 | **−2.92** | 51.6 |
| FX vs USD | Panel (6 countries) | 1,525 | −0.048 | −1.73 | 49.0 |
| Equity | US only | 305 | −0.030 | −0.43 | 54.8 |
| Bonds 10Y | US only | 305 | −0.067 | −0.90 | 51.5 |

**Cross-sectional relative-value equity** (each month de-mean CS across the six markets, long low-CS / short high-CS,
gross 1): **Sharpe 0.08, 0.3% annualised over 305 months** — significant t-stats, no tradable edge. The regime read at
that build: latest US Cyclical Strength **z = 0.77 (2026-05-31)**; last month with all three factors present was
2026-04-30 (G +0.15, I +1.23, L +0.08, CS +0.49) — a mildly reflationary, late-cycle posture on that vintage.

*The single-country null and the near-zero cross-sectional Sharpe are the notebook's honest findings and are recorded
here verbatim; they are not to be upgraded into an "edge" on a later re-run without a fresh audit.*

## Files in this folder
- `Macroeconomic Cycles and Asset Class Returns.html` — the rendered notebook (864 KB, 2026-09-19 15:58; supersedes the 862 KB 2026-07-03 17:37 build)
- `Macroeconomic Cycles and Asset Class Returns.ipynb` — the runnable source (520 KB, 2026-09-19 15:58; supersedes the 518 KB 2026-07-03 17:37 build)

## Related
[[the-dv01-both-legs-flattener-bug]] (the construction-bug lesson that shaped how later curve-timing systems in [[LangAlpha Strategy System|the Strategy Lab]] were built and audited) · [[00 - GMD Overview & Structural Edge|Global Macro Database]] · [[Global Macro Brain]]
