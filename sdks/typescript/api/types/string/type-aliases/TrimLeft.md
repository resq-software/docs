# Type Alias: TrimLeft\<S\>

&gt; **TrimLeft**\<`S`\> = `S` *extends* `` `${Whitespace}${infer R}` `` ? `TrimLeft`\<`R`\> : `S`

Defined in: [string.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L33)

Remove leading whitespace from a string literal type.

## Type Parameters

### S

`S` *extends* `string`
