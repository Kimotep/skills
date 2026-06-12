# OUTPUT.md — generating the writer skill

This document defines how to produce the final output after synthesis is confirmed. The 
output is not a flat set of documents — it's a working Claude skill: a folder with its own 
`SKILL.md` and reference files, ready to be installed in a project or packaged as `.skill`.

---

## Naming convention

The writer's name (the "slug") was proposed at the start of the session and confirmed in 
theme 8. It must work as a skill name, so:

- Lowercase, hyphen-separated, no spaces or special characters
- Max 64 characters
- No leading/trailing hyphens, no double hyphens

If the user wants it in the `tumaini-` family, prefix accordingly (e.g. `tumaini-blogvoice`). 
If it belongs to a specific brand or project instead, name it for that 
(e.g. `acme-copywriter`, `kim-newsletter-voice`). Either is fine — this is the user's call, 
made in theme 8.

Before generating, confirm the slug one more time:

> "I'll build this as **[slug]** — that'll be the skill's folder and name. Last chance to 
> change it before I write the files."

---

## File set — what to generate

```
[slug]/
├── SKILL.md                       # entry point: voice-at-a-glance + routing
├── references/
│   ├── voice-profile.md           # full voice profile (always generated)
│   ├── blog-posts.md              # if selected in theme 8
│   ├── marketing-copy.md          # if selected
│   ├── email-newsletters.md       # if selected
│   ├── social-media.md            # if selected
│   ├── personal-messaging.md      # if selected
│   └── [custom-format].md         # any additional formats named in theme 8
└── README.md
```

Generate `SKILL.md`, `references/voice-profile.md`, one reference file per content type 
confirmed in theme 8, and `README.md`. Do not generate reference files for formats that 
weren't selected.

---

### `[slug]/SKILL.md`

The entry point. Keep this lean — the full profile lives in `references/voice-profile.md`. 
This file's job is triggering and routing.

```
---
name: [slug]
description: >
  Use this skill whenever [user/brand] needs written content — [comma-separated list of 
  selected content types] — and wants it in their established voice: [2-3 tone words]. 
  Triggers include requests to draft, write, edit, or rewrite [content types], or any request 
  to match [user/brand]'s tone or style. Always check references/voice-profile.md for the 
  full voice definition, and the matching references/[content-type].md file for 
  format-specific guidance, before writing anything.
license: MIT
metadata:
  generated_by: tumaini-voice
  version: 0.1.0
  generated_on: [session date]
---

# [Writer name]

[One-sentence purpose statement from synthesis.]

## Voice at a glance
- Tone: [tone words]
- Formality: [formality level]
- Person: [first/second/third]
- Energy: [energy description]
- Never: [the single most important anti-pattern or boundary]

Full profile: [`references/voice-profile.md`](./references/voice-profile.md)

## Before writing anything

1. Identify the content type being requested.
2. Read `references/voice-profile.md` for the baseline voice — every piece starts here.
3. If the content type matches one of the references below, read that file too. It may 
   adjust the baseline (length, structure, tone shifts).
4. If the content type doesn't match any reference, use `voice-profile.md` alone and ask 
   whether a new reference should be added for this format.

## Content types

| Format | Reference | Adjustments from baseline |
|---|---|---|
| [Format name] | `references/[file].md` | [adjustment note, or "None — use baseline voice"] |

[Repeat per selected content type.]

## Hard boundaries

[Verbatim list from interview theme 7 — what would make a draft wrong, no exceptions.]
```

---

### `[slug]/references/voice-profile.md`

The full voice definition. Every piece of writing this skill produces should be checked 
against this file.

```
# [Writer name] — voice profile

## Purpose
[One sentence — what this writer is for, and its scope (single voice / one of several).]

## Audience(s)
[Who reads this, and what they come to it for.]

## Tone & personality
- Tone words: [3-5 words]
- Formality: [description, with an example if one was given]
- Person: [first / second ("you") / third, and any nuance]
- Energy: [calm and measured / punchy and urgent / varies by format]
- Humor: [present/absent, and what kind]

## Structure & formatting habits
[Typical length (by format if it varies). How pieces open and close. Formatting habits — 
headers, lists, bold, em-dashes — and how heavily they're used.]

## Vocabulary
**Reach for:** [words/phrases the user uses often]  
**Avoid:** [words/phrases the user dislikes or never uses]

## Signature moves
[Recurring techniques — direct address, callbacks, specific transitions, framings, sign-offs.]

## Anti-patterns ("sounds like AI")
[Specific things that would make a draft feel generic or wrong for this voice — named in 
theme 7, verbatim where possible.]

## Notes from writing samples
[2-3 concrete patterns observed and confirmed during the interview, with brief justification. 
If no samples were provided, write: "None — this profile is built from the interview only. 
If patterns described here don't match in practice, samples can sharpen it later."]

## Assumptions
[Ledger format. For each assumption:
- **[Assumption]** — [why it was made]. *Safe to defer — revisit if [X].*
Blocking assumptions should not appear here — they were resolved during synthesis. If "none", 
write "None — all decisions confirmed."]
```

