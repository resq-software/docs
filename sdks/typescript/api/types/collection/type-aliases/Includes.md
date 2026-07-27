# Type Alias: Includes\<T, E\>

&gt; **Includes**\<`T`, `E`\> = `T` *extends* readonly \[infer H, `...(infer R)`\] ? \[`E`\] *extends* \[`H`\] ? \[`H`\] *extends* \[`E`\] ? `true` : `Includes`\<`R`, `E`\> : `Includes`\<`R`, `E`\> : `false`

Defined in: [collection.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L71)

Whether `T` includes the element `E` (structural equality).

## Type Parameters

### T

`T` *extends* readonly `unknown`[]

### E

`E`
