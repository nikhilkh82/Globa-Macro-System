"""Global Macro System — the Global Macro Brain vault plus the engines that keep it live.

Layers (the LLM-Wiki pattern):
    brain/      the Obsidian vault (LLM-owned markdown)
    gms.brain   lint / sync / log tooling for the vault
    gms.data    free-data loaders (FRED, Yahoo) with a local cache
    gms.engine  the regime and cross-asset engines documented in the vault
"""

__version__ = "0.1.0"
