# Function: getIndicesBelow()

&gt; **getIndicesBelow**(`above`, `n`): [`IndexKey`](../type-aliases/IndexKey)[]

Defined in: [reordering.ts:124](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L124)

Generate `n` keys that all sort before `above`, evenly spaced.

Jittered (non-deterministic strings) outside `NODE_ENV=test`; see
[getIndicesBetween](./getIndicesBetween).

## Parameters

### above

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Upper bound, or `null`/`undefined` to prepend from the end.

### n

`number`

How many keys to mint. `0` returns an empty array.

## Returns

[`IndexKey`](../type-aliases/IndexKey)[]

`n` keys in ascending order, each less than `above`.

## Throws

When `above` is a non-canonical order key.
