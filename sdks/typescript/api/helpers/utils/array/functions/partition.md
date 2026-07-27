# Function: partition()

&gt; **partition**\<`T`\>(`arr`, `predicate`): \[`T`[], `T`[]\]

Defined in: [packages/helpers/src/utils/array.ts:236](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L236)

**`Internal`**

Split an array into two arrays based on a predicate function.

Partitions an array into two arrays: one containing items that satisfy
the predicate, and another containing items that do not. The original array order is preserved.

## Type Parameters

### T

`T`

## Parameters

### arr

`T`[]

The array to partition

### predicate

(`item`) =&gt; `boolean`

The predicate function to test each item

## Returns

\[`T`[], `T`[]\]

A tuple of two arrays: [satisfying items, non-satisfying items]

## Example

```ts
const [evens, odds] = partition([1, 2, 3, 4, 5], x => x % 2 === 0)
// evens: [2, 4], odds: [1, 3, 5]

const [adults, minors] = partition(
  [{name: 'Alice', age: 30}, {name: 'Bob', age: 17}],
  person => person.age >= 18
)
// adults: [{name: 'Alice', age: 30}], minors: [{name: 'Bob', age: 17}]
```
