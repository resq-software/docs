# Type Alias: Flatten\<T\>

&gt; **Flatten**\<`T`\> = `T` *extends* readonly \[infer First, `...(infer Rest extends readonly unknown[][])`\] ? \[`...First`, `...Flatten<Rest>`\] : \[\]

Defined in: [collection.ts:148](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L148)

Flatten a tuple of tuples by one level —
`Flatten<[[1, 2], [3]]>` is `[1, 2, 3]`.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
