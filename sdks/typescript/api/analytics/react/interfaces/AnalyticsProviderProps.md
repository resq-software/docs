# Interface: AnalyticsProviderProps

Defined in: [react/index.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L47)

Props for [AnalyticsProvider](../functions/AnalyticsProvider).

## Properties

### children?

&gt; `optional` **children?**: `ReactNode`

Defined in: [react/index.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L62)

Wrapped tree.

***

### config

&gt; **config**: [`AnalyticsConfig`](../../index/interfaces/AnalyticsConfig)

Defined in: [react/index.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L54)

Provider configuration — PostHog/GA4 credentials,
cross-subdomain cookie domain, debug flag, etc. Read once on
mount; later prop changes do **not** re-initialise the
singleton (use [reset](../../index/functions/reset) + a remount if you need that).

***

### deferUntilIdle?

&gt; `optional` **deferUntilIdle?**: `boolean`

Defined in: [react/index.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L60)

Wait for `requestIdleCallback` before booting analytics so it
never sits on the LCP critical path. Defaults to `true`. Set
to `false` only when you need first-paint events captured.
