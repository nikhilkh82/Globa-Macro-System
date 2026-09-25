"""Append-only vault log: `## [YYYY-MM-DD] <verb> | <title>` entries in `00 - Home/log.md`.

Entries are never rewritten or reordered (the dated-record rule). Append in Python —
the log grows large and shell heredocs fail on it.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

VERBS = ("ingest", "refresh", "lint", "extend", "publish", "fix", "structure", "query")


def append(brain: Path, verb: str, title: str, body: str = "", when: date | None = None) -> str:
    if verb not in VERBS:
        raise ValueError(f"verb must be one of {VERBS}, got {verb!r}")
    when = when or date.today()
    entry = f"\n## [{when.isoformat()}] {verb} | {title}\n"
    if body.strip():
        entry += "\n" + body.strip() + "\n"
    path = brain / "00 - Home" / "log.md"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    return entry


def tail(brain: Path, n: int = 5) -> list[str]:
    path = brain / "00 - Home" / "log.md"
    heads = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.startswith("## [")]
    return heads[-n:]
