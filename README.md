# ResQ Docs

[![Mintlify](https://img.shields.io/badge/powered%20by-Mintlify-0073E6?style=flat-square)](https://mintlify.com)
[![Live](https://img.shields.io/badge/docs-docs.resq.software-0ea5e9?style=flat-square)](https://docs.resq.software)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square)](LICENSE)

> Official documentation for **ResQ Tactical OS** — the decentralized kinetic operating system for autonomous disaster response. Mesh-networked coordination when infrastructure fails. Built with Mintlify, MDX, and auto-generated API references from OpenAPI specs.

## Contents

| Section | Description |
| :--- | :--- |
| **Overview** | Landing page with platform summary and entry points |
| **API Reference — Infrastructure** | Incidents, evidence, blockchain events, Solana delivery/airspace endpoints |
| **API Reference — Coordination HCE** | Fleet management, mission dispatch, telemetry, WebSocket, and admin endpoints |

API references are auto-generated from OpenAPI specs in `specs/infrastructure.json` and `specs/coordination.json`.

## Local Development

**Prerequisites:** Node.js v19+

```bash
# Install the Mintlify CLI
npm i -g mint

# Clone the repo
git clone https://github.com/resq-software/docs.git
cd docs

# Start the local preview server
mint dev
```

Open [http://localhost:3000](http://localhost:3000). Changes to `.mdx` files hot-reload instantly.

## Writing Documentation

Pages are `.mdx` files with YAML frontmatter:

```mdx
---
title: 'Your Page Title'
description: 'One-line description shown in search and cards'
---

Content goes here. Full MDX syntax supported — import React components, use Mintlify's built-in `<Card>`, `<Tabs>`, `<CodeGroup>`, etc.
```

**Navigation** is controlled by `docs.json`. Add a new page by creating the `.mdx` file and adding its path to the appropriate group in `navigation.tabs`:

```json
{
  "group": "Start here",
  "pages": ["index", "your-new-page"]
}
```

**API reference** pages point to an OpenAPI spec:

```mdx
---
title: My Service API
openapi: ../specs/my-service.json
---
```

Drop new OpenAPI specs in `specs/` and reference them the same way.

## Validation

```bash
# Check for broken links before pushing
mint broken-links
```

## Deployment

Push to `main` — the Mintlify GitHub App triggers a build and deploys to the production CDN automatically. No manual steps required.

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| Preview won't start | Delete `~/.mintlify` cache and re-run `mint dev` |
| `sharp` module errors | Ensure Node v19+ and reinstall the CLI |
| Broken links in CI | Run `mint broken-links` locally first |

## Contributing

1. Fork and create a branch: `docs/your-topic`
2. Preview changes locally: `mint dev`
3. Check for broken links: `mint broken-links`
4. Open a PR — describe what changed and why

Write in active voice. Keep sentences short. If documenting an API, verify the endpoint behavior against the actual service before publishing.

## License

Copyright 2026 ResQ. Licensed under the [Apache License, Version 2.0](LICENSE).
