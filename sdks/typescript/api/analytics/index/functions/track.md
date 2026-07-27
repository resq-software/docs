# Function: track()

&gt; **track**\<`E`\>(`event`, ...`args`): `void`

Defined in: [index.ts:461](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L461)

Emit an event through the shared [analytics](../variables/analytics) singleton. Convenience
wrapper over [Analytics.track](../classes/Analytics#track).

## Type Parameters

### E

`E` *extends* `string`

The event name, narrowed to a registered key when one exists.

## Parameters

### event

`E`

The event name.

### args

...[`TrackArgs`](../type-aliases/TrackArgs)\<`E`\>

The event payload, shaped by [TrackArgs](../type-aliases/TrackArgs).

## Returns

`void`
