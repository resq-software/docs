# Interface: AnalyticsEvents

Defined in: [index.ts:34](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/index.ts#L34)

Augmentable typed event registry. Consumers extend this via module
augmentation to get type-safe `track()` calls:

```ts
declare module "@resq-sw/analytics" {
  interface AnalyticsEvents {
    "briefing_requested": { tier: "civilian" | "defense" };
    "cta_clicked": { id: string; section: string };
  }
}
```

## Indexable

> \[`event`: `string`\]: `Record`\<`string`, `unknown`\> \| `undefined`
