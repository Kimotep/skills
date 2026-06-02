# Output Templates

All Keen EyeOS outputs are `.md` files. Use these templates as the base structure.
Fill in all sections; mark any unknown sections as `[TBD — pending user input]`.

---

## Keen Design Plan {#keen-design-plan}

```markdown
# Keen Design Plan — [Project Name]
_Generated: [date]_

## Project Overview
**Platform(s):** [iOS / macOS / iPadOS / etc]
**Deployment target:** [e.g., iOS 16+]
**App type:** [e.g., productivity / media / utility / social]

## The User
[2–3 sentence description of primary user and their context]

## The Core Moment
> "[When I ____], I want to [____], so I can [____]."

## Design Principles
1. [Principle — stated as an actionable rule, e.g. "Prioritize glanceability over depth on first open"]
2. [Principle]
3. [Principle]
_(3–5 principles)_

## Visual Language Direction
**Color posture:** [e.g., System-native with a single accent color / Full custom palette]
**Typography:** [e.g., System type scale only / Custom display font for headlines]
**Spacing philosophy:** [e.g., Use system defaults (16pt margins) / Dense information layout]
**Iconography:** [e.g., SF Symbols throughout / Custom icon set]

## Navigation Pattern
**Recommended:** [e.g., TabView with 4 tabs + NavigationStack per tab]
**Rationale:** [1–2 sentences]

## Component Philosophy
[1 paragraph: when to use system native vs custom, and the reasoning]

## Success Looks Like
- [Observable outcome 1]
- [Observable outcome 2]

## Open Questions
- [Any unresolved design decisions that need future Keen sessions]
```

---

## Keen Wireframes {#keen-wireframes}

```markdown
# Keen Wireframes — [Feature or Screen Name]
_Project: [Project Name] | Date: [date]_

## Context
**Screen:** [Where this lives in the app]
**Entry point:** [How user arrives here]
**Navigation type:** [Push / Sheet / Popover / Root]

## Wireframe: [State Name, e.g. "Default / Populated"]

[ASCII wireframe here]

### Annotations
| Element | Component | Notes |
|---|---|---|
| [Label from wireframe] | [SwiftUI component] | [Behavior or constraint note] |

---

## Wireframe: [State Name, e.g. "Empty State"]

[ASCII wireframe here]

### Annotations
...

---

## Interaction Notes
- [Tap on X → navigates to Y]
- [Swipe left on row → reveals delete action]
- [Pull down → refreshes]
```

---

## Keen Technical Handover {#keen-technical-handover}

```markdown
# Keen Technical Handover — [Feature or Screen Name]
_Project: [Project Name] | Date: [date] | Platform: [iOS/macOS/etc]_

## Overview
[1–2 sentence description of what this spec covers]

## Deployment Target
Minimum OS: [e.g., iOS 16.0]
Tested on: [e.g., iPhone 15 Pro, iPhone SE 3rd gen]

## Navigation
- Presented as: [NavigationStack push / .sheet / .fullScreenCover / .popover]
- Dismiss: [Back button / swipe / explicit Done button]

## Screen Structure
```swift
// Structural pseudocode — not final implementation
NavigationStack {
    List {
        Section {
            ForEach(items) { item in
                ItemRow(item: item)
            }
        }
    }
    .navigationTitle("Title")
    .searchable(text: $query)
}
```

## Components

### [Component Name]
- **Type:** [SwiftUI component]
- **Purpose:** [What it does in this feature]
- **Key parameters:** [relevant init params and modifiers]
- **States:** [default / loading / disabled / error]
- **Accessibility:** [label, hint, traits required]

### [Component Name]
...

## Layout
- **Margins:** [e.g., 16pt horizontal, system default vertical]
- **Spacing:** [e.g., 12pt between rows, 8pt within row content]
- **Safe area:** [respected / ignored where and why]

## Typography
| Role | Style | Notes |
|---|---|---|
| Screen title | `.title2` / `.navigationTitle` | |
| Row primary | `.body` | |
| Row secondary | `.subheadline` `.secondary` | |
| Caption | `.caption` | |

## Color
| Token | Usage | Light | Dark |
|---|---|---|---|
| Primary action | Buttons, links | `.tint` (system blue) | same |
| Destructive | Delete, remove | `.red` | same |
| Background | Screen bg | `.systemGroupedBackground` | same |

## Accessibility
- [ ] All interactive elements have `.accessibilityLabel`
- [ ] Focus order follows visual reading order
- [ ] Supports Dynamic Type (no fixed heights on text containers)
- [ ] Tested with VoiceOver navigation
- [ ] Reduce Motion: [note any animations that need `.animation(nil)` fallback]

## Open Items
- [ ] [Any unresolved question for developer or designer]
```

---

## Keen Stage {#keen-stage}

```markdown
# Keen Stage — [Screen Name]
_Project: [Project Name] | Device: [device] | Appearance: [light/dark]_

## Staged Mockup

[Device frame with screen content — ASCII or HTML/SVG artifact]

## Design Decisions Visible in This Stage
1. [Decision and rationale]
2. [Decision and rationale]

## What This Doesn't Show
- [Interaction / animation not representable in static mockup]
- [Dynamic content that will vary]

## Next Step
[ ] Confirm → proceed to Keen Technical Handover
[ ] Adjust → return to Keen Polish or Keen Feature
```
