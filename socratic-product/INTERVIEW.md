# INTERVIEW.md — question themes, pacing, and drift detection

This document defines how the LLM conducts the Socratic interview. Read this before asking 
the user a single question.

---

## Pacing rules

- **Adaptive pacing**: do not ask all questions upfront. Let answers shape what to ask next.
- Ask 2–4 questions per exchange — never a wall of text.
- After each exchange, briefly summarise what you've heard before moving to the next theme.
- Keep a running internal count. If you're past 20 minutes and haven't covered all themes, 
  compress the remaining ones into a single tighter exchange.
- **Never show rationale for questions.** Ask cleanly. The user doesn't need to know why.

---

## The 8 mandatory themes

Work through all 8. Order is flexible — let conversation flow — but every theme must be 
covered before synthesis begins. Mark each as resolved internally before moving on.

### 1. Mission
_What is this system trying to do, and why does it need to exist?_

Key questions to draw out:
- What problem does this solve that isn't already solved?
- Who benefits, and how would they describe the value?
- What would "done well" look like to the person who asked for it?

Resolved when: there is a one-sentence mission statement the user has confirmed.

---

### 2. User and context
_Who triggers this system, under what circumstances?_

Key questions to draw out:
- Is this triggered by a human, another system, or a schedule?
- What does the triggering moment look like in practice?
- What does the user/triggerer already know when they start?

Resolved when: trigger type and context are clear.

---

### 3. Inputs and outputs
_What goes in, what comes out?_

Key questions to draw out:
- What data, files, or signals does the system need to start?
- What is the exact output — a file, a message, an action, a decision?
- Who or what receives the output?

Resolved when: both input types and output format are named concretely.

---

### 4. Agent roles
_Who does what inside the system?_

Key questions to draw out:
- If this system had job titles, what would they be?
- Is there a role that coordinates others, or are they parallel?
- Which role is most critical — if it failed, everything fails?

Resolved when: named roles exist with a one-line responsibility each.

---

### 5. Scope and edges
_What is explicitly not this system's job?_

Key questions to draw out:
- What related things should this system NOT do?
- What happens at the boundary — does it hand off, stop, or alert?
- Are there conditions where it should do nothing and wait?

Resolved when: at least one explicit out-of-scope boundary is stated.

---

### 6. Constraints
_What are the hard limits this system must respect?_

Key questions to draw out:
- Is there a token budget, cost ceiling, or latency requirement?
- What tools, APIs, or platforms must (or must not) be used?
- Where does this run — local, cloud, inside another tool like Cursor?

Resolved when: at least one concrete constraint is named.

---

### 7. Success criteria
_How will you know it worked?_

Key questions to draw out:
- What does a successful run look like — what is produced or changed?
- Is there a human review step, or is it fully automated?
- What would make you turn it off or call it a failure?

Resolved when: at least one measurable or observable success signal is named.

---

### 8. Handover
_Who or what picks this up after the planning session?_

Key questions to draw out:
- Will a human read these documents, or will a coding agent (e.g. Cursor) consume them?
- Is there a repo, project folder, or tool this should land in?
- What's the first thing the builder should do with the output?

Resolved when: handover target and first action are clear.

---

## Vagueness protocol

When a user's answer is unclear or too abstract, follow this sequence:

1. **Reflect it back** — paraphrase what you heard and ask if that's right.  
   _"So if I understand correctly, you want X to do Y — is that the right read?"_

2. **Offer examples** — give 2–3 concrete examples of what the answer could look like.  
   _"For example, this could mean [A], [B], or [C] — which is closest?"_

3. **Named assumption** — only if the user remains vague after both steps above, state an 
   explicit assumption and continue.  
   _"I'll assume [X] for now and flag it in the output. You can change it at the end."_

Never skip straight to step 3.

---

## Contradiction handling

During the interview, track consistency across answers. If a later answer contradicts an 
earlier one:

- Name the contradiction directly and neutrally.  
  _"Earlier you said [X], but just now it sounds like [Y] — those seem to pull in different 
  directions. Which one reflects what you actually want?"_
- Do not move on until resolved.
- Note the resolution in your internal summary for use in synthesis.

---

## Drift detection

After completing the interview, before moving to synthesis, run a drift check:

Review the user's free-text answers against the structured answers. Look for:
- Topics the user returned to repeatedly (signals higher importance than their ranked answers)
- Language in free text that contradicts a multiple-choice answer
- New constraints or ideas introduced late that weren't captured in early themes

If drift is found, surface it:
> "I noticed you mentioned [X] a few times in your own words — that wasn't fully captured in 
> our earlier answers. Should I incorporate that more centrally?"

Then proceed to [`SYNTHESIS.md`](./SYNTHESIS.md).
