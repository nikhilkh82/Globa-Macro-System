# Global Macro System

A systematic global-macro research and trading system, built from the **Global Macro Brain**. The Brain is an LLM-maintained Obsidian wiki covering the method, every macro domain, the live regime reads, a 20-plus-system strategy lab and the live PFTM trading system. It sits alongside the Python engines that keep those reads current.

*Research and education only. Not investment advice.*

## Layout

```
brain/                          the Obsidian vault (open this folder in Obsidian)
  00 - Home/                    MOC, generated index, append-only log, schema, health
  01 - Framework/ … 17 - Commodities/, 38 - PFTM System/
gms/                            python -m gms <command>
  brain/                        vault lint, catalog sync, append-only log
  data/                         FRED + Yahoo loaders with an on-disk cache
  engine/regime.py              Macro Regime Allocation Engine (growth × inflation → playbook)
  engine/pulse.py               Macro Pulse cross-asset z-score monitor + honest event study
tools/                          lint_brain.py / brain_sync.py shims (the vault docs call these)
tests/                          offline tests on synthetic data
outputs/                        engine JSON + dated notes (git-ignored)
```

## Quick start

```bash
pip install -e .[dev]
python -m pytest            # offline
python -m gms lint          # vault health: 0 broken, 0 orphans
python -m gms regime        # current regime, allocation, vol-matched backtest table
python -m gms pulse         # today's dominant cross-asset variable + signal study
python -m gms refresh       # both engines, then lint + sync
```

Set `FRED_API_KEY` to use the keyed FRED API. Without it, the loader falls back to the public CSV endpoint.

## The engines, in one line each

- **Regime.** INDPRO YoY plus payrolls YoY measures growth. CPI YoY above 3% counts as high inflation. Together they place the economy in one of four quadrants, read with a 2-month publication lag. Each quadrant maps to a fixed ETF playbook, and a VIX > 20 overlay de-risks half of the risk assets. Every comparison leg is vol-matched to 10% so the effect of switching is isolated. The vault's recorded result is a **+0.02 Sharpe switching edge**, which is a near-null. The engine's real value is drawdown control.
- **Pulse.** Each instrument's move is divided by its trailing 60-day volatility. The monitor names the instrument with the largest move today (the "dominant variable") across US10Y, US3M, DXY, WTI, SPY, QQQ and VIX. A study then tests whether a |z| ≥ 2 move predicts the next 10 days. Mostly it doesn't: the VIX-fear → SPY edge fails a Bonferroni correction.

## Working on the vault

See [`CLAUDE.md`](CLAUDE.md) and `brain/00 - Home/_Vault Schema & Conventions.md`. In short:

- Dated records are append-only.
- `data_asof` is separate from `updated`.
- The index is generated.
- Every change ends with lint → sync → log.
