# Function: rotateArray()

&gt; **rotateArray**\<`T`\>(`arr`, `offset`): `T`[]

Defined in: [packages/helpers/src/utils/array.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L43)

Rotate the contents of an array by a specified offset.

Creates a new array with elements shifted to the left by the specified number of positions.
Both positive and negative offsets result in left shifts (elements move left, with elements
from the front wrapping to the back).

## Type Parameters

### T

`T`

## Parameters

### arr

`T`[]

The array to rotate

### offset

`number`

The number of positions to shift left (both positive and negative values shift left)

## Returns

`T`[]

A new array with elements shifted left by the specified offset

## Example

```ts
rotateArray([1, 2, 3, 4], 1) // [2, 3, 4, 1]
rotateArray([1, 2, 3, 4], -1) // [2, 3, 4, 1]
rotateArray(['a', 'b', 'c'], 2) // ['c', 'a', 'b']
```
