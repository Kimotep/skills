# Keen Stage — Keen EyeOS Sub-skill

**Purpose**: Produce a visual, device-framed representation of the design. Turns wireframes
into a staged mockup that communicates the design in context.

**Invoke when**:
- User asks "can I see what it would look like?"
- User wants to present or share the design concept
- Wireframes are confirmed and user wants a higher-fidelity view
- User says "show me in an iPhone" or "stage this"

---

## Stage Setup Questions

### 1. Device Frame
> "Which device should we stage this in?"
- A) iPhone 15 Pro (6.1", standard)
- B) iPhone 15 Pro Max (6.7", large)
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
> "How detailed should the mockup be?"
- A) Structural (boxes and labels — fast, good for layout decisions)
- B) Styled (typography, color, realistic component shapes)
- C) Polished (as close to final as possible without Figma)

---

## Rendering Approach

Based on the harness:

### ASCII (always available)
Use for structural fidelity. Include:
- Device outline with corner radius suggestion
- Status bar row (if requested)
- Screen content using box-drawing characters
- Component labels
- Bottom safe area / home indicator

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

### HTML/SVG (if artifact harness supports it)
Render a styled device frame with proper proportions. Use CSS custom properties for color tokens.
- iPhone frame: 390×844pt viewport at 2x scale representation
- Use SF Pro–equivalent system font stack: `-apple-system, BlinkMacSystemFont`
- Colors: use Apple's semantic palette (system backgrounds, labels, tints)

---

## Output

- `keen-stage.md` containing the device mockup with annotations
- If HTML artifact is produced: include a note that this is a layout reference, not production code
- Always pair the stage with a summary of key design decisions visible in the mockup
