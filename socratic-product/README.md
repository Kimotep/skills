# socratic-agentic-workflow

A skill for Claude that runs a structured, time-boxed interview to design an agentic system 
— before any code is written.

You describe an idea. The skill asks the right questions. You end up with a coherent set of 
linked Markdown documents capturing mission, agent roles, file scaffold, system logic, and 
a handover brief ready for a builder or coding agent.

**Target session time: ~30 minutes.**  
**Output: 5 linked MD files, named after your project.**

---

## What it produces

| File | Purpose |
|---|---|
| `[slug]-MISSION.md` | Why the system exists, success criteria, scope boundaries |
| `[slug]-AGENTS.md` | Agent roles, responsibilities, coordination model |
| `[slug]-SCAFFOLD.md` | Recommended folder and file structure |
| `[slug]-LOGIC.md` | System flow diagram and logic notes |
| `[slug]-HANDOVER.md` | Builder entry point, open questions, first prompt |

---

## How to use

Paste the contents of `SKILL.md` as a system prompt, or invoke it as a skill in a Claude 
environment that supports skill loading.

Then just start describing your idea. The skill takes it from there.

---

## Skill files

```
socratic-agentic-workflow/
├── SKILL.md         # Main skill definition and entry point
├── INTERVIEW.md     # Question themes, pacing, drift detection
├── SYNTHESIS.md     # Reflection and confirmation phase
├── OUTPUT.md        # File generation rules and templates
└── README.md        # This file
```

---

## Design principles

- **Always asks, never assumes** — inference level is minimal by design
- **Catches contradictions** — surfaces inconsistencies before they become build problems  
- **Token efficient** — output is lean; every line earns its place
- **Handover-ready** — output is structured for Cursor, other coding agents, or a human builder
- **Time-boxed** — the whole session fits in 30 minutes

---

## Status

Version 0.1.0 — initial draft. Built collaboratively via Socratic session.  
Feedback welcome via [tumaini.dk](https://tumaini.dk) or GitHub issues.

---

## License

MIT — free to use, adapt, and share. Attribution appreciated.

*By Kim Tumaini Jørgensen*
