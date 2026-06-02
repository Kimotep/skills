# Keen Signal — Keen EyeOS Sub-skill

**Purpose**: Navigate design decisions that are directly constrained or enabled by technical
and data realities. Bridges what you *want* to show with what you *can* show.

**Invoke when**:
- User mentions data availability affecting design ("I only have X from the API")
- Design choices depend on OS version capabilities
- Performance or architecture constraints limit UI options
- User asks "can I even do X on iOS?"
- User is choosing between two approaches with different technical tradeoffs
- Keen Feature or Keen Polish surfaces a constraint that needs deeper investigation

---

## Signal Questions

### 1. The Intended Experience
> "What do you want the user to experience — ignoring technical constraints for a moment?"

### 2. The Data Reality
> "What data is actually available, and in what form?"
- Prompt: "Is it local or fetched? How fast does it arrive? Is it always present, or sometimes missing?"
- Ask about: pagination, caching, offline behavior, real-time vs batch

### 3. The API/Framework Boundary
> "What platform or framework version are you targeting?"
- Some components (e.g., `contentUnavailableView`, `Inspector`, `.searchPresentationToolbarBehavior`)
  have specific OS floor requirements
- Ask: "What's your minimum deployment target? iOS 16? 17? macOS 13?"

### 4. The Constraint Map
After collecting answers, produce a **Signal Map**:

```
Desired experience: [what user wants]
Available data: [what exists]
Gap: [what's missing or delayed]
Constraint: [API/OS/performance limit]
Design response: [how to adapt the design to fit reality]
Fallback state: [what the UI shows when data is absent or late]
```

---

## Common Signal Patterns

| Constraint | Design Response |
|---|---|
| Data loads slowly | Skeleton views, progressive disclosure, optimistic UI |
| Data sometimes missing | Meaningful empty states, not blank screens |
| iOS 16 min target | Avoid `.navigationDestination`, use NavigationStack carefully |
| iOS 17+ available | Use `Observable` macro, `ScrollPosition`, `TipKit` |
| Variable content length | Avoid fixed heights; use `.fixedSize` judiciously |
| Large data sets | Use `List` (lazy) not `ScrollView + ForEach` for performance |
| Offline-first | Cache-aware component states; visual indicators for stale data |

---

## Output

- **Signal Map** (inline, confirms understanding)
- Design recommendation adjusted for constraints
- Flagged alternatives if the preferred approach isn't feasible
- Notes for **Keen Technical Handover** if this is part of a larger feature spec
