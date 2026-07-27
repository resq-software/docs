# Function: getIndicesAbove()

&gt; **getIndicesAbove**(`below`, `n`): [`IndexKey`](../type-aliases/IndexKey)[]

Defined in: [reordering.ts:109](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L109)

Generate `n` keys that all sort after `below`, evenly spaced.

Jittered (non-deterministic strings) outside `NODE_ENV=test`; see
[getIndicesBetween](./getIndicesBetween).

## Parameters

### below

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Lower bound, or `null`/`undefined` to append from the start.

### n

`number`

How many keys to mint. `0` returns an empty array.

## Returns

[`IndexKey`](../type-aliases/IndexKey)[]

`n` keys in ascending order, each greater than `below`.

## Throws

When `below` is a non-canonical order key.
