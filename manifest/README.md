# manifest

**Give form to the work. Say "manifest this" — the skill reads the room and decides the rest.**

Manifest takes whatever has happened in the current conversation and produces a designed document you can share, hand off, or present. You don't explain what goes in it. The skill figures out what matters, what to cut, and how to structure it.

The PDF is the vehicle. The skill is editorial judgment.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)
![Version](https://img.shields.io/badge/version-0.2.0-blue)

---

## Two modes

**Auto** — say "manifest this" (or just "manifest") and the skill decides everything: format, structure, what gets a section, what gets a callout, what gets cut. It reads the conversation and makes the call.

**Intent-guided** — add direction and the skill executes against it:
- "manifest this as slides for the board" → slides, board-appropriate tone
- "one-pager focused on the cost breakdown" → tight report, cost section leads
- "give this form as a data report" → tables and charts front and centre

In both modes, no back-and-forth. The skill goes immediately.

---

## When to use it

Any point in a session when the work deserves a shareable form. Works for: plans, analyses, decisions, comparisons, research findings, project briefs, pitches, session summaries, data reports with charts and tables.

---

## How it works

The skill runs a five-phase process — all internal, no back-and-forth:

1. **Read the room** — scans the conversation for what was produced and why
2. **Pick a format** — report, slides, data, or mixed
3. **Build the spec** — assembles a JSON content spec, one section per idea
4. **Generate** — runs `scripts/generate_pdf.py` via weasyprint → PDF
5. **Present** — shares the file with a one-sentence summary

---

## Output formats

| Format | Best for |
|---|---|
| `report` | Analysis, findings, summaries, plans |
| `slides` | Presentations, pitches, walkthroughs — one idea per page |
| `data` | Comparisons, tables, metrics, charts |
| `mixed` | Most real work — a bit of everything |

---

## Section types

`text` · `bullets` · `table` · `callout` · `code` · `diagram` · `chart`

Charts are native — bar charts rendered via matplotlib, embedded as PNG.

---

## Visual styles

| Style | Feel |
|---|---|
| `minimal` | Near-black typography, blue chart accent, clean editorial |
| `rich` | Deep purple, more expressive — good for design-forward content |

---

## Dependencies

`generate_pdf.py` auto-installs on first run:

```bash
pip install weasyprint matplotlib --break-system-packages
```

---

## Folder structure

```
manifest/
├── SKILL.md              # Skill entry point
├── README.md             # This file
├── CHANGELOG.md          # Version history
└── scripts/
    └── generate_pdf.py   # HTML → PDF renderer (weasyprint + matplotlib)
```

---

## Author

Kim Tumaini Jørgensen — [tumaini.dk](https://tumaini.dk)
