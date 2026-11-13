#!/usr/bin/env python3
"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

The joke is fixed text, so the program is deterministic: every run writes
the same bytes. It honours MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

JOKE = "My coding agent fixed the bug. It added a comment above the bug that said 'TODO: fix this later.'"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
