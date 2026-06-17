# Changelog

## v0.6.0

Interview is now fully multiple-choice UI, and the output includes a harness root config file.

- **Multiple-choice interview enforced.** Every interview question must use the `AskUserQuestion`
  tool — no inline text questions. Options are 2–4 choices with automatic freeform fallback. The
  only exceptions are brief inline detail follow-ups, session-open prose, and theme summaries.
  Rule documented in a new "Interview UI rule" section in INTERVIEW.md.
- **New Theme 9: Development harness.** Asks which AI coding tool the builder will use —
  Claude Code, Cursor, Windsurf, OpenCode, other, or none. Drives which root config file is
  generated.
- **New harness root config file in output.** Every session now produces a seventh file:
  `CLAUDE.md`, `.cursorrules`, `.windsurfrules`, `opencode.json`, or `AGENT-INSTRUCTIONS.md`
  (fallback), depending on Theme 9. Content is a compressed, builder-facing version of the plan:
  mission summary, agent roles, constraints, do-nots, first task, and reference file list.
  For OpenCode, emitted as valid JSON. Template and file-name map documented in OUTPUT.md.
- **README.md template updated** to include the harness file row.
- **Delivery message updated** to reference the seventh file and tell the user where to put it.

## v0.5.0

Agent specs now meet a quality bar, the mission is checked against what already exists, and 
the whole plan gets an index.

- **New "Agent design pass" in SYNTHESIS.md.** Every agent role drafted in theme 4 is checked 
  against five conventions: single responsibility with explicit boundaries, an input → 
  output contract, a tool/context scope, a stated coordination role, and a 
  failure/escalation path. Load-bearing gaps go through the vagueness protocol; minor gaps 
  become safe-to-defer assumptions. No new interview questions.
- **`[slug]-AGENTS.md` restructured per agent.** Each role now has Responsibility (with 
  "Does NOT..." boundaries where relevant), Input → Output, Tools/context, Coordination 
  role, and If it fails.
- **New "Mission grounding pass" in OUTPUT.md.** If the idea has an obvious comparison point, 
  uses `WebSearch` to check for similar tools and adds a factual "How this differs" section 
  to `[slug]-MISSION.md`. Skipped (and noted as such) for internal/specific ideas.
- **Architect pass now also surfaces pitfalls.** Alongside structure and tooling, it pulls 
  2–3 stack-specific failure modes — from search or from `scaffold-patterns.md`'s new 
  "Common pitfalls" line — into a new "Watch for" section in `[slug]-HANDOVER.md`.
- **`[slug]-HANDOVER.md` gains a "Definition of done"** — a checklist version of 
  `[slug]-MISSION.md`'s success criteria — and an **MVP cut line** in the recommended build 
  order, separating the first working version from deliberate v2 work.
- **New `[slug]-README.md`.** A short index generated last, linking all five other files 
  with a one-line description and recommended read order. Output is now six files.
- **`scaffold-patterns.md` now includes "Common pitfalls" per pattern**, alongside "Tooling 
  defaults", as the fallback baseline for the architect pass's pitfall list.

## v0.4.0

The scaffold is now grounded in current best practice, not just a cached pattern.

- **New "Architect pass" in OUTPUT.md.** Runs silently before SCAFFOLD.md is generated: 
  starts from the matching `scaffold-patterns.md` entry, and if a specific framework or tool 
  was named, uses `WebSearch` to confirm current recommended structure and tooling (folder 
  layout, package manager, test framework, linter/formatter, env handling) before finalizing 
  the layout. Skips search for generic or undecided stacks.
- **New "## Tooling" section in SCAFFOLD.md.** Names the package manager, test framework, 
  linter/formatter, and env/config handling concretely for the stack — or "Deferred" if the 
  stack is undecided.
- **`scaffold-patterns.md` now includes "Tooling defaults" per pattern** as a fallback 
  baseline, explicitly overridable by the architect pass for named frameworks.
- **New core principle**: the scaffold reflects current best practice for the named stack, 
  not a guess — grounded via search when a specific framework is involved.

## v0.3.0

The output is now meant to be the actual first commit of the new project, not just a planning
folder.

- **Theme 6 (Constraints) now asks for project type and stack.** Web app, CLI tool, browser
  extension, agent pipeline, API service, library, or "undecided" — plus language/stack if
  known. Resolved-when criteria updated accordingly.
- **New `references/scaffold-patterns.md`.** Starter repo skeletons for each project type,
  each with inline comments and a short rationale. An "Undecided" pattern covers the case
  where type/stack wasn't settled in interview.
- **`[slug]-SCAFFOLD.md` now merges two layers.** The planning docs + `agents/`/`rules/`
  folders (always present) plus a product-layer structure (`src/`, `tests/`, config, etc.)
  picked from `scaffold-patterns.md` to match the project's type.
- **New "Why each piece is here" section in SCAFFOLD.md.** One line per top-level item,
  grouped by planning docs / agents-rules / product layer — expands on anything not already
  obvious from its inline comment, especially product-layer choices.

## v0.2.0

Changes based on dogfooding the skill on a real project — see 
[Putting my /skills to use](https://www.tumaini.dk/posts/scraper).

- **"No implementation details" → "no code".** The constraints theme (6) legitimately asks 
  where the system runs, what tools it must use, and how credentials are handled. That's not 
  an implementation detail to avoid — it's a decision to capture. SKILL.md now draws the line 
  at code, not implementation context.
- **Assumptions are now classified.** SYNTHESIS.md distinguishes "safe to defer" assumptions 
  (low blast radius, fine to leave for build time) from "blocking" ones (touch agent roles, 
  the scaffold, or the critical path). Blocking assumptions get pushed back on via the 
  vagueness protocol instead of being waved through as a footnote.
- **Out-of-scope boundaries that shape system flow are flagged for LOGIC.md.** A boundary like 
  "no third crawl pass" isn't just a note in MISSION.md — if it changes branching or flow, it 
  belongs in the logic file too.
- **Assumption ledger in HANDOVER.md.** Safe-to-defer assumptions now come with a "resolve by" 
  build step, so the builder knows exactly when a deferred decision becomes due instead of 
  discovering it mid-build.
- **Pause and resume.** If a ~15-minute checkpoint shows the idea is still taking shape rather 
  than time just running short, the skill offers to pause and write a `[slug]-STATE.md` file 
  instead of compressing the remaining themes. A second session resumes from there rather than 
  restarting.

## v0.1.0

Initial release. Eight-theme Socratic interview, synthesis and confirmation step, five linked 
output files (MISSION, AGENTS, SCAFFOLD, LOGIC, HANDOVER).
