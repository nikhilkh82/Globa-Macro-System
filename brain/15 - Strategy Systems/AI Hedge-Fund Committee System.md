---
title: AI Hedge-Fund Committee System
category: strategy-lab
type: live-read
data_asof: 2026-09-19
summary: "Deterministic virattt/ai-hedge-fund port: 15 rule-set agents vote BUY/HOLD/SELL on 12 large-caps; decision-support, not a backtest — 2026-09-19 screen: 5 BUY (NVDA, GOOGL, MSFT, AMZN, JPM), WMT the lone SELL."
tags: [global-macro, strategy, multi-agent, equity-screen, investor-personas, decision-support, ai-hedge-fund]
data_vintage: "LIVE — Yahoo fundamentals + prices; screen re-run 2026-09-19 (`aihf_latest.json`, as_of 2026-09-19). The 2026-06-23 snapshot and its 2026-08-15 re-check are retired records"
sources: 1
updated: 2026-09-19
---

# AI Hedge-Fund Committee System

> **Superseded 2026-09-19.** The screen was re-run today (`AI Hedge Fund/aihf_latest.json`, `as_of` 2026-09-19): **UNH is now HOLD** (5 bull / 7 bear, net −2) and **MSFT BUY** (8 / 3, net +5), so the drift warned about below has been re-scored and the instruction to re-run the screen is satisfied. The banner below is kept verbatim as the record of the retired 2026-06-23 screen and its 2026-08-15 input re-check.

> ### ⚠️ Snapshot verdicts — inputs re-checked 2026-08-15
>
> Committee verdicts are a **point-in-time screen**, not maintained calls. Two have drifted materially:
>
> - **UNH "Consensus SELL"** — the stated basis has partly reversed: analyst target upside **+0.8% → +18.3%**,
>   trailing P/E **30.6 → 25.6**, ROE **12.2% → 14.2%**. Only the growth leg held (revenue growth 2.0% → 0.4%).
> - **MSFT "HOLD"** — **+32.5%** since the snapshot (373.94 → 495.40), now +14.5% above its 200dma, with target
>   upside compressing +52.8% → +14.5% as price caught up. It sat two net votes short of BUY at the time.
>
> Re-run the screen rather than reading these verdicts as current.


