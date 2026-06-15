---
name: socratic-agentic-workflow
description: >
  Use this skill when a user wants to design an agentic system before writing any code.
  Triggers include: "help me plan an AI workflow", "I want to build an agent system", 
  "help me structure my agentic project", "I have an idea for an AI tool", or any request 
  to think through multi-agent logic, file scaffolding, or system design for an LLM-powered 
  project. This skill runs a structured, time-boxed Socratic interview (target: 30 minutes) 
  and produces a linked set of MD documents ready for handover to a builder or coding agent — 
  including a starter repo structure tailored to the project's type and stack, and agent 
  specs written to a defined quality standard (responsibilities, I/O contracts, tool scope, 
  and failure handling).
license: MIT
metadata:
  author: Kim Tumaini Jørgensen
  version: 0.5.0
  outputs:
    - README.md  # index linking the other five files, generated last
    - MISSION.md  # now includes "How this differs" from comparable tools
    - AGENTS.md  # each agent now specced with I/O contract, tool scope, and failure path
    - SCAFFOLD.md  # starter repo structure tailored to the project type
    - LOGIC.md
    - HANDOVER.md  # now includes a definition of done and a "Watch for" pitfalls list
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
2. **Synthesis** — AI reflects on answers, flags contradictions, surfaces assumptions, and 
   runs an agent design pass that checks every agent role against five quality conventions
3. **Output** — two silent pre-generation passes ground the scaffold and mission in current 
   reality (using `WebSearch` when relevant), then generate a named, linked set of MD files — 
   including an index file — the user can take away

Read all linked documents before starting:
- [`INTERVIEW.md`](./INTERVIEW.md) — question themes, pacing rules, and drift detection logic
- [`SYNTHESIS.md`](./SYNTHESIS.md) — how to reflect, challenge, and confirm before generating output
- [`OUTPUT.md`](./OUTPUT.md) — how to name, structure, and link the deliverable MD files
- [`references/scaffold-patterns.md`](./references/scaffold-patterns.md) — starter repo
  structures by project type, used when generating `[slug]-SCAFFOLD.md`

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

**The scaffold reflects current best practice, not a cached template.**  
Before generating `[slug]-SCAFFOLD.md`, run the architect pass in 
[`OUTPUT.md`](./OUTPUT.md): start from the matching pattern in 
[`references/scaffold-patterns.md`](./references/scaffold-patterns.md), and if a specific 
framework or tool was named, use `WebSearch` to confirm its current recommended structure 
and tooling before committing to a layout. This is silent — it doesn't add questions to the 
interview, it just means the output is grounded rather than guessed. The same pass also 
surfaces 2–3 stack-specific pitfalls for `[slug]-HANDOVER.md`'s "Watch for" section.

**Agents are specced to a standard, not just named.**  
During synthesis, every agent role is checked against five conventions: single 
responsibility with explicit boundaries, a concrete input → output contract, a defined tool 
and context scope, a stated coordination role, and a named failure/escalation path. Gaps 
that are load-bearing get resolved via the vagueness protocol; minor gaps become 
safe-to-defer assumptions. This is what `[slug]-AGENTS.md` is built from.

**The mission is checked against what already exists.**  
If the idea has an obvious comparison point ("a Zapier for X"), the mission grounding pass 
in [`OUTPUT.md`](./OUTPUT.md) uses `WebSearch` to check for similar tools and adds a factual 
"How this differs" note to `[slug]-MISSION.md`. If the idea is too specific or internal to 
compare, this is skipped and noted as such — no search for the sake of it.

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
