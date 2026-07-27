# Function: asFunc()

&gt; **asFunc**(`v`, `context?`): `object`

Defined in: [packages/math/src/value.ts:164](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L164)

Extract the closure parts from a `func` value, or throw [SortError](../../error/classes/SortError).

## Parameters

### v

[`Value`](../type-aliases/Value)

The value to unwrap.

### context?

`string`

Optional description for the error message.

## Returns

`object`

The compiled body and captured closure.

### body

&gt; `readonly` **body**: [`CompiledExpr`](../../ast/type-aliases/CompiledExpr)

### closure

&gt; `readonly` **closure**: readonly [`Value`](../type-aliases/Value)[]

## Throws

If `v` is not `func`-sorted.
