# Type Alias: Expand\<T\>

&gt; **Expand**\<`T`\> = [`Simplify`](../../object/type-aliases/Simplify)\<`T`\>

Defined in: [compat.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/compat.ts#L46)

Legacy alias of [Simplify](../../object/type-aliases/Simplify) — flattens a type into a single object
literal so IDE tooltips and error messages show the resolved shape instead of
a chain of intersections. Purely cosmetic; assignability is unchanged.

## Type Parameters

### T

`T`

The type to expand for display.
