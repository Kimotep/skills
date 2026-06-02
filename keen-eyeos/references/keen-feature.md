# Keen Feature — Keen EyeOS Sub-skill

**Purpose**: Design a new screen, flow, or capability within an existing (or in-progress) app.
Works from user intent → structure → wireframe → handover.

**Invoke when**:
- User wants to add something new to their app
- User has a feature idea and needs to figure out how it should look and work
- User says "I want to add a [X] screen" or "I need a way for users to [Y]"

---

## Pre-Flight: Establish App Context

Before feature-specific questions, confirm app-level understanding. Ask only what isn't known:

1. **App type**: What kind of app is this? (If not established from Keen Vision)
2. **Navigation pattern**: Tab bar / navigation stack / split view / other?
3. **Visual language**: Any existing color/type system in place?
4. **Feature entry point**: How does the user get to this feature? (What triggers it?)

---

## Keen Feature Questions

### 1. The Job
> "What job does this feature do for the user? Complete this sentence: 'When I [situation], I want to [action], so I can [outcome].'"
- Offer to fill in collaboratively if user is stuck

### 2. The Shape
> "How much of the screen should this take up?"
- A) Full screen (new destination) · B) Sheet/modal (temporary task) · C) Inline (within existing screen) · D) Popover/menu · E) Not sure yet

### 3. The Data
> "What information does the user need to see, and what can they do with it?"
- Prompt: "List the pieces of information (nouns) and the actions (verbs) — don't worry about layout yet"

### 4. The States
> "What are the different states this feature can be in?"
- Offer defaults: Empty state · Loading · Populated · Error · Partial data

### 5. The Frequency
> "How often will a user interact with this? Glance daily? Use deeply once a week? One-time setup?"
- This affects information density, gesture depth, and visual weight

### 6. The Edge
> "What's the most unusual or difficult situation a user might be in when they hit this feature?"
- e.g., offline, low data, first-time user, returning after months

---

## Structure Before Layout

After the questions, produce a **Feature Structure** (not a wireframe yet):

```
Feature: [Name]
Entry: [how user arrives]
States: [list]
Content elements: [noun list]
Actions: [verb list]
Recommended shape: [Full screen / Sheet / etc] — rationale: [1 sentence]
Navigation: [back / dismiss / deep link?]
```

Confirm with user. Then proceed to Keen Wireframes output.

---

## Output

1. **Keen Wireframes** — ASCII wireframe for each key state (min: empty + populated)
2. **Keen Technical Handover** — component spec for the feature
   - SwiftUI component list with parameters
   - Layout: VStack/HStack/LazyVGrid/etc structure
   - Navigation type: NavigationStack push / .sheet / .popover
   - Accessibility: label requirements, focus order
