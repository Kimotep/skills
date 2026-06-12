# tumaini-voice

A skill for Claude that interviews you about how you write, then builds a new Claude skill 
that writes the same way.

You describe the writer you need — a brand voice, a personal voice, a copywriter for a 
project. The skill asks the right questions, optionally reads writing samples you provide, 
and produces an installable skill: a personalized writer ready to drop into any project to 
draft blog posts, marketing copy, emails, social posts, or messages in your voice.

**Target session time: ~30 minutes.**  
**Output: a new, installable skill — not a style guide.**

---

## What it produces

| File | Purpose |
|---|---|
| `[slug]/SKILL.md` | Entry point for the generated writer — voice at a glance, routing to references |
| `[slug]/references/voice-profile.md` | Full voice profile — tone, audience, structure, vocabulary, boundaries |
| `[slug]/references/[content-type].md` | One per content type selected (blog, marketing, email, social, personal messaging, or custom) |
| `[slug]/README.md` | What this writer is and how to use it |
| `[slug]-STATE.md` | *(conditional)* Session checkpoint if the interview is paused before completion |

---

## How to use

Install the packaged `.skill` file in a Claude environment that supports skill loading, or 
paste the contents of `SKILL.md` as a system prompt.

Then describe the writer you need. If you have a piece or two of writing that already sounds 
like you, paste or attach them — optional, but it sharpens the result.

The output is itself a skill: drop the generated `[slug]/` folder into any project, or 
package it as `.skill` for easy install.

---

## Skill files

```
tumaini-voice/
├── SKILL.md         # Main skill definition and entry point
├── INTERVIEW.md     # Question themes, sample analysis, pacing, pause/resume
├── SYNTHESIS.md     # Reflection, assumption classification, and confirmation phase
├── OUTPUT.md        # Naming, structure, and templates for the generated writer skill
├── CHANGELOG.md     # Version history
└── README.md        # This file
```

---

## Design principles

- **Always asks, never assumes** — inference level is minimal by design
- **Samples are evidence, not gospel** — writing samples are checked against stated tone, not 
  used to silently override it
- **Classifies assumptions** — flags which guesses are safe to defer and which would shape 
  the whole voice profile
- **Token efficient** — output is lean; every line earns its place
- **Time-boxed, with pause/resume** — the whole session fits in 30 minutes, with a graceful 
  pause if a voice isn't fully articulated yet
- **Output is installable** — the result is a working skill, not a document to remember to 
  paste in

---

## Shares a design pattern with socratic-agentic-workflow

This skill shares its operating principles with 
[socratic-agentic-workflow](../socratic-product/README.md) — same Socratic interview pattern, 
same assumption-classification and pause/resume design. Where socratic-agentic-workflow plans 
*systems*, tumaini-voice builds *writers*.

---

## Status

Version 0.1.0 — initial release. See [CHANGELOG.md](./CHANGELOG.md).

Feedback welcome via [tumaini.dk](https://tumaini.dk) or GitHub issues.

---

## License

MIT — free to use, adapt, and share. Attribution appreciated.

*By Kim Tumaini Jørgensen*
