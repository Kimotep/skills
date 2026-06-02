# Keen Vision — Keen EyeOS Sub-skill

**Purpose**: Establish shared understanding of a project's design direction before any feature
or element work begins. This is the "north star" session. Output is a Keen Design Plan.

**Invoke when**:
- User is starting a new app from scratch
- User wants to align on the overall feel and direction of an existing app before iterating
- User says something like "I don't know what I want it to look like yet"
- Sub-tasks are feeling inconsistent — suggesting the vision was never established

---

## Keen Vision Questions

Run these in order, one at a time. Adapt language to `[USER_LEVEL]`.

### 1. The Core Moment
> "Imagine your app working perfectly. What is the user doing in the single most important moment?"
- Multiple choice (if user is stuck): A) Looking up information · B) Creating something · C) Completing a task · D) Being notified/informed · E) Something else

### 2. The User
> "Who is using this? Describe them."
- Prompt if stuck: approximate age, technical confidence, context (commuting? at desk? glancing quickly?)

### 3. The Platform Contract
> "Which Apple platforms do you need to support?" (select all that apply)
- A) iPhone · B) iPad · C) Mac (native) · D) Mac Catalyst · E) Apple Watch · F) visionOS

> "What's the minimum iOS/macOS version you're targeting?"

### 4. The Feel
*Frame this at [USER_LEVEL]:*
- **Beginner**: "If your app was a physical object or a place, what would it be?"
- **Intermediate**: "Pick a vibe: [A] Clean/minimal · [B] Warm/personal · [C] Bold/expressive · [D] Functional/professional · [E] Playful"
- **Practised+**: "Where does this sit on these axes? (System-native ↔ Custom-branded) and (Content-first ↔ Chrome-forward)"

### 5. The Benchmark
> "Is there an existing app — Apple's own or third-party — whose design you admire or want to learn from?"
- Note: this is reference inspiration, not copying intent

### 6. The Anti-Pattern
> "Is there anything about common app design that you specifically want to avoid?"

---

## Vision Summary

After collecting answers, produce a **Vision Brief** (3–5 sentences) and confirm with user before
proceeding to output. Structure:

> "[App name] is a [platform] app for [user]. The core moment is [action]. The feel should be
> [adjectives], leaning toward [native/custom] UI with [content/chrome]-first layout.
> Inspiration: [reference apps]. Avoid: [anti-patterns]."

---

## Output: Keen Design Plan

After confirmation, generate `keen-design-plan.md` using the template in `output-templates.md`.

Sections:
- Project name and platform(s)
- User definition
- Core user moment
- Design principles (3–5, stated as actionable rules)
- Visual language direction (color posture, type scale intent, spacing philosophy)
- Navigation pattern recommendation with rationale
- Component philosophy (system-native vs custom, and when to cross the line)
- What success looks like (1–2 measurable or observable outcomes)
