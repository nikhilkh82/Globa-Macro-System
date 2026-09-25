from datetime import date
from pathlib import Path

import pytest

from gms.brain import lint, log, sync, vault


def page(meta: dict, body: str) -> str:
    fm = "\n".join(f"{k}: {v}" for k, v in meta.items())
    return f"---\n{fm}\n---\n\n{body}\n"


@pytest.fixture
def brain(tmp_path: Path) -> Path:
    b = tmp_path / "brain"
    (b / "00 - Home").mkdir(parents=True)
    (b / "01 - Framework").mkdir()
    (b / "09 - Synthesis").mkdir()
    (b / "00 - Home" / "Global Macro Brain.md").write_text(
        page({"title": "Global Macro Brain", "type": "meta", "data_asof": "n/a", "summary": '"map"'},
             "[[The Global Macros Framework]] · [[Regime — Live|live regime]] · [[index]] · [[_Vault Schema & Conventions]]"), encoding="utf-8")
    (b / "00 - Home" / "_Vault Schema & Conventions.md").write_text(
        page({"title": "_Vault Schema & Conventions", "type": "reference", "data_asof": "n/a", "summary": '"schema"'},
             "Start at [[Global Macro Brain]]."), encoding="utf-8")
    (b / "00 - Home" / "log.md").write_text(page({"title": "log", "type": "meta", "data_asof": "n/a", "summary": '"log"'}, "# log"), encoding="utf-8")
    (b / "01 - Framework" / "The Global Macros Framework.md").write_text(
        page({"title": "The Global Macros Framework", "type": "domain", "data_asof": "n/a", "summary": '"method"'},
             "See [[Regime — Live#Current]] and `[[not a link]]`."), encoding="utf-8")
    (b / "09 - Synthesis" / "Regime — Live.md").write_text(
        page({"title": "Regime — Live", "aliases": '["Regime - Live"]', "type": "live-read", "data_asof": "2026-06-01",
              "summary": '"Reflation"'}, "Back to [[The Global Macros Framework]]. Report: [[Report.html]]"), encoding="utf-8")
    return b


def test_links_parse_alias_heading_and_skip_code():
    assert vault.extract_links("[[A|x]] [[B#h]] ![[C.png]] `[[D]]`\n```\n[[E]]\n```") == ["A", "B", "C.png"]


def test_lint_clean_vault_resolves_aliases(brain: Path):
    (brain / "01 - Framework" / "The Global Macros Framework.md").write_text(
        page({"title": "The Global Macros Framework", "type": "domain", "data_asof": "n/a", "summary": '"method"'},
             "[[Regime - Live]]"), encoding="utf-8")
    sync.main(brain, today=date(2026, 6, 10))
    rep = lint.run(brain, today=date(2026, 6, 10))
    assert rep.broken == [] and rep.orphans == [] and rep.ok
    assert rep.missing_assets == [{"page": "Regime — Live", "target": "Report.html"}]


def test_lint_flags_broken_orphan_and_stale(brain: Path):
    (brain / "09 - Synthesis" / "Lonely.md").write_text(
        page({"title": "Lonely", "type": "strategy-system", "data_asof": "2026-01", "summary": '"x"'}, "[[Nowhere]]"), encoding="utf-8")
    rep = lint.run(brain, today=date(2026, 9, 25))
    assert {"page": "Lonely", "target": "Nowhere"} in rep.broken
    assert rep.orphans == ["Lonely"]
    stale = {s["page"] for s in rep.stale}
    assert stale == {"Lonely", "Regime — Live"}  # 267 > 120 days; 116 > 45 days
    assert not rep.ok


def test_index_links_do_not_count_as_inbound(brain: Path):
    (brain / "09 - Synthesis" / "Lonely.md").write_text(
        page({"title": "Lonely", "type": "meta", "data_asof": "n/a", "summary": '"x"'}, "body"), encoding="utf-8")
    sync.main(brain, today=date(2026, 9, 25))
    assert "[[Lonely]]" in (brain / "00 - Home" / "index.md").read_text(encoding="utf-8")
    assert lint.run(brain).orphans == ["Lonely"]


def test_sync_writes_catalog_and_gates_on_summaries(brain: Path):
    n = sync.main(brain, today=date(2026, 9, 25))
    text = (brain / "00 - Home" / "index.md").read_text(encoding="utf-8")
    assert n == 5 and "## 09 - Synthesis" in text and "### live-read (1)" in text
    for i in range(3):
        (brain / "09 - Synthesis" / f"Bare {i}.md").write_text("no frontmatter", encoding="utf-8")
    with pytest.raises(sync.GateError):
        sync.main(brain)


def test_log_is_append_only(brain: Path):
    log.append(brain, "fix", "one", when=date(2026, 9, 25))
    log.append(brain, "lint", "two", when=date(2026, 9, 26))
    assert log.tail(brain, 2) == ["## [2026-09-25] fix | one", "## [2026-09-26] lint | two"]
    with pytest.raises(ValueError):
        log.append(brain, "rewrite", "nope")
