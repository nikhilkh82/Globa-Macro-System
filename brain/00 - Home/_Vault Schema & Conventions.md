---
title: Vault Schema & Conventions
category: meta
type: reference
data_asof: n/a
summary: "The wiki's own schema (v2, 2026-09-08): 19-folder layout, the type / data_asof / summary frontmatter contract, seven page types with lint clocks, the dated-record rule, and the refresh > lint > sync > log ritual."
tags: [meta, schema, maintenance, conventions]
data_vintage: "schema v2 — rewritten 2026-09-08 to describe the vault as it is (19 folders, mixed live/historical corpus)"
sources: 0
updated: 2026-09-19
---

# Vault Schema & Conventions

This file is the **schema** for the Global Macro Brain — the operating manual an LLM agent reads before ingesting a source, answering a query, refreshing data, or linting the vault. It encodes the *Global Macros* global-macro / long-short hedge-fund strategy as a living, interlinked knowledge base. Start at [[Global Macro Brain]]; the catalog is the generated [[index]]; the history is the append-only [[log]].

> **Pattern.** Raw sources (immutable, `../raw/`) → the wiki (LLM-owned markdown, this vault) → this schema (the conventions) → the tools (`../tools/`, which refresh data, lint the vault and regenerate its catalog pages). See the project `CLAUDE.md` for the underlying "LLM Wiki" idea and the seven non-negotiables every session must know.

> **Schema v2 (2026-09-08).** v1 (2026-06-18) described a 10-folder, historical-only vault. The vault is now 19 folders and roughly half its pages are *live*. v2 adds three frontmatter fields — `type`, `data_asof`, `summary` — that make liveness, staleness and the catalog machine-readable, and it moves `index.md` from hand-maintained to generated.

## Layout (19 top-level folders)

```
Global Macro Brain/
  00 - Home/                      MOC, generated index, append-only log, this schema, auto health + dashboard map
  01 - Framework/                 The method: Global Macros process, trade-idea funnel, endo/exo toolkit,
                                  econometric frameworks, curriculum map, glossary
  02 - Macro Indicators/          GDP, leading/coincident/lagging, M2, inventories, commodities + measurement refs
  03 - Rates & Bonds/             Government yields, yield curve & recession, corporate credit & spreads
  04 - FX/                        Endogenous-exogenous framework, USD & G10, live UK + Australia scorecards
  05 - Positioning & Sentiment/   COT, VIX & implied vol, bull & bear markets
  06 - Equities & Sectors/        Sector rotation, company screening, spread trades, LEI-circularity caveat
  07 - Technical & Statistical/   ATR, distribution of returns, price action
  08 - Portfolio & Risk/          Portfolio management, risk management, position sizing, performance metrics
  09 - Synthesis/                 Live regime page + cockpit, historical regime snapshot, the desk's own
                                  engine write-ups, the strategy-lab capstone
  10 - Global Macro Dashboard/    META despite the name: session records, decisions, open items, operating specs
  11 - USA Country Analysis/      Live USA report (docx/pdf/html) + companion page
  12 - Major Economies Analysis/  Seven-economy comparative report (docx/pdf/html) + companion page
  13 - Macro Cycles & Asset Returns/  The macro-cycles notebook (ipynb/html) + companion page
  14 - Global Macro Database/     Eight GMD chapters + dashboard + its own build log (GMD Folder Log.md)
  15 - Strategy Systems/          Every backtested strategy replication (free data, point-in-time, audited)
  16 - Central Banks & Monetary Policy/
  17 - Commodities/
  38 - PFTM System/               The live, actively-traded system — one companion page per dashboard.
                                  Numbered 38 to MIRROR the raw/ source folder it is built from; the gap is deliberate.
```

Folders `11`–`14` hold non-markdown deliverables (docx / pdf / html / ipynb / json) beside their pages; those files are *outputs* of `../tools/build_*.py`, regenerated on refresh, and are never edited by hand.

## The frontmatter contract (every page)

```yaml
---
title: <exact note title>
category: <folder-aligned vocabulary, lowercase — see below>
type: domain | reference | live-read | strategy-system | dashboard-page | deep-dive | meta
data_asof: YYYY-MM-DD | YYYY-MM | n/a
summary: "<one sentence, <=220 chars: what the page is + its single most important current finding>"
tags: [global-macro, ...]
data_vintage: "<free text: what data the page is built from and through when>"
sources: <n>
updated: YYYY-MM-DD
---
```

