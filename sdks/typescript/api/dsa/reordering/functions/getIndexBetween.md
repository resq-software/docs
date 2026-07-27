# Function: getIndexBetween()

&gt; **getIndexBetween**(`below`, `above`): [`IndexKey`](../type-aliases/IndexKey)

Defined in: [reordering.ts:140](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L140)

Mint a single key that sorts strictly between two bounds.

Jittered (non-deterministic string) outside `NODE_ENV=test`; see
[getIndicesBetween](./getIndicesBetween).

## Parameters

### below

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Lower bound, or `null`/`undefined` for "no lower bound".

### above

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Upper bound, or `null`/`undefined` for "no upper bound".

## Returns

[`IndexKey`](../type-aliases/IndexKey)

A key `k` with `below < k < above`.

## Throws

When `below` is not strictly less than `above`, or when
  either bound is a non-canonical order key.
