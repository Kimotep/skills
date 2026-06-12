# SYNTHESIS.md — reflection, classification, and confirmation before output

This document defines what happens between the end of the interview and the generation of the 
new writer skill. Do not skip this phase, even if the interview felt clean.

---

## Purpose of synthesis

The interview collects raw material — tone words, examples, opinions, maybe samples. 
Synthesis turns that into a coherent voice profile. The LLM's job here is to:

1. Compress everything into a single, usable picture
2. Surface anything that still doesn't add up — including sample vs stated-tone mismatches
3. Get explicit user confirmation before writing any files

---

## Step 1 — internal review

Before saying anything to the user, do a silent review across all 8 themes:

- Is there a confirmed purpose statement and scope (one voice, or first of several)?
- Is at least one audience named, with what they expect?
- Are tone words, formality, person, and energy confirmed?
- Were writing samples analyzed and their patterns confirmed — or was opting out explicit?
- Are structure and formatting habits named?
- Are "reach for this" and "never this" vocabulary items named?
- Are at least one anti-pattern and one hard boundary named?
- Is the content-type list confirmed, with the writer's name and install context?
- Were any contradictions found and resolved?
- Were any named assumptions made? (These must appear in the output)

If any item is unresolved, go back and ask before continuing.

### Classify named assumptions

For each named assumption, decide:

- **Safe to defer** — a small detail, cheap to fix later (a word choice, one example, minor 
  formatting preference).
- **Blocking** — shapes the whole voice profile: formality level, person, primary audience, 
  or which content types exist. Getting this wrong means the generated writer sounds wrong 
  across everything it produces.

If an assumption looks blocking, don't let it ride. Go back through the vagueness protocol 
before continuing. Only genuinely low-stakes details should reach the output tagged "safe to 
defer".

### Voice consistency check

If writing samples were provided, do one more pass: do the tone words, formality, and person 
from theme 3 actually match the patterns observed in the samples? Small differences are 
normal — a sample might be more polished than someone's natural speaking tone, for instance. 
But if there's a real tension (stated "punchy and short" vs samples that are long and 
meandering, or vice versa), surface it now if it wasn't already resolved in theme 4.

---

## Step 2 — present a synthesis summary

Show the user a compact summary of the voice profile. Use this format:

> **[Writer name] — voice profile**
>
> **Purpose:** [one sentence — what this writer is for]  
> **Audience(s):** [who reads this, and what they expect]  
> **Voice:** [3–5 tone words; formality; person; energy]  
> **Sample-based notes:** [2–3 concrete patterns observed, or "none — built from interview 
> only"]  
> **Structure & formatting:** [typical length/structure; formatting habits]  
> **Vocabulary:** [a few "reach for" and "avoid" items]  
> **Boundaries & anti-patterns:** [what would make a draft obviously wrong]  
> **Content types:** [list, with any per-format adjustments noted]  
> **Installs to:** [project(s) or "general purpose"]  
>
> **Assumptions made:** [each tagged safe to defer / blocking, or "none"]  
> **Contradictions resolved:** [summary, or "none"]

Then ask:

> "Does this sound like you? Anything to adjust before I build the writer?"

Do not generate files until the user confirms.

---

## Step 3 — handle corrections

If the user corrects something:
- Update your internal model
- Re-state only the corrected item in the summary
- Confirm once more before proceeding

If the user confirms: proceed to [`OUTPUT.md`](./OUTPUT.md).
