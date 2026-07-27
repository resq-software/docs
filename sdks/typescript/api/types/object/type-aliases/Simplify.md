# Type Alias: Simplify\<T\>

&gt; **Simplify**\<`T`\> = `{ [K in keyof T]: T[K] }` & `object`

Defined in: [object.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L42)

Flatten intersections and mapped types into a single object literal so hover
tooltips and error messages show `{ a: 1; b: 2 }` instead of
`A & B & Omit<…>`. No effect on assignability — purely cosmetic, but it makes
complex branded/derived types readable.

## Type Parameters

### T

`T`
