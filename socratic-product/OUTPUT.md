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
- `jobbot-README.md`
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

Generate all six planning files plus one harness root file in every session. Do not skip any.
`[slug]-README.md` is generated last, since it indexes the other files — but list it first
when presenting the set, since it's where the user starts reading.

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

## How this differs
[From the mission grounding pass below: how this differs from comparable tools, or "Not 
applicable — internal/specific to [context]."]

## Assumptions
[Any named assumptions from the interview, or "None."]

---
→ See [slug]-AGENTS.md for who does the work.  
→ See [slug]-SCAFFOLD.md for the file structure.
```

---

### `[slug]-AGENTS.md`

Defines every agent role in the system, to the standard set by the agent design pass in
[`SYNTHESIS.md`](./SYNTHESIS.md).

```
# [Project name] — agents

## Roles

### [Agent name]
**Responsibility:** [One sentence — what this agent does. If there's realistic overlap with 
another agent, add "Does NOT [x] — that's [other agent]'s job."]  
**Triggered by:** [What starts this agent's work.]  
**Input → Output:** [What it receives → what it produces, concretely.]  
**Tools/context:** [What it needs access to — APIs, files, other agents' output. Nothing 
more than that.]  
**Coordination role:** [Orchestrator / worker / peer — and what it hands off to, or 
"terminal".]  
**If it fails:** [Retry / fall back / escalate / halt — and to whom or what.]

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

---

### Harness root file

Generated for every session based on the answer to Theme 9. This file goes at the repo root
and tells the builder's AI coding tool how to work in this project.

**File name by harness:**

| Harness | File |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursorrules` |
| Windsurf | `.windsurfrules` |
| OpenCode | `opencode.json` |
| Other (named) | whatever the tool's convention is — ask if unknown |
| None / undecided | `AGENT-INSTRUCTIONS.md` |

**Content template (Markdown harnesses):**

```
# [Project name] — [harness name] instructions

## What this project is
[2–3 sentences from [slug]-MISSION.md's "What this is" section.]

## Agent roles
[One line per agent from [slug]-AGENTS.md — name + one-sentence responsibility only.]

## Constraints
[Verbatim constraint list from [slug]-HANDOVER.md's "Constraints to respect".]

## Do not
- Write code outside the scaffold defined in [slug]-SCAFFOLD.md
- Make decisions not covered in [slug]-AGENTS.md without asking
- Modify agent boundaries without reviewing [slug]-AGENTS.md first

## Start here
[First item from [slug]-HANDOVER.md's recommended build order.]

## Reference files
- [slug]-MISSION.md — why this exists
- [slug]-AGENTS.md — who does what
- [slug]-SCAFFOLD.md — repo structure
- [slug]-LOGIC.md — system flow
- [slug]-HANDOVER.md — build order and open decisions
```

**For `opencode.json`**, emit valid JSON instead:

```json
{
  "project": "[Project name]",
  "instructions": "[2–3 sentence mission summary]",
  "agents": ["[agent name]: [one-line responsibility]"],
  "constraints": ["[constraint 1]", "..."],
  "doNot": [
    "Write code outside the defined scaffold",
    "Make decisions not covered in AGENTS.md without asking"
  ],
  "startHere": "[first build order item]",
  "referenceFiles": ["MISSION.md", "AGENTS.md", "SCAFFOLD.md", "LOGIC.md", "HANDOVER.md"]
}
```

---

## Pre-generation passes

Run both of these silently, after synthesis is confirmed and before writing any files.
Neither asks the user anything new — they make sure the output reflects reality (current
practice, existing tools) rather than a guess or a cached template.

### Architect pass — grounds SCAFFOLD.md and HANDOVER.md's "Watch for"

1. Take the project type and stack named in theme 6.
2. Look up the matching pattern in
   [`references/scaffold-patterns.md`](./references/scaffold-patterns.md) — this is the
   starting skeleton, tooling baseline, and common-pitfalls baseline.
3. **If a specific framework or tool was named** (e.g. "Next.js", "FastAPI", "a Chrome
   extension", "a Typer CLI") and its conventions could plausibly have moved on since
   training, use `WebSearch` to check the current recommended project structure and standard
   tooling — folder layout, package manager, test framework, linter/formatter, env handling.
   Prefer official docs or the framework's own starter/scaffolding tool over blog posts.
4. **If the stack is generic, very stable, or undecided**, skip the search — use the
   scaffold-patterns.md pattern, its tooling defaults, and its common pitfalls as-is. Don't
   search for the sake of it.
5. Merge findings into the scaffold-patterns.md skeleton: keep what still applies, override
   anything search shows has changed, and use the result to fill in the structure and the
   `## Tooling` section below.
6. If search meaningfully changes the *shape* of the structure (not just file names),
   say so in one line under "Notes on structure" — no need to narrate the research.
7. Take 2–3 pitfalls or failure modes specific to this stack/pattern — from search if it
   surfaced any (e.g. a known footgun in a framework's current version), otherwise from
   scaffold-patterns.md's "Common pitfalls" line. These feed `## Watch for` in
   `[slug]-HANDOVER.md`. If genuinely nothing stands out, write "[None specific — standard
   practices for this stack apply.]"

This pass changes only the product layer of SCAFFOLD.md, its tooling, and the "Watch for"
list. It does not revisit scope, agents, or logic — those are already confirmed.

### Mission grounding pass — grounds MISSION.md's "How this differs"

1. If the mission (theme 1) describes something with an obvious category or comparison
   point (e.g. "like a Zapier for X", "a Slack bot that does Y"), use `WebSearch` to check
   for existing tools that do something similar.
2. If the idea is clearly internal, personal, or too specific to compare (e.g. "automates my
   team's Friday status report"), skip the search — write "Not applicable — internal/specific
   to [context]."
3. Summarise in 1–2 factual sentences how this system differs from what's out there, or that
   it's a novel combination. No promotional framing — this is for the builder, not a pitch.

This pass does not change scope, success criteria, or anything else already confirmed — it
only adds context for `## How this differs` in MISSION.md.

---

### `[slug]-SCAFFOLD.md`

The starter structure for the project — both the planning layer (always the same six docs
plus `agents/`/`rules/`) and the first commit of the actual product, tailored to what's being
built and grounded in current best practice via the architect pass above.

Take the project type named in theme 6, merge the architect pass's findings into the matching
pattern from [`references/scaffold-patterns.md`](./references/scaffold-patterns.md), and
build the tree below. Don't bolt the product layer on as a separate, unrelated block — it
should read as one coherent structure. If project type was left undecided, use the Undecided
pattern and say so plainly; don't invent a stack.

```
# [Project name] — scaffold

## Project type
[From theme 6: web app / CLI tool / browser extension / agent pipeline / API service / 
library / undecided — plus stack or language, if named. If undecided, say so here.]

## Recommended structure

[slug]/
├── [slug]-README.md         # Index — start here
├── [slug]-MISSION.md        # Why this exists
├── [slug]-AGENTS.md         # Who does what
├── [slug]-SCAFFOLD.md       # This file
├── [slug]-LOGIC.md          # How it flows
├── [slug]-HANDOVER.md       # What the builder needs
├── agents/
│   ├── [agent-name].md      # Per-agent prompt/rules file, one per role in AGENTS.md
│   └── ...
├── rules/
│   └── [constraint-name].md # Named constraints and boundaries from the interview
[+ product-layer items from the matching scaffold-patterns.md entry, merged into the tree —
   e.g. src/, tests/, config files, named and commented per that pattern]

## Why each piece is here
[One line per top-level item, grouped as: planning docs, agents/rules, product layer.
Skip anything fully explained by its inline comment above — expand only on items that 
aren't obvious from the comment, especially product-layer choices tied to the project type.]

## Tooling
[From the architect pass: package manager, test framework, linter/formatter, and env/config 
handling — named concretely for the stack (e.g. "pnpm, Vitest, ESLint + Prettier, 
.env.local"). If a specific framework's own convention covers one of these, say so (e.g. 
"testing: Next.js + Vitest per current Next.js docs"). If stack is undecided, write 
"Deferred — see [slug]-HANDOVER.md for first decision."]

## Notes on structure
[Project-specific explanations beyond the above — what should NOT be in the repo, naming 
decisions made, anything about how the project type shaped this structure. If project type 
is undecided, note that the product layer is deferred and "pick a stack" belongs in 
[slug]-HANDOVER.md as an open decision.]

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

## Definition of done
[Checklist version of [slug]-MISSION.md's "Success looks like" — one checkbox per signal, 
so the builder can tell when a first version is actually finished.]
- [ ] [Signal 1]
- [ ] [Signal 2]

## Recommended build order
[Sequence agents/components so the critical path (from [slug]-AGENTS.md) works end-to-end 
first. If the full system is more than a first version needs, mark where the MVP ends — 
everything above the line is the first build target, everything below is a deliberate v2.]

1. [First thing to do]
2. [Second thing]
3. [etc.]
[— MVP ends here — *(omit this line if there's no meaningful cut)*]
4. [Later addition]

## Watch for
[2–3 pitfalls or failure modes for this stack/pattern, from the architect pass in 
OUTPUT.md — or "[None specific — standard practices for this stack apply.]"]

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

### `[slug]-README.md`

A short index for the project plan. Generate this last, once the other five files exist, so
the descriptions below are accurate rather than aspirational.

```
# [Project name]

[One-sentence mission, taken from [slug]-MISSION.md's mission statement.]

## Files in this plan

| File | What's in it | Read it... |
|---|---|---|
| [slug]-HANDOVER.md | Decisions made, definition of done, build order, first prompt | First |
| [slug]-MISSION.md | Why this exists, success criteria, how it differs from existing tools | For context |
| [slug]-AGENTS.md | Agent roles, contracts, coordination, failure handling | Before building agents/ |
| [slug]-SCAFFOLD.md | Starter repo structure and tooling | When setting up the repo |
| [slug]-LOGIC.md | System flow, branches, and error states | While wiring agents together |
| [harness filename] | Root instructions for [harness] — drop at repo root | Automatically loaded by your coding tool |

## Quick start
[1–2 sentences: create the structure in [slug]-SCAFFOLD.md, then start with 
[slug]-HANDOVER.md's recommended build order.]

---
This plan was generated by a Socratic planning session — see [slug]-HANDOVER.md for what's 
decided and what's still open.
```

---

## Conditional file — `[slug]-STATE.md`

Only generated if the session is paused before synthesis (see "Pause and resume" in 
[`INTERVIEW.md`](./INTERVIEW.md)). Replaces the full file set for this session — do not 
generate the six files above if this file is generated instead.

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

Generate the five linked files first, then `[slug]-README.md` last. Present them in chat in
this order:

1. Confirm the slug, file names, and harness root file name
2. Output `[slug]-README.md` first (it's the index), then the other five planning files in
   the order shown in its table, then the harness root file last — each in a clearly labelled
   fenced code block
3. End with:

> "All seven files are ready, starting with `[slug]-README.md` as the index. The harness
> root file ([filename]) goes at the repo root — your [harness] will pick it up automatically.
> Copy the planning files into your project folder in any order —  
> `[slug]-HANDOVER.md` is the best starting point for a builder.  
> Want to rename the project slug, adjust anything, or start a build session now?"

---

## Token hygiene in output

- No filler sentences. Every line earns its place.
- No re-explaining decisions already captured in another file — use cross-links instead.
- If a section has nothing to say (e.g. no branches in the logic), write one line: 
  `[None identified — linear flow confirmed.]`
- Keep the Mermaid diagram to the actual flow. Do not add decorative nodes.
