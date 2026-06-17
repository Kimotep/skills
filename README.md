# Kimotep Skills

**A curated library of AI prompt systems** — structured prompts that help you think clearly *before* you design, build, plan, or write.

Each one is a self-contained system prompt (`SKILL.md`) — paste it into ChatGPT, Claude, Gemini, or any AI assistant that takes custom instructions. Instead of guessing what to ask, it asks *you* — in the right order — then hands back something concrete: a brief, a design spec, a project plan, or a new writer skill in your own voice.

If you're using Claude specifically, each folder can also be installed directly as a Claude Skill — see [Quick start](#quick-start).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
![Skills](https://img.shields.io/badge/skills-6-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## See it in action

You say: *"I want to build a habit tracker app but I'm not sure what to focus on first."*
→ context-compass asks a few quick questions (what's already decided, what you haven't thought about, where this is going)
→ You get: a ready-to-run brief — goal, context, one concrete first step — in under five minutes.

---

## Who this is for

- **Solo builders & indie hackers** who want to scope an idea before opening an editor
- **Apple platform developers & designers** who want native-feeling SwiftUI/UIKit UI without guessing
- **Founders & PMs** planning multi-agent or AI workflow systems before writing any code
- **Writers, marketers, and founders** who want an AI that writes in *their* voice, not a generic one
- **Anyone mid-session** who wants to turn what they're working on into a polished, shareable PDF — without re-explaining the content

---

## Quick start

1. Pick a skill below and open its folder.
2. Either:
   - copy the contents of its `SKILL.md` and paste it as a system prompt or custom 
     instructions in your AI assistant of choice (ChatGPT, Claude, Gemini, etc.), **or**
   - if you're using Claude: install the folder directly as a Skill in Claude Code, Cowork, 
     or Claude Desktop.
3. Describe what you're working on — the skill takes it from there with guided questions.

No setup, no dependencies, no API keys.

---

## Skills

| Skill | Use it when... | Produces |
|---|---|---|
| [**context-compass**](./context-compass/) | You have a rough idea and want to sharpen it into a clear brief in a few minutes | A ready-to-run brief — or jumps straight into the work if you say "start now" |
| [**keen-eyeos**](./keen-eyeos/) | You're designing for iOS, macOS, iPadOS, watchOS, or visionOS and want native-feeling UI, component picks, or HIG-aligned screens | Design plan, wireframes, dev handover spec, device mockup |
| [**socratic-product**](./socratic-product/) *(socratic-agentic-workflow)* | You have an idea for an AI agent or multi-agent system and want to plan it before writing code | An indexed plan: mission, agent specs with contracts and failure paths, a starter repo scaffold, system logic, a handover doc — plus a harness root config file (`CLAUDE.md`, `.cursorrules`, etc.) ready to drop in the repo |
| [**voice-compass**](./voice-compass/) | You want an AI writer that sounds like you — for a blog, brand, or your own voice | An installable writer skill: voice profile + per-format reference docs |
| [**manifest**](./manifest/) | You want to give the current work a shareable form — say "manifest this" and the skill reads the room and decides the rest, or add intent ("as slides", "one-pager for the board") and it executes against that | A designed PDF: report, slides, data, or mixed — light, never dense |
| [**feature-compass**](./feature-compass/) | You're adding a new feature to an existing project and want to align on exactly what it is before building starts | A `[feature]-BRIEF.md` — agreed feature summary, task list, and a ready-to-paste coding session prompt |

---

## Real-world examples

- **"I have a vague idea for a side project and don't know where to start."** → `context-compass` turns it into a brief in under five minutes, or starts building right away.
- **"My SwiftUI settings screen feels off, but I can't say why."** → `keen-eyeos` diagnoses the issue and recommends the native fix, with platform-aware reasoning.
- **"I want to build a multi-agent research tool but don't want to start coding blind."** → `socratic-product` runs a 30-minute structured interview (all multiple-choice) and hands you an indexed plan plus a ready-to-drop harness config file (`CLAUDE.md`, `.cursorrules`, etc.) for your coding tool.
- **"I want my AI to write newsletter drafts that actually sound like me."** → `voice-compass` interviews you (and reads your writing samples) and outputs a new, installable "writes like you" skill.
- **"Manifest this."** → `manifest` reads the current conversation, decides what form the work should take, and produces a designed document — report, slides, or data — in one call. Or add intent: _"as slides for the board"_ and it executes against that.
- **"I want to add a search feature to my app."** → `feature-compass` interviews you (always multiple-choice), reads your project config, and hands back a brief with task list and a ready-to-paste coding session prompt.

---

## Repo structure

```
.
├── context-compass/     # Quick idea-sharpening warm-up
├── keen-eyeos/           # Apple platform design companion
├── socratic-product/     # Agentic system planning interview
├── voice-compass/         # Personalized writer skill builder
├── manifest/              # Turn current work into a polished PDF
├── feature-compass/       # Scope and align on a new feature before building
├── LICENSE
└── README.md
```

Each skill folder follows the same pattern: `SKILL.md` (entry point — paste as a system prompt anywhere, or install directly if you're using Claude), `README.md` (full docs), `CHANGELOG.md` (version history), and a `references/` or `scripts/` folder where needed.

---

## Shared design pattern

`socratic-product` and `voice-compass` share an operating pattern — a time-boxed Socratic interview, *always-ask-never-assume*, assumption classification, and pause/resume via a `STATE.md` checkpoint. One plans agentic systems; the other builds personalized writers.

---

## Status

All skills are MIT-licensed and actively maintained. See each skill's `CHANGELOG.md` for full version history.

| Skill | Version |
|---|---|
| context-compass | 0.2.0 |
| keen-eyeos | 1.0 |
| socratic-product | 0.6.0 |
| voice-compass | 0.3.0 |
| manifest | 0.2.0 |
| feature-compass | 0.2.0 |

---

## Author

Kim Tumaini Jørgensen — [tumaini.dk](https://tumaini.dk)

Feedback and issues welcome via [tumaini.dk](https://tumaini.dk) or GitHub Issues.

---

MIT License — free to use, adapt, and share.
