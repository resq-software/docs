# Type Alias: ParseInt\<S\>

&gt; **ParseInt**\<`S`\> = `S` *extends* `` `${infer N extends number}` `` ? `N` : `never`

Defined in: [string.ts:107](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L107)

Parse a numeric string literal into a `number` literal type —
`ParseInt<"42">` is `42`. Resolves to `never` for non-numeric strings.

## Type Parameters

### S

`S` *extends* `string`
