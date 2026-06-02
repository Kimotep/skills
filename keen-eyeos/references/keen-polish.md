# Keen Polish — Keen EyeOS Sub-skill

**Purpose**: Diagnose and fix design feel for an existing UI element, screen, or flow.
This is the "something's off but I don't know what" sub-skill.

**Invoke when**:
- User says "it doesn't look right", "feels off", "too plain", "not native enough"
- User wants to iterate on a specific component or screen
- User has working code but is unhappy with the visual result
- User asks "which component should I use instead of X"

---

## Diagnosis First

Before suggesting fixes, understand what's actually wrong. Ask:

### 1. The Problem Statement
> "Describe what feels wrong — it can be vague. Words like 'too flat', 'feels crowded', 'looks cheap', or 'doesn't feel like an Apple app' are all useful starting points."

### 2. Show the Evidence *(if possible)*
> "Can you share a screenshot or paste your SwiftUI code? Even a rough description of what's on screen works."
- If code is shared: read it carefully, identify component choices, spacing, and color usage
- If screenshot: note contrast, density, type hierarchy, component misuse

### 3. The Benchmark
> "What does it look like when it's working well? Is there a screen in your app or another app that feels right?"

---

## Polish Diagnostic Framework

When reviewing an existing UI, evaluate against these axes:

| Axis | Ask yourself |
|---|---|
| **Component fit** | Is the native component being used for the right job? |
| **Visual hierarchy** | Is it clear what to look at first? |
| **Spacing & rhythm** | Does it breathe? Are elements too tight or too loose? |
| **Type scale** | Are the right text styles being used (title, headline, body, caption)? |
| **Color confidence** | Is the color intentional, or scattered? |
| **State clarity** | Is interactive vs non-interactive content visually distinct? |
| **Platform feel** | Does this look like it belongs on this Apple platform? |

---

## Polish Questions (component-level)

### For a specific component:
1. What is this component trying to communicate or enable?
2. What component is currently being used?
3. What feels wrong about it? (appearance / behavior / placement / all of them)
4. Is this inside a List, a ScrollView, a toolbar, or floating?

### Replacement recommendation format:
```
Current: [component]
Issue: [what's wrong and why]
Recommended: [component]
Rationale: [1–2 sentences grounded in HIG or visual logic]
Code direction: [SwiftUI snippet or param guidance]
```

---

## Output

- Inline diagnosis with prioritized fix list (most impactful first)
- **Keen Wireframes** showing the before/after structure if layout is involved
- **Keen Technical Handover** if fixes are substantial enough to spec out
- Short list of "quick wins" (1-line fixes) vs "considered changes" (structural)
