# Type Alias: Without\<T, U\>

&gt; **Without**\<`T`, `U`\> = `{ [K in Exclude<keyof T, keyof U>]?: never }`

Defined in: [object.ts:167](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L167)

The keys of `T` that are absent from `U`, each typed `never` — the helper
behind [XOR](./XOR). Present only so the "forbidden" keys of one branch are
explicitly excluded in the other.

## Type Parameters

### T

`T`

### U

`U`
