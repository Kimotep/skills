---
name: context-compass
description: >
  Use this skill when the user has an idea, task, or problem they want to get moving on but
  hasn't fully worked out how to phrase it for an agent yet. Triggers include: "help me
  think this through", "I want to start something but I'm not sure how to put it", "turn
  this into a prompt I can use", "what am I missing here", "help me figure out what I
  actually need", or any request to scope, frame, or kick off a task before diving in. This
  is a quick, always-available skill (a few minutes, not a long session) — every question is
  multiple choice with a free-text option, in plain language. It surfaces angles the user
  may not have considered, then produces a ready-to-run prompt or brief for an agent session.
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.1.0
  outputs:
    - A ready-to-run prompt or brief, shown in chat (optionally saved as [slug]-BRIEF.md)
---

# context-compass

A fast, always-on warm-up for starting anything with an agent. You describe what's on your
mind — rough is fine. A few quick questions sharpen it, surface a couple of things you might
not have thought about yet, and the result is a prompt ready to hand to an agent (this
session or a new one).

**Target time: a few minutes.** This is the opposite of a deep interview — use it constantly,
not just for big things.

---

## The one rule: every question is multiple choice + freeform

No open-ended "tell me everything" questions. Every question:

- is short, plain language
- offers 2–4 concrete options
- always allows a free-text answer instead (via the question tool's "Other", or by inviting
  "...or just tell me")

Keep total wording minimal. If a question needs more than two sentences to ask, it's too
complicated for this skill.

---

## The flow

### Step 0 — The seed

Ask, freeform only:

> "What are you trying to get moving on? A sentence or two is plenty — rough is fine."

### Step 1 — Read it (silent)

Don't ask anything yet. Privately note:
- What kind of task this sounds like (build/make, write, research/decide, fix/debug,
  plan/organize — or a mix)
- What's already clear vs. still vague
- Whether this is actually a quick-prompt task, or big enough that a deeper skill would serve
  better (see "When this isn't the right tool" below)

### Step 2 — Context check

Ask, multiple choice + freeform:

> "What's already in place for this?"
> A) Nothing yet — starting from scratch
> B) I've got some files, notes, or examples already
> C) This builds on something that already exists
> D) Not sure yet

### Step 3 — Open it up (the important step)

This is the core value of the skill: surface 2–3 things the user likely hasn't decided yet,
based on what they've said so far. Pick relevant lenses from
[`references/angles.md`](./references/angles.md) — don't dump the whole list, just the ones
that fit this task. Phrase each as a short option.

> "A couple of things worth deciding now:"
> A) [angle 1, phrased as a real choice — e.g. "Is this a one-off, or something you'll come
>    back to and reuse?"]
> B) [angle 2]
> C) Neither — what I said covers it
> + freeform for anything else

If the user picks an angle, ask the one or two follow-up details needed to resolve it — still
multiple choice + freeform, still brief.

### Step 4 — Boundaries

Ask, multiple choice + freeform:

> "Anything that's off-limits, or that has to be true no matter what?"
> A) Nothing in particular
> B) Keep it private / local — nothing external
> C) Use only what I already have — no new tools or accounts
> D) Has to be quick — not a big project

(Adjust options B–D to fit the task type from Step 1 if a different constraint is more
likely relevant.)

### Step 5 — Destination

Ask, multiple choice + freeform:

> "Who's this for?"
> A) You, right now — paste it into this or a new chat
> B) A coding agent (e.g. Claude Code)
> C) Someone else — a teammate or contractor
> D) Not sure yet — just want it written down

---

## Output

Produce the result directly in chat — no preamble, just the prompt:

```
[One or two sentences: what needs doing]

Context: [from Step 2 — what's already in place, or "starting from scratch"]

Decided: [resolved angles from Step 3, stated as facts/instructions — omit if none]

Constraints: [from Step 4, or "None specified"]

First step: [one concrete action to start with]
```

Then ask:

> "Ready to use as-is, want any of it adjusted, or should I save this as a file?"

If the user wants it saved, write `[slug]-BRIEF.md` where `[slug]` is a short kebab-case name
derived from Step 0 — propose one, let the user change it.

---

## When this isn't the right tool

If Step 1 reveals the task is actually large — a multi-agent system, or a personalized
writing voice that'll get reused constantly — say so before going further:

> "This sounds bigger than a quick prompt — it might be worth a proper session with
> [socratic-agentic-workflow / tumaini-voice]. Want the quick version now anyway, or should
> we switch?"

Let the user choose. Don't assume bigger is better — sometimes a quick prompt now is exactly
right, with a deeper session later.

---

## Core principles

**Multiple choice + freeform, always.** This is what makes the skill fast and low-friction —
the user never faces a blank box, but never feels boxed in either.

**Surface what's missing, don't just record what's said.** Step 3 is the point of this
skill. A user who already knew exactly what to ask for wouldn't need it.

**Plain language, minimal words.** No jargon, no explaining why a question is being asked —
just ask it.

**Fast by default.** If in doubt, ask one fewer question, not one more. The user can always
ask for more depth.
