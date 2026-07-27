# Function: mergeArraysAndReplaceDefaults()

&gt; **mergeArraysAndReplaceDefaults**\<`Key`, `T`\>(`key`, `customEntries`, `defaults`): `T`[]

Defined in: [packages/helpers/src/utils/array.ts:320](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/array.ts#L320)

**`Internal`**

Merge custom entries with defaults, replacing defaults that have matching keys.

Combines two arrays by keeping all custom entries and only the default entries
that don't have a matching key in the custom entries. Custom entries always override defaults.
The result contains remaining defaults first, followed by all custom entries.

Matching is by the value at `key`, deduped through a `Set`; a default is
dropped when any custom entry shares its key. Custom entries are appended
verbatim, so duplicates among the custom entries themselves are preserved.

## Type Parameters

### Key

`Key` *extends* `string`

The literal name of the identity property (captured `const` so
  the key type is preserved).

### T

`T` *extends* `{ [K in string]: string }`

The entry shape; the `extends { [K in Key]: string }` bound
  requires every entry to carry a string-valued property named `Key`.

## Parameters

### key

`Key`

The property name to use as the unique identifier

### customEntries

readonly `T`[]

Array of custom entries that will override defaults

### defaults

readonly `T`[]

Array of default entries

## Returns

`T`[]

A new array with defaults filtered out where custom entries exist, plus all custom entries

## Example

```ts
const defaults = [{type: 'text', value: 'default'}, {type: 'number', value: 0}]
const custom = [{type: 'text', value: 'custom'}]

mergeArraysAndReplaceDefaults('type', custom, defaults)
// Result: [{type: 'number', value: 0}, {type: 'text', value: 'custom'}]

const tools = [{id: 'select', name: 'Select'}, {id: 'draw', name: 'Draw'}]
const customTools = [{id: 'select', name: 'Custom Select'}]

mergeArraysAndReplaceDefaults('id', customTools, tools)
// Result: [{id: 'draw', name: 'Draw'}, {id: 'select', name: 'Custom Select'}]
```
