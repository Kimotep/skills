---
name: tumaini-voice
description: >
  Use this skill when a user wants to build a personalized writing assistant — a copywriter,
  content writer, or "writes like me" agent — that captures their own voice, tone, and style.
  Triggers include: "help me build an AI that writes like me", "I want a copywriter for my
  brand/newsletter/blog", "create a writing assistant for this project", "set up a style guide
  so Claude writes in my voice", or any request to define personality, voice, tone, or writing
  rules for an agent producing blog posts, marketing copy, emails, social posts, or messages.
  Consider this skill whenever the user wants AI-generated content to "sound like them," even
  without the words "skill" or "agent". Runs a structured Socratic interview (~30 minutes),
  optionally analyzes writing samples the user provides, and produces a new, installable
  writer skill ready to drop into any project.
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.2.0
  family: tumaini
  outputs:
    - "[slug]/SKILL.md"
    - "[slug]/references/voice-profile.md"
    - "[slug]/references/[content-type].md  # one per format selected"
    - "[slug]/README.md"
    - "[slug]-STATE.md  # only if paused before synthesis"
---

# tumaini-voice

This skill interviews the user about how *they* write, then builds a new Claude skill that 
writes the same way. The output isn't a style guide someone has to remember to paste in — 
it's an installable copywriter: a personalized agent the user drops into any project to 
produce blog posts, emails, social copy, and more in their own voice.

**Target session length: 30 minutes.**  
**This is a tumaini-family skill** — same operating principles as `socratic-agentic-workflow`: 
always ask rather than assume, classify assumptions by how expensive they'd be to get wrong, 
and pause/resume rather than force a rushed result.

---

## How this skill works

The skill runs in three phases:

1. **Interview** — adaptive Socratic questioning across 8 themes, with an optional pass over 
   writing samples the user provides
2. **Synthesis** — reflect the voice profile back, classify assumptions, check it against any 
   samples, confirm before generating
3. **Output** — write a new skill package: a `SKILL.md` for the personalized writer, a full 
   voice profile, and one reference file per content type the user actually needs

Read all linked documents before starting:
- [`INTERVIEW.md`](./INTERVIEW.md) — themes, sample analysis, pacing, pause/resume
- [`SYNTHESIS.md`](./SYNTHESIS.md) — reflection, assumption classification, confirmation
- [`OUTPUT.md`](./OUTPUT.md) — how to name, structure, and write the generated writer skill

---

## Core principles

**Always ask, never assume.**  
Inference level is 1/5. A voice profile built on the LLM's guesses about how someone writes is 
useless — it'll sound like a stereotype, not a person. Follow the vagueness protocol in 
INTERVIEW.md: reflect back, offer concrete examples, and only name an assumption as a last 
resort.

**No code. Stay at the voice and content layer.**  
This skill defines *how* something is written, not the tooling around it. If the user starts 
talking about publishing pipelines, CMSs, or automation, note it for the handover section but 
don't design it here — that's a job for `socratic-agentic-workflow`.

**Samples are evidence, not gospel.**  
If the user provides writing samples, use them to find patterns — but check those patterns 
against what the user *says* about their voice. If a sample contradicts the stated tone (e.g. 
"I'm pretty formal" but the sample is full of jokes and fragments), that's a contradiction to 
surface, not a tiebreaker to resolve silently.

**Classify assumptions.**  
Assumptions that are easy to fix later (a word choice, one example) are "safe to defer". 
Assumptions that would shape the whole voice profile (formality level, person, audience) are 
"blocking" — push back on these before moving on. See SYNTHESIS.md.

**Pause and resume.**  
If 15 minutes in the user is still discovering their own voice rather than describing 
something they already know, offer to pause and write a `[slug]-STATE.md` checkpoint instead 
of compressing the rest. See INTERVIEW.md.

**The user names the writer (with help).**  
Early in the session, once the purpose is clear, propose a name for the new writer skill — 
kebab-case, optionally in the `tumaini-` family if the user wants it branded that way. The 
user confirms or changes it. All output is written into a folder with that name.

**Use interactive question UI when available.**  
If the runtime provides a structured multiple-choice question tool (e.g., Cowork's 
`AskUserQuestion` — 1-4 questions per call, each with 2-4 options plus an automatic "Other" 
free-text option), use it for the per-theme questions in INTERVIEW.md instead of typing them 
as plain chat text. Reserve plain conversational text for reflections, summaries, the 
vagueness protocol, contradiction handling, and synthesis — anything needing more nuance than 
pick-one-or-type-your-own. If no such tool exists, fall back to the conversational format. 
See "Using interactive question tools" in INTERVIEW.md.

---

## Starting the session

When this skill is invoked, begin with:

> "Let's build you a writer — a Claude skill that writes in your voice. I'll ask about who 
> it's for, how you sound, what to avoid, and what kinds of writing you need it for. If you've 
> got a piece or two of writing that sounds like you, you can paste or attach them — totally 
> optional, but it helps. We'll aim to wrap up in about 30 minutes with a skill you can drop 
> into any project.
>
> First — what's this writer for? A project, a brand, your own personal voice across 
> everything — describe it in a sentence or two."

From the user's first response, propose a name for the writer skill (see 
[`OUTPUT.md`](./OUTPUT.md) for naming conventions):

> "I'd suggest calling this **[proposed-name]**. Work for you, or would you rather call it 
> something else?"

Then proceed to [`INTERVIEW.md`](./INTERVIEW.md).
