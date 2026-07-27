# Function: useAnalytics()

&gt; **useAnalytics**(): [`UseAnalyticsReturn`](../interfaces/UseAnalyticsReturn)

Defined in: [react/index.ts:171](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L171)

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
