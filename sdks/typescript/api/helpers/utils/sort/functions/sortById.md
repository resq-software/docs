# Function: sortById()

&gt; **sortById**\<`T`\>(`a`, `b`): `-1` \| `0` \| `1`

Defined in: [packages/helpers/src/utils/sort.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/sort.ts#L51)

Compares two objects by their id property for use with Array.sort().
Sorts objects in ascending order based on their id values.

Ordering is by the `<` / `>` relational operators, so it is well-defined for
string or numeric ids but yields `0` (treated as equal) whenever neither
comparison is true — e.g. `NaN` ids or mutually incomparable types — which
leaves such elements in their original relative order.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### a

`T`

First object to compare

### b

`T`

Second object to compare

## Returns

`-1` \| `0` \| `1`

1 if a.id \> b.id, -1 if a.id \< b.id, 0 if a.id === b.id

## Example

```ts
const items = [
  { id: 'c', name: 'Charlie' },
  { id: 'a', name: 'Alice' },
  { id: 'b', name: 'Bob' },
]

const sorted = items.sort(sortById)
// [{ id: 'a', name: 'Alice' }, { id: 'b', name: 'Bob' }, { id: 'c', name: 'Charlie' }]
```
