# Function: ga4Stream()

> **ga4Stream**(`measurementId`, `domains?`): [`GA4ProviderConfig`](../../index/interfaces/GA4ProviderConfig)

Defined in: [next/index.ts:139](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/next/index.ts#L139)

Build a [GA4ProviderConfig](../../index/interfaces/GA4ProviderConfig) with cross-subdomain linker
domains. Drop into `AnalyticsConfig.ga4`:

```ts
const config: AnalyticsConfig = {
  posthog: { ... },
  ga4: ga4Stream("G-XXXXXXX", ["resq.software", "research.resq.software", "viz.resq.software"]),
};
```

## Parameters

### measurementId

`string`

GA4 Measurement ID (`G-…`).

### domains?

`string`[]

Domain allow-list passed to gtag's `linker.domains`,
  so cross-subdomain navigation no longer counts as referral
  traffic.

## Returns

[`GA4ProviderConfig`](../../index/interfaces/GA4ProviderConfig)
