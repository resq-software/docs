# Variable: structuredClone

&gt; `const` **structuredClone**: \<`T`\>(`i`) =&gt; `T`

Defined in: [packages/helpers/src/utils/value.ts:153](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/value.ts#L153)

Create a deep copy of a value. Uses the structuredClone API if available, otherwise uses JSON.parse(JSON.stringify()).

The two backends are **not** equivalent, and which one is active is fixed at
module load (see [isNativeStructuredClone](./isNativeStructuredClone)):
- Native: preserves `Date`, `Map`, `Set`, `ArrayBuffer`, cyclic references, etc.
- JSON fallback: only round-trips JSON-representable data — `Date` becomes a
  string, `Map`/`Set`/functions/`undefined` are dropped, and a falsy input is
  returned as-is without copying. The example below is faithful under the native
  backend; under the fallback the `date` field would come back as a string.

## Type Parameters

### T

`T`

## Parameters

### i

`T`

The value to clone.

## Returns

`T`

A deep copy of the input value.

## Throws

(native backend) if `i` holds a non-cloneable value
  such as a function or symbol.

## Throws

(JSON fallback) if `i` contains a circular reference or a
  `BigInt`, since `JSON.stringify` cannot serialize either.

## Example

```ts
const original = { a: 1, b: { c: 2 } }
const copy = structuredClone(original)

copy.b.c = 3
console.log(original.b.c) // 2 (unchanged)
console.log(copy.b.c) // 3

// Works with complex objects
const complexObject = {
  date: new Date(),
  array: [1, 2, 3],
  nested: { deep: { value: "test" } }
}
const cloned = structuredClone(complexObject)
```
