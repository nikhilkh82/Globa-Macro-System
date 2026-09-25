"""Repo-relative paths. Every tool resolves from here — never from a literal machine path."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAIN = Path(os.environ.get("GMS_BRAIN", ROOT / "brain"))
HOME = BRAIN / "00 - Home"
OUTPUTS = Path(os.environ.get("GMS_OUTPUTS", ROOT / "outputs"))
CACHE = Path(os.environ.get("GMS_CACHE", ROOT / ".cache"))
