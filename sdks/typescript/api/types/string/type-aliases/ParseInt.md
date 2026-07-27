# Type Alias: ParseInt\<S\>

&gt; **ParseInt**\<`S`\> = `S` *extends* `` `${infer N extends number}` `` ? `N` : `never`

Defined in: [string.ts:107](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L107)

Parse a numeric string literal into a `number` literal type —
`ParseInt<"42">` is `42`. Resolves to `never` for non-numeric strings.

## Type Parameters

### S

`S` *extends* `string`
