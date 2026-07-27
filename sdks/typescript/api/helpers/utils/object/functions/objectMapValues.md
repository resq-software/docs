# Function: objectMapValues()

&gt; **objectMapValues**\<`Key`, `Value`\>(`object`): `Value`[]

Defined in: [packages/helpers/src/utils/object.ts:117](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L117)

**`Internal`**

An alias for `Object.values` that treats the object as a map and so preserves the type of the
values. Unlike standard Object.values which returns unknown[], this maintains the specific value types.

## Type Parameters

### Key

`Key` *extends* `string`

### Value

`Value`

## Parameters

### object

`{ [K in string]: Value }`

The object to get values from

## Returns

`Value`[]

Array of values with preserved types

## Example

```ts
const scores = { alice: 85, bob: 92, charlie: 78 }
const values = objectMapValues(scores)
// values is Array<number> instead of unknown[]
```
