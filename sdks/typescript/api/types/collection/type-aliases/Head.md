# Type Alias: Head\<T\>

&gt; **Head**\<`T`\> = `T` *extends* readonly \[infer H, `...unknown[]`\] ? `H` : `never`

Defined in: [collection.ts:31](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L31)

The first element of a tuple, or `never` for the empty tuple.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
