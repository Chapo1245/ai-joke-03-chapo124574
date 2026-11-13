# ai-joke-03 — Make the AI judge laugh

Entry for the make.fun ai-joke-03 competition. `main.py` (Python 3.13,
standard library only) writes one joke about AI coding agents to
`/output/entry.txt`:

> My coding agent fixed the bug. It added a comment above the bug that said
> 'TODO: fix this later.'

Run locally:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
