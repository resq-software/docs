# Type Alias: Tail\<T\>

&gt; **Tail**\<`T`\> = `T` *extends* readonly \[`unknown`, `...(infer R)`\] ? `R` : \[\]

Defined in: [collection.ts:36](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L36)

Everything after the first element of a tuple (the empty tuple if `T` is empty).

## Type Parameters

### T

`T` *extends* readonly `unknown`[]
