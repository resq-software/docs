# Function: success()

&gt; **success**\<`T`\>(`value`): `Success`\<`T`\>

Defined in: [packages/helpers/src/helpers.ts:163](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L163)

Wrap a value in a Success branch. The returned object is frozen
so consumers cannot mutate `success`/`value` after the fact.

## Type Parameters

### T

`T`

## Parameters

### value

`T`

The value the operation produced.

## Returns

`Success`\<`T`\>

`{ success: true, value }` (frozen).
