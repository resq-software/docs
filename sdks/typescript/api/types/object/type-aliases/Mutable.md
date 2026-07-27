# Type Alias: Mutable\<T\>

&gt; **Mutable**\<`T`\> = `{ -readonly [K in keyof T]: T[K] }`

Defined in: [object.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L34)

Non-recursively strip `readonly` from every property. The dual of the
built-in `Readonly`.

## Type Parameters

### T

`T`
