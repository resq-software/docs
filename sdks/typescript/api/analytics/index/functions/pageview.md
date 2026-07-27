# Function: pageview()

&gt; **pageview**(`url?`): `void`

Defined in: [index.ts:487](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L487)

Emit a manual pageview through the shared [analytics](../variables/analytics) singleton.
Convenience wrapper over [Analytics.pageview](../classes/Analytics#pageview).

## Parameters

### url?

`string`

Explicit page URL; defaults to the current location.

## Returns

`void`