A **deterministic, free-data port of [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** — a multi-agent "committee" of famous-investor and analyst philosophies that screens a stock universe and aggregates to a BUY/HOLD/SELL. The original drives each agent with an LLM over paid fundamentals; this rebuild keeps the **multi-agent structure** but replaces every LLM with a **transparent, deterministic rule-set** scored on free live data. Built 2026-06-23.

> **Decision-support / idea-generation, not a backtested strategy.** No performance is claimed — see the scope note. Education only.

## Provenance — what we adapted
The source ships ~13 investor-persona agents (Buffett, Graham, Munger, Wood, Lynch, Burry, Druckenmiller, Taleb, Fisher, Ackman, Damodaran, Pabrai, Jhunjhunwala) + 4 analyst agents (Valuation, Sentiment, Fundamentals, Technicals) + a risk manager + portfolio manager, each an **LLM** over `financialdatasets.ai` (paid). We extracted the **quantitative rule-set** under each agent (e.g. Buffett: ROE>15%, op-margin>15%, D/E<0.5, margin-of-safety) and reimplemented it deterministically on **free Yahoo data** — reproducible and transparent, but a simplification.

## How it works
- **15 agents:** 11 investor personas + 4 analysts (Valuation / Fundamentals / Technicals / Sentiment), each a rule-set returning *(score, max, reason)* → bullish (≥0.6 of max) / neutral / bearish (≤0.35). A **risk manager** flags leverage/beta; a **portfolio manager** aggregates the 15 votes to **BUY** (net ≥ +4 agents), **SELL** (net ≤ −4), else **HOLD**.
- **Data (free, live):** Yahoo **`quoteSummary`** via the cookie/crumb handshake for fundamentals (ROE, margins, D/E, P/E, P/B, PEG, revenue/earnings growth, FCF, market cap, beta, analyst target) + the **chart API** for 2y daily prices (3/6/12-month momentum, vs-200-dma, RSI-14, 52-week position).
- **Universe:** 12 liquid large-caps across sectors (AAPL, MSFT, NVDA, GOOGL, AMZN, META, JPM, JNJ, XOM, WMT, UNH, V) — configurable.

## Outputs (`AI Hedge Fund/`)
- **`AI Hedge Fund Dashboard.html`** — light theme, Chart.js inlined: a net-consensus bar, a committee decision table (decision, bull/bear split, key metrics, risk flags), and a **vote heatmap** (names × 15 agents, hover for each agent's reasoning).
- **`AI Hedge Fund Note <date>.md`** + **`aihf_latest.json`**.
Tools: `tools/ai_hedge_fund.py` · `ai_hedge_fund_report.py` · `build_ai_hedge_fund.py`.

## Result — today's snapshot (12 names, 15 agents)
- **Consensus BUY (5):** NVDA (11 bull / 1 bear, net +10; ROE 117.2%, revenue +105.9%), GOOGL (11/1, net +10; P/E 17.4, +38.7% 12m), MSFT (8/3, net +5), AMZN (8/3, net +5), JPM (7/3, net +4) — quality + growth + momentum names the growth/quality agents converge on.
- **Consensus SELL (1):** WMT — 0 bull / 11 bear, net −11, the only name with no bull vote at all: P/E 38.8 on +5.9% revenue growth and a 3.5% operating margin.
- Everything else **HOLD**: META (7/4, net +3), XOM (7/5, +2), V (6/6, 0), AAPL (5/6, −1), JNJ (4/6, −2), UNH (5/7, −2). The audit fixes below are baked into the code that produced this run; the robustness check itself ('no decision changed') is the 2026-06-23 record and was not re-run today.

> **Live-data note — refreshed 2026-09-19.** Every figure in this section is the screen of **2026-09-19**, read from `AI Hedge Fund/aihf_latest.json` (rebuilt 2026-09-19 15:52, `as_of` 2026-09-19). It supersedes the **2026-06-23** verdicts this page carried and their **2026-08-15** input re-check — the superseded 2026-06-23 verdicts are listed in [[log]]; the 2026-08-15 input re-check is preserved verbatim in the banner at the top, which is now a record of that retired screen, not a live warning. Versus 2026-06-23: **MSFT, AMZN and JPM moved HOLD → BUY**, **META BUY → HOLD** (12-month momentum −14.7%), and **UNH SELL → HOLD** — the drift the banner flagged, now re-scored (analyst-target upside +27.8%, ROE 14.2%, but revenue growth only +0.4%).

## Honest scope & caveats
- The personas are **deterministic quantitative caricatures** of each investor's philosophy (explicit thresholds), **not** LLM reasoning — a faithful simplification.
- It is a **current-snapshot decision-support tool, not a backtested alpha strategy.** No performance is claimed: free **point-in-time** fundamentals don't exist, so the committee *cannot* be honestly backtested (today's snapshot only). This is deliberate — unlike [[Hedge-Fund Replication System]] (which *is* validated out-of-sample), this tool's value is structured idea-generation, not a measured edge.
- **The bull/bear counts are value-aware, not symmetric:** the strict deep-value personas (**Graham, Burry**) rank names by cheapness but rarely cast a BUY on a richly-valued mega-cap universe — they act as one-sided value/short screens here. Read the consensus as *growth/quality/momentum agents vs value/tail agents*, not an even vote.
- Sentiment is a price/analyst-target proxy (no news-LLM); fundamentals are TTM single-period; large-cap US only; revised data.

## Audit
Adversarially audited (2-lens: data-units + faithfulness/framing) → **10 flagged, only 2 confirmed, both LOW** (the data-unit handling — the main risk — was clean, 8 false alarms). Fixed: (1) RSI used 15 changes → proper RSI(14); (2) the **Burry agent was degenerate** (deep-value bar unreachable on mega-caps → constant bearish) → regraded so it discriminates by degree, and the one-sided value-persona behaviour is now disclosed. No decision changed.

## Related
[[Hedge-Fund Replication System]] · [[AI Analyst Committee — Stock Selection (June 2026)]] · [[Target-Beta Factor Portfolio (June 2026)]] · [[Analyst System — Live Cockpit (June 2026)]] · [[The Global Macros Framework]]
