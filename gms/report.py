"""Engine outputs: `outputs/<engine>_latest.json` plus a dated markdown note.

Engines never edit vault pages. The Brain ritual (schema: Operations > Refresh) is that
whoever refreshes reads these outputs and updates the live-read / strategy-system pages
under the dated-record rule, then lints, syncs and logs.
"""

from __future__ import annotations

import json
import math
from datetime import date
from pathlib import Path

from gms import paths


def _clean(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_clean(v) for v in o]
    return o


def write_json(name: str, payload: dict, out: Path | None = None) -> Path:
    out = out or paths.OUTPUTS
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{name}_latest.json"
    path.write_text(json.dumps(_clean(payload), indent=2, default=str), encoding="utf-8")
    return path


def pct(x, digits: int = 2) -> str:
    return "—" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:.{digits}f}%"


def num(x, digits: int = 2) -> str:
    return "—" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:+.{digits}f}"


def regime_note(payload: dict) -> str:
    c = payload["current"]
    lines = [
        f"# Macro Regime Engine — run {payload['asof']}",
        "",
        f"**Current regime: {c['regime']}** (macro month {c['macro_month']}: growth composite {c['growth']:+.2f}, CPI YoY {c['inflation']:.2f}%). "
        f"VIX {c['vix']:.2f} — overlay {'ON' if c['vix_overlay_on'] else 'off'}.",
        "",
        "Allocation: " + " / ".join(f"{k} {v * 100:.0f}%" for k, v in c["weights"].items()),
        "",
        f"Switching edge vs static blend: {c['switching_edge_sharpe']:+.3f} Sharpe.",
        "",
        f"## Backtest — {payload['window']} (n={payload['n']} monthly, legs vol-matched to 10%)",
        "",
        "| Strategy | Sharpe | CAGR | Vol | MaxDD |",
        "|---|---|---|---|---|",
    ]
    for name, m in payload["table"].items():
        lines.append(f"| {name} | {m['sharpe']:.2f} | {pct(m['cagr'])} | {pct(m['vol'], 1)} | {pct(m['maxdd'], 1)} |")
    lines += ["", "Regime distribution: " + ", ".join(f"{k} {v}" for k, v in payload["regime_dist"].items()), ""]
    return "\n".join(lines)


def pulse_note(payload: dict) -> str:
    d = payload["dominant"]
    lines = [
        f"# Macro Pulse — board {d['date']}",
        "",
        f"**Dominant variable: {d['instrument']} at {num(d['z'])}σ — {d['regime']}.**",
        "",
        "| Instrument | Driver | z | 1-day | 1-week | Close |",
        "|---|---|---|---|---|---|",
    ]
    for r in payload["board"]:
        lines.append(f"| {r['instrument']} | {r['driver']} | {num(r['z'])} | {pct(r['chg_1d'])} | {pct(r['chg_1w'])} | {r['close']} |")
    lines += ["", f"## Does an abnormal move predict? (|z| >= {payload['config']['z_thresh']}, fwd {payload['config']['horizon']}d)", "",
              "| Signal | → | n | fwd | edge (pp) | t | hit |", "|---|---|---|---|---|---|---|"]
    for s in payload["study"]:
        lines.append(f"| {s['signal']} | {s['target']} | {s['n']} | {pct(s.get('fwd'))} | {num(s.get('edge_pp'))} | {num(s.get('t'))} | {pct(s.get('hit'), 1)} |")
    lines.append("")
    return "\n".join(lines)


def write_note(name: str, text: str, asof: str | None = None, out: Path | None = None) -> Path:
    out = (out or paths.OUTPUTS) / "notes"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{name} {asof or date.today().isoformat()}.md"
    path.write_text(text, encoding="utf-8")
    return path
