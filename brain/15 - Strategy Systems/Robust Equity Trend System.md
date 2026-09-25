---
title: Robust Equity Trend System
category: strategy-lab
type: strategy-system
data_asof: 2026-09-24
summary: "Tzotchev robust trend on a 10-market equity-ETF panel plus a never-flip macro overlay, walk-forward 1998–2026 — a verified null: trend IC ≈ 0, trails buy-and-hold; the overlay is within noise (t 0.67)."
tags: [global-macro, strategy, trend-following, equity-momentum, tzotchev, macro-overlay, null-result, backtest]
data_vintage: "LIVE (10 equity ETFs + FRED, 1998-06→2026-08) — engine re-run 2026-09-24 16:14"
sources: 1
updated: 2026-09-24
---

# Robust Equity Trends & Headwinds

A free-data port of the Macrosynergy **"Equity trend-following with market and macro data"** notebook: a **Tzotchev (2018) robust trend** signal on a panel of equity-index ETFs, optionally **modified by a macro support/headwind overlay** that amplifies/dampens (but never flips) the trend. Built 2026-06-23.

> **A well-verified honest near-null:** equity-index trend-following barely predicts over this period, and the macro overlay's apparent improvement is *within the noise band*. Research/education only.

## Provenance — what we adapted
The source builds per-country equity trend signals (the robust trend) and modifies them with per-country **quantamental** macro scores (domestic spending, inflation, equity carry, liquidity), tested on local-currency equity-index futures (JPMaQS, paid). We kept the **robust-trend method and the never-flip macro modifier**, and ran them on free data.

