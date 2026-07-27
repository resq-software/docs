# Function: minBy()

&gt; **minBy**\<`T`\>(`arr`, `fn`): `T` \| `undefined`

Defined in: [packages/helpers/src/utils/array.ts:160](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L160)

**`Internal`**

Find the item in an array with the minimum value according to a function.

Finds the array item that produces the smallest value when passed through
the provided function. Returns undefined for empty arrays.

Selection uses `<`, so an item is only chosen when it is strictly smaller than
the running minimum. Items whose `fn` returns `NaN` are never selected (any
comparison with `NaN` is false); likewise a non-empty array returns
`undefined` when every `fn` result is `Infinity`. On ties the first-seen item
wins.

## Type Parameters

### T

`T`

## Parameters

### arr

readonly `T`[]

The array to search

### fn

(`item`) =&gt; `number`

Function to compute the comparison value for each item

## Returns

`T` \| `undefined`

The item with the minimum value, or `undefined` if the array is empty
  (or nothing compares smaller than the initial `Infinity`).

## Example

```ts
const people = [{name: 'Alice', age: 30}, {name: 'Bob', age: 25}]
minBy(people, p => p.age) // {name: 'Bob', age: 25}

minBy([3, 1, 4, 1, 5], x => x) // 1
minBy([], x => x) // undefined
```
