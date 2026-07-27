# Type Alias: LiteralUnion\<Known\>

&gt; **LiteralUnion**\<`Known`\> = `Known` \| `string` & `object`

Defined in: [string.ts:101](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L101)

The "open literal union" idiom: a known set of string literals that still
accepts any other string, while preserving autocomplete for the known
members. `LiteralUnion<"development" | "production">` behaves like `string`
but suggests the two known values.

## Type Parameters

### Known

`Known` *extends* `string`