## How it works
- **Panel:** 10 developed-market equity ETFs (SPY, EWJ, EWG, EWU, EWA, EWC, EWL, EWQ, EWP, EWH), Yahoo monthly **USD total returns**.
- **Robust trend (Tzotchev):** for lookbacks {2, 3, 6, 12, 24} months, `SIGNAL = 2·Φ(mean/std·√N) − 1` (a bounded [−1,1] function of the trend's t-statistic), averaged into one multi-horizon trend.
- **Macro modification (never flips):** a **global** macro-support composite (point-in-time z of US retail-sales YoY, −CPI YoY, M2 YoY, −HY OAS; lagged 1m) → `C = 2/(1+e^{−2·support})`, `adtrend = ((1−sign(tr)) + sign(tr)·C)·tr` — amplify (up to 2×) or dampen (to 0×).
- **Strategy:** per market, position = signal / trailing-vol; panel return = gross-normalised; vol-targeted to 10%; walk-forward (signals ≤ t, macro lagged, earn t→t+1). Vanilla (trend) and modified (adtrend) use **identical machinery** so the comparison isolates the overlay.

## Outputs (`Equity Trend/`)
- **`Equity Trend Dashboard.html`** — light theme, Chart.js inlined: growth-of-100 (vanilla vs modified vs buy-and-hold), a benchmark table, and the panel-IC comparison bar.
- **`Equity Trend Note <date>.md`** + **`eqtrend_latest.json`**.
Tools: `tools/equity_trend.py` · `equity_trend_report.py` · `build_equity_trend.py`.

## Result — 1998-06 → 2026-08 (n=339, 10 markets, vol-targeted 10%)
| Strategy | Sharpe | CAGR | Vol | MaxDD |
|---|---|---|---|---|
| Macro-modified robust trend | 0.45 | 4.78% | 12.1% | −29.6% |
| Vanilla robust trend | 0.42 | 4.45% | 12.1% | −28.4% |
| Equal-weight panel (buy & hold) | **0.48** | 5.18% | 12.2% | −36.1% |
| All-equity (SPY) | **0.64** | 9.02% | 15.4% | −50.8% |

*Vintage: engine **re-run 2026-09-24 16:14** (`eqtrend_latest.json`, `as_of` 2026-09-24) and every Sharpe/CAGR/Vol/MaxDD above is **unchanged** from the 2026-09-08 verification — re-checked cell by cell against the payload, and `Equity Trend Note 2026-09-24.md` is identical to the 2026-09-08 note apart from its title line and the live support z. The run still ends at the last **completed** month, **2026-08** (n=339, 3390 signal-return pairs), so no new return months entered the sample and the window did not move; that alone would **not** guarantee unmoved figures — these engines re-pull revised data, and the sibling [[Managed-Futures Trend System]] did drift on an unmoved window this pass — so the figures were re-checked rather than assumed. Added this pass: the Vol column and the two benchmark rows' CAGR/Vol/MaxDD, from `perf_vanilla` / `perf_modified` / `perf_ew` / `perf_spy`. (Supersedes the earlier "metrics refreshed 2026-09-08" provenance note.) The audit verdicts below are unchanged and still refer to the original adversarial review.*

- **Vanilla robust trend has essentially no predictive power: panel IC +0.009 (~0)**, and it **trails simply buying & holding** (equal-weight 0.48, all-SPY 0.64).
- **The trend book does not even buy its weaker return with less risk:** at 12.1% vol it runs essentially level with the equal-weight panel (12.2%), so the ~0.7pp of forgone CAGR is not compensated by a lower-vol ride. Its one genuine advantage is drawdown — −28.4% vanilla against the panel's −36.1% and SPY's −50.8% (`perf_ew.maxdd` / `perf_spy.maxdd`, surfaced 2026-09-24).
- **This is genuine, not an implementation artifact:** the audit verified the machinery is causal and sound, and **even plain 12-month momentum has IC −0.037** (slightly *anti*-predictive) on the same panel (`ic_plain12m`; quoted as −0.04 before 2026-09-24, now at the payload's own precision). Equity-index TSMOM is the weakest trend asset class, and across these USD country ETFs over 1998–2026 it simply didn't pay (the choppy QE-era bull whipsawed it).
- **The macro overlay points the right way but is within the noise:** IC +0.009 → +0.039, Sharpe 0.42 → 0.45, MaxDD −28.4% → −29.6%. But with only ~2–3 effectively-independent markets, the **month-block bootstrap IC SE is 0.059**, so the modified IC (**t = 0.67**) and the edge are **within ~1 SE of zero — not statistically distinguishable from no overlay effect**.

## Live signal — 2026-09-24
*From the 2026-09-24 16:14 engine run (`eqtrend_latest.json`).*

- **Global macro-support z = +0.22** (`current_support`) — mildly **supportive**, so the never-flip modifier `C = 2/(1+e^{−2·support})` sits above 1 and is currently **amplifying** whatever trend each market shows, up to the 2× cap. It is not flipping any position; by construction it cannot. **⚠️ This is a sign flip produced by today's run — flagged here, not absorbed:** the previous published read (`Equity Trend Note 2026-09-16.md`) carried support z **−0.19**, which matches this construction's **2026-07** value (−0.191) — the last month computable then, since the composite needs ≥3 of its 4 monthly inputs — so the modifier was *damping* (C ≈ 0.81), not amplifying. The 2026-08 month (+0.218) entered with this run — and the sign change is a **data-availability threshold being crossed, not a macro turn**: FRED serves only 786 daily HY OAS observations here, i.e. month keys from 2023-09, and `expanding_z` returns nothing until a leg has `Z_MIN = 36` months of history, so the credit leg was `None` at 2026-06 (34) and 2026-07 (35) and entered the composite for the **first time** at 2026-08 (exactly 36). The −0.19 was therefore a **three-input** mean (spend +0.102, −CPI −0.463, liquidity −0.212); on the same three inputs August still reads **−0.117**. The verdict is unaffected (next bullet).
- **What that is worth: nothing measurable.** The overlay's whole measured effect is IC +0.009 → +0.039 against a bootstrap SE of **0.059** (t **0.67**), so a +0.22 support reading is a conviction tilt inside the noise band, not a signal. The page's verdict is a near-null and the live reading does not change it.
- **The support score's four inputs, decomposed.** Each input enters as an **expanding z of its own history**, not as a raw level (`tools/equity_trend.py`: `expanding_z` over {RSAFS YoY, −CPI YoY, M2SL YoY, −BAMLH0A0HYM2}); the decomposition below was re-derived from FRED on the same construction this session and reproduces `current_support` exactly. **Tight HY credit is almost the whole of the +0.22** — the credit leg keys FRED to calendar months and takes the **last daily print of the month**, not a monthly average (`fred_monthly` in `tools/equity_trend.py` assigns `by[d[:7]] = v` in date order), so the input is the **2026-08-31 close of 2.63pp** (August's daily *average* was 2.70pp; the 09-22 daily read is 2.68pp). It enters negatively and scores **z +1.22**; retail sales **+6.01% YoY** (RSAFS, Aug-2026) adds **+0.30**. There are **two** drags, not one: **CPI +3.35% YoY** (CPIAUCSL, Aug-2026, vs Jul **+3.30%**) at **z −0.49**, and **M2 +5.66% YoY** (M2SL, Aug-2026), which sits *below* its own expanding mean and so scores **z −0.15** — money growth pushes support **down**, not up. Mean of the four = **+0.2175 → +0.22**. The score is therefore near-neutral because one strongly supportive credit input is offset by inflation *and* by money growth that is only average — not because two tailwinds cancel one headwind. *(The daily market read of HY OAS is **2.68pp** on 09-22 in `tools/macro_pack.json`; the composite's input is the Aug-2026 monthly average, **2.63pp**.)*

## Verdict
- **Mechanical equity-index trend-following was a near-null over this period** (IC ~0, Sharpe 0.42, trailing buy-and-hold) — confirmed by plain momentum also failing. Unlike the multi-asset CTA in [[Managed-Futures Trend System]] (where rates/commodities/FX trend carried the book), *equity-only* trend has little to offer here. **⚠️ Flagged 2026-09-24 — the parenthetical is not supported by that build's own attribution:** its `sector_attr[].contrib` over 2000-03→2026-08 reads Commodities **+73.4**, Equities **+72.9**, FX **+21.4**, Rates **+21.2**, i.e. equity trend is the *joint-largest* contributor there, not a laggard carried by the other three. The contrast that does hold is between a **diversified multi-asset** book and an **equity-only** one, not between asset classes. Flagged for correction at the next audit; the near-null verdict on *this* page does not depend on it.
- **The macro support/headwind overlay is directionally sensible but statistically indistinguishable from chance** (IC t 0.67). It's a reasonable conviction-modulation that improves the drawdown, not a measured edge. **Update 2026-09-08: this no longer holds — on the refreshed window the overlay slightly *worsens* max drawdown (−28.4% → −29.6%). The drawdown benefit was the one point in the overlay's favour, so that claim is withdrawn pending an audit re-run; the headline near-null verdict is unaffected.** **Re-verified 2026-09-24:** the 2026-09-08 withdrawal **stands unchanged** — on the re-run engine the overlay still worsens max drawdown (−28.4% → −29.6%, `perf_vanilla.maxdd` → `perf_modified.maxdd`) on an unmoved window, and the IC t is still 0.67 against a bootstrap SE of 0.059. Nothing recovered; the audit re-run is still owed. The honest takeaway: **in equities, holding the index beat timing it**, and macro-enhancing a weak trend yields a weak result you can't tell apart from noise.

## Audit
Adversarially audited (2-lens: look-ahead/soundness + framing). **The audit's key verdict: no look-ahead, and the weak result is *genuine*, not artificially weak from a bug** (causal signals/vols, lagged macro, earn t→t+1, identical machinery for both legs, correct IC orientation — all verified). 4 LOW findings, addressed: added a **month-block bootstrap IC SE** (0.056) showing the overlay edge is within ~1 SE of zero; aligned the plain-12m cross-check to the same window/timing; aligned the IC universe to the traded panel.

## Caveats
- Trend on **USD-denominated** country-ETF returns (includes FX — a free-data simplification vs local-currency index futures); the macro support is a **global** US-led proxy applied to all markets (vs the notebook's per-country quantamental scores); vol-targeted 10%; revised data; 1-month macro lag.

## Related
[[Managed-Futures Trend System]] · [[Macro-Aware Risk Parity System]] · [[Macro Curve-Trade Strategy]] · [[ML Macro-Direction Model]] · [[The Global Macros Framework]] · [[Analyst System — Live Cockpit (June 2026)]]
