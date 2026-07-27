# Function: isPromise()

&gt; **isPromise**(`value`): `value is Promise<unknown>`

Defined in: [\_utils.ts:33](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/_utils.ts#L33)

Narrow `value` to a thenable (native `Promise` or a duck-typed then-able).

## Parameters

### value

`unknown`

The value to test.

## Returns

`value is Promise<unknown>`

`true` when `value` exposes a callable `then`.
