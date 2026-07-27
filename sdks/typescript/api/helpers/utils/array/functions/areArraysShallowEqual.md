# Function: areArraysShallowEqual()

&gt; **areArraysShallowEqual**\<`T`\>(`arr1`, `arr2`): `boolean`

Defined in: [packages/helpers/src/utils/array.ts:273](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L273)

**`Internal`**

Check if two arrays are shallow equal.

Compares two arrays for shallow equality by checking if they have the same length
and the same elements at each index using Object.is comparison. Returns true if arrays are
the same reference, have different lengths, or any elements differ.

## Type Parameters

### T

`T`

## Parameters

### arr1

readonly `T`[]

First array to compare

### arr2

readonly `T`[]

Second array to compare

## Returns

`boolean`

True if arrays are shallow equal, false otherwise

## Example

```ts
areArraysShallowEqual([1, 2, 3], [1, 2, 3]) // true
areArraysShallowEqual([1, 2, 3], [1, 2, 4]) // false
areArraysShallowEqual(['a', 'b'], ['a', 'b']) // true
areArraysShallowEqual([1, 2], [1, 2, 3]) // false

const obj = {x: 1}
areArraysShallowEqual([obj], [obj]) // true (same reference)
areArraysShallowEqual([{x: 1}], [{x: 1}]) // false (different objects)
```
