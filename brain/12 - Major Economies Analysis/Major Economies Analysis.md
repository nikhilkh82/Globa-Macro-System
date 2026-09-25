---
title: Major Economies Analysis
category: country
type: dashboard-page
data_asof: 2026-09-19
summary: "Comparative US/EZ/UK/JP/CA/AU/CN macro dashboard + Word report (CPI, rates, 10Y, unemployment, endo/carry-exo); 2026-09-19 rebuild: US +17 / EZ +15 now Inflationary, Japan +40, China −58 deflating"
tags: [global-macro, country-analysis, comparative, cpi, rates, endo, exo, report]
data_vintage: "LIVE FRED-OECD, rebuild of 2026-09-19 (monthly OECD series, lagged)"
sources: 1
updated: 2026-09-19
---

# Major Economies Analysis — folder 12

**What it is** — Comparative macro analysis across **US / EZ / UK / JP / CA / AU / CN** on CPI, policy rates, 10Y yields, unemployment, plus each country's endo bias and carry-exo read: a Word + PDF report **and** an interactive comparative dashboard. `tools/build_country_comparison.py`.

**Current read (2026-09-19 rebuild, live FRED-OECD)**: divergence, with the West firmer — endo US +17 / EZ +15 (both now "Inflationary"), UK +13 ("Mildly Inflationary"); CA +9, AU +10 ("Mildly Inflationary"); China deflating (endo −58, "Deflationary"); Japan normalizing (+40, now "Strongly Inflationary"); Asia composite (JP/CN/KR/IN) −15. Snapshot table (CPI YoY / short rate / 10Y / unemployment): US 3.7% / 3.8% / 4.7% / 4.4% · EZ 3.2% / 2.0% / 3.2% / 6.7% · UK 3.4% / 3.7% / 5.0% / 4.9% · JP −0.5% / 1.5% / 2.9% / 2.4% · CA 2.3% / 2.3% / 3.7% / 6.4% · AU 2.4% / 4.5% / 5.0% / 4.5% · CN −0.1% / 1.5% / n/a / n/a. Carry exo vs USD: AUD +23 (LONG AUD) · GBP −4 (NEUTRAL) · CAD −51 (SHORT CAD) · EUR −60 (SHORT EUR) · JPY −79 (SHORT JPY). Dashboard banner (fixed text in the builder): the West (US/EZ/UK) and Japan run reflationary, China is in outright deflation, Japan is the upside outlier on rate normalization; the carry differential favours AUD over JPY vs USD.

*Superseded 2026-09-19: the 2026-09-08 rebuild readings, which are listed in [[log]], are replaced by the 2026-09-19 rebuild above (the dashboard header and the Word report are both stamped 2026-09-19). US and EZ endo each crossed the +15 "Inflationary" line (+14 → +17, +14 → +15), Japan crossed the +40 "Strongly Inflationary" line (+39 → +40), China held at −58, and the headline divergence is unchanged. (The 2026-09-11 refresh had replaced the Jun-2026-vintage read, China −57 and Japan +39, with the 2026-09-08 rebuild.) The old "as of 2026-06-21" stamp caveat no longer applies: `tools/build_country_comparison.py` now stamps the build date (fixed 2026-09-11). Caveats: (1) the dashboard's US CPI of 3.7% sits above the calendar-matched BLS figure of +3.35% y/y (Aug-2026), most likely because `tools/endo_scores.py` computes year-on-year change from a 12-observation offset rather than matching calendar dates (a missing monthly print would turn it into a 13-month change), so use the BLS figure for the US; (2) the short-rate column is the monthly OECD 3-month interbank rate, not the policy rate, and the Word report's country briefs are fixed builder prose written before this week's hikes (the US brief still says the Fed "has eased only partway"). Cross-check vs the verified FRED snapshot of 2026-09-19 (BLS/Fed/ECB series, fresher than the lagged OECD-harmonised series the dashboard plots): both major central banks tightened in the same week that the energy shock re-intensified. The Fed made its first hike of the cycle, to 3.75–4.00% (effective 2026-09-17; EFFR 3.88% on 2026-09-17), and the ECB raised its deposit rate from 2.25% to 2.50% (effective 2026-09-16), as WTI rose to $107.02 and Brent to $130.80 (2026-09-15). US CPI +3.35% y/y and core CPI +2.45% y/y (Aug-2026), unemployment 4.1% (Aug-2026), 10Y 4.94% (2026-09-17).*

## Files in this folder
- `Major Economies Dashboard.html` — the interactive comparative version (rebuilt 2026-09-19 from live FRED-OECD; header stamp "as of 2026-09-19", the build date)
- `Major Economies - Comparative Macro Analysis.docx` / `.pdf` — the written report (`.docx` regenerated 2026-09-19 alongside the dashboard, stamped "Report date: September 19, 2026"; `.pdf` not regenerated since 2026-06-21 and still shows the June-vintage table)

## Related
[[USA Country Analysis]] (the single-country deep-dive this generalizes) · [[Cross-Country Endo & Divergence Backtest]] (folder 38's live, backtested version of the same cross-country idea) · [[00 - GMD Overview & Structural Edge|Global Macro Database]] · [[Global Macro Brain]]
