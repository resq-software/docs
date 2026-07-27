# Type Alias: DeepNonNullable\<T\>

&gt; **DeepNonNullable**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `object` ? `{ [K in keyof T]: DeepNonNullable<NonNullable<T[K]>> }` : `NonNullable`\<`T`\>

Defined in: [object.ts:141](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L141)

Recursively remove `null` and `undefined` from every property.

## Type Parameters

### T

`T`
