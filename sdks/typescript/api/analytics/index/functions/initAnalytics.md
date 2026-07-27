# Function: initAnalytics()

&gt; **initAnalytics**(`config`): `Promise`\<`void`\>

Defined in: [index.ts:451](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L451)

Initialise the shared [analytics](../variables/analytics) singleton. Convenience wrapper over
[Analytics.init](../classes/Analytics#init).

## Parameters

### config

[`AnalyticsConfig`](../interfaces/AnalyticsConfig)

PostHog/GA4 credentials plus cross-subdomain and debug flags.

## Returns

`Promise`\<`void`\>

A promise that resolves once provider bootstrapping has settled, and
  rejects on the same conditions as [Analytics.init](../classes/Analytics#init) (failed `posthog-js`
  import or `posthog.init` throw).
