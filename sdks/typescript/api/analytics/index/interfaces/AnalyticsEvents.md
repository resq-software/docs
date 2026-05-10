# Interface: AnalyticsEvents

Defined in: [index.ts:34](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L34)

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
