# Component Guide — Core (All Levels)

Loaded for every session regardless of user level.
Covers the components that appear in the vast majority of iOS apps.

Confidence markers: ✅ standard · ⚠ has caveats · 🔴 workaround needed
OS floor noted inline: `16+`, `17+`

---

## Navigation

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Hierarchical drill-down | `NavigationStack` | 16+ | ✅ | Replaces `NavigationView` ↩ |
| Tab switching | `TabView` | all | ✅ | Use `.tabItem` modifier |
| Temporary task/overlay | `.sheet` | all | ✅ | Prefer over push for self-contained tasks |
| Confirmation / destructive | `.confirmationDialog` | all | ✅ | Use instead of Alert for 3+ options |
| Single dismissable message | `.alert` | all | ✅ | Max 2 actions |
| Contextual options | `.contextMenu` | all | ✅ | Long press (iOS) / right-click (Mac) |

---

## Lists & Scroll

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Scrollable rows | `List` | all | ✅ | Lazy, best for long data sets |
| Section grouping | `Section` inside `List` | all | ✅ | Supports headers and footers |
| Pull to refresh | `.refreshable` on `List` | all | ✅ | Also works on `ScrollView` |
| Swipe row actions | `.swipeActions` | 15+ | ✅ | Replaces `editActions` ↩ |
| Drag to reorder | `.onMove` on `List` | all | ⚠ | Requires `EditButton` or manual `.editMode` |

---

## Input & Controls

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Short text input | `TextField` | all | ✅ | Add `.textContentType` for autofill |
| Multi-line text | `TextEditor` | all | ⚠ | No native placeholder — ZStack overlay workaround 🔴 |
| On/off toggle | `Toggle` | all | ✅ | Default renders as switch |
| Pick from list | `Picker` | all | ✅ | Styles: `.menu` `.segmented` `.wheel` `.inline` |
| Date / time | `DatePicker` | all | ✅ | `.compact` inline · `.graphical` calendar |
| Bounded number | `Stepper` | all | ✅ | Good for small integer ranges |
| Range value | `Slider` | all | ✅ | Add `step:` for discrete values |
| Search | `.searchable()` | 15+ | ✅ | Attach to `NavigationStack` or `List` |

---

## Content Display

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Any text | `Text` | all | ✅ | Always use semantic font styles |
| Font styles | `.font(.title)` → `.caption2` | all | ✅ | Never hardcode sizes — Dynamic Type |
| Local image | `Image("name")` | all | ✅ | `.resizable().scaledToFit()` |
| Remote image | `AsyncImage` | 15+ | ⚠ | No built-in error UI — handle phases explicitly |
| SF Symbol | `Image(systemName:)` | all | ✅ | Match symbol weight to surrounding text |
| Icon + label pair | `Label` | all | ✅ | Often missed — use instead of manual HStack |
| Loading indicator | `ProgressView` | all | ✅ | `.circular` or `.linear` |
| Empty state | `ContentUnavailableView` | 17+ | ✅ | Use custom VStack fallback on 16 |

---

## Layout Primitives

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Vertical stack | `VStack` | all | ✅ | Eager — never use for long lists |
| Horizontal stack | `HStack` | all | ✅ | Set `alignment:` and `spacing:` explicitly |
| Z-axis overlay | `ZStack` | all | ✅ | Badges, overlays, background fills |
| Flexible space | `Spacer()` | all | ⚠ | Use sparingly — prefer alignment params |
| Padding | `.padding()` | all | ✅ | Use system multiples: 8, 12, 16, 20 |
| Safe area | `.ignoresSafeArea(.keyboard)` | all | ⚠ | Only ignore exactly what you intend |

---

## Buttons & Affordance

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Any tappable element | `Button` | all | ✅ | Never use `onTapGesture` on complex views |
| Destructive action | `Button(role: .destructive)` | 15+ | ✅ | System renders in red automatically |
| Inline options menu | `Menu` | all | ✅ | Toolbar and inline — distinct from `.contextMenu` |
