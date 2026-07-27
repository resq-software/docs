# Type Alias: Tail\<T\>

&gt; **Tail**\<`T`\> = `T` *extends* readonly \[`unknown`, `...(infer R)`\] ? `R` : \[\]

Defined in: [collection.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L36)

Everything after the first element of a tuple (the empty tuple if `T` is empty).

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
