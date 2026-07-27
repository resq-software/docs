# Type Alias: Simplify\<T\>

&gt; **Simplify**\<`T`\> = `{ [K in keyof T]: T[K] }` & `object`

Defined in: [object.ts:42](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L42)

Flatten intersections and mapped types into a single object literal so hover
tooltips and error messages show `{ a: 1; b: 2 }` instead of
`A & B & Omit<…>`. No effect on assignability — purely cosmetic, but it makes
complex branded/derived types readable.

## Type Parameters

### T

`T`
