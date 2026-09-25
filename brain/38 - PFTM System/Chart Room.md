---
title: Chart Room
category: pftm-system
type: dashboard-page
data_asof: 2026-09-19
summary: "The candlestick execution view: EMA20/Keltner charts with the audited engine's entry/stop/target lines and a CFTC COT crowdedness pane per PFTM ticket (3 TAKE / 10 WATCH at 2026-09-19: USD/JPY short, WTI and Dow longs)."
tags: [global-macro, charts, candlestick, keltner, interactive, trades, technical, decision-support]
data_vintage: "prices: live Yahoo daily · levels: the audited Macro+COT engine"
sources: 1
updated: 2026-09-19
---

# Chart Room — the setups behind the tickets

Professional **interactive trade charts** for every actionable instrument (TAKE + WATCH): daily **candlesticks**
with **EMA20 + Keltner(2×ATR) bands** and — the point — the engine's **actual entry / stop / target lines drawn on
the chart**, so every ticket is a visually verifiable setup (the skill's Module 3, visualized). Built 2026-07-03
("continue to build better interactive and professional finance charts with more analysis").

> **Decision-support / education only — NOT investment advice.**

## What it shows (`Chart Room/Chart Room.html`)
- **Instrument picker** — chips grouped ✓ TAKE / ⚠ WATCH (currently **3/10** at the 2026-09-19 build — USD/JPY short, WTI Crude and Dow Jones longs TAKE; *the 2/11 of 2026-09-11 is superseded, the 0/7 of the 2026-09-08 build was an empty-endo artefact, and 10/5 was the 2026-07-03 book*); click to switch charts instantly.
- **Candlestick chart** (offline Chart.js — floating-bar bodies + thin wick bars, green close≥open / red down),
  **EMA20** (amber), **Keltner upper/lower** (blue) recomputed identically to the trade engine's technicals, and
  dashed **Entry (blue) / Stop (red) / Target (green)** level lines with values in the legend. OHLC hover tooltip.
- **Volume pane** underneath (direction-colored; hidden with a note for spot FX, which has no exchange volume).
- **COT pane** (added 2026-07-03): weekly CFTC large-spec **net %OI history** as direction-colored bars with
  **±1.5σ crowded bands** and a zero line — the visual behind every confirm/crowded/contrarian call. The header
  gives the live read (net %, state, z, signal); for USD/××× pairs it labels the **foreign currency's futures**
  (the engine's convention). Window syncs with the range (52w at ≤6M, 104w at 1Y).
- **Range toggles** 1M / 3M / 6M / 1Y (period-aware y-axis; panes column-aligned via a fixed 72px axis).
- **Keyboard navigation** — ← → arrows cycle instruments.
- **Analysis strip per instrument** — 12 cells: last, trend, Keltner trigger, ATR%, COT (z·pctile·signal),
  **distance to entry/stop/target**, R:R, **52-week range position**, risk $, size $ — plus the full macro + COT
  rationale line (including the endo-divergence note).

**Current book (source `chartroom_latest.json`, as_of 2026-09-19, generated 2026-09-19 15:41; the build's regime input reads *Mildly Inflationary* · Reflation / Overheating):** 3 TAKE / 10 WATCH. TAKE, all HIGH-conviction with live level lines, and all three entered at the last close (distance to entry 0.00%, so each stop sits at its budgeted distance): **USD/JPY SHORT** (conv 2.17, last 156.855, 59% of 52w range, range-bound, trigger pullback to mid (EMA20); entry 156.855 · stop 160.802 · target 148.962; COT on the JPY future net +22% OI, z +1.27, 84th pctile, with endo divergence +7.5 confirming), **WTI Crude LONG** (2.07, 100.30, 70%, trend up, mid-channel; entry 100.30 · stop 91.11 · target 118.67; COT contrarian-support, z −1.48) and **Dow Jones LONG** (2.06, 51,682.64, 68%, mid-channel; entry 51,682.64 · stop 50,608.57 · target 53,830.78). ⚠ Two things the analysis strip shows: the Dow's trend reads DOWN, against the long; and USD/JPY's last price is a flat single-price bar stamped 2026-09-19 (a Saturday; open = high = low = close, with no 18 Sep bar), so the short's entry is pinned to that quote. WTI here is the Yahoo front-month future (100.30 at the 18 Sep close, off its 105.83 close of 15 Sep), not the FRED spot series quoted elsewhere in the vault ($107.02 on 15 Sep). WATCH, all LOW conviction: Natural Gas LONG (1.07, 2.912, 8%), S&P 500 LONG (1.06, 7,650.50, 89%), NASDAQ 100 LONG (1.06, 29,644.17, 86%), AUD/USD SHORT (1.00, 0.7121, 82%), NZD/USD LONG (0.62, 0.5724, 28%), Copper LONG (0.57, 6.615, 92%; its COT pane reads crowded, z +1.72, 96th pctile), USD/CHF SHORT (0.49, 0.8218, 93%), GBP/USD LONG (0.31, 1.3394, 46%), EUR/USD SHORT (0.30, 1.1489, 23%), USD/CAD SHORT (0.30, 1.3987, 66%). The WATCH charts carry `entry / stop / target = null`, so their dashed level lines and distance / R:R / risk $ / size $ cells render empty. Prices run to the 2026-09-18 close for the futures, the US indexes, EUR/USD, GBP/USD and USD/CHF; USD/JPY, AUD/USD, NZD/USD and USD/CAD end in the flat 2026-09-19 bar. COT history runs to the 2026-09-15 report. *Refreshed 2026-09-19: supersedes the 2 TAKE / 11 WATCH book of the 2026-09-11 build (WTI Crude and Dow Jones longs; USD/JPY was then a WATCH short and USD/CAD a WATCH long), whose per-instrument readings are listed in [[log]]. That build had itself superseded the 0 TAKE / 7 WATCH book of 2026-09-08, an artefact of an empty endo input (0 of 19 Excel drivers loaded after the workbooks were moved; fixed 2026-09-11) and not a market read, and the 10 TAKE / 5 WATCH book of 2026-07-03.*

## Build
`tools/chart_room.py` (engine: ~1y daily OHLCV per actionable instrument from Yahoo; EMA/ATR/Keltner series;
packages the audited engine's levels + analysis) → `chartroom_latest.json` → `tools/chart_room_report.py`
(renderer) → orchestrator `build_chart_room.py`. In `build_all_2026.py` (regenerates on every refresh — the charts
always show the CURRENT book's levels), a Main-Dashboard card ("Chart Room") and a cockpit ★ drill-down.

## Notes
- Candlesticks are implemented with Chart.js floating bars (no external financial plugin → stays fully offline).
- No new trade logic — prices are display-layer; all levels/conviction come verbatim from the audited engine → no
  separate audit needed.
- 52-week position + distance-to-levels give the quick read: e.g. a LONG at 90% of its 52w range near the upper
  Keltner is a breakout-chase; one at 25% near the lower band is a contrarian/pullback entry.

## Related
[[Global Macro Trading Dashboard]] · [[Macro + COT Trade Signals]] · [[Cross-Country Endo & Divergence Backtest]] · [[Global Macro Hedge Fund Strategy (Memo)]] · [[2026 Trading System — Operating Manual]]
