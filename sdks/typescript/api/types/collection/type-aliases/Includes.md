# Type Alias: Includes\<T, E\>

&gt; **Includes**\<`T`, `E`\> = `T` *extends* readonly \[infer H, `...(infer R)`\] ? \[`E`\] *extends* \[`H`\] ? \[`H`\] *extends* \[`E`\] ? `true` : `Includes`\<`R`, `E`\> : `Includes`\<`R`, `E`\> : `false`

Defined in: [collection.ts:71](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L71)

Whether `T` includes the element `E` (structural equality).

## Type Parameters

### T

`T` *extends* readonly `unknown`[]

### E

`E`
