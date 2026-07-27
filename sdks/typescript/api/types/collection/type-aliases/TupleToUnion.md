# Type Alias: TupleToUnion\<T\>

&gt; **TupleToUnion**\<`T`\> = `T`\[`number`\]

Defined in: [collection.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L65)

Collapse a tuple into the union of its element types —
`TupleToUnion<["a", "b"]>` is `"a" | "b"`. The idiomatic way to turn a
`readonly [...] as const` allow-list into a validating literal union.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
