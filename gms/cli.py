"""`python -m gms <command>` — the vault ritual and the engines.

    lint      structural checks; regenerates _Brain Health (exit 1 on broken links/orphans)
    sync      regenerates index.md + brain_index.json from frontmatter
    log       append `## [date] <verb> | <title>` to the vault log
    regime    run the Macro Regime Allocation Engine on live FRED + Yahoo data
    pulse     run the Macro Pulse cross-asset z-score monitor on live Yahoo data
    refresh   regime + pulse, then lint + sync
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from gms import paths, report


def cmd_lint(args) -> int:
    from gms.brain import lint

    rep = lint.main(paths.BRAIN, write=not args.no_write)
    if args.json:
        print(rep.to_json())
    else:
        print(f"pages {rep.pages} | broken {len(rep.broken)} | orphans {len(rep.orphans)} | duplicates {len(rep.duplicates)} "
              f"| stale {len(rep.stale)} | asset links not in repo {len(rep.missing_assets)}")
        for b in rep.broken[:50]:
            print(f"  BROKEN  {b['page']} -> [[{b['target']}]]")
        for o in rep.orphans:
            print(f"  ORPHAN  {o}")
        for d in rep.duplicates:
            print(f"  DUPLICATE  {d}")
    return 0 if rep.ok else 1


def cmd_sync(args) -> int:
    from gms.brain import sync

    try:
        n = sync.main(paths.BRAIN)
    except sync.GateError as e:
        print(f"sync refused: {e}", file=sys.stderr)
        return 2
    print(f"index.md + brain_index.json regenerated ({n} pages)")
    return 0


def cmd_log(args) -> int:
    from gms.brain import log

    print(log.append(paths.BRAIN, args.verb, args.title, args.body or "").strip())
    return 0


def cmd_regime(args) -> int:
    from gms.data import fred, yahoo
    from gms.engine import regime

    macro = fred.frame(regime.MACRO_IDS, start="1990-01-01")
    cash = fred.series(regime.CASH_ID, start="1990-01-01")
    prices = yahoo.frame(regime.ASSETS, start="2007-01-01")
    vix = yahoo.closes("^VIX", start="2007-01-01")
    res = regime.backtest(macro, prices, vix, cash)
    asof = date.today().isoformat()
    payload = {
        "asof": asof,
        "window": f"{res.legs.index[0]:%Y-%m} → {res.legs.index[-1]:%Y-%m}",
        "n": int(len(res.legs)),
        "current": res.current,
        "table": res.table,
        "regime_dist": res.regimes.value_counts().to_dict(),
        "regimes": {k.strftime("%Y-%m"): v for k, v in res.regimes.items()},
    }
    print(f"wrote {report.write_json('regime', payload)}")
    note = report.regime_note(payload)
    print(f"wrote {report.write_note('Macro Regime Engine', note, asof)}\n\n{note}")
    return 0


def cmd_pulse(args) -> int:
    from gms.data import yahoo
    from gms.engine import pulse

    cfg = pulse.Config()
    closes = yahoo.frame([sym for sym, _ in pulse.INSTRUMENTS.values()], start="2000-01-01")
    closes.columns = list(pulse.INSTRUMENTS)
    rows, dominant = pulse.board(closes, cfg)
    payload = {
        "asof": date.today().isoformat(),
        "meta": {"start": f"{closes.index[0]:%Y-%m-%d}", "end": f"{closes.index[-1]:%Y-%m-%d}"},
        "config": vars(cfg),
        "board": rows,
        "dominant": dominant,
        "domfreq": pulse.dominant_frequency(closes, cfg),
        "study": pulse.study(closes, cfg),
    }
    print(f"wrote {report.write_json('macro_pulse', payload)}")
    note = report.pulse_note(payload)
    print(f"wrote {report.write_note('Macro Pulse', note, payload['asof'])}\n\n{note}")
    return 0


def cmd_refresh(args) -> int:
    rc = 0
    for fn in (cmd_regime, cmd_pulse):
        try:
            fn(args)
        except Exception as e:  # one engine failing must not block the vault checks
            print(f"{fn.__name__} failed: {e}", file=sys.stderr)
            rc = 1
    args.no_write, args.json = False, False
    return max(rc, cmd_lint(args), cmd_sync(args))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="gms", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lint")
    s.add_argument("--json", action="store_true")
    s.add_argument("--no-write", action="store_true", help="don't regenerate _Brain Health")
    s.set_defaults(fn=cmd_lint)
    sub.add_parser("sync").set_defaults(fn=cmd_sync)
    s = sub.add_parser("log")
    s.add_argument("verb")
    s.add_argument("title")
    s.add_argument("--body")
    s.set_defaults(fn=cmd_log)
    sub.add_parser("regime").set_defaults(fn=cmd_regime)
    sub.add_parser("pulse").set_defaults(fn=cmd_pulse)
    sub.add_parser("refresh").set_defaults(fn=cmd_refresh)
    args = p.parse_args(argv)
    return args.fn(args)
