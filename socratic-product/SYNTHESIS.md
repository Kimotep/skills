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
> **Assumptions made:** [list any named assumptions, or "none"]  
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
