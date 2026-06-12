# Kimotep Skills

A collection of structured skills for Claude — designed to improve how you think before you build, design, or ship.

Each skill is a prompt system that asks the right questions in the right order, then produces outputs you can actually use.

---

## Skills

| Skill | What it does | Output |
|---|---|---|
| [keen-eyeos](./keen-eyeos/) | Apple platform design companion — guides intent, structure, and component selection | Design plan, wireframes, dev spec, mockup |
| [socratic-product](./socratic-product/) (socratic-agentic-workflow) | Pre-code agentic system design via structured Socratic interview | Mission, agents, scaffold, logic, handover docs |
| [tumaini-voice](./tumaini-voice/) | Builds a personalized writer skill via structured Socratic interview, optionally informed by writing samples | An installable writer skill: voice profile + per-format reference docs |

---

## The tumaini family

`socratic-agentic-workflow` and `tumaini-voice` share an operating pattern — a time-boxed 
Socratic interview, always-ask-never-assume, assumption classification, and pause/resume via 
a `STATE.md` checkpoint. One plans agentic systems; the other builds personalized writers. 
Future skills following this pattern will be added here under the same `tumaini-` branding.

---

## How to use

Each skill folder contains a `SKILL.md`. Paste it as a system prompt in Claude, or load it as a skill in Claude Code.

---

## Author

Kim Tumaini Jørgensen — [tumaini.dk](https://tumaini.dk)

---

MIT License — free to use, adapt, and share.
