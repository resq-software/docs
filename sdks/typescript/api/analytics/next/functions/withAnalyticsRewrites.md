# Function: withAnalyticsRewrites()

> **withAnalyticsRewrites**\<`T`\>(`nextConfig`, `options?`): `T`

Defined in: [next/index.ts:90](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L90)

Wrap a Next.js config to add reverse-proxy rewrites for
`@resq-sw/analytics`.

Adds two rules to the `beforeFiles` rewrite array:

1. `/<prefix>/static/:path* → assetsUpstream/static/:path*`
   (PostHog snippet bundle).
2. `/<prefix>/:path*        → upstream/:path*`
   (everything else: capture, decide, `/e/`).

Pre-existing user-defined rewrites are preserved — the proxy
rules go *first* so they win when paths overlap. Also forces
`skipTrailingSlashRedirect: true`, which is required for the
proxy to work reliably across `/ingest` and `/ingest/`.

## Type Parameters

### T

`T` *extends* `MinimalNextConfig`

The user's full `next.config.{js,ts}` type.

## Parameters

### nextConfig

`T`

### options?

[`AnalyticsRewriteOptions`](../interfaces/AnalyticsRewriteOptions) = `{}`

## Returns

`T`

## Example

```ts
import { withAnalyticsRewrites } from "@resq-sw/analytics/next";

export default withAnalyticsRewrites({
  reactStrictMode: true,
  // ...rest of your config
});
```
