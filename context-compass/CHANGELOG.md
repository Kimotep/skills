# Changelog

## v0.2.0 — execute now

- Step 5 (Destination) now leads with "Start now — right here in this chat"
- If the user picks "start now," the skill skips the "ready to use as-is" question and moves
  straight from the brief into doing the first step, using Context/Decided/Constraints as
  the operating brief for the rest of the session (setting up a task list first if the work
  is multi-step)
- Hand-off destinations (new chat/agent, someone else, not sure) keep the original
  brief-and-ask behavior
- New core principle: the brief is the spec once "start now" is chosen — no re-litigating
  decisions already made

## v0.1.0 — initial release

- Quick, always-available flow: seed question, context check, "open it up" (surfaces
  unconsidered angles), boundaries, destination
- Every question is multiple choice with a free-text option — no open-ended prompts
- `references/angles.md` lens library for the "open it up" step, organized by task type
  (build, write, research/decide, fix/debug, plan/organize) plus general fallback lenses
- Output is a ready-to-run prompt/brief shown in chat, optionally saved as `[slug]-BRIEF.md`
- Points to `socratic-agentic-workflow` or `tumaini-voice` when a task looks like it needs a
  deeper session instead
