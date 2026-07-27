# Function: getIndicesBetween()

&gt; **getIndicesBetween**(`below`, `above`, `n`): [`IndexKey`](../type-aliases/IndexKey)[]

Defined in: [reordering.ts:90](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L90)

Generate `n` keys that sort strictly between two bounds, evenly spaced.

Outside `NODE_ENV=test` the keys are jittered with `Math.random`, so the
exact strings returned are **non-deterministic** (see the module overview);
only their relative order (`below < result[i] < above`) is guaranteed.

## Parameters

### below

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Lower bound, or `null`/`undefined` for "no lower bound".

### above

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

Upper bound, or `null`/`undefined` for "no upper bound".

### n

`number`

How many keys to mint. `0` returns an empty array without
  validating the bounds.

## Returns

[`IndexKey`](../type-aliases/IndexKey)[]

`n` keys in ascending order.

## Throws

When `below` is not strictly less than `above`, or when
  either bound is a non-canonical order key.
