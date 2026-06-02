# Component Guide — Platform-Specific (iPad / Mac)

Loaded when iPad or Mac is in [PROJECT_CONTEXT] AND [USER_LEVEL] is Practised or Expert.
Covers components that behave differently or only exist on multi-window / large-screen platforms.

---

## Navigation (iPad / Mac)

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Sidebar + content + detail | `NavigationSplitView` (3-column) | 16+ | ✅ | Adaptive — collapses to stack on iPhone |
| 2-column split | `NavigationSplitView` (2-column) | 16+ | ✅ | |
| Inspector panel (trailing) | `.inspector(isPresented:)` | 17+ | ✅ | macOS / iPadOS only — sheet on iPhone |
| Floating panel / popover | `.popover` | all | ⚠ | Becomes `.sheet` on iPhone — design for both |

---

## Mac-Specific

| Use case | Component | OS | Confidence | Notes |
|---|---|---|---|---|
| Mac-style settings window | `Settings` scene | macOS | ✅ | Use `Form` inside — renders with tab bar |
| Window toolbar | `.toolbar` with `ToolbarItem(placement: .navigation)` | macOS | ✅ | |
| Menu bar commands | `Commands` + `CommandMenu` | macOS | ✅ | |
| Mac Catalyst adaptation | `.UIKitBehavior` / `preferredUserInterfaceStyle` | macOS | ⚠ | Catalyst quirks are many — test thoroughly |
| Context menu on hover | `.onHover` + `.contextMenu` | macOS | ✅ | |

---

## iPad Layout Patterns

| Pattern | Approach | Notes |
|---|---|---|
| Sidebar always visible (regular) | `NavigationSplitView` with `.sidebar` column | Default on iPad landscape |
| Compact fallback (iPhone / portrait) | Automatic stack collapse | Test both size classes |
| Drag and drop | `.onDrop` / `.draggable` | 16+ SwiftUI API; more capable in UIKit |
| Multi-column `Table` | `Table` with `TableColumn` | Collapses to single column on iPhone |
| Floating keyboard handling | `.ignoresSafeArea(.keyboard, edges: .bottom)` | Only ignore when layout demands it |

---

## Adaptive Design Checklist

When supporting both iPhone and iPad/Mac from one codebase:

- [ ] `NavigationSplitView` tested in both compact and regular size class
- [ ] `.popover` has a fallback design for iPhone (it becomes a sheet)
- [ ] `Table` has a single-column iPhone layout or is gated by size class
- [ ] Toolbar placements tested — `.primaryAction` behaves differently per platform
- [ ] `.inspector` confirmed it degrades gracefully to sheet on iPhone
- [ ] Font sizes and spacing feel right at both screen densities
