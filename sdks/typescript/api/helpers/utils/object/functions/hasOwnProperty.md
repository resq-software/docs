# Function: hasOwnProperty()

&gt; **hasOwnProperty**(`obj`, `key`): `boolean`

Defined in: [packages/helpers/src/utils/object.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L44)

**`Internal`**

Safely checks if an object has a specific property as its own property (not inherited).
Uses Object.prototype.hasOwnProperty.call to avoid issues with objects that have null prototype
or have overridden the hasOwnProperty method.

## Parameters

### obj

`object`

The object to check

### key

`string`

The property key to check for

## Returns

`boolean`

True if the object has the property as its own property, false otherwise

## Example

```ts
const obj = { name: 'Alice', age: 30 }
hasOwnProperty(obj, 'name') // true
hasOwnProperty(obj, 'toString') // false (inherited)
hasOwnProperty(obj, 'unknown') // false
```
