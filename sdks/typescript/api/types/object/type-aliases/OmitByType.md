# Type Alias: OmitByType\<T, V\>

&gt; **OmitByType**\<`T`, `V`\> = `{ [K in keyof T as T[K] extends V ? never : K]: T[K] }`

Defined in: [object.ts:136](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L136)

Drop the properties of `T` whose value type is assignable to `V`.

## Type Parameters

### T

`T`

### V

`V`
