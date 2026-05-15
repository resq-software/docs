# Interface: AnalyticsRewriteOptions

Defined in: [next/index.ts:39](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L39)

Options for [withAnalyticsRewrites](../functions/withAnalyticsRewrites).

Defaults are tuned for PostHog's US ingestion endpoints; override
`upstream` / `assetsUpstream` for EU regions or self-hosted
deployments.

## Properties

### assetsUpstream?

> `optional` **assetsUpstream?**: `string`

Defined in: [next/index.ts:45](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L45)

PostHog static-assets endpoint. Default `"https://us-assets.i.posthog.com"`.

***

### prefix?

> `optional` **prefix?**: `string`

Defined in: [next/index.ts:41](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L41)

Local path prefix that proxies to PostHog. Default `"/ingest"`.

***

### upstream?

> `optional` **upstream?**: `string`

Defined in: [next/index.ts:43](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L43)

PostHog ingestion endpoint. Default `"https://us.i.posthog.com"`.
