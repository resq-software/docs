# Interface: AnalyticsEvents

Defined in: [index.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L56)

Augmentable typed event registry. Consumers extend this via module
augmentation to get type-safe `track()` calls:

```ts
declare module "@resq-systems/analytics" {
  interface AnalyticsEvents {
    "briefing_requested": { tier: "civilian" | "defense" };
    "cta_clicked": { id: string; section: string };
  }
}
```

The base is intentionally empty (no string index signature): a signature
would collapse [EventName](../type-aliases/EventName) to plain `string` and destroy autocomplete.
Keys only exist once a consumer augments this interface.
