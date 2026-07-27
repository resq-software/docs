# Type Alias: Mutable\<T\>

&gt; **Mutable**\<`T`\> = `{ -readonly [K in keyof T]: T[K] }`

Defined in: [object.ts:34](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L34)

Non-recursively strip `readonly` from every property. The dual of the
built-in `Readonly`.

## Type Parameters

### T

`T`
