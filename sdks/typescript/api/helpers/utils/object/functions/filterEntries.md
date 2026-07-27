# Function: filterEntries()

&gt; **filterEntries**\<`Key`, `Value`\>(`object`, `predicate`): `{ [K in string]: Value }`

Defined in: [packages/helpers/src/utils/object.ts:212](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L212)

**`Internal`**

Filters an object using a predicate function, returning a new object with only the entries
that pass the predicate. Optimized to return the original object if no changes are needed.

When nothing is filtered out, the **same** object reference is returned (not a
copy) — callers relying on referential equality for memoization can depend on
this. Only own enumerable string keys are considered.

## Type Parameters

### Key

`Key` *extends* `string`

### Value

`Value`

## Parameters

### object

`{ [K in string]: Value }`

The object to filter

### predicate

(`key`, `value`) =&gt; `boolean`

Function that tests each key-value pair

## Returns

`{ [K in string]: Value }`

A new object with only the entries that pass the predicate, or the original object if unchanged

## Example

```ts
const scores = { alice: 85, bob: 92, charlie: 78 }
const passing = filterEntries(scores, (name, score) => score >= 80)
// { alice: 85, bob: 92 }
```
