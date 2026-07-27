# Type Alias: RecursivePartial\<T\>

&gt; **RecursivePartial**\<`T`\> = [`DeepPartial`](../../object/type-aliases/DeepPartial)\<`T`\>

Defined in: [compat.ts:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/compat.ts#L37)

Legacy alias of [DeepPartial](../../object/type-aliases/DeepPartial) — recursively marks every property
optional. Kept only so code using the `RecursivePartial` name from other
toolkits compiles unchanged; new code should import [DeepPartial](../../object/type-aliases/DeepPartial).

## Type Parameters

### T

`T`

The object type to make deeply optional.
