# Type Alias: OmitByType\<T, V\>

&gt; **OmitByType**\<`T`, `V`\> = `{ [K in keyof T as T[K] extends V ? never : K]: T[K] }`

Defined in: [object.ts:136](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L136)

Drop the properties of `T` whose value type is assignable to `V`.

## Type Parameters

### T

`T`

### V

`V`
