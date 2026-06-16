# Changelog — manifest

## v0.2.0 — 2026-06-16

Visual redesign of `generate_pdf.py` — lighter, more editorial, built to breathe.

- **New typographic system** — oversized cover title with 2pt rule underline, eyebrow "Manifest" label, near-black heading palette
- **Section layout** — hairline dividers, stacked label + heading, generous vertical rhythm
- **Bullets** — dot markers, hairline row separators, max-width body text (64ch)
- **Callout** — italic pull-quote with left bar only; no background box, no border-radius
- **Tables** — muted uppercase column headers, hairline rows; no coloured stripe
- **Charts** — native `chart` section type added: matplotlib bar charts rendered as embedded PNG
- **Page numbers** — centred at bottom, barely visible grey
- Renamed skill from `instant-pdf` → `manifest`; updated all triggers and philosophy in SKILL.md
- Added `README.md` and `CHANGELOG.md`
- Removed from `.gitignore` — published to repo

## v0.1.0 — 2026-06-14

Initial build as `instant-pdf`.

- `SKILL.md` with five-phase workflow: read the room → pick format → build spec → generate → present
- `scripts/generate_pdf.py` — weasyprint HTML→PDF renderer
- Section types: `text`, `bullets`, `callout`, `code`, `diagram`, `table`
- Two themes: `minimal` (blue accent) and `rich` (purple accent)
- Cover page, `@page` A4 margins, page numbers
- Auto-installs weasyprint if missing
- Live test: session summary PDF + 6-chart skills analysis PDF
