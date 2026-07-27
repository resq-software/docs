# Type Alias: TupleToUnion\<T\>

&gt; **TupleToUnion**\<`T`\> = `T`\[`number`\]

Defined in: [collection.ts:65](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L65)

Collapse a tuple into the union of its element types —
`TupleToUnion<["a", "b"]>` is `"a" | "b"`. The idiomatic way to turn a
`readonly [...] as const` allow-list into a validating literal union.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
