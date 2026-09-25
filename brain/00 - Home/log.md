---
title: log
category: meta
type: meta
data_asof: n/a
summary: "Append-only operations log for the git-hosted vault (from 2026-09-25). Entries before the migration stay in the OneDrive log.md and Log Archive 2026-06 to 2026-07."
tags: [meta, log, append-only]
data_vintage: "append-only record; started 2026-09-25 at the git migration"
sources: 0
updated: 2026-09-25
---

# log

Append-only, newest at the bottom. Every entry follows the format `## [YYYY-MM-DD] <verb> | <title>`. Never edit or reorder an entry. Append with `python -m gms log <verb> "<title>" --body "..."`. Rules: [[_Vault Schema & Conventions]] · map: [[Global Macro Brain]].

> **Pre-migration history is not in git.** The vault's log from 2026-06 to 2026-09-24 is kept verbatim on OneDrive, in `Global Macro Hedge Fund Strategy/Global Macro Brain/00 - Home/`. It is split across `log.md` (about 188 KB) and `Log Archive 2026-06 to 2026-07.md` (about 384 KB). It was not copied here: the dated-record rule forbids a lossy copy, and the MCP transfer can't move those files byte-for-byte.