| Field | Meaning | Who sets it |
|---|---|---|
| `type` | What kind of page this is (table below). Drives lint rules and the index. | The author, once. |
| `data_asof` | The date the page's **data** was last verified against its source. `n/a` for pages with no data claims. **Not** the touch date. | Whoever last re-verified the figures. |
| `summary` | The one-liner the generated [[index]] shows. Rewrite it when the page's headline finding changes. | The author; refreshed on ingest/refresh. |
| `updated` | When the *file* was last edited. Metadata-only migrations do not bump it. | Any edit. |
| `category` | Folder-aligned facet: `meta framework indicators rates fx positioning equities technical portfolio-risk synthesis country cycles gmd strategy-lab central-banks commodities pftm-system`. | Set from the folder. |
| `data_vintage` | Free-text provenance ("LIVE — FRED + CFTC, through Aug-2026"; "1959–2021 teaching corpus"). Human-readable; the machine fields are `type` + `data_asof`. | The author. |

**Why `data_asof` exists.** `updated:` records when a file was touched. Twice (2026-08-22, 2026-09-08) a refresh found pages that looked fresh by `updated:` while quoting superseded figures, and pages flagged "aging" whose data was current. The linter now reads `data_asof` by page type instead.

## Page types and what each is allowed to claim

| `type` | What it is | Lint clock | Body convention |
|---|---|---|---|
| `domain` | A macro-domain teaching page built from the historical corpus | none | *What it is* → *Key datasets* → *Charts & key trends* → *How it's used* → *See also*. Its figures are the corpus's; a live counterpart, if any, is a dated note or a link to a live-read page — the corpus description is never "refreshed". |
| `reference` | Glossary, conventions, measurement rules, registers, calendars, curriculum map, this schema | none | Definitions and rules; no market reads. |
| `live-read` | Asserts CURRENT figures re-pulled from live sources | **45 days** | A rolling "current" page replaces its figures in place with a supersession note; a page that stacks `## Live read — YYYY-MM-DD` sections adds the newest **above** the old and never edits the old. |
| `strategy-system` | A backtested strategy write-up: metrics table + audit verdict | **120 days** | Digits move on re-run; null verdicts are preserved verbatim; a *flipped* conclusion is flagged inline and sent for re-audit, never quietly rewritten. Audit sections are records. |
| `dashboard-page` | Companion page documenting an HTML dashboard / Excel tool | **45 days** | Says what the dashboard shows and how it is rebuilt; links the HTML. |
| `deep-dive` | A long-form research chapter (GMD, notebooks) | none | Its own dated vintage; refreshed by re-running its builder. |
| `meta` | Session records, decisions, open items, specs, health, map, index, log, lessons | none | Chronological; append-only where dated. |

## The dated-record rule (the one rule that must not be broken)

A dated record — a `## Live read — YYYY-MM-DD` (or `## Live read (YYYY-MM-DD)`) section, a `## Snapshot — YYYY-MM-DD` / `## Current read — YYYY-MM-DD` section, a `## [YYYY-MM-DD] …` log entry, a `(build snapshot)` figure, anything under a supersession banner — is **never rewritten**. To update, add a newer dated section above it and state what it supersedes. Rewriting history to look current is the failure mode this vault is built to avoid.

**What is *not* a dated record:** a date that records when a section was *created* rather than when a read was *taken* — `## The CCC spread, live and tested (added 2026-08-17)`, `## Desk Analyst — econometric engines (v3, 2026-07-18)`. Those are provenance stamps on **rolling** sections: update their figures in place with an inline supersession note, and keep the stamp. Likewise `## Result — 2012-05 → 2026-08` on a strategy page is a backtest *window* (a run parameter), updated when the backtest re-runs. The test: *does the date say when this text was true?* If yes, it is a record; if it says when the section was born, it is not.

**Page-title suffixes** like *(June 2026)* record the month a page was **first built**, not its data vintage; the data vintage is `data_asof`. Titles are not renamed on refresh, because renames break inbound links and the six tools that reference these pages by name.

## Operations

