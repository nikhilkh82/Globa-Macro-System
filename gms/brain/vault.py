"""Load the vault: pages, frontmatter and wikilinks.

The schema is `brain/00 - Home/_Vault Schema & Conventions.md`. Only the parts the
tools need are modelled here: the frontmatter contract and Obsidian link syntax.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
# [[target]], [[target|alias]], [[target#heading]], ![[embed]]
WIKILINK = re.compile(r"!?\[\[([^\[\]]+?)\]\]")
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")

# Pages whose links are generated or which are roots — never counted as inbound
# evidence (index links everything) and never flagged as orphans.
GENERATED = {"index", "_Brain Health", "Dashboards - Brain Map"}
ROOTS = {"Global Macro Brain", "index", "log", "_Brain Health", "Dashboards - Brain Map"}

PAGE_TYPES = ("domain", "reference", "live-read", "strategy-system", "dashboard-page", "deep-dive", "meta")
# Lint clocks in days, by page type (schema: "Page types and what each is allowed to claim").
CLOCKS = {"live-read": 45, "dashboard-page": 45, "strategy-system": 120}


@dataclass
class Page:
    path: Path
    name: str  # note name = file stem; Obsidian resolves [[name]] by this
    folder: str
    meta: dict
    body: str
    links: list[str] = field(default_factory=list)

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.name)

    @property
    def type(self) -> str | None:
        t = self.meta.get("type")
        return str(t) if t else None

    @property
    def summary(self) -> str | None:
        s = self.meta.get("summary")
        return str(s).strip() if s else None

    @property
    def data_asof(self) -> str | None:
        v = self.meta.get("data_asof")
        return None if v is None else str(v)

    @property
    def aliases(self) -> list[str]:
        a = self.meta.get("aliases") or []
        return [str(x) for x in (a if isinstance(a, list) else [a])]


def parse(text: str) -> tuple[dict, str]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return (meta if isinstance(meta, dict) else {}), text[m.end():]


def link_target(raw: str) -> str:
    """`Name#heading|alias` -> `Name`."""
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target.replace("\\", "")  # `[[a\|b]]` inside tables escapes the pipe


def extract_links(body: str) -> list[str]:
    body = INLINE_CODE.sub("", FENCE.sub("", body))
    return [t for t in (link_target(m) for m in WIKILINK.findall(body)) if t]


def load(brain: Path) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for path in sorted(brain.rglob("*.md")):
        rel = path.relative_to(brain)
        if any(part.startswith(".") for part in rel.parts):
            continue
        meta, body = parse(path.read_text(encoding="utf-8"))
        page = Page(path=path, name=path.stem, folder=rel.parts[0] if len(rel.parts) > 1 else "",
                    meta=meta, body=body, links=extract_links(body))
        if page.name in pages:
            # Duplicate note names make [[name]] ambiguous; keep both visible to lint.
            pages[f"{page.name}\x00{rel}"] = page
        else:
            pages[page.name] = page
    return pages


def resolver(pages: dict[str, Page]) -> dict[str, str]:
    """Lower-cased note name / alias -> canonical note name (Obsidian resolves only these)."""
    names: dict[str, str] = {}
    for key, p in pages.items():
        canonical = key.split("\x00", 1)[0]
        for k in [canonical, *p.aliases]:
            names.setdefault(k.lower(), canonical)
    return names


def resolve(target: str, names: dict[str, str]) -> str | None:
    t = target.strip()
    if t.lower().endswith(".md"):
        t = t[:-3]
    t = t.rsplit("/", 1)[-1]  # [[folder/Note]] resolves by note name
    return names.get(t.lower())


ASSET_EXT = re.compile(r"\.(html?|pdf|docx?|xlsx?|pptx?|ipynb|png|jpe?g|gif|svg|json|csv|js)$", re.I)


def is_asset(target: str) -> bool:
    return bool(ASSET_EXT.search(target))
