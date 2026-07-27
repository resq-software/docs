# Type Alias: TrackArgs\<E\>

&gt; **TrackArgs**\<`E`\> = `E` *extends* keyof [`AnalyticsEvents`](../interfaces/AnalyticsEvents) ? `undefined` *extends* [`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\] ? \[[`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\]\] : `object` *extends* [`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\] ? \[[`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\]\] : \[[`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\]\] : \[`Record`\<`string`, `unknown`\>\]

Defined in: [index.ts:132](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L132)

Arguments accepted by [Analytics.track](../classes/Analytics#track) after the event name, as a
rest tuple. For a registered event the payload arg is **required** exactly
when its type has at least one required key (`{}` is not assignable to it),
and optional otherwise. Unregistered names accept an optional free-form
property bag.

## Type Parameters

### E

`E` *extends* [`EventName`](./EventName)
