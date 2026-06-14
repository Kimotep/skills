# INTERVIEW.md — themes, sample analysis, pacing, and pause/resume

This document defines how the LLM conducts the interview. Read this before asking the user a 
single question.

---

## Pacing rules

- **Adaptive pacing**: do not ask all questions upfront. Let answers shape what to ask next.
- Ask 2–4 questions per exchange — never a wall of text.
- After each exchange, briefly summarise what you've heard before moving on.
- Keep a running internal count. If you're past 20 minutes and haven't covered all themes, 
  compress the remaining ones into a single tighter exchange — unless the pause/resume 
  condition below applies instead.
- **Never show rationale for questions.** Ask cleanly. The user doesn't need to know why.
- The writing-samples pass (theme 4) can happen whenever it's natural — often right after 
  theme 3, once the user has described their voice in words and a sample can confirm or 
  complicate that.

---

## Using interactive question tools

If the runtime exposes a structured question tool (e.g., Cowork's `AskUserQuestion` — up to 
4 multiple-choice questions per call, each with 2-4 options plus an automatic "Other" 
free-text option), use it for the theme questions below instead of typing them as plain chat 
text:

- Turn each theme's "Key questions to draw out" into 1-4 short questions per call, matching 
  the 2-4-questions-per-exchange pacing rule above. Word options the way a user might phrase 
  the answer themselves — "Other" always covers anything not listed.
- After the user answers, briefly summarise what was chosen/typed before moving on, same as 
  for conversational answers.
- Use plain conversational text instead for: reflections and summaries, the vagueness 
  protocol, contradiction handling, sample analysis discussion, drift detection, and 
  synthesis — anything needing back-and-forth nuance rather than pick-one-or-type-your-own.
- If no such tool is available, ask everything conversationally as described throughout this 
  document.

**Example — theme 3 (voice and personality) as structured questions:**
- "How formal should this voice be?" → Casual / Conversational / Professional but warm / 
  Formal (+ Other)
- "Which person does this voice write in?" → First person ("I") / Second person ("you") / 
  Third person or brand voice (+ Other)
- "Is humor part of this voice?" → No, rarely / Dry or understated / Playful / 
  Self-deprecating (+ Other)

---

## The 8 themes

Work through all 8. Order is flexible — let conversation flow — but every theme must be 
covered before synthesis begins. Mark each as resolved internally before moving on.

### 1. Purpose and where this voice lives
_What is this writer for, and where will it be used?_

Key questions to draw out:
- Is this for a specific brand or project, or a personal voice that should carry across 
  everything?
- Which project(s) will this skill end up installed in?
- Does the user need one voice here, or do they wear different hats (e.g. professional vs 
  personal) that might need separate writers?

Resolved when: there's a one-sentence purpose statement and a clear scope — one voice, or a 
note that this is the first of several.

---

### 2. Audience
_Who reads this, and what do they expect?_

Key questions to draw out:
- Who is the primary reader? Does the audience change by format (e.g. blog readers vs email 
  subscribers)?
- What do they already know about the user or the topic?
- What's the relationship — peer, customer, follower, colleague?
- What do they come to this content for — information, entertainment, persuasion, connection?

Resolved when: at least one audience is named, with what they expect from the content.

---

### 3. Voice and personality
_What does this voice sound like?_

Key questions to draw out:
- If this voice were a person talking, how would they come across? Ask for 3–5 tone words.
- Formality — formal, casual, somewhere in between? An example helps more than a label.
- First person, second person ("you"), or more removed/third person?
- Humor — present or absent? If present, what kind — dry, playful, self-deprecating?
- Energy — calm and measured, or punchy and urgent? Does it vary by format?

Resolved when: a short tone-word list plus formality, person, and energy are confirmed.

---

### 4. Writing samples (optional)
_Do you have writing that already sounds like you?_

Ask directly:
> "Do you have one to three pieces — a blog post, an email, even a few paragraphs — that 
> sound like you? You can paste them here or attach a file. Totally optional — if not, we'll 
> work from how you describe your voice."

**If the user provides samples:**
- Read them. Look for concrete, observable patterns: sentence length and rhythm, paragraph 
  structure, recurring words or phrases, how pieces open and close, anything that would feel 
  distinctly *theirs* if a generic AI wrote the same topic.
- Reflect back 2–3 specific patterns and confirm: "I'm noticing X, Y, Z — does that feel like 
  an accurate read, or am I off?"
- If a pattern in the sample contradicts what the user said in theme 3 (e.g. they said 
  "formal" but the sample is loose and funny), treat this as a contradiction — see 
  Contradiction handling below. Don't quietly pick one.

**If the user has no samples:**
- Skip. Note in synthesis that the profile is interview-only. This is fine — just slightly 
  lower confidence, and worth saying so in the output rather than pretending otherwise.

Resolved when: samples are analyzed and patterns confirmed, or the user has explicitly opted 
out.

---

### 5. Structure and formatting habits
_How do pieces usually take shape?_

Key questions to draw out:
- Typical length — does it vary by format (a social post vs a blog post vs an email)?
- How do pieces usually open and close? Any go-to moves — a question, a short story, a stat, 
  a direct claim?
