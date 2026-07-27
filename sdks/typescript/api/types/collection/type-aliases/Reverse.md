# Type Alias: Reverse\<T\>

&gt; **Reverse**\<`T`\> = `T` *extends* readonly \[infer H, `...(infer R)`\] ? \[`...Reverse<R>`, `H`\] : \[\]

Defined in: [collection.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L56)

Reverse a tuple's element order.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
