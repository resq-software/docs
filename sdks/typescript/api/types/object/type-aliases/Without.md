# Type Alias: Without\<T, U\>

&gt; **Without**\<`T`, `U`\> = `{ [K in Exclude<keyof T, keyof U>]?: never }`

Defined in: [object.ts:167](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L167)

The keys of `T` that are absent from `U`, each typed `never` — the helper
behind [XOR](./XOR). Present only so the "forbidden" keys of one branch are
explicitly excluded in the other.

## Type Parameters

### T

`T`

### U

`U`