- Formatting habits — headers, bullet lists, bold text, em-dashes — used heavily, sparingly, 
  or avoided on purpose?

Resolved when: structure/length and formatting preferences are named, at least at a general 
level that a future writer could follow.

---

### 6. Vocabulary and signature moves
_What words and moves make this sound like you?_

Key questions to draw out:
- Words or phrases the user reaches for often — even small ones (e.g. "honestly", "here's the 
  thing", specific transitions).
- Words or phrases the user actively dislikes or would never use.
- Any signature techniques — direct address to the reader, callbacks to earlier points, 
  recurring metaphors or framings, a particular way of ending a piece.

Resolved when: at least a few "reach for this" and "never this" items are named — these are 
some of the most useful lines in the final output.

---

### 7. Boundaries and anti-patterns
_What would make this writer obviously wrong?_

Key questions to draw out:
- What does "sounds like AI" mean to this user, specifically? Clichés, em-dash overuse, 
  "in today's fast-paced world"-style openers, excessive hedging, something else entirely?
- Are there topics, claims, or tones that are off-limits for this voice?
- What's an instant red flag — what would make the user reject a draft outright, no second 
  read needed?

Resolved when: at least one concrete anti-pattern and one hard boundary are named.

---

### 8. Content types and handover
_What does this writer need to produce, and where does it go?_

Key questions to draw out:
- Which formats need their own reference? Offer the common starting set — blog posts / 
  long-form, marketing & product copy, email & newsletters, social media, personal messaging 
  — and ask if anything's missing or irrelevant. The user can add formats not on this list.
- For each format selected, does anything shift from the baseline voice? (e.g. "LinkedIn can 
  be punchier than my blog", "emails are warmer than my marketing copy")
- Confirm the writer's name (proposed at the start of the session — revisit if needed) and 
  where it'll be installed: one project, several, or shared across all of them.

Resolved when: a confirmed list of content types (each with any voice adjustments), and a 
confirmed name plus install context.

---

## Vagueness protocol

When a user's answer is unclear or too abstract, follow this sequence:

1. **Reflect it back** — paraphrase what you heard and ask if that's right.  
   _"So your voice is more conversational than corporate — is that the right read?"_

2. **Offer examples** — give 2–3 concrete examples of what the answer could look like.  
   _"For example, that could mean opening with a question, a short anecdote, or a direct 
   claim — which feels closest to how you'd start?"_

3. **Named assumption** — only if the user remains vague after both steps, state an explicit 
   assumption and continue. Before doing so, check whether this assumption would be "safe to 
   defer" or "blocking" (see SYNTHESIS.md) — if blocking, don't settle for an assumption; keep 
   working the vagueness protocol or flag it for a second pass.  
   _"I'll assume a warm, conversational tone for now and flag it in the output — easy to 
   adjust later."_

Never skip straight to step 3.

---

## Contradiction handling

Track consistency across answers, including between stated preferences and any writing 
samples. If a later answer — or a sample — contradicts an earlier one:

- Name the contradiction directly and neutrally.  
  _"Earlier you described this as fairly formal, but the piece you shared reads pretty loose 
  and funny — those pull in different directions. Which one is closer to what you want this 
  writer to do?"_
- Do not move on until resolved.
- Note the resolution for use in synthesis.

---

## Pause and resume

Around the 15-minute mark, take stock. Building a voice profile is personal — some users know 
exactly how they sound; others are discovering it as they go. If most themes are still open 
and answers feel exploratory rather than confirmed — lots of "hmm, let me think", revised 
answers, or "I've never put it into words before" — the 30-minute frame won't hold, and 
compressing harder will produce a thin, generic profile. Offer a way out:

> "We're about halfway through and there's still a lot to work out — which makes sense, this 
> isn't something most people have written down before. We can keep going, or I can save 
> where things stand and you pick this up fresh next session."

If the user chooses to pause, skip synthesis and output entirely. Write a single 
`[slug]-STATE.md` file (see [`OUTPUT.md`](./OUTPUT.md)) capturing what's resolved, what's 
open, any sample analysis done so far, and the user's own words on anything still fuzzy. The 
next session resumes from there rather than restarting.

This differs from ordinary compression (see pacing rules above): compression is for someone 
who knows their voice but ran long on one topic. Pausing is for a voice that isn't fully 
articulated yet. If unsure which applies, ask the user directly.

---

## Drift detection

After completing the interview, before moving to synthesis, run a drift check:

Review the user's free-text answers (and any samples) against the structured answers. Look 
for:
- Topics or qualities the user returned to repeatedly — these often matter more than their 
  ranked answers suggest
- Language in free text or samples that sits awkwardly with a more structured answer (e.g. 
  theme 3 vs theme 4)
- New preferences introduced late that weren't captured earlier

If drift is found, surface it:
> "I noticed you kept coming back to [X] — that wasn't fully captured in our earlier answers. 
> Should it be more central to the voice profile?"

Then proceed to [`SYNTHESIS.md`](./SYNTHESIS.md).
