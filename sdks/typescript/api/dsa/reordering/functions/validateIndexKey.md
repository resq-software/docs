# Function: validateIndexKey()

&gt; **validateIndexKey**(`index`): `asserts index is IndexKey`

Defined in: [reordering.ts:67](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L67)

Assert that an externally-sourced string is a canonical [IndexKey](../type-aliases/IndexKey),
narrowing it in place on success.

## Parameters

### index

`string`

The candidate key (e.g. read from storage or a request).

## Returns

`asserts index is IndexKey`

## Throws

With message `invalid index: <index>` when `index` is the
  reserved smallest-integer key or otherwise not a canonical order key.
