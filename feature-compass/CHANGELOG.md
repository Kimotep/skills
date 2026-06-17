# Changelog

## v0.2.0 — initial release

- Context-first entry: reads session and project config before touching the filesystem;
  only scans for `CLAUDE.md`, `.cursorrules`, `ROADMAP.md`, etc. if stack/harness not
  already clear from the active session
- Six-area interview, all via `AskUserQuestion` (multiple-choice + freeform): what it does,
  why now, tech fit, UI, roadmap and conflicts, output format
- UI definition pass: `show_widget` mockup, text description, or TBD
- Harness detection → automatic brief output location (Claude Code, Cursor, Windsurf,
  OpenCode, or ask user)
- Output: `[feature-name]-BRIEF.md` with feature statement, why, tech notes, UI,
  roadmap check, ordered task list, and a ready-to-paste coding session prompt
