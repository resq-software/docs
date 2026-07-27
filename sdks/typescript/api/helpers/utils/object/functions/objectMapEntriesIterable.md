# Function: objectMapEntriesIterable()

&gt; **objectMapEntriesIterable**\<`Key`, `Value`\>(`object`): `IterableIterator`\<\[`Key`, `Value`\]\>

Defined in: [packages/helpers/src/utils/object.ts:162](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L162)

**`Internal`**

Returns the entries of an object as an iterable iterator.
Useful when working with large collections, to avoid allocating an array.
Only yields own properties (not inherited ones).

## Type Parameters

### Key

`Key` *extends* `string`

### Value

`Value`

## Parameters

### object

`{ [K in string]: Value }`

The object to iterate over

## Returns

`IterableIterator`\<\[`Key`, `Value`\]\>

Iterator yielding key-value pairs with preserved types

## Example

```ts
const largeMap = { a: 1, b: 2, c: 3 } // Imagine thousands of entries
for (const [key, value] of objectMapEntriesIterable(largeMap)) {
  // Process entries one at a time without creating a large array
  console.log(key, value)
}
```
