# Function: getIndexBelow()

&gt; **getIndexBelow**(`above?`): [`IndexKey`](../type-aliases/IndexKey)

Defined in: [reordering.ts:171](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L171)

Mint a single key that sorts before `above` (i.e. a new first item).

Jittered (non-deterministic string) outside `NODE_ENV=test`; see
[getIndicesBetween](./getIndicesBetween).

## Parameters

### above?

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

The current first key, or `null` for an empty list.

## Returns

[`IndexKey`](../type-aliases/IndexKey)

A key less than `above`.

## Throws

When `above` is a non-canonical order key.
