# Type Alias: Last\<T\>

&gt; **Last**\<`T`\> = `T` *extends* readonly \[`...unknown[]`, infer L\] ? `L` : `never`

Defined in: [collection.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L39)

The last element of a tuple, or `never` for the empty tuple.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