- **Ingest.** Drop a source into `../raw/`, inspect it (`python ../tools/xl_inspect.py "<file>"`), update the relevant page(s), set their `data_asof` and `summary`, append `## [YYYY-MM-DD] ingest | <title>` to [[log]], then lint + sync (below). One source can touch 10–15 pages.
- **Query.** Read the generated [[index]] (page · type · summary · data as-of, one table per folder, plus a second view grouped by `type` at [[index#By type]]), drill in, synthesise with `[[wikilink]]` citations, and file durable answers back as new pages (usually under `09 - Synthesis/`).
- **Refresh.** `python tools/auto_refresh.py` re-pulls every online source and rebuilds the Explorer chain (also runs hourly from Task Scheduler); `tools/refresh_all.ps1` rebuilds the FRED-backed endo/exo templates (**needs Excel closed** — it drives COM); `python tools/build_all_2026.py` rebuilds the dashboard suite. Then update `data_asof` on every page whose figures were re-verified, and refresh live-read pages per the dated-record rule.
- **Lint.** `python tools/lint_brain.py` — broken wikilinks, orphans, index coverage, schema coverage (`type`/`data_asof`/`summary` present), and data-bearing pages past their `data_asof` limit. Must report **0 broken, 0 orphans**. Regenerates [[_Brain Health]].
- **Sync.** `python tools/brain_sync.py` — regenerates [[index]] from frontmatter (gated: refuses if <90% of pages carry `summary`), [[Dashboards - Brain Map]], and `brain_index.json` (read by the launcher).
- **Log.** Append `## [YYYY-MM-DD] <verb> | <title>` to [[log]] — verbs in use: `ingest`, `refresh`, `lint`, `extend`, `publish`, `fix`, `structure`. Append from Python; the file is >500 KB. [[GMD Folder Log]] (`14 - Global Macro Database/GMD Folder Log.md`) is a second, folder-scoped build log for the GMD chapters only — renamed from `log.md` on 2026-09-19, because two notes named `log` made every `[[log]]` link ambiguous and the linter silently counted one page too few. **Archive rule:** when [[log]] passes ~250 KB, move whole months older than the previous month, verbatim and in order, into a `Log Archive YYYY-MM to YYYY-MM` page linked from the top of the log (first: [[Log Archive 2026-06 to 2026-07]]). Moving is not editing: no entry is ever rewritten or reordered.

## Wikilinks and hubs

- **A link that cannot be edited gets an alias on its target.** Page titles use the em dash (—); a link typed with an ASCII hyphen, or with a title's build suffix dropped, is broken in Obsidian as well as in lint. When such a link sits inside a dated record (a log entry), do not edit the record — add the linked form to the target page's `aliases: ["..."]` frontmatter (the line after `title:`). Obsidian and `lint_brain.py` both resolve aliases (lint since 2026-09-19). Adding an alias is metadata-only: it does not bump `updated:`.
- **Note names are unique vault-wide.** Obsidian resolves `[[name]]` by file name, so two notes with the same name make every link to either one ambiguous. `lint_brain.py` reports duplicate names as a defect (added 2026-09-19, when `00 - Home/log.md` and `14 - Global Macro Database/log.md` were found colliding).
- **The MOC is a map, the index is the catalog.** [[Global Macro Brain]] is hand-curated: start-here doors, an intent-based navigator, one entry page per folder, the link hubs. It must **not** re-catalog pages — that is what the generated [[index]] is for, and a hand-written catalog drifts (on 2026-09-12 the old MOC still described a 287-series Explorer; the vault had 458). Add a page to the MOC only if it is a folder entry page or answers a question in the navigator; every page reaches the MOC through its folder's entry page and the index.

- Link by the exact note filename: `[[Leading Indicators]]`; alias display text with `[[Name|shown]]`. Link liberally — cross-references are the point; the linter treats any page with zero inbound links as a defect, and [[_Brain Health]] lists the weakest nodes as cross-linking candidates.
- Hubs by inbound links: [[The Global Macros Framework]], [[Risk Management]], [[Analyst System — Live Cockpit (June 2026)]], [[Leading Indicators]], [[Trade Idea Generation Process]]. New pages should link *to* at least one hub and be linked *from* at least one.

## Tooling

- `../tools/xl_inspect.py` — inspects `.xlsx/.xlsm/.xls`: sheets, charts, date ranges, per-column stats. Many sheets are **reverse-chronological**.
- `../tools/xlfind.py` — `find_wb("<name>.xlsx")` resolves a `raw/2.8` workbook move-proof (the user files workbooks into topic subfolders; literal paths have silently broken four loaders).
- `../tools/lint_brain.py`, `../tools/brain_sync.py` — the vault's structural checks and generated pages (above).
- Python is `C:\Users\nikhi\AppData\Local\Python\pythoncore-3.14-64\python.exe` with `PYTHONIOENCODING=ascii:replace`; bare `python` is a broken Store shim.

## See also
- [[Global Macro Brain]] · [[index]] · [[log]] · [[_Brain Health]] · [[Dashboards - Brain Map]] · [[The Global Macros Framework]]
