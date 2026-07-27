# Function: getIndexAbove()

&gt; **getIndexAbove**(`below?`): [`IndexKey`](../type-aliases/IndexKey)

Defined in: [reordering.ts:157](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L157)

Mint a single key that sorts after `below` (i.e. a new last item).

Jittered (non-deterministic string) outside `NODE_ENV=test`; see
[getIndicesBetween](./getIndicesBetween).

## Parameters

### below?

[`IndexKey`](../type-aliases/IndexKey) \| `null` \| `undefined`

The current last key, or `null` for an empty list.

## Returns

[`IndexKey`](../type-aliases/IndexKey)

A key greater than `below`.

## Throws

When `below` is a non-canonical order key.
