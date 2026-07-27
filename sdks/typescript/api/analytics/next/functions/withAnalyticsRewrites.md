# Function: withAnalyticsRewrites()

&gt; **withAnalyticsRewrites**\<`T`\>(`nextConfig`, `options?`): `T` & `Required`\<`Pick`\<`MinimalNextConfig`, `"rewrites"` \| `"skipTrailingSlashRedirect"`\>\>

Defined in: [next/index.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L102)

Wrap a Next.js config to add reverse-proxy rewrites for
`@resq-systems/analytics`.

Adds two rules to the `beforeFiles` rewrite array:

1. `/<prefix>/static/:path* → assetsUpstream/static/:path*`
   (PostHog snippet bundle).
2. `/<prefix>/:path*        → upstream/:path*`
   (everything else: capture, decide, `/e/`).

Pre-existing user-defined rewrites are preserved — the proxy
rules go *first* so they win when paths overlap. Also forces
`skipTrailingSlashRedirect: true`, which is required for the
proxy to work reliably across `/ingest` and `/ingest/`.

Pure: returns a new config object and never mutates `nextConfig`. The
wrapped `rewrites` awaits the original `rewrites()` on each invocation, so if
the user's function throws or rejects, the composed one rejects the same way.

## Type Parameters

### T

`T` *extends* `MinimalNextConfig`

The user's full `next.config.{js,ts}` type; the return type
  preserves it while marking `rewrites` and `skipTrailingSlashRedirect` present.

## Parameters

### nextConfig

`T`

The existing Next.js config to wrap; its own `rewrites`
  are preserved and run after the proxy rules.

### options?

[`AnalyticsRewriteOptions`](../interfaces/AnalyticsRewriteOptions) = `{}`

Proxy overrides (path `prefix`, PostHog `upstream` /
  `assetsUpstream`); defaults target PostHog US ingestion.

## Returns

`T` & `Required`\<`Pick`\<`MinimalNextConfig`, `"rewrites"` \| `"skipTrailingSlashRedirect"`\>\>

The config with proxy rewrites and `skipTrailingSlashRedirect` set.

## Example

**\`next.config.ts\`**

```ts
import { withAnalyticsRewrites } from "@resq-systems/analytics/next";

export default withAnalyticsRewrites({
  reactStrictMode: true,
  // ...rest of your config
});
```
