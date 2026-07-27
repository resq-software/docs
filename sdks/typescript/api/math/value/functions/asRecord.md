# Function: asRecord()

&gt; **asRecord**(`v`, `context?`): `Readonly`\<`Record`\<`string`, [`Value`](../type-aliases/Value)\>\>

Defined in: [packages/math/src/value.ts:183](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L183)

Extract the record dictionary from a `record` value, or throw [SortError](../../error/classes/SortError).

## Parameters

### v

[`Value`](../type-aliases/Value)

The value to unwrap.

### context?

`string`

Optional description for the error message.

## Returns

`Readonly`\<`Record`\<`string`, [`Value`](../type-aliases/Value)\>\>

The wrapped record dictionary.

## Throws

If `v` is not `record`-sorted.
