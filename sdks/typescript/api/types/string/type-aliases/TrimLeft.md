# Type Alias: TrimLeft\<S\>

&gt; **TrimLeft**\<`S`\> = `S` *extends* `` `${Whitespace}${infer R}` `` ? `TrimLeft`\<`R`\> : `S`

Defined in: [string.ts:33](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L33)

Remove leading whitespace from a string literal type.

## Type Parameters

### S

`S` *extends* `string`
