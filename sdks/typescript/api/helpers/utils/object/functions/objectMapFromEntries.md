# Function: objectMapFromEntries()

&gt; **objectMapFromEntries**\<`Key`, `Value`\>(`entries`): `{ [K in string]: Value }`

Defined in: [packages/helpers/src/utils/object.ts:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L187)

**`Internal`**

An alias for `Object.fromEntries` that treats the object as a map and so preserves the type of the
keys and values. Creates an object from key-value pairs with proper TypeScript typing.

## Type Parameters

### Key

`Key` *extends* `string`

### Value

`Value`

## Parameters

### entries

readonly readonly \[`Key`, `Value`\][]

Array of key-value pairs to convert to an object

## Returns

`{ [K in string]: Value }`

Object with preserved key and value types

## Example

```ts
const pairs: Array<['name' | 'age', string | number]> = [['name', 'Alice'], ['age', 30]]
const obj = objectMapFromEntries(pairs)
// obj is { name: string | number, age: string | number }
```
