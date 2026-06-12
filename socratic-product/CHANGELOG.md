# Changelog

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
