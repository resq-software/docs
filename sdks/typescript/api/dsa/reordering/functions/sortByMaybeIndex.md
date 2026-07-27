# Function: sortByMaybeIndex()

&gt; **sortByMaybeIndex**\<`T`\>(`a`, `b`): `number`

Defined in: [reordering.ts:222](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L222)

Comparator ordering objects whose `index` may be missing. Items with an
index sort ascending among themselves; an item without an index (`null` or
`undefined`) always sorts *after* one that has an index. Two index-less
items compare equal.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### a

`T`

### b

`T`

## Returns

`number`

A negative number, `0`, or a positive number per the usual
  comparator contract.
