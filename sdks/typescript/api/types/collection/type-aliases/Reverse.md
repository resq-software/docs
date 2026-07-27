# Type Alias: Reverse\<T\>

&gt; **Reverse**\<`T`\> = `T` *extends* readonly \[infer H, `...(infer R)`\] ? \[`...Reverse<R>`, `H`\] : \[\]

Defined in: [collection.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L56)

Reverse a tuple's element order.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
