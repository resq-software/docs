# Function: sortByMaybeIndex()

&gt; **sortByMaybeIndex**\<`T`\>(`a`, `b`): `number`

Defined in: [reordering.ts:222](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L222)

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
