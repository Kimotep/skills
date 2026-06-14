# context-compass

A skill for Claude that's a fast, always-on warm-up for starting anything with an agent.

You describe what's on your mind — rough is fine. A few quick multiple-choice-plus-freeform
questions sharpen it, surface a couple of things you probably haven't decided yet, and the
result is a brief — ready to start on right here, or hand off to another chat or agent.

**Target time: a few minutes.** Use it constantly, not just for big things.

---

## What it produces

A ready-to-run brief, shown directly in chat:

```
[What needs doing]

Context: [what's already in place]

Decided: [resolved angles from the "open it up" step]

Constraints: [if any]

First step: [one concrete action]
```

Then, depending on where you said it's going:

- **Start now** — the skill skips straight from the brief into doing the first step, in
  this same session, using the brief as its operating spec
- **Hand off / someone else / not sure** — you're asked whether to use it as-is, adjust it,
  or save it as `[slug]-BRIEF.md`

---

## How to use

Install the packaged `.skill` file in a Claude environment that supports skill loading, or
paste the contents of `SKILL.md` as a system prompt.

Then just say what's on your mind. The skill takes it from there — a handful of short
questions, each with options plus room to answer your own way.

---

## Skill files

```
context-compass/
├── SKILL.md              # Main skill definition, flow, and output format
├── references/
│   └── angles.md         # Lens library for the "open it up" step
├── CHANGELOG.md           # Version history
└── README.md              # This file
```

---

## Design principles

- **Multiple choice + freeform, always** — no blank-box questions, but never boxed in either
- **Surfaces what's missing** — the "open it up" step exists because the most useful thing
  this skill does is point out what you haven't decided yet
- **Plain language, minimal words** — no jargon, no explaining why a question is being asked
- **Fast by default** — a few minutes, not a session. When a task is clearly bigger, it says
  so and points to a deeper skill instead of forcing a quick pass

---

## When to reach for something deeper instead

context-compass is intentionally light. For a 30-minute structured interview that produces a
full set of planning documents or a personalized writer skill, see
[socratic-agentic-workflow](../socratic-product/README.md) or
[tumaini-voice](../tumaini-voice/README.md). context-compass will say so if a task looks like
it needs that level of depth.

---

## Status

Version 0.2.0. See [CHANGELOG.md](./CHANGELOG.md).

Feedback welcome via [tumaini.dk](https://tumaini.dk) or GitHub issues.

---

## License

MIT — free to use, adapt, and share. Attribution appreciated.

*By Kim Tumaini Jørgensen*
