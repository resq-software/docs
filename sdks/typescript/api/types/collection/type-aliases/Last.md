# Type Alias: Last\<T\>

&gt; **Last**\<`T`\> = `T` *extends* readonly \[`...unknown[]`, infer L\] ? `L` : `never`

Defined in: [collection.ts:39](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L39)

The last element of a tuple, or `never` for the empty tuple.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
