# Interface: AnalyticsRewriteOptions

Defined in: [next/index.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L41)

Options for [withAnalyticsRewrites](../functions/withAnalyticsRewrites).

Defaults are tuned for PostHog's US ingestion endpoints; override
`upstream` / `assetsUpstream` for EU regions or self-hosted
deployments.

## Properties

### assetsUpstream?

&gt; `optional` **assetsUpstream?**: `string`

Defined in: [next/index.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L47)

PostHog static-assets endpoint. Default `"https://us-assets.i.posthog.com"`.

***

### prefix?

&gt; `optional` **prefix?**: `string`

Defined in: [next/index.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L43)

Local path prefix that proxies to PostHog. Default `"/ingest"`.

***

### upstream?

&gt; `optional` **upstream?**: `string`

Defined in: [next/index.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L45)

PostHog ingestion endpoint. Default `"https://us.i.posthog.com"`.
