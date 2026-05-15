# Function: AnalyticsProvider()

> **AnalyticsProvider**(`__namedParameters`): `ReactNode`

Defined in: [react/index.ts:102](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L102)

Boot the analytics singleton once on mount and render `children`.

Idempotent — repeat mounts (e.g. fast-refresh, tree-rebuild) are
detected via a ref guard and do not re-initialise PostHog / GA4.

## Parameters

### \_\_namedParameters

[`AnalyticsProviderProps`](../interfaces/AnalyticsProviderProps)

## Returns

`ReactNode`

## Examples

```tsx
<AnalyticsProvider config={config}>
  <App />
</AnalyticsProvider>
```

```tsx
<AnalyticsProvider config={config} deferUntilIdle={false}>
  <App />
</AnalyticsProvider>
```
