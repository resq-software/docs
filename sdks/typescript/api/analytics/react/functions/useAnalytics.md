# Function: useAnalytics()

> **useAnalytics**(): [`UseAnalyticsReturn`](../interfaces/UseAnalyticsReturn)

Defined in: [react/index.ts:160](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L160)

Component-level access to the analytics surface.

Does **not** subscribe to React state — calls to `track` are pure
side effects, so the hook is safe to call once per component
without causing re-renders.

## Returns

[`UseAnalyticsReturn`](../interfaces/UseAnalyticsReturn)

## Example

```tsx
const { track } = useAnalytics();
<button onClick={() => track("cta_clicked", { id: "hero" })}>Click</button>
```
