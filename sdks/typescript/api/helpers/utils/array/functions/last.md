# Function: last()

&gt; **last**\<`T`\>(`arr`): `T` \| `undefined`

Defined in: [packages/helpers/src/utils/array.ts:129](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L129)

**`Internal`**

Get the last element of an array.

Returns the last element of an array, or undefined if the array is empty.
Works with readonly arrays and preserves the element type.

## Type Parameters

### T

`T`

## Parameters

### arr

readonly `T`[]

The array to get the last element from

## Returns

`T` \| `undefined`

The last element of the array, or undefined if the array is empty

## Example

```ts
last([1, 2, 3]) // 3
last(['a', 'b', 'c']) // 'c'
last([]) // undefined
```
