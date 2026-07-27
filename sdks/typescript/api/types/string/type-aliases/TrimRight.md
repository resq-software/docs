# Type Alias: TrimRight\<S\>

&gt; **TrimRight**\<`S`\> = `S` *extends* `` `${infer R}${Whitespace}` `` ? `TrimRight`\<`R`\> : `S`

Defined in: [string.ts:36](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L36)

Remove trailing whitespace from a string literal type.

## Type Parameters

### S

`S` *extends* `string`
