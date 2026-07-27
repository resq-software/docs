# Type Alias: TrimRight\<S\>

&gt; **TrimRight**\<`S`\> = `S` *extends* `` `${infer R}${Whitespace}` `` ? `TrimRight`\<`R`\> : `S`

Defined in: [string.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L36)

Remove trailing whitespace from a string literal type.

## Type Parameters

### S

`S` *extends* `string`
