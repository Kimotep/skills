# OUTPUT.md — generating, naming, and linking the deliverable files

This document defines how to produce the final output after synthesis is confirmed.  
All files are Markdown. All files are linked to each other. All files are named with the 
project slug as a prefix.

---

## Naming convention

The project slug is derived from the confirmed project name:
- Lowercase, hyphen-separated
- No special characters
- Max 3 words

Examples: `jobbot`, `content-pipeline`, `daily-brief`

All output files follow this pattern: `[slug]-[FILETYPE].md`  
Example set for project "jobbot":
- `jobbot-MISSION.md`
- `jobbot-AGENTS.md`
- `jobbot-SCAFFOLD.md`
- `jobbot-LOGIC.md`
- `jobbot-HANDOVER.md`

Tell the user the slug before generating files:
> "I'll use **[slug]** as the project prefix. Files will be named `[slug]-MISSION.md` etc.  
> Change it now or at the end — just say the word."

---

## File set — what to generate

Generate all five files in every session. Do not skip any.

---

### `[slug]-MISSION.md`

The single source of truth for why this system exists.

```
# [Project name] — mission

## What this is
[2–3 sentences. What the system does and for whom.]

## Why it needs to exist
[1–2 sentences. What problem it solves that isn't solved otherwise.]

## Mission statement
> [One sentence. Confirmed with user during synthesis.]

## Success looks like
[Bullet list of observable signals that the system is working.]

## Out of scope
[Bullet list of explicit boundaries — what this system does NOT do.]

## Assumptions
[Any named assumptions from the interview, or "None."]

---
→ See [slug]-AGENTS.md for who does the work.  
→ See [slug]-SCAFFOLD.md for the file structure.
```

---

### `[slug]-AGENTS.md`

Defines every agent role in the system.

```
# [Project name] — agents

## Roles

### [Agent name]
**Responsibility:** [One sentence.]  
**Triggered by:** [What starts this agent's work.]  
**Input:** [What it receives.]  
**Output:** [What it produces.]  
**Hands off to:** [Next agent or endpoint, or "terminal".]

[Repeat for each agent.]

## Coordination model
[How agents relate: sequential pipeline / parallel / orchestrator+workers / other.  
One short paragraph.]

## Critical path
[Which agent(s), if they fail, cause the whole system to fail. One sentence.]

---
→ See [slug]-LOGIC.md for how agents connect in flow.  
→ See [slug]-MISSION.md for the overall purpose.
```

---

### `[slug]-SCAFFOLD.md`

The recommended file and folder structure for the project.

```
# [Project name] — scaffold

## Recommended structure

[slug]/
├── [slug]-MISSION.md        # Why this exists
├── [slug]-AGENTS.md         # Who does what
├── [slug]-SCAFFOLD.md       # This file
├── [slug]-LOGIC.md          # How it flows
├── [slug]-HANDOVER.md       # What the builder needs
├── agents/
│   ├── [agent-name].md      # Per-agent prompt/rules file
│   └── ...
├── rules/
│   └── [constraint-name].md # Named constraints and boundaries
└── [any tool-specific config files noted in constraints]

## Notes on structure
[Any project-specific explanations — why certain folders exist, 
what should NOT be in the repo, naming decisions made.]

## Token hygiene
[How to keep context lean: which files a coding agent should load per task, 
which files are reference-only and should not be injected automatically.]

---
→ See [slug]-AGENTS.md for what goes in agents/.  
→ See [slug]-HANDOVER.md for how to initialise this structure.
```

---

### `[slug]-LOGIC.md`

The flow of the system expressed as a readable diagram and accompanying logic notes.

```
# [Project name] — logic

## Flow overview

[Mermaid flowchart or ASCII diagram showing the system flow.
Prefer Mermaid if the builder environment supports it.]

\`\`\`mermaid
flowchart TD
    A([Trigger]) --> B[Agent: name]
    B --> C{Decision or branch?}
    C -- yes --> D[Agent: name]
    C -- no --> E([Output / end])
\`\`\`

## Logic notes

### Trigger conditions
[What starts the system. Edge cases that affect the trigger.]

### Branch points
[Any conditional logic — what determines which path is taken.]

### Error states
[What should happen if an agent fails or produces unexpected output.]

### Loops and retries
[Whether any step repeats, and under what condition it stops.]

---
→ See [slug]-AGENTS.md for agent definitions.  
→ See [slug]-HANDOVER.md for build order recommendation.
```

---

### `[slug]-HANDOVER.md`

Everything a builder (human or coding agent) needs to start work immediately.

```
# [Project name] — handover

## For the builder

This document is the entry point for whoever builds this system.  
Read [slug]-MISSION.md first if you need context. Otherwise, start here.

## What has been decided
[Bullet summary of all confirmed decisions from the interview and synthesis.]

## What has NOT been decided
[Explicit list of open questions or deferred decisions.  
Do not leave this blank — if nothing is open, write "None — all decisions confirmed."]

## Named assumptions
[Ledger format. For each assumption, one line:
- **[Assumption]** — [why it was made]. *Safe to defer — resolve by: [build step].*
Blocking assumptions should not appear here — they should have been resolved during synthesis 
(see SYNTHESIS.md). If "none", write "None — all decisions confirmed."]

## Recommended build order
1. [First thing to do]
2. [Second thing]
3. [etc.]

## Suggested first prompt (for coding agent handover)
[A ready-to-use prompt the user can paste into Cursor or similar, 
referencing the scaffold and mission doc.]

> "You are building [project name]. Read [slug]-MISSION.md and [slug]-SCAFFOLD.md first.
> Your first task is [first action]. Do not write any code outside the defined scaffold. 
> Ask before making decisions not covered in [slug]-AGENTS.md."

## Constraints to respect
[Verbatim list from the interview — token limits, tool restrictions, platform requirements.]

---
→ Start with [slug]-MISSION.md.  
→ Then [slug]-SCAFFOLD.md to set up the structure.  
→ Then [slug]-AGENTS.md to define agent files.  
→ Use [slug]-LOGIC.md as the reference during build.
```

---

## Conditional file — `[slug]-STATE.md`

Only generated if the session is paused before synthesis (see "Pause and resume" in 
[`INTERVIEW.md`](./INTERVIEW.md)). Replaces the full file set for this session — do not 
generate the five files above if this file is generated instead.

```
# [Project name] — session state

## Resolved themes
[Each of the 8 themes that reached "resolved" status, with a one-line summary of what was 
confirmed.]

## Open themes
[Remaining themes, with whatever the user has said so far — even if rough or contradictory. 
Don't smooth it over; the next session needs the raw material as given.]

## In the user's own words
[Direct quotes or close paraphrases of anything the user kept returning to — the drift signal 
for the next session.]

## Resume instructions
Pick up with [next theme]. Do not re-ask resolved themes unless the user wants to revisit them.
```

---

## Delivery format

After generating all five files in chat, present them in this order:

1. Confirm the slug and file names
2. Output each file in a clearly labelled fenced code block
3. End with:

> "All five files are ready. Copy them into your project folder in any order —  
> `[slug]-HANDOVER.md` is the best starting point for a builder or coding agent.  
> Want to rename the project slug, adjust anything, or start a build session now?"

---

## Token hygiene in output

- No filler sentences. Every line earns its place.
- No re-explaining decisions already captured in another file — use cross-links instead.
- If a section has nothing to say (e.g. no branches in the logic), write one line: 
  `[None identified — linear flow confirmed.]`
- Keep the Mermaid diagram to the actual flow. Do not add decorative nodes.
