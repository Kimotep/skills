---
name: keen-eyeos
description: >
  Apple platform UI/UX design skill for iOS, macOS, iPadOS, watchOS, and visionOS.
  Trigger when the user needs help with native SwiftUI/UIKit component selection,
  screen or feature design, UI polish, wireframes, design specs, or HIG compliance.
  Also trigger for phrases like "my UI feels off", "which component should I use",
  "does this feel like an Apple app", or "design my feature". See README.txt for
  full background and creator intent.
---

# Keen EyeOS

A structured design companion for Apple platform projects.
See `README.txt` for full background, creator intent, and scope.

**Token strategy:** SKILL.md is always in context. All reference files load lazily —
only what the session needs, gated by the choices below.

---

## 0. Entry Point: Intent Check (Fast Path Gate)

**Before running the full setup flow, check if this is a one-shot question.**

A one-shot question is one where:
- A single sub-skill can answer it completely
- No project context is needed to give a good answer
- No output file is expected

Examples: "Which component should I use for a settings screen?", "What's the difference
between `.sheet` and `.fullScreenCover`?", "How do I add swipe actions to a List row?"

**If the intent is clearly one-shot:**
→ Answer directly using loaded component guides appropriate to apparent user level
→ At the end, offer: "Want to go deeper on this within a full Keen EyeOS session?"
→ Do not run Steps 1–4

**If the intent requires design work, output files, or project context:**
→ Proceed to Step 1 below

---

## 1. Keen Level Check

Determines language register AND which component tier to load.

```
"To make sure I frame things the right way — where would you place yourself?"

A) New to design — I know what I want but not the vocabulary
   → loads: component-guide-core.md only
   → language: plain English, analogies over jargon, no API names

B) Design basics — I've built some UI before
   → loads: component-guide-core.md
   → language: design terms fine, SwiftUI names introduced with brief context

C) Comfortable with Apple HIG and SwiftUI/UIKit
   → loads: component-guide-core.md + component-guide-advanced.md
   → language: full API names, HIG references, tradeoff discussions

D) Design/engineering pro — go deep
   → loads: component-guide-core.md + component-guide-advanced.md + component-guide-platform.md
   → language: peer-level, no hand-holding, edge cases and gotchas welcome
```

Store as `[USER_LEVEL]`: Beginner / Intermediate / Practised / Expert.
Load indicated component guide(s) now. Do not load others unless session demands it.

---

## 2. Keen Context Check

Determines whether project context needs to be built or loaded.

```
"Are we working within an existing project?"

A) Yes — I have a Keen Design Plan already
   → paste or describe it → stored as [PROJECT_CONTEXT] → skip vision questions
   → token note: replaces ~3–4 vision questions later in session

B) Yes — but nothing formally written down
   → run Fast Context Questions below (4 questions)
   → token note: 4 questions now prevents redundant clarification throughout

C) No — starting fresh
   → [PROJECT_CONTEXT] = none → Keen Vision recommended as first sub-skill
   → token note: lightest start, vision built as we go
```

**Fast Context Questions (option B only)** — one at a time:
1. Platform(s): iPhone / iPad / Mac / Watch / other?
2. Core user action — one sentence: "The main thing a user does is ___"
3. Visual style in place? Colors, fonts, general vibe?
4. Navigation pattern: tabs / sidebar / stack / something else?

Summarize as `[PROJECT_CONTEXT]`, confirm before continuing.
Offer to generate a Keen Design Plan as a session byproduct.

**Platform-aware loading** once platform is known:
- iPhone only → skip `component-guide-platform.md` unless Expert
- iPad or Mac in scope → load `component-guide-platform.md` at Practised+
- Watch / visionOS → not covered in component guides; reference Apple HIG directly

---

## 3. Keen Output Check

Determines which output templates to load and shapes session depth.

```
"What do you want to walk away with? Pick one or more:"

A) Keen Design Plan
   — written brief: vision, principles, design direction
   → loads: output-templates.md#keen-design-plan
   → token note: vision-focused, component depth reduced

B) Keen Wireframes
   — annotated ASCII screen layouts
   → loads: output-templates.md#keen-wireframes
   → token note: layout and structure questions prioritised

C) Keen Technical Handover
   — developer-ready spec: components, layout, spacing, accessibility
   → loads: output-templates.md#keen-technical-handover
   → token note: heaviest output — component guides loaded fully for your level

D) Keen Stage
   — visual mockup inside a device frame
   → loads: keen-stage.md + output-templates.md#keen-stage
   → token note: runs at end of session regardless of other choices

E) Not sure yet — let's figure it out
   → no templates loaded now; recommended at session close
   → token note: lightest start, templates loaded only when output becomes clear
```

Store as `[KEEN_OUTPUTS]`. Load only the indicated template sections now.

---

## 4. Sub-skill Routing

Ask: "What are we working on today?" and route based on answer.
Load the relevant sub-skill reference file at this point — not before.

```
"Which of these fits best?"

A) Set or align on overall design direction  → keen-vision.md
B) Design a new screen or feature            → keen-feature.md
C) Fix something that feels off              → keen-polish.md
D) Design is limited by data or tech         → keen-signal.md
E) Show me what it looks like in a device    → keen-stage.md
```

Load only the chosen sub-skill's file. Do not pre-load others.
Keen Stage may already be loaded from Step 3 — do not load twice.

---

## Keen Design Questions Framework

One question at a time. Multiple-choice where possible. Language at `[USER_LEVEL]`.

**Question Ladder:**
1. Intent — what is this for, who uses it, what job does it do?
2. Context — where does it live, what comes before/after?
3. Constraints — platform, OS target, existing design system?
4. Ambition — native/neutral or distinctive/expressive?
5. Blockers — what's been tried, what felt wrong?

After 3–5 questions: summarize and confirm. If corrected, re-summarize before proceeding.

Language guide is internalized in the level definitions above.
Load `references/language-guide.md` only if mid-session recalibration is needed.

---

## Component Authority

- Prefer native SwiftUI first
- Flag UIKit when SwiftUI has a known gap for the use case
- Always note OS floor: `15+` `16+` `17+`
- Flag custom components and state the tradeoff explicitly
- Confidence markers: ✅ standard · ⚠ has caveats · 🔴 workaround needed

Component files (load per Step 1 + platform):
- `references/component-guide-core.md` — all levels, always
- `references/component-guide-advanced.md` — Practised / Expert
- `references/component-guide-platform.md` — iPad/Mac in scope, Practised+

---

## Reference Index

| File | Load when | Size |
|---|---|---|
| `keen-vision.md` | Keen Vision chosen | small |
| `keen-feature.md` | Keen Feature chosen | small |
| `keen-polish.md` | Keen Polish chosen | small |
| `keen-signal.md` | Keen Signal chosen | small |
| `keen-stage.md` | Keen Stage chosen (Step 3 or 4) | small |
| `component-guide-core.md` | Always (Step 1) | medium |
| `component-guide-advanced.md` | Practised / Expert | medium |
| `component-guide-platform.md` | iPad/Mac + Practised+ | medium |
| `language-guide.md` | Mid-session recalibration only | small |
| `output-templates.md` | Per output chosen in Step 3 | medium |
| `README.txt` | User asks about skill background/intent | small |
