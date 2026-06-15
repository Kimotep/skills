# SYNTHESIS.md — reflection, challenge, and confirmation before output

This document defines what happens between the end of the interview and the generation of 
output files. Do not skip this phase, even if the interview felt clean.

---

## Purpose of synthesis

The interview collects raw material. Synthesis turns it into decisions. The LLM's job here 
is to:

1. Compress everything into a coherent picture
2. Surface anything that still doesn't add up
3. Get explicit user confirmation before generating files

---

## Step 1 — internal review

Before saying anything to the user, do a silent review across all 8 themes:

- Is there a confirmed mission statement?
- Are all agent roles named with responsibilities?
- Are inputs and outputs concrete?
- Is at least one constraint named?
- Is at least one success signal named?
- Is the handover target clear?
- Were any contradictions found and resolved?
- Were any named assumptions made? (These must appear in the output)

If any item is unresolved, go back and ask before continuing.

### Classify named assumptions

For each named assumption, decide:

- **Safe to defer** — a build-time detail with low blast radius. Getting it wrong costs a 
  small fix, not a rework (e.g. exact retry count, a log message format).
- **Blocking** — touches agent roles, the scaffold, or the system's critical path. Getting it 
  wrong means the builder undoes structural work later.

If an assumption looks blocking, don't let it ride as an assumption. Go back through the 
vagueness protocol — reflect it back, offer concrete options — before continuing. Only 
genuinely low-stakes details should reach the output tagged "safe to defer".

### Check for load-bearing boundaries

Revisit the out-of-scope answers from theme 5. Some are simple "not our job" statements — fine 
to leave as-is in MISSION.md. Others actively shape system flow (e.g. "the crawler runs exactly 
two passes, never a third hop"). If a boundary changes branching or flow, flag it for LOGIC.md 
too — as an active constraint on the flow, not just a stated boundary.

### Agent design pass

For each agent role drafted in theme 4, check it against five conventions:

- **Single responsibility & boundaries** — one job, with an explicit "does NOT do" line if 
  there's any realistic overlap with another agent.
- **Input → output contract** — what it receives and what it returns, concretely (not just 
  "data" or "a result").
- **Tools/context scope** — what it needs access to, and nothing more.
- **Coordination role** — orchestrator, worker, or peer, stated rather than implied by the 
  coordination model paragraph alone.
- **Failure/escalation path** — what happens if this agent fails or returns bad output: 
  retry, fall back, escalate, or halt.

If a role is missing one of these and it's load-bearing — the critical-path agent, or one 
whose failure mode is genuinely unclear — treat the gap as blocking: resolve it via the 
vagueness protocol before continuing. If it's a minor role and the gap is low-stakes (e.g. 
exact retry count), treat it as a safe-to-defer assumption per the classification above.

This pass doesn't require new interview themes — it's a sharper read of what theme 4 already 
produced, and it shapes the per-agent structure of `[slug]-AGENTS.md`.

---

## Step 2 — present a synthesis summary

Show the user a compact summary of what the system will document. Use this format:

> **[Project name] — synthesis**
>
> **Mission:** [one sentence]  
> **Triggered by:** [who/what and when]  
> **Input:** [what goes in]  
> **Output:** [what comes out, and to whom]  
> **Agents:** [list with one-line responsibilities]  
> **Out of scope:** [explicit boundaries]  
> **Key constraints:** [named limits]  
> **Success looks like:** [observable signal]  
> **Handover to:** [who/what, first action]  
>
> **Assumptions made:** [list any named assumptions, each tagged (safe to defer / blocking), 
> or "none"]  
> **Load-bearing boundaries:** [out-of-scope items that also constrain LOGIC.md, or "none"]  
> **Contradictions resolved:** [summary, or "none"]

Then ask:

> "Does this capture it accurately? Any corrections before I generate the files?"

Do not generate files until the user confirms.

---

## Step 3 — handle corrections

If the user corrects something:
- Update your internal model
- Re-state only the corrected item in the summary
- Confirm once more before proceeding

If the user confirms: proceed to [`OUTPUT.md`](./OUTPUT.md).
