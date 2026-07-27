# Type Alias: EventName

&gt; **EventName** = keyof [`AnalyticsEvents`](../interfaces/AnalyticsEvents) *extends* `never` ? `string` : keyof [`AnalyticsEvents`](../interfaces/AnalyticsEvents) \| `string` & `object`

Defined in: [index.ts:121](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L121)

The set of trackable event names. Falls back to plain `string` until a
consumer augments [AnalyticsEvents](../interfaces/AnalyticsEvents); once augmented, it becomes the
union of registered keys plus `(string & {})` so ad-hoc names still compile
while registered names autocomplete.
