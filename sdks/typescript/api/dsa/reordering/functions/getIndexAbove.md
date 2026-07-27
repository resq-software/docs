# Function: getIndexAbove()

&gt; **getIndexAbove**(`below?`): [`IndexKey`](../type-aliases/IndexKey)

Defined in: [reordering.ts:157](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L157)

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
