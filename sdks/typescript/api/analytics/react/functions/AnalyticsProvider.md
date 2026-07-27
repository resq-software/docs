# Function: AnalyticsProvider()

&gt; **AnalyticsProvider**(`__namedParameters`): `ReactNode`

Defined in: [react/index.ts:109](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L109)

Boot the analytics singleton once on mount and render `children`.

Idempotent — repeat mounts (e.g. fast-refresh, tree-rebuild) are
detected via a ref guard and do not re-initialise PostHog / GA4.

The boot is fire-and-forget: the init promise is not awaited, so a rejected
init (see [Analytics.init](../../index/classes/Analytics#init)) surfaces as an unhandled rejection rather
than an error thrown from render. Toggling `deferUntilIdle` after mount has no
effect — init runs at most once.

## Parameters

### \_\_namedParameters

[`AnalyticsProviderProps`](../interfaces/AnalyticsProviderProps)

## Returns

`ReactNode`

## Examples

**Default (idle-deferred boot)**

```tsx
<AnalyticsProvider config={config}>
  <App />
</AnalyticsProvider>
```

**Eager boot for first-paint events**

```tsx
<AnalyticsProvider config={config} deferUntilIdle={false}>
  <App />
</AnalyticsProvider>
```
