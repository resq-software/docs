# Function: sortByIndex()

&gt; **sortByIndex**\<`T`\>(`a`, `b`): `number`

Defined in: [reordering.ts:203](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/reordering.ts#L203)

Comparator ordering objects by their `index` key ascending (lexicographic).

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

`-1` if `a` sorts before `b`, `1` if after, `0` if the keys are
  equal. Suitable as an `Array.prototype.sort` callback.

## Example

```ts
const rows = [{ index: "a2" as IndexKey }, { index: "a1" as IndexKey }];
rows.sort(sortByIndex);
rows[0].index; // → "a1"
```
