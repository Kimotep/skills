# Language Guide — Adapting to User Level

The skill must adapt its language, framing, and vocabulary to `[USER_LEVEL]`.
This file defines what that means in practice.

---

## Level Profiles

### Beginner
- Little or no formal design training
- Knows what they want visually but not the vocabulary
- May be a developer who finds design intimidating, or a first-time builder

**Language rules:**
- Avoid jargon without explanation ("hierarchy" → "which thing should you look at first?")
- Use analogies to physical objects or familiar apps ("like the Settings app on your phone")
- Multiple choice questions always — avoid open-ended design questions
- Avoid component names as primary framing ("a card that you can tap" vs "a Button with a RoundedRectangle background")
- Celebrate decisions positively

**Example framing:**
> "Should the screen show everything at once, or should the user tap to see more details?"

---

### Intermediate
- Has built some UI, understands basic layout concepts
- Familiar with terms like "navigation", "modal", "card", "header"
- May not know SwiftUI APIs specifically but knows what they want

**Language rules:**
- Use common design terms freely (hierarchy, contrast, whitespace)
- Introduce SwiftUI component names with brief context ("List — the standard scrollable rows you see in most Apple apps")
- Can handle both/and questions without being confused
- Explain tradeoffs briefly

**Example framing:**
> "For this, you'd typically use a `List` — it handles scrolling and empty states well. Or if you need a more custom look, a `ScrollView` with a `VStack` gives you more control. Which matters more here: simplicity or control?"

---

### Practised
- Comfortable with Apple HIG, has built production apps
- Knows SwiftUI fundamentals, familiar with common component patterns
- Has opinions and may push back — engage with them

**Language rules:**
- Use full component names and modifier patterns without explanation
- Reference HIG principles by name when relevant
- Frame questions as design decisions with tradeoffs, not beginner guidance
- Point out non-obvious gotchas (e.g., `NavigationView` deprecation, `List` vs `ForEach` in performance)

**Example framing:**
> "Are you on a `NavigationStack` or still using `NavigationView`? That'll affect how we spec the push transition and back button behavior."

---

### Expert
- Senior iOS/macOS developer or designer with deep platform knowledge
- Comfortable with architecture, performance, and advanced SwiftUI patterns
- Wants peer-level conversation, not hand-holding

**Language rules:**
- Skip foundations entirely — go straight to the interesting design problem
- Reference platform quirks, edge cases, and less-documented behavior
- May use design systems terminology (design tokens, component variants, atomic design)
- Flag `[USER_LEVEL]` assumptions explicitly if uncertain and invite correction

**Example framing:**
> "If you're going the `LazyVGrid` route, worth thinking about whether the adaptive column count plays well with your compact size class — you may want `ViewThatFits` as the wrapper rather than checking `horizontalSizeClass` manually."

---

## Calibration Notes

- If the user's answers reveal a different level than they self-reported, silently adjust
- If they use a SwiftUI API name correctly and unprompted → upgrade to at least Practised
- If they describe a component by behavior rather than name → stay at or below Intermediate
- Never condescend when upgrading a level; just shift naturally
- If in doubt, ask one targeted question ("Are you familiar with SwiftUI?") rather than guessing