---

### `[slug]/references/[content-type].md`

One file per content type confirmed in theme 8. Use this shared shape, filled in with 
whatever the user said about that format (theme 8 adjustments) plus the structural defaults 
below as a starting point — adjust or remove defaults that don't match what the user said.

```
# [Content type] — format notes

## When this applies
[What kinds of requests this covers.]

## Adjustments from baseline voice
[Anything that shifts from voice-profile.md for this format — tone, formality, energy, 
length. If nothing shifts, write "None — use the baseline voice as-is."]

## Typical structure
[Length and shape for this format. Use the defaults below as a starting point if the user 
didn't specify otherwise:]

[Repeat per selected content type.]

## Checklist before delivering
- [ ] Matches the tone words and person in voice-profile.md
- [ ] Follows the structure above (or a deliberate, explainable departure)
- [ ] None of the anti-patterns from voice-profile.md are present
- [ ] [Any format-specific check from the interview]
```

**Structural defaults by format** (use only if the user didn't give their own, and adjust 
freely — these are starting points, not rules):

- **Blog posts / long-form** — hook or framing in the first 1-2 sentences, body developed in 
  sections, a clear takeaway or close rather than trailing off.
- **Marketing & product copy** — lead with the benefit, not the feature; one clear call to 
  action; short paragraphs.
- **Email & newsletters** — a subject line that earns the open, a greeting that matches the 
  relationship from theme 2, body, and a sign-off consistent with the voice.
- **Social media** — front-load the point (most platforms cut off previews); platform-aware 
  length; a hook that doesn't rely on a link to make sense.
- **Personal messaging** — shortest and least polished of all formats. Match how the user 
  actually writes a quick message, not a refined version of it. Fragments and informal 
  punctuation may be correct here even if avoided elsewhere.

---

### `[slug]/README.md`

```
# [Writer name]

Generated by [tumaini-voice](https://github.com/Kimotep/skills) on [date].

[One-sentence purpose statement.]

## What this is

A Claude skill that writes in [user/brand]'s voice: [tone words]. Covers: 
[comma-separated content types].

## How to use

Install this skill (or paste `SKILL.md` as context) in any project where you want content in 
this voice. The skill routes each request to `references/voice-profile.md` plus the matching 
format file under `references/`.

## Updating this voice

Run `tumaini-voice` again to revise — either start fresh or describe what's changed since this 
version.
```

---

## Conditional file — `[slug]-STATE.md`

Only generated if the session is paused before synthesis (see "Pause and resume" in 
[`INTERVIEW.md`](./INTERVIEW.md)). Replaces the file set above for this session.

```
# [Writer name] — session state

## Resolved themes
[Each of the 8 themes that reached "resolved" status, with a one-line summary.]

## Open themes
[Remaining themes, with whatever the user has said so far — even if rough, contradictory, or 
"still figuring this out". Don't smooth it over.]

## Sample notes so far
[Any patterns identified from writing samples, even partial. "None reviewed yet" if 
applicable.]

## In the user's own words
[Direct quotes or close paraphrases of anything the user kept returning to — the drift signal 
for the next session.]

## Resume instructions
Pick up with [next theme]. Do not re-ask resolved themes unless the user wants to revisit them.
```

---

## Delivery format

After generating all files in chat:

1. Confirm the slug and file list
2. Output each file in a clearly labelled fenced code block, grouped by path 
   (`[slug]/SKILL.md`, `[slug]/references/voice-profile.md`, etc.)
3. End with:

> "[Writer name] is ready. Drop the `[slug]/` folder into any project to use it, or I can 
> package it as a `.skill` file for easy install. Want to test it on a quick piece of writing 
> before we wrap up?"

If the user wants to test it, write a short sample in the new voice using only the generated 
files as guidance — this is the fastest way to catch a profile that reads right in summary 
but wrong in practice.

---

## Token hygiene in output

- No filler sentences. Every line earns its place — this skill will be loaded into context 
  every time it's used.
- Keep `SKILL.md` lean; detail belongs in `references/`.
- If a section has nothing to say (e.g. no formatting habits worth noting), write one line: 
  `[None identified.]` rather than padding.
