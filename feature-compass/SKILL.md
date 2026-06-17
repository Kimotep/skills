---
name: feature-compass
description: >
  Use this skill when a user wants to add a new feature to an existing project and needs
  help scoping, clarifying, or aligning on what it should be before building starts.
  Triggers include: "I want to add a feature", "help me think through this feature",
  "I'm not sure how to approach this new feature", "we need to add X to our app", or
  any time a user describes new functionality they want to introduce. This skill interviews
  the user (always multiple-choice with freeform) to build a shared, clear understanding
  of the feature — what it does, why, how it fits the tech, what the UI looks like, and
  what needs to happen. It produces a brief the user can take straight into a build session.
  Trigger this skill whenever a new feature is being considered, even informally.
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.2.0
  outputs:
    - "[feature]-BRIEF.md — agreed feature summary, task list, and coding session prompt"
---

# Feature Compass

Align on what the feature is before anything gets built. This skill interviews the user
through a set of focused questions — always multiple choice with freeform — until the
feature is clearly understood: what it does, why it's needed, how it fits the project, what
the UI looks like, and what needs to happen to build it.

The output is a brief the user can hand straight to a coding session.

**Every question uses `AskUserQuestion`. No prose questions.**  
**Target time: 10–15 minutes.**

---

## Entry point

### Step 1 — Read context, then fill gaps

This is an execution skill — it runs inside an active project session. The stack, harness,
and conventions are usually already in context from a loaded `CLAUDE.md`, `.cursorrules`,
or similar. Use that first.

**Check context before touching the filesystem:**
- Is the stack already known from the current session? Use it — don't re-read config files.
- Is the harness already clear (e.g. this is a Claude Code session)? Set the output
  location accordingly — don't ask.
- Is there a roadmap already in context? Use it for conflict checks.

**Only scan the filesystem if context is missing.** If the stack, harness, or roadmap
aren't clear from the current session, look for:

| File | What to extract |
|---|---|
| `CLAUDE.md` | Stack, conventions, features in progress |
| `.cursorrules` / `.windsurfrules` / `opencode.json` | Stack, harness |
| `ROADMAP.md` / `TODO.md` / `PLAN.md` | Planned work |
| `package.json` / `pyproject.toml` / `Cargo.toml` | Framework, dependencies |

**Harness → output location:**

| Harness | Brief goes in |
|---|---|
| Claude Code | Project root alongside `CLAUDE.md` |
| Cursor | Project root |
| Windsurf | Project root |
| OpenCode | Project root |
| Unknown | Ask user in area 6 |

### Step 2 — Feature name

If the user invoked the skill with a description (e.g. "add dark mode to my React app"),
extract what you can from it and skip questions already answered.

If invoked bare, open with:

> "What feature are you adding? Describe it in a sentence — rough is fine."

From the first answer, propose a feature name:

> "I'll call this **[proposed name]**. Good, or do you want something different?"

Confirm the name, then move into the interview.

---

## Interview

Six areas to cover. Order is flexible — follow the conversation. Use `AskUserQuestion`
for every question. Between areas, reflect back what you've heard in one sentence before
moving on.

If the feature description already answers an area clearly, skip it.

---

### 1. What it does
Get to a crisp one-sentence description of what the feature does for the user.

Good questions to ask:
- What does the user do with it? (action-oriented options)
- What problem does it solve or what does it make easier?
- What would "working well" look like from the user's perspective?

Resolved when: you can write a one-sentence feature statement the user would confirm.

---

### 2. Why now
Understand the motivation. This shapes priority and scope decisions later.

Good questions to ask:
- Is this user-requested, internally driven, or technically motivated?
- What's the trigger — user feedback, a new use case, a blocker, something else?

Resolved when: the motivation is clear enough to explain it to someone new.

---

### 3. Tech fit
Understand how the feature sits inside the existing project — not to design the solution,
but to catch obvious mismatches early.

Good questions to ask:
- What stack or framework is the project using?
- Does this feature need anything new — a library, an API, a new data model?
- Is there anything in the current setup that might make this harder or simpler?

If the user doesn't know the answer to a tech question, that's fine — note it as an open
question for the build session, don't block on it.

Resolved when: the stack is known and any obvious tech dependencies or concerns are named.

---

### 4. UI
Determine whether the feature has a UI component and get enough definition to describe it.

First ask: does this feature have a UI? If no, skip the rest of this area.

If yes, ask what the user wants to define now:
- A rough visual sketch (Claude renders a widget mockup in chat — user reacts and refines)
- A description (what the user sees and does, in words)
- Leave it for later (just note that UI is TBD)

**If the user chooses a visual sketch:** use `show_widget` to render a minimal HTML mockup
of the key screen or interaction. Keep it structural — layout and elements, not styling.
Present it and ask: "What's right, what's off, what's missing?" Iterate once, then lock
the description.

**If the user chooses a description:** ask 1–2 focused questions about placement,
interaction, and any key states. Lock the description from their answers.

Resolved when: the UI is either described well enough to hand to a builder, or marked TBD.

---

### 5. Roadmap and conflicts
Check whether this feature conflicts with, depends on, or overlaps anything already planned.

First: look for a roadmap file in the project (`ROADMAP.md`, `TODO.md`, `PLAN.md`,
`docs/roadmap.md`). If found, read it and surface any relevant items directly.

If none found: ask the user what's in the pipeline — anything planned or in progress that
this feature might touch.

If there are no conflicts: confirm and move on.

Resolved when: conflicts are identified and noted, or confirmed absent.

---

### 6. Output format
Skip this area if the project scan detected a harness — the output location is already set.

If no harness was detected, ask:
- Where should the brief be saved? (project root, a docs/ folder, somewhere else, or just
  show it in chat)
- Is there a naming convention to follow? (or use `[feature-name]-BRIEF.md` as default)

This is the last question before synthesis.

---

## Synthesis

Before writing the brief, do a quick internal check:

- Is the feature statement clear and confirmed?
- Are there open questions that should be flagged (not blocking — just noted for the builder)?
- Are there any contradictions in what the user said that should be surfaced?

If something is unclear, ask one more targeted question. Otherwise proceed to output.

---

## Output

### `[feature-name]-BRIEF.md`

```
# [Feature name]

## What it does
[One-sentence confirmed feature statement.]

## Why it's being added
[1–2 sentences on motivation and timing.]

## Tech notes
[What stack it lives in. Any new dependencies or concerns named in the interview.
If something was left open, note it as: "Open: [question] — resolve before building."]

## UI
[The agreed UI description, or "TBD — define before building."]

## Roadmap
[Any conflicts or dependencies, or "No conflicts identified."]

## Task list
[A short ordered list of what needs to happen — not code, just the steps:]
1. [First thing]
2. [Second thing]
3. [etc.]

## Start here (coding session prompt)
> "I'm building [feature name] for [project]. Here's the brief: [feature-name]-BRIEF.md.
> Start with [task 1]. Ask before making decisions not covered in the brief."

## Open questions
[Anything that came up but wasn't resolved — for the builder to sort out.
If none: "None — everything confirmed."]
```

---

## Delivery

Save the brief to the location the user specified in area 6. Then:

> "Brief is saved. The task list and prompt at the bottom are ready to paste into a coding
> session. Anything to adjust before you start building?"