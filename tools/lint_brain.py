"""Compatibility shim for the vault docs: `python tools/lint_brain.py` == `python -m gms lint`."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gms.cli import main  # noqa: E402

sys.exit(main(["lint", *sys.argv[1:]]))
