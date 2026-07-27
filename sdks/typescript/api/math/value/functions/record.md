# Function: record()

&gt; **record**(`val`): [`Value`](../type-aliases/Value)

Defined in: [packages/math/src/value.ts:107](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L107)

Wrap a JS record as a `record`-sorted value.

Stores `val` by reference — unlike [mkSet](./mkSet), it does not copy or freeze —
so the caller retains ownership and any later mutation of `val` is visible
through the returned value. Pass a fresh object if you need isolation.

## Parameters

### val

`Record`\<`string`, [`Value`](../type-aliases/Value)\>

## Returns

[`Value`](../type-aliases/Value)
