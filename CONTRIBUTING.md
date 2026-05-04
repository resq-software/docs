# Contribute to ResQ docs

Thanks for helping improve [docs.resq.software](https://docs.resq.software). This guide gets you set up.

## How to contribute

### Option 1 — Edit directly on GitHub

1. Navigate to the page you want to edit.
2. Click the pencil icon ("Edit this file").
3. Make your changes and open a pull request.

### Option 2 — Local development

1. Fork and clone the repository.
2. Install the Mintlify CLI: `npm i -g mint`.
3. Create a branch from `main` using the `docs/<topic>` convention.
4. Make changes; run `mint dev` to preview at `http://localhost:3000`.
5. Run `mint broken-links` before pushing.
6. Commit and open a pull request against `main`.

See [README.md](README.md#local-development) for the full local workflow.

## Writing guidelines

- **Active voice.** "Run the command" — not "The command should be run".
- **Second person.** Address the reader as "you", not "the user".
- **One idea per sentence.** Keep them short.
- **Lead with the goal.** Start instructions with what the reader wants to accomplish.
- **Consistent terminology.** Don't alternate between synonyms for the same concept.
- **Show, don't just tell.** Include examples.

## Brand and style

Brand tokens, typography, and component conventions are codified in [`custom.css`](custom.css) and [`AGENTS.md`](AGENTS.md). Use the existing tokens — don't introduce new accent colors, decorative gradients, or non-brand fonts.

## Scope

This is the public-facing docs site. Keep content focused on the platform:

- **Yes:** API integration, concepts, architecture, authentication, examples for ResQ Tactical OS.
- **No:** Mintlify component reference, tutorials about MDX, AI-tooling setup for the docs repo. That belongs in this file or `README.md`, not as a published page.
