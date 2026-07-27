# Interface: PostHogProviderConfig

Defined in: [index.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L64)

PostHog provider credentials and init overrides. The `key` is the only
required field; `host`/`uiHost` target non-default (EU or self-hosted)
regions and `options` is merged over the package defaults set in
[Analytics.init](../classes/Analytics#init).

## Properties

### host?

&gt; `optional` **host?**: `string`

Defined in: [index.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L68)

Ingestion `api_host`; absence defaults to `https://us.i.posthog.com`. Set for EU or self-hosted regions.

***

### key

&gt; **key**: `string`

Defined in: [index.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L66)

PostHog project API key (`phc_…`). The only required field.

***

### options?

&gt; `optional` **options?**: `Partial`\<`PostHogConfig`\>

Defined in: [index.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L72)

Raw `posthog-js` init options merged *over* the package defaults, so a key set here wins.

***

### uiHost?

&gt; `optional` **uiHost?**: `string`

Defined in: [index.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L70)

PostHog app host for toolbar/session links; absence leaves PostHog's own default.
