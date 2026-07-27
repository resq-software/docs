# Function: record()

&gt; **record**(`val`): [`Value`](../type-aliases/Value)

Defined in: [packages/math/src/value.ts:107](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L107)

Wrap a JS record as a `record`-sorted value.

Stores `val` by reference — unlike [mkSet](./mkSet), it does not copy or freeze —
so the caller retains ownership and any later mutation of `val` is visible
through the returned value. Pass a fresh object if you need isolation.

## Parameters

### val

`Record`\<`string`, [`Value`](../type-aliases/Value)\>

## Returns

[`Value`](../type-aliases/Value)
