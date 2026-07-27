# Type Alias: PickByType\<T, V\>

&gt; **PickByType**\<`T`, `V`\> = `{ [K in keyof T as T[K] extends V ? K : never]: T[K] }`

Defined in: [object.ts:131](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L131)

Keep only the properties of `T` whose value type is assignable to `V`.

## Type Parameters

### T

`T`

### V

`V`
