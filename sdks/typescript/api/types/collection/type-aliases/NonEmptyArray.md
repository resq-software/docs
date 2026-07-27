# Type Alias: NonEmptyArray\<T\>

&gt; **NonEmptyArray**\<`T`\> = \[`T`, `...T[]`\]

Defined in: [collection.ts:139](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L139)

An array guaranteed to hold at least one element. Assigning `[]` to a
`NonEmptyArray<T>` is a compile error — handy for "you must supply at least
one target / recipient / allowed origin" APIs.

## Type Parameters

### T

`T`
