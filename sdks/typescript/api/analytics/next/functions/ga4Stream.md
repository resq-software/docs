# Function: ga4Stream()

&gt; **ga4Stream**(`measurementId`, `domains?`): [`GA4ProviderConfig`](../../index/interfaces/GA4ProviderConfig)

Defined in: [next/index.ts:152](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/next/index.ts#L152)

Build a [GA4ProviderConfig](../../index/interfaces/GA4ProviderConfig) with cross-subdomain linker domains. Drop
the result into `AnalyticsConfig.ga4`.

## Parameters

### measurementId

`Brand`

GA4 Measurement ID (`G-…`).

### domains?

`LiteralUnion`\<`"resq.software"` \| `"research.resq.software"` \| `"viz.resq.software"`\>[]

Domain allow-list passed to gtag's `linker.domains`,
  so cross-subdomain navigation no longer counts as referral
  traffic.

## Returns

[`GA4ProviderConfig`](../../index/interfaces/GA4ProviderConfig)

A GA4 provider config carrying the ID and linker domains.

## Example

```ts
const config: AnalyticsConfig = {
  posthog: { key: "phc_…" },
  ga4: ga4Stream(sanitizeGa4Id("G-XXXXXXX")!, ["resq.software", "research.resq.software"]),
};
```
