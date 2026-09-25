"""Compatibility shim for the vault docs: `python tools/brain_sync.py` == `python -m gms sync`."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gms.cli import main  # noqa: E402

sys.exit(main(["sync", *sys.argv[1:]]))
