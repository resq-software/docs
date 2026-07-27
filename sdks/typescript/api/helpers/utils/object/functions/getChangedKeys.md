# Function: getChangedKeys()

&gt; **getChangedKeys**\<`T`\>(`obj1`, `obj2`): keyof `T`[]

Defined in: [packages/helpers/src/utils/object.ts:367](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L367)

**`Internal`**

Compares two objects and returns an array of keys where the values differ.
Uses Object.is for comparison, which handles NaN and -0/+0 correctly.
Only checks keys present in the first object.

## Type Parameters

### T

`T` *extends* `object`

## Parameters

### obj1

`T`

The first object (keys to check come from this object)

### obj2

`T`

The second object to compare against

## Returns

keyof `T`[]

Array of keys where values differ between the objects

## Example

```ts
const before = { name: 'Alice', age: 25, city: 'NYC' }
const after = { name: 'Alice', age: 26, city: 'NYC' }
const changed = getChangedKeys(before, after)
// ['age']
```
