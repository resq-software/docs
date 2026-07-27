# Function: areObjectsShallowEqual()

&gt; **areObjectsShallowEqual**\<`T`\>(`obj1`, `obj2`): `boolean`

Defined in: [packages/helpers/src/utils/object.ts:275](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L275)

**`Internal`**

Performs a shallow equality check between two objects. Compares all enumerable own properties
using Object.is for value comparison. Returns true if both objects have the same keys and values.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### obj1

`T`

First object to compare

### obj2

`T`

Second object to compare

## Returns

`boolean`

True if objects are shallow equal, false otherwise

## Example

```ts
const a = { x: 1, y: 2 }
const b = { x: 1, y: 2 }
const c = { x: 1, y: 3 }
areObjectsShallowEqual(a, b) // true
areObjectsShallowEqual(a, c) // false
areObjectsShallowEqual(a, a) // true (same reference)
```
