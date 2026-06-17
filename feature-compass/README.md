# feature-compass

A skill for Claude that aligns you on exactly what a new feature is before a single line of code gets written.

You describe the feature — rough or detailed. The skill asks focused multiple-choice questions to get to a shared, clear understanding: what it does, why it's being added, how it fits the tech, what the UI looks like, and whether it conflicts with anything already planned. The result is a brief you can paste straight into a coding session.

**Target time: 10–15 minutes.**  
**Output: a `[feature]-BRIEF.md` — agreed feature summary, task list, and coding session prompt.**

---

## What it produces

| File | Purpose |
|---|---|
| `[feature-name]-BRIEF.md` | Feature statement, why, tech notes, UI description, roadmap check, ordered task list, and a ready-to-paste coding session prompt |

---

## How to use

Invoke the skill when you're about to add a feature. Either describe it upfront:

> `/feature-compass add dark mode to my React app`

Or invoke bare and it'll ask:

> `/feature-compass`

Every question is multiple-choice with a free-text option. No prose interviews.

The skill reads your project's existing config (`CLAUDE.md`, `.cursorrules`, `ROADMAP.md`, etc.) to skip questions it can already answer from context.

---

## Skill files

```
feature-compass/
├── SKILL.md        # Main skill definition and entry point
├── CHANGELOG.md    # Version history
└── README.md       # This file
```

---

## Design principles

- **Context-first** — reads the session and project config before asking anything; only scans the filesystem if the stack or harness isn't already clear
- **Always multiple-choice** — every question uses `AskUserQuestion`; no prose interrogations
- **Scoping, not building** — produces alignment and a task list, never code
- **Plug-and-play with any harness** — detects Claude Code, Cursor, Windsurf, OpenCode and saves the brief in the right place automatically

---

## Status

Version 0.2.0 — initial release. See [CHANGELOG.md](./CHANGELOG.md).

Feedback welcome via [tumaini.dk](https://tumaini.dk) or GitHub issues.

---

## License

MIT — free to use, adapt, and share. Attribution appreciated.

*By Kim Tumaini Jørgensen*
