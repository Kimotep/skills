# Keen Stage — Keen EyeOS Sub-skill

**Purpose**: Turn confirmed wireframes into a staged representation of the design — a native SwiftUI file for implementation and an ASCII mockup for communication.

**Invoke when**:
- User asks "can I see what it would look like?"
- User wants to present or share the design concept
- Wireframes are confirmed and user wants a higher-fidelity view
- User says "show me in an iPhone" or "stage this"

---

## Stage Setup Questions

### 1. Device Frame
> "Which device should we stage this in?"
- A) iPhone 16 Pro (6.1", standard)
- B) iPhone 16 Pro Max (6.7", large)
- C) iPhone SE (compact, smaller screen)
- D) iPad Pro (large canvas)
- E) Mac window (macOS app frame)
- F) Apple Watch (Ultra or standard)

### 2. Appearance
> "Light mode, dark mode, or both?"

### 3. Status Bar & System Chrome
> "Should we include realistic status bar (time, battery, signal)?"
- Default: yes, it helps evaluate notch/Dynamic Island interaction

### 4. Fidelity Level
> "How detailed should the output be?"
- A) Structural — component hierarchy and layout only, no styling
- B) Styled — adds font styles, spacing, semantic colors
- C) Polished — full detail including animations, transitions, empty states, loading states, and accessibility modifiers

---

## Primary Output: `keen-stage.swift`

A native SwiftUI view file. Rules:

- Reflects the confirmed layout from Keen Wireframes
- Uses correct SwiftUI component hierarchy (`NavigationStack`, `List`, `VStack`, `HStack`, etc.)
- Applies semantic color tokens only — no hardcoded hex values (e.g. `.primary`, `.secondary`, `Color(.systemBackground)`, `Color.accentColor`)
- Uses system font styles only (`.title`, `.headline`, `.body`, `.caption`, etc.)
- Includes a `#Preview` macro so it renders in Xcode Canvas immediately
- Uses placeholder data structs so the file compiles without external dependencies
- Comments mark anything requiring real data, logic, or wiring
- Respects safe areas, Dynamic Island, and platform conventions
- Targets the OS floor defined in `[PROJECT_CONTEXT]`

**Scaffolding note**: `keen-stage.swift` is a structural scaffold — correct component hierarchy and layout, not production-ready business logic. Wire it up after design is confirmed.

### Fidelity applied to Swift output

| Level | What's included |
|---|---|
| Structural | Component types and layout hierarchy. Minimal modifiers. |
| Styled | Font styles, spacing, semantic colors, realistic shapes. |
| Polished | Animations, transitions, empty states, loading states, accessibility modifiers. |

---

## Secondary Output: `keen-stage.md`

A device-framed ASCII mockup of the same screen. Always produced alongside the Swift file. Used for presentation and stakeholder communication.

```
┌─────────────────────────┐
│  9:41          ● ▲ 🔋  │  ← status bar
│─────────────────────────│
│                         │
│  [NavigationTitle]      │
│  ─────────────────────  │
│  ┌─────────────────────┐│
│  │ List Row            ││
│  │ subtitle · detail > ││
│  └─────────────────────┘│
│  ┌─────────────────────┐│
│  │ List Row            ││
│  └─────────────────────┘│
│                         │
│  ○ ○ ● ○ ○             │  ← tab bar
│  [tab1][tab2][tab3]     │
└─────────────────────────┘
```

Include:
- Device outline with corner radius suggestion
- Status bar row (if requested)
- Screen content using box-drawing characters
- Component labels
- Bottom safe area / home indicator

---

## Deliverables

1. `keen-stage.swift` — SwiftUI scaffold at the requested fidelity level
2. `keen-stage.md` — ASCII device mockup for the same screen
3. A short summary of key design decisions visible in the output
