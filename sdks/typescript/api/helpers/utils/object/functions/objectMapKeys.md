# Function: objectMapKeys()

&gt; **objectMapKeys**\<`Key`\>(`object`): `Key`[]

Defined in: [packages/helpers/src/utils/object.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L95)

**`Internal`**

An alias for `Object.keys` that treats the object as a map and so preserves the type of the keys.
Unlike standard Object.keys which returns string[], this maintains the specific string literal types.

## Type Parameters

### Key

`Key` *extends* `string`

## Parameters

### object

`{ readonly [K in string]: unknown }`

The object to get keys from

## Returns

`Key`[]

Array of keys with preserved string literal types

## Example

```ts
const config = { theme: 'dark', lang: 'en' } as const
const keys = objectMapKeys(config)
// keys is Array<'theme' | 'lang'> instead of string[]
```
