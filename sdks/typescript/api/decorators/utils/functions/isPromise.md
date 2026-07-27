# Function: isPromise()

&gt; **isPromise**(`value`): `value is Promise<unknown>`

Defined in: [\_utils.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L33)

Narrow `value` to a thenable (native `Promise` or a duck-typed then-able).

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is Promise<unknown>`

`true` when `value` exposes a callable `then`.
