# Function: sortByIndex()

&gt; **sortByIndex**\<`T`\>(`a`, `b`): `number`

Defined in: [reordering.ts:203](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L203)

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
