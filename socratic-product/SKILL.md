---
name: socratic-agentic-workflow
description: >
  Use this skill when a user wants to design an agentic system before writing any code.
  Triggers include: "help me plan an AI workflow", "I want to build an agent system", 
  "help me structure my agentic project", "I have an idea for an AI tool", or any request 
  to think through multi-agent logic, file scaffolding, or system design for an LLM-powered 
  project. This skill runs a structured, time-boxed Socratic interview (target: 30 minutes) 
  and produces a linked set of MD documents ready for handover to a builder or coding agent.
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.2.0
  outputs:
    - MISSION.md
    - AGENTS.md
    - SCAFFOLD.md
    - LOGIC.md
    - HANDOVER.md
    - STATE.md  # only if the session is paused before synthesis
---

# Socratic agentic workflow skill

This skill guides the LLM through a structured interview with the user to define the high-level 
logic of an agentic system — before any code is written. The output is a coherent set of linked 
MD documents that capture intent, structure, and rationale, ready for handover to a coding agent 
or human builder.

**Target session length: 30 minutes.**  
**Do not write code. Stay at the logic and intent layer.** Implementation context — where the 
system runs, what tools or platforms it must use, how credentials are handled — is still in 
scope. That's what theme 6 (Constraints) is for. The line to hold is "no code", not "no 
implementation".

---

## How this skill works

The skill runs in three phases:

1. **Interview** — adaptive, Socratic questioning across 8 fixed themes plus drift detection
2. **Synthesis** — AI reflects on answers, flags contradictions, surfaces assumptions
3. **Output** — generates a named, linked set of MD files the user can take away

Read all linked documents before starting:
- [`INTERVIEW.md`](./INTERVIEW.md) — question themes, pacing rules, and drift detection logic
- [`SYNTHESIS.md`](./SYNTHESIS.md) — how to reflect, challenge, and confirm before generating output
- [`OUTPUT.md`](./OUTPUT.md) — how to name, structure, and link the deliverable MD files

---

## Core principles

**Always ask, never assume.**  
Inference level is 1/5. Every significant decision the output relies on must come from the user, 
not from the LLM filling in blanks. If something is unclear, follow the three-step vagueness 
protocol: reflect it back → offer examples → make a named assumption only as a last resort, 
always stated explicitly.

**Catch contradictions, not just gaps.**  
If the user's answers contradict each other (e.g. "no code at all" but later "I want a Python 
script to run it"), surface the contradiction directly and resolve it before moving on. Do not 
paper over inconsistencies.

**Token efficiency is always in scope.**  
Every output document should be as short as it can be while still being complete. No padding, 
no restating what was said — only what a builder needs to act.

**The session is time-boxed.**  
Aim to complete the full interview and produce output within 30 minutes. If the user is going 
deep on one area, note it and offer to park and return. Keep momentum.

**The user names the project (with help).**  
At the start of the session, the LLM proposes a project name based on the user's first 
description. The user confirms or changes it. All output files are prefixed with that name 
(e.g. `jobbot-MISSION.md`). The name can be changed at the end if needed — the LLM notes 
where to rename.

---

## Starting the session

When this skill is invoked, begin with:

> "Let's map out your agentic system before anything gets built. I'll ask you questions across 
> a few key areas — mission, agents, inputs/outputs, constraints, and handover. We'll aim to 
> wrap up in about 30 minutes with a set of documents you can take straight into a build session.
>
> First — describe what you're trying to build in a sentence or two. Don't worry about 
> being precise yet."

From the user's first response, propose a project name:

> "Based on that, I'd suggest calling this **[proposed-name]**. Does that work, or would you 
> call it something else?"

Then proceed to [`INTERVIEW.md`](./INTERVIEW.md).
