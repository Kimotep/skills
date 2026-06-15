# socratic-agentic-workflow

A skill for Claude that runs a structured, time-boxed interview to design an agentic system 
— before any code is written.

You describe an idea. The skill asks the right questions. You end up with a coherent set of 
linked Markdown documents capturing mission, agent roles, file scaffold, system logic, and 
a handover brief ready for a builder or coding agent.

**Target session time: ~30 minutes.**  
**Output: 6 linked MD files, named after your project.**

---

## What it produces

| File | Purpose |
|---|---|
| `[slug]-README.md` | Index — links the other five files with a one-line description and read order |
| `[slug]-MISSION.md` | Why the system exists, success criteria, scope boundaries, how it differs from comparable tools |
| `[slug]-AGENTS.md` | Agent roles specced with responsibilities/boundaries, I/O contracts, tool scope, coordination role, and failure handling |
| `[slug]-SCAFFOLD.md` | Starter repo structure — planning docs plus a product layer tailored to the project's type and stack, with tooling choices grounded in current best practice |
| `[slug]-LOGIC.md` | System flow diagram and logic notes |
| `[slug]-HANDOVER.md` | Builder entry point, definition of done, build order with MVP cut line, pitfalls to watch for, first prompt |
| `[slug]-STATE.md` | *(conditional)* Session checkpoint if the interview is paused before completion |

---

## How to use

Install the packaged `.skill` file in a Claude environment that supports skill loading, or 
paste the contents of `SKILL.md` as a system prompt.

Then just start describing your idea. The skill takes it from there.

---

## Skill files

```
socratic-agentic-workflow/
├── SKILL.md         # Main skill definition and entry point
├── INTERVIEW.md     # Question themes, pacing, drift detection, pause/resume
├── SYNTHESIS.md     # Reflection, assumption classification, and confirmation phase
├── OUTPUT.md        # File generation rules and templates
├── references/
│   └── scaffold-patterns.md  # Starter repo skeletons by project type
├── CHANGELOG.md     # Version history
└── README.md        # This file
```

---

## Design principles

- **Always asks, never assumes** — inference level is minimal by design
- **Catches contradictions** — surfaces inconsistencies before they become build problems  
- **Token efficient** — output is lean; every line earns its place
- **Handover-ready** — output is structured for Cursor, other coding agents, or a human builder
- **Scaffold matches the project** — the starter repo structure is picked from a library of 
  patterns (web app, CLI, browser extension, agent pipeline, API, library) based on what's 
  actually being built, not a generic template
- **Grounded in current best practice** — an architect pass checks current conventions, 
  tooling, and known pitfalls for any named framework via web search before finalizing the 
  scaffold and handover
- **Agents meet a quality bar** — every agent role is checked for a single responsibility, 
  an I/O contract, a tool/context scope, a coordination role, and a failure path before 
  `[slug]-AGENTS.md` is written
- **Mission is checked against reality** — a quick web search confirms whether something 
  comparable already exists, and how this differs, when the idea has an obvious comparison 
  point
- **Time-boxed** — the whole session fits in 30 minutes, with a graceful pause/resume if an 
  idea isn't fully formed yet

---

## Status

Version 0.5.0. See [CHANGELOG.md](./CHANGELOG.md). v0.2.0 came from dogfooding the skill on a 
real project, written up at [Putting my /skills to use](https://www.tumaini.dk/posts/scraper).

Feedback welcome via [tumaini.dk](https://tumaini.dk) or GitHub issues.

---

## License

MIT — free to use, adapt, and share. Attribution appreciated.

*By Kim Tumaini Jørgensen*
