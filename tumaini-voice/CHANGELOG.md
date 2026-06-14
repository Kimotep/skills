# Changelog

## v0.2.0 — interactive question UI

- When the runtime provides a structured multiple-choice question tool (e.g., Cowork's 
  `AskUserQuestion`), the interview now uses it for theme questions — options worded as 
  likely answers, with an "Other" free-text fallback
- Conversational text remains for reflections, vagueness protocol, contradiction handling, 
  drift detection, and synthesis
- Falls back to fully conversational interview if no such tool exists

## v0.1.0 — initial release

- Socratic interview across 8 themes: purpose, audience, voice and personality, writing 
  samples (optional), structure and formatting, vocabulary and signature moves, boundaries 
  and anti-patterns, content types and handover
- Optional writing-sample analysis, with contradiction handling between stated tone and 
  observed patterns
- Synthesis phase with assumption classification (safe to defer / blocking) and a voice 
  consistency check against samples
- Output is an installable Claude skill: `SKILL.md`, `references/voice-profile.md`, and one 
  `references/[content-type].md` per selected format
- Pause/resume via `[slug]-STATE.md`, consistent with `socratic-agentic-workflow`
- Part of the `tumaini` skill family — shares design principles with 
  `socratic-agentic-workflow`
