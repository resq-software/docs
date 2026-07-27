# Function: getIndices()

&gt; **getIndices**(`n`, `start?`): [`IndexKey`](../type-aliases/IndexKey)[]

Defined in: [reordering.ts:187](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L187)

Build an initial run of `n + 1` ascending keys, with `start` as the first.

The keys after `start` are jittered (non-deterministic strings) outside
`NODE_ENV=test`; see [getIndicesBetween](./getIndicesBetween). `start` itself is returned
verbatim.

## Parameters

### n

`number`

How many keys to append after `start`.

### start?

[`IndexKey`](../type-aliases/IndexKey) = `...`

The first key; defaults to `"a1"`.

## Returns

[`IndexKey`](../type-aliases/IndexKey)[]

`n + 1` keys in ascending order, beginning with `start`.

## Throws

When `start` is a non-canonical order key.
