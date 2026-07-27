# Function: objectMapEntries()

&gt; **objectMapEntries**\<`Obj`\>(`object`): \[keyof `Obj`, `Obj`\[keyof `Obj`\]\][]

Defined in: [packages/helpers/src/utils/object.ts:139](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L139)

**`Internal`**

An alias for `Object.entries` that treats the object as a map and so preserves the type of the
keys and values. Unlike standard Object.entries which returns `Array<[string, unknown]>`, this maintains specific types.

## Type Parameters

### Obj

`Obj` *extends* `object`

## Parameters

### object

`Obj`

The object to get entries from

## Returns

\[keyof `Obj`, `Obj`\[keyof `Obj`\]\][]

Array of key-value pairs with preserved types

## Example

```ts
const user = { name: 'Alice', age: 30 }
const entries = objectMapEntries(user)
// entries is Array<['name' | 'age', string | number]>
```
