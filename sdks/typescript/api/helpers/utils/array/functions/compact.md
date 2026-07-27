# Function: compact()

&gt; **compact**\<`T`\>(`arr`): `NonNullable`\<`T`\>[]

Defined in: [packages/helpers/src/utils/array.ts:108](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L108)

**`Internal`**

Remove null and undefined values from an array.

Creates a new array with all null and undefined values filtered out.
The resulting array has a refined type that excludes null and undefined.

## Type Parameters

### T

`T`

## Parameters

### arr

`T`[]

The array to compact

## Returns

`NonNullable`\<`T`\>[]

A new array with null and undefined values removed

## Example

```ts
compact([1, null, 2, undefined, 3]) // [1, 2, 3]
compact(['a', null, 'b', undefined]) // ['a', 'b']
```
