# Interface: AnalyticsConfig

Defined in: [index.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L93)

Top-level analytics configuration passed to [Analytics.init](../classes/Analytics#init). Both
providers are optional so a consumer can run PostHog only, GA4 only, or
neither (e.g. `disabled` in preview environments).

## Properties

### cookieDomain?

&gt; `optional` **cookieDomain?**: `any`

Defined in: [index.ts:104](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L104)

Cross-subdomain cookie domain in normalized leading-dot form. Typed as the
nominal [CookieDomain](../../resq/type-aliases/CookieDomain) so a bare host string is a compile error here:
mint one with [toCookieDomain](../../resq/functions/toCookieDomain) / [inferCookieDomain](../functions/inferCookieDomain) or take it
from [resolveResqCookieDomain](../../resq/functions/resolveResqCookieDomain).

***

### debug?

&gt; `optional` **debug?**: `boolean`

Defined in: [index.ts:112](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L112)

When `true`, `track`/`identify` log to `console.debug` before dispatch — even while `disabled`.

***

### disabled?

&gt; `optional` **disabled?**: `boolean`

Defined in: [index.ts:110](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L110)

Kill switch: when `true`, [Analytics.init](../classes/Analytics#init) boots no providers and
every dispatch method becomes a no-op (debug logging still fires). Use for
preview/CI environments.

***

### ga4?

&gt; `optional` **ga4?**: [`GA4ProviderConfig`](./GA4ProviderConfig)

Defined in: [index.ts:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L97)

GA4 provider; omit to run without GA4. Build one with `ga4Stream`.

***

### posthog?

&gt; `optional` **posthog?**: [`PostHogProviderConfig`](./PostHogProviderConfig)

Defined in: [index.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L95)

PostHog provider; omit to run without PostHog.
