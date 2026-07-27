# Function: asBool()

&gt; **asBool**(`v`, `context?`): `boolean`

Defined in: [packages/math/src/value.ts:151](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L151)

Extract the `boolean` from a `bool` value, or throw [SortError](../../error/classes/SortError).

## Parameters

### v

[`Value`](../type-aliases/Value)

The value to unwrap.

### context?

`string`

Optional description for the error message.

## Returns

`boolean`

The wrapped boolean.

## Throws

If `v` is not `bool`-sorted.
