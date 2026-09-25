# Global Macro System — read this first

This repo is an instance of the **LLM-Wiki** pattern. The wiki is `brain/` (the Global Macro Brain, an Obsidian vault). The tools are the `gms` Python package. The vault's own schema is `brain/00 - Home/_Vault Schema & Conventions.md`. **Read it before touching a page.**

| Layer | Where | Who writes it |
|---|---|---|
| Raw sources | OneDrive `Global Macro Hedge Fund Strategy/raw/` (15 GB, not in git) | the user; immutable |
| Wiki | `brain/` | the LLM agent |
| Schema | `brain/00 - Home/_Vault Schema & Conventions.md` + this file | co-evolved |
| Tools | `gms/` (`python -m gms …`) | the LLM agent |
| Engine outputs | `outputs/` (JSON + dated notes; git-ignored except `.gitkeep`) | `gms regime` / `gms pulse` |

## Non-negotiables

1. **Dated records are never rewritten.** This covers a `## Live read — YYYY-MM-DD` section, a log entry, and any value under a supersession banner. To update, add a newer dated section *above* the old one and say what it supersedes.
2. **`data_asof:` is not `updated:`.** `updated` records when the file was last touched. `data_asof` records when the page's data was last checked against its source. Lint reads `data_asof`, using the clock for each page type: `live-read` and `dashboard-page` 45 days, `strategy-system` 120 days.
3. **`00 - Home/index.md`, `brain_index.json` and `_Brain Health.md` are generated.** Never edit them by hand. Edit the page's frontmatter, then run sync or lint.
4. **Finish every vault change with this ritual:**
   ```
   python -m gms lint        # must report 0 broken, 0 orphans, 0 duplicates
   python -m gms sync
   python -m gms log <verb> "<title>" --body "<what changed>"
   ```
   The allowed verbs are `ingest refresh lint extend publish fix structure query`.
5. **Engines never edit vault pages.** `gms regime` and `gms pulse` write only to `outputs/`. The refresh step is a person or agent reading those outputs and updating the live-read and strategy-system pages under rule 1.
6. **Link by exact note filename.** Page titles use the em dash (—). If a link typed with a hyphen sits inside a dated record, don't edit the record. Add the hyphen form to the target page's `aliases:` instead.
7. **Keep machine paths out of code.** Resolve everything through `gms/paths.py`. You can override locations with the `GMS_BRAIN`, `GMS_OUTPUTS` and `GMS_CACHE` environment variables.

## Commands

```
pip install -e .[dev]
python -m pytest                 # offline; synthetic fixtures only
python -m gms regime             # FRED (INDPRO, PAYEMS, CPIAUCSL, TB3MS) + Yahoo ETFs -> outputs/regime_latest.json
python -m gms pulse              # Yahoo daily, 7 instruments -> outputs/macro_pulse_latest.json
python -m gms refresh            # regime + pulse + lint + sync
```

- Set `FRED_API_KEY` to use FRED's keyed API. Without it, `gms` falls back to the public fredgraph CSV.
- Pulls are cached in `.cache/` for 12 hours. If a pull fails, `gms` falls back to the last good cached copy.
- The Claude Code cloud sandbox blocks FRED and Yahoo, so run the engines on a machine with open internet. CI runs only tests and lint.

## What is not in git

The vault's binary deliverables are not in git. These are the docx, pdf, html and ipynb reports in folders `10`–`14`, and the HTML dashboards. They are built by the desktop builder scripts, which stay on OneDrive. Lint counts links to those files as *asset links not in repo*, not as broken links. The archived logs before this migration also stay on OneDrive: see `brain/00 - Home/log.md`.

`brain/00 - Home/Dashboards - Brain Map.md` is a **frozen snapshot**. The desktop `brain_sync.py` generates it from the dashboards on disk, and they aren't in git, so `gms sync` doesn't rebuild it. Lint treats it as an ordinary page, so its links count as inbound links. Refresh it by re-copying it from OneDrive after a desktop sync. `Log Archive 2026-06 to 2026-07.md` is a placeholder page that points to the verbatim archive on OneDrive.
