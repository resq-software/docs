# Type Alias: Head\<T\>

&gt; **Head**\<`T`\> = `T` *extends* readonly \[infer H, `...unknown[]`\] ? `H` : `never`

Defined in: [collection.ts:31](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L31)

The first element of a tuple, or `never` for the empty tuple.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
