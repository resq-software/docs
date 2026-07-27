# Function: asFunc()

&gt; **asFunc**(`v`, `context?`): `object`

Defined in: [packages/math/src/value.ts:164](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L164)

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
