# Function: getIndicesBelow()

&gt; **getIndicesBelow**(`above`, `n`): [`IndexKey`](../type-aliases/IndexKey)[]

Defined in: [reordering.ts:124](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L124)

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
