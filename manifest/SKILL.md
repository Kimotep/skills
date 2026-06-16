---
name: manifest
description: >
  Use this skill whenever the user wants to give form to the work in the current conversation —
  whether or not they know what they want. Triggers include "manifest this", "make this a
  document", "give this form", "ship this as a PDF", "make something I can share", "I want a
  one-pager", "turn this into something presentable", or simply "manifest". Two modes: (1)
  auto — the user says "manifest this" and the skill decides everything — format, structure,
  what to include, what to cut; (2) intent-guided — the user adds direction ("manifest this
  as slides for the board", "make a one-pager focused on the technical approach") and the
  skill executes against that intent. In both cases the skill reads context automatically.
  Output is a polished PDF — designed, never dense.
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.2.0
  outputs:
    - A designed PDF — light, editorial, built around the work not the format
---

# Manifest

Give form to the thinking. Whatever has happened in this conversation — a plan, an analysis,
a decision, a comparison, a build — manifest it as something the user can hold, share, or
hand off.

The PDF is the vehicle. The skill is editorial judgment: what matters, what to cut, how to
structure it so the reader gets the point immediately.

The output should feel **designed, not generated**. Light, not dense. Every page breathes.

The skill runs through `scripts/generate_pdf.py`. Read it before generating.

---

## Two modes

**Auto** — user says "manifest this" (or similar) with no further direction.
The skill makes all the calls: what the document covers, what format it takes, what gets
a full section vs. a callout vs. nothing. State the intent out loud before proceeding —
_"Manifesting a [type] doc covering [topics]."_ — then go immediately.

**Intent-guided** — user adds direction: _"manifest this as slides for the board"_,
_"one-pager focused on the cost breakdown"_, _"give this form as a data report"_.
Honor the intent exactly. It overrides the skill's defaults on format, scope, and emphasis.

In both cases: no back-and-forth, no confirmation. Start unless the conversation is empty.

---

## Phase 1: Read the room

Scan the conversation. Identify:

1. **What exists** — what was produced, discussed, or decided?
2. **What it's for** — external sharing? Internal reference? Pitch? Quick handoff?
   This shapes density and tone above everything else.
3. **User intent** — did they specify format, audience, or angle? If yes, that wins.
   If no, choose based on the content.
4. **Style signal** — did they say anything about look and feel? If not, default to
   `minimal`. Use `rich` when content is visual-heavy or design-forward.

---

## Phase 2: Pick a format

| Format | When | Feel |
|---|---|---|
| **report** | Analysis, findings, summaries, plans | Sectioned, readable, editorial |
| **slides** | Things meant to be walked through, presented, pitched | One idea per page, visual |
| **data** | Comparisons, tables, metrics, charts | Numbers front, callouts for the headline |
| **mixed** | Most real work — a bit of everything | Flexible, section-by-section |

Default to **mixed** when in doubt. Default to **report** for short, focused output.

---

## Phase 3: Build the spec

Assemble a Python dict. Every section should earn its place — don't pad.

```python
spec = {
    "title": "...",
    "subtitle": "...",       # optional — date, context, project name
    "style": "minimal",      # "minimal" | "rich"
    "type": "mixed",         # report | slides | data | mixed
    "sections": [
        {
            "heading": "...",
            "type": "text",    # text | bullets | table | code | callout | diagram | chart
            "content": "..."   # string (text/code/diagram) | list (bullets) | list-of-dicts (table) | dict (chart)
        }
    ]
}
```

**Section types:**

- `text` — prose. Keep it tight.
- `bullets` — `content` is a list of strings.
- `table` — `content` is `[{"Col": "val", ...}, ...]`
- `callout` — editorial pull-quote. One insight only — no padding.
- `code` — code block. `content` is a string.
- `diagram` — Mermaid source. Renders as a styled block.
- `chart` — bar chart. `content` is `{"labels": [...], "values": [...], "ylabel": "..."}`

For **slides**: each section = one slide. One heading, one type, brief content.

---

## Phase 4: Generate

```bash
python scripts/generate_pdf.py \
  --spec-file /tmp/manifest_spec.json \
  --output /path/to/output.pdf
```

---

## Phase 5: Present

Share the file. One sentence on what it covers. Note anything omitted and why.

---

## Editorial principles

- **Lead with the point.** Most important thing first.
- **Never fill a page for the sake of it.** Thin content = callout or bullet, not a padded paragraph.
- **Callouts are for one thing.** The single most important insight. If everything is a callout, nothing is.
- **Every page breathes.** Whitespace is design, not waste.
