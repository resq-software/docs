# Function: asNum()

&gt; **asNum**(`v`, `context?`): `number`

Defined in: [packages/math/src/value.ts:125](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L125)

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
