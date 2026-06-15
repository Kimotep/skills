# Scaffold patterns — starter structures by project type

Reference for [`OUTPUT.md`](../OUTPUT.md), used when generating `[slug]-SCAFFOLD.md`. Each
pattern below is a starting skeleton for the **product layer** — the actual repo, alongside
the planning docs and `agents/`/`rules/` folders that are always generated.

Pick the pattern that matches the project type named in interview theme 6. Adapt names and
add/remove items based on what was actually said — these are starting points, not checklists
to fill blindly. If the stack wasn't decided, use the pattern's shape but leave file
extensions and config files generic (e.g. `src/` instead of `src/index.ts`), and note in
"Notes on structure" that the stack is still open.

If the project type doesn't match any pattern, or the user said "not sure yet", use the
**Undecided** pattern at the end.

Each pattern includes a **Tooling defaults** line — a sensible baseline for package manager,
test framework, linter/formatter, and env handling. Treat these as a fallback. Per the
Architect pass in [`OUTPUT.md`](../OUTPUT.md), if a specific framework was named, current
docs/conventions for that framework take precedence over these defaults.

---

## Web app

```
src/
├── pages/ or routes/      # Top-level views/routes
├── components/            # Reusable UI pieces
├── lib/                    # Shared logic — API clients, helpers
└── styles/                 # Global styles, if not co-located
public/                     # Static assets served as-is
tests/                       # Test suite, mirroring src/ structure
[config files]              # e.g. package.json, framework config, .env.example
```

Why: separates what's rendered (`pages`/`components`) from what's shared (`lib`) so agents
working on one view don't need to load the whole app. `public/` and config are flagged
reference-only in token hygiene — rarely need to be in context.

**Tooling defaults:** npm or pnpm; Vitest or Jest for unit tests; ESLint + Prettier;
`.env` + `.env.example` for config. If a meta-framework was named (Next.js, Remix, Nuxt,
SvelteKit, etc.), defer to that framework's current docs for structure and test setup.

---

## CLI tool

```
src/ or [package-name]/
├── cli.[ext]               # Entry point — argument parsing, dispatch
├── commands/               # One file per subcommand
└── lib/                    # Shared logic used across commands
tests/                       # Test suite, mirroring commands/
[config files]              # e.g. package.json/pyproject.toml, entry-point registration
```

Why: `commands/` keeps each subcommand independently editable — an agent working on one
command doesn't need the others in context. `cli.[ext]` stays thin; logic lives in `lib/`
so it's testable without invoking the CLI.

**Tooling defaults:** language's standard package manager (npm, pip/uv, cargo, go modules);
language's standard test framework (pytest, Vitest/Jest, cargo test, go test); standard
linter/formatter for that language (ruff/black, ESLint/Prettier, rustfmt, gofmt). Config via
flags or a config file — CLIs rarely need `.env`.

---

## Browser extension

```
src/
├── manifest.json           # Extension manifest — permissions, entry points
├── background/             # Background/service worker scripts
├── content/                # Content scripts injected into pages
├── popup/                   # Popup UI (if any)
└── lib/                    # Shared logic across the above
icons/                       # Extension icons at required sizes
```

Why: background, content, and popup scripts run in different contexts with different
permissions — keeping them in separate folders makes those boundaries visible. `manifest.json`
is the single source of truth for what the extension can do; flag it for review whenever
permissions change.

**Tooling defaults:** npm or pnpm; a build step (Vite or similar) targeting Manifest V3;
Vitest or Jest for unit tests, Playwright for end-to-end if needed; ESLint + Prettier. No
secrets in extension code — anything sensitive stays server-side.

---

## Agent pipeline / automation

```
agents/                      # Per-agent code/prompts — mirrors [slug]-AGENTS.md roles
├── [agent-name]/
│   ├── prompt.md or .[ext] # Agent definition or implementation
│   └── ...
pipeline/ or orchestrator/   # Coordination logic — sequencing, handoffs
config/                       # Runtime config — schedules, credentials references (not values)
tests/                        # Test suite, especially for handoffs and error states
```

Why: `agents/` mirrors the roles already defined in `[slug]-AGENTS.md` one-to-one, so the
mapping from planning doc to code is obvious. `pipeline/` is separate because coordination
logic changes independently of any single agent's internals. Never commit actual credentials
to `config/` — only references to where they're stored.

**Tooling defaults:** language's standard package manager (pip/uv or npm, depending on
stack); pytest or Vitest for tests, with particular attention to handoff and error-state
tests; ruff/black or ESLint/Prettier; config/secrets referenced via env vars, never
hardcoded.

---

## API / backend service

```
src/
├── routes/ or handlers/    # Endpoint definitions
├── services/                # Business logic, called by routes
├── models/                  # Data models / schema
└── lib/                     # Shared utilities
tests/                        # Test suite, mirroring routes/ and services/
[config files]               # e.g. package.json, env config, migration tooling
```

Why: `routes/` stays thin and delegates to `services/` — keeps endpoint files short enough
that an agent can load just the route plus the one service it calls, not the whole backend.

**Tooling defaults:** npm/pnpm or pip/uv, depending on stack; Vitest/Jest or pytest;
ESLint + Prettier or ruff/black; `.env` + `.env.example`, plus a migration tool (e.g. Prisma,
Alembic) if there's a database. If a specific framework was named (FastAPI, Express, NestJS,
etc.), defer to that framework's current docs for routing/testing conventions.

---

## Library / package (incl. a Claude skill)

```
[package-name]/
├── SKILL.md or src/index.[ext]   # Entry point / main definition
├── references/                    # Supporting docs loaded on demand, not by default
├── examples/                       # Usage examples
└── tests/                          # Test suite
```

Why: mirrors the pattern this very repo uses — a thin entry point plus a `references/`
folder for material that's useful but shouldn't be loaded into every context. Good default
for anything meant to be reused across projects rather than run as its own product.

**Tooling defaults:** language's standard package manager, if the package is distributed
(npm for an npm package, pip/uv for a Python package); pytest/Vitest/Jest for tests matching
the language; standard linter/formatter for that language. For a Claude skill specifically,
no package manager is needed — just the file structure above.

---

## Undecided

If project type or stack wasn't resolved in interview, don't invent one. Use:

```
[slug]/
├── [slug]-MISSION.md
├── [slug]-AGENTS.md
├── [slug]-SCAFFOLD.md
├── [slug]-LOGIC.md
├── [slug]-HANDOVER.md
├── agents/
└── rules/
```

And note in "Notes on structure":

> "Project type and stack weren't decided in this session — the product-layer structure
> (`src/`, etc.) isn't included. [slug]-HANDOVER.md should treat 'pick a stack' as the first
> open decision, not an implementation detail to skip."

**Tooling defaults:** none — write "Deferred — see [slug]-HANDOVER.md" in the Tooling section
of SCAFFOLD.md.
