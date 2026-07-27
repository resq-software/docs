# Type Alias: DeepNonNullable\<T\>

&gt; **DeepNonNullable**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `object` ? `{ [K in keyof T]: DeepNonNullable<NonNullable<T[K]>> }` : `NonNullable`\<`T`\>

Defined in: [object.ts:141](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L141)

Recursively remove `null` and `undefined` from every property.

## Type Parameters

### T

`T`
