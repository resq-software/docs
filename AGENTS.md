# Documentation project instructions

## About this project

- Public docs for **ResQ Tactical OS** — the decentralized kinetic operating system for autonomous disaster response.
- Built on [Mintlify](https://mintlify.com). Pages are MDX with YAML frontmatter; configuration lives in `docs.json`.
- Deployed at [docs.resq.software](https://docs.resq.software).
- Run `mint dev` to preview locally. Run `mint broken-links` before opening a PR.

## Site shape

The site is intentionally narrow:

- `index.mdx` — branded landing: hero, platform APIs, SDK registry cards, ecosystem links.
- `api-reference/introduction.mdx` — overview of the two API services.
- `api-reference/` (OpenAPI groups) — auto-generated per-operation pages from `specs/infrastructure.json` and `specs/coordination.json`.

Maintainer / contributor onboarding lives in `README.md` and `CONTRIBUTING.md` — **not** as public docs pages. Do not add Mintlify reference pages, AI-tooling guides, or "how to author docs" content here.

## Terminology

- Use **"ResQ Tactical OS"** in marketing-leaning copy, **"ResQ"** in API/technical copy.
- The product description is the brand-locked tagline: *"the decentralized kinetic operating system for autonomous disaster response. Mesh-networked coordination when infrastructure fails."*
- **Infrastructure API** (Rust + Axum) — incidents, evidence, blockchain anchoring, AI analysis, Solana operations.
- **Coordination API** (TypeScript + Elysia) — fleet telemetry, mission dispatch, IPFS storage, fault injection, HITL approval.
- HITL = Human-in-the-Loop (EU AI Act Art. 14).

## Style preferences

**Brand source of truth:** `custom.css` (oklch tokens + utilities) and the ResQ Style Guide for rationale.

### Writing
- Active voice, second person ("you").
- One idea per sentence.
- Sentence case for headings.
- Bold for UI elements: Click **Settings**.
- Code formatting for file names, commands, paths.

### Colors
- Dark is the default theme. Light is opt-in via `.light` class.
- No decorative gradients, purple, teal, or pink accents.
- `primary` (ResQ Red) for primary actions and key accents only.
- `info` (Signal Blue) for informational and urgent/system actions only.
- `success` / `warning` for their semantic roles only.
- Do not stack multiple accent colors on one component.

### Typography
- **Syne** — display headings, card titles, large stat values.
- **DM Sans** — body copy, default UI text, descriptions.
- **DM Mono** — labels, buttons, badges, data labels, code, keyboard tokens.

### Spacing & radius
- 4px base spacing unit.
- 6px radius for cards, inputs, buttons, panels.
- 4px radius for smaller controls and chips.
- 3px radius for badges and code-like tokens.

### Transitions
- Never `transition-all`. Always specify exact properties.
- Animate only compositor-friendly properties (`transform`, `opacity`, color-family).
- Do not animate layout properties per-frame.

### Brand utility classes (in `custom.css`)
- `.resq-hero` — operational hero frame; uses `og-backdrop.png` with a flat scrim and a radar grid overlay. Used on `index.mdx` only.
- `.resq-eyebrow` — DM Mono uppercase label with a Signal Blue indicator.
- `.resq-pill` + `--ok` / `--info` / `--warn` / `--primary` — status chips matching the brand banner vocabulary.

## Canonical asset paths

Use these exact paths when adding visuals — do not introduce parallel inventory.

| Purpose | Path |
| :--- | :--- |
| Navbar logo (light theme) | `/assets/logos/lockup-horizontal-light.svg` |
| Navbar logo (dark theme) | `/assets/logos/lockup-horizontal-dark.svg` |
| Favicon | `/assets/icons/resq-mark-color.svg` |
| Mark variants (mono / gradient) | `/assets/icons/`, `/assets/logos/` |
| Hero backdrop | `/og-backdrop.png` (vector source: `/assets/logos/og-backdrop.svg`) |
| OG sharing image | `/og-banner.png` (vector source: `/assets/logos/og-banner.svg`) |
| Apple touch icon | `/pwa/ios/180.png` |
| Web manifest | `/manifest.webmanifest` |

## Content boundaries

- Do not document internal admin features unless explicitly scoped.
- Do not rewrite locked brand copy from the brand guide PDF.
- Do not add Mintlify reference content (markdown syntax, components how-tos, navigation config) — those belong in Mintlify's own docs.
- Do not add maintainer-oriented content (CLI setup, deploy flow, AI tooling) as public pages — that lives in `README.md` and `CONTRIBUTING.md`.

## Git hooks

Canonical hooks from [`resq-software/dev`](https://github.com/resq-software/dev). Install:

```bash
curl -fsSL https://raw.githubusercontent.com/resq-software/dev/main/scripts/install-hooks.sh | bash
```

To pin to a specific revision instead of rolling `main`:

```bash
RESQ_DEV_REF=<commit-sha-or-tag> curl -fsSL \
  https://raw.githubusercontent.com/resq-software/dev/<commit-sha-or-tag>/scripts/install-hooks.sh | bash
```

See [Git hooks contract in `resq-software/dev`](https://github.com/resq-software/dev/blob/main/AGENTS.md#git-hooks). Repo-specific logic goes in `.git-hooks/local-<hook-name>` (none needed for this repo).
