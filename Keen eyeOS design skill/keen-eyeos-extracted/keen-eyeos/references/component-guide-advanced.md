# Component Guide — Advanced (Practised / Expert)

Loaded when [USER_LEVEL] is Practised or Expert.
Covers less common components, newer APIs, and patterns with meaningful tradeoffs.

---

## Data & Charts

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Bar / line / point chart | `Chart` + `BarMark` / `LineMark` / `PointMark` | 16+ | ✅ | Swift Charts framework — import separately |
| Area chart | `AreaMark` | 16+ | ✅ | |
| Circular progress / gauge | `Gauge` | 16+ | ✅ | Styles: `.circular` `.linear` `.accessoryCircular` |
| Multi-column data | `Table` | 16+ | ⚠ | iPad / Mac only — collapses on iPhone |

---

## Forms & Settings

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Settings / preferences screen | `Form` | all | ✅ | Renders differently per platform — test on each |
| Key/value display row | `LabeledContent` | 16+ | ✅ | Replaces manual HStack for info rows ↩ |
| Expandable section | `DisclosureGroup` | all | ✅ | Good for progressive disclosure in forms |
| Grouped content block | `GroupBox` | all | ✅ | More prominent on macOS than iOS |

---

## Media & System

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Native share sheet | `ShareLink` | 16+ | ✅ | Replaces UIActivityViewController ↩ |
| Photo library picker | `PhotosPicker` | 16+ | ✅ | No permission prompt needed for picker UI |
| Map view | `Map` | all | ⚠ | MapKit for SwiftUI — API changed significantly in 17+ |

---

## Scroll & Collections (Advanced)

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Grid layout | `LazyVGrid` / `LazyHGrid` | all | ✅ | Define `GridItem` columns — use `.adaptive` for responsive |
| Horizontal snap scroll | `ScrollView(.horizontal)` + `.scrollTargetBehavior` | 17+ | ✅ | Pre-17: manual offset tracking 🔴 |
| Scroll position tracking | `scrollTargetLayout` + `ScrollPosition` | 17+ | ✅ | |
| Pagination / infinite scroll | `List` + `.onAppear` on last item | all | ⚠ | Or `scrollTargetLayout` on 17+ |

---

## Toolbar & Navigation (Advanced)

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Toolbar items | `.toolbar` + `ToolbarItem` | all | ✅ | Use `placement:` explicitly |
| Grouped toolbar items | `ToolbarItemGroup` | all | ✅ | |
| Search toolbar behavior | `.searchPresentationToolbarBehavior` | 17+ | ⚠ | Only needed when overriding default |
| Inline tips / feature callouts | `TipKit` | 17+ | ✅ | System-managed display frequency |

---

## Layout (Advanced)

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Adaptive to available space | `ViewThatFits` | 16+ | ✅ | Prefer over `horizontalSizeClass` checks |
| Geometry-dependent layout | `GeometryReader` | all | 🔴 | Last resort — breaks layout predictability. Use anchors or `.containerRelativeFrame` (17+) instead |
| Container-relative sizing | `.containerRelativeFrame` | 17+ | ✅ | Cleaner replacement for many GeometryReader uses ↩ |

---

## SF Symbols (Advanced)

| Pattern | Notes |
|---|---|
| Rendering mode | `.symbolRenderingMode(.hierarchical / .palette / .multicolor)` |
| Variable value | `Image(systemName: "wifi", variableValue: 0.7)` — animatable signal/progress |
| Weight matching | `.fontWeight()` on surrounding text propagates to symbol |
| Scale | `.imageScale(.small / .medium / .large)` |
| Animation (17+) | `.symbolEffect(.bounce / .pulse / .variableColor)` |

---

## Color Semantics

Always use semantic colors — never hardcode hex in production UI.

| Token | Usage |
|---|---|
| `.primary` / `.secondary` | Text hierarchy |
| `.systemBackground` | Main screen background |
| `.secondarySystemBackground` | Cards, grouped sections |
| `.systemGroupedBackground` | Grouped List background |
| `.secondarySystemGroupedBackground` | Cells inside grouped List |
| `.tint` | Accent color — set once at app root |
| `Color("AssetName")` | Custom brand colors with dark mode variants in asset catalog |

