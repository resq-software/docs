# Function: asSet()

&gt; **asSet**(`v`, `context?`): `ReadonlySet`\<`number`\>

Defined in: [packages/math/src/value.ts:138](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L138)

Extract the `ReadonlySet<number>` from a `set` value, or throw [SortError](../../error/classes/SortError).

## Parameters

### v

[`Value`](../type-aliases/Value)

The value to unwrap.

### context?

`string`

Optional description for the error message.

## Returns

`ReadonlySet`\<`number`\>

The wrapped set.

## Throws

If `v` is not `set`-sorted.
