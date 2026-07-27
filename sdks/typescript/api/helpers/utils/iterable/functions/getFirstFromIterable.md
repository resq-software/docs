# Function: getFirstFromIterable()

&gt; **getFirstFromIterable**\<`T`\>(`set`): `T` \| `undefined`

Defined in: [packages/helpers/src/utils/iterable.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/iterable.ts#L48)

Get the first item from an iterable Set or Map.

"First" is defined by iteration order, which for both `Set` and `Map` is
insertion order — so this returns the earliest-inserted value. For a `Map` the
value (not the key) is returned. Reads a single element without materializing
an array.

## Type Parameters

### T

`T` = `unknown`

The element type for a `Set`, or the value type for a `Map` (its
  key type is intentionally unconstrained).

## Parameters

### set

`Set`\<`T`\> \| `Map`\<`unknown`, `T`\>

The iterable Set or Map to get the first item from

## Returns

`T` \| `undefined`

The first value from the Set or Map, or `undefined` if it is empty

## Example

```ts
const A = getFirstFromIterable(new Set([1, 2, 3])) // 1
const B = getFirstFromIterable(
	new Map([
		['a', 1],
		['b', 2],
	])
) // 1
```
