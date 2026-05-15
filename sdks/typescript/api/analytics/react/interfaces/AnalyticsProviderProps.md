# Interface: AnalyticsProviderProps

Defined in: [react/index.ts:45](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L45)

Props for [AnalyticsProvider](../functions/AnalyticsProvider).

## Properties

### children?

> `optional` **children?**: `ReactNode`

Defined in: [react/index.ts:60](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L60)

Wrapped tree.

***

### config

> **config**: [`AnalyticsConfig`](../../index/interfaces/AnalyticsConfig)

Defined in: [react/index.ts:52](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L52)

Provider configuration — PostHog/GA4 credentials,
cross-subdomain cookie domain, debug flag, etc. Read once on
mount; later prop changes do **not** re-initialise the
singleton (use [reset](../../index/functions/reset) + a remount if you need that).

***

### deferUntilIdle?

> `optional` **deferUntilIdle?**: `boolean`

Defined in: [react/index.ts:58](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L58)

Wait for `requestIdleCallback` before booting analytics so it
never sits on the LCP critical path. Defaults to `true`. Set
to `false` only when you need first-paint events captured.
