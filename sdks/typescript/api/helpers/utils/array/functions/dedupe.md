# Function: dedupe()

&gt; **dedupe**\<`T`\>(`input`, `equals?`): `T`[]

Defined in: [packages/helpers/src/utils/array.ts:79](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L79)

Remove duplicate items from an array.

Creates a new array with duplicate items removed. Uses strict equality by default,
or a custom equality function if provided. Order of first occurrence is preserved.

Comparison is pairwise against every item already kept, so runtime is O(n²);
for large arrays with cheap identity semantics prefer a `Set`. `equals` is
invoked as `equals(candidate, kept)`.

## Type Parameters

### T

`T`

## Parameters

### input

`T`[]

The array to deduplicate

### equals?

(`a`, `b`) =&gt; `boolean`

Optional custom equality function to compare items (defaults to strict equality)

## Returns

`T`[]

A new array with duplicate items removed

## Example

```ts
dedupe([1, 2, 2, 3, 1]) // [1, 2, 3]
dedupe(['a', 'b', 'a', 'c']) // ['a', 'b', 'c']

// With custom equality function
const objects = [{id: 1}, {id: 2}, {id: 1}]
dedupe(objects, (a, b) => a.id === b.id) // [{id: 1}, {id: 2}]
```
