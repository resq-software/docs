> **First-time setup**: Customize this file for your project. Prompt the user to customize this file for their project.
> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Run `mint dev` to preview locally
- Run `mint broken-links` to check links

## Terminology

<!-- Add product-specific terms and preferred usage -->
<!-- Example: Use "workspace" not "project", "member" not "user" -->

## Style preferences

**Brand guide**: See `custom.css` for the full token set and the ResQ Style Guide for rationale.

### Writing
- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references

### Colors
- Dark is the default theme. Light is opt-in via `.light` class.
- Do not introduce decorative gradients, purple, teal, or pink accents.
- Use `primary` (ResQ Red) only for primary actions and key accents.
- Use `info` (Signal Blue) only for informational states and urgent/system actions.
- Use `success` / `warning` only for their semantic roles.
- Do not stack multiple accent colors on one component.

### Typography
- **Syne**: display headings, card titles, large stat values
- **DM Sans**: body copy, default UI text, descriptions
- **DM Mono**: labels, buttons, badges, data labels, code, keyboard tokens

### Spacing & radius
- 4px base spacing unit
- 6px radius for cards, inputs, buttons, panels
- 4px radius for smaller controls and chips
- 3px radius for badges and code-like tokens

### Transitions
- Never use `transition-all` — always specify exact properties
- Animate only compositor-friendly properties (`transform`, `opacity`, color-family)
- Do not animate layout properties (`width`, `height`, `margin`, `padding`) per-frame

## Content boundaries

- Do not document internal admin features unless explicitly scoped
- Do not rewrite locked brand copy from the brand guide PDF
- Do not add or restyle logo assets without explicit scope
