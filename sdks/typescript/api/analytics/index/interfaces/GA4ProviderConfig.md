# Interface: GA4ProviderConfig

Defined in: [index.ts:81](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L81)

GA4 provider config. `measurementId` is the branded [Ga4MeasurementId](../../resq/type-aliases/Ga4MeasurementId)
so only a sanitized ID reaches gtag; `domains` seeds the cross-subdomain
linker allow-list. Build one ergonomically with `ga4Stream` from
`@resq-systems/analytics/next`.

## Properties

### domains?

&gt; `optional` **domains?**: `LiteralUnion`\<`"resq.software"` \| `"research.resq.software"` \| `"viz.resq.software"`\>[]

Defined in: [index.ts:85](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L85)

Cross-subdomain linker allow-list for gtag's `linker.domains`; absence or `[]` skips linker setup entirely.

***

### measurementId

&gt; **measurementId**: `Brand`

Defined in: [index.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L83)

Branded, sanitized GA4 Measurement ID; mint via [sanitizeGa4Id](../../resq/functions/sanitizeGa4Id).
