# Function: asNum()

&gt; **asNum**(`v`, `context?`): `number`

Defined in: [packages/math/src/value.ts:125](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L125)

Extract the `number` from a `num` value, or throw [SortError](../../error/classes/SortError).

## Parameters

### v

[`Value`](../type-aliases/Value)

The value to unwrap.

### context?

`string`

Optional description for the error message (e.g. operator name).

## Returns

`number`

The wrapped number.

## Throws

If `v` is not `num`-sorted.
