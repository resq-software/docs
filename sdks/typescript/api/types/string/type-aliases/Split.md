# Type Alias: Split\<S, D\>

&gt; **Split**\<`S`, `D`\> = `S` *extends* `` `${infer Head}${D}${infer Tail}` `` ? \[`Head`, `...Split<Tail, D>`\] : \[`S`\]

Defined in: [string.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L47)

Split a string literal on a delimiter into a tuple of segments —
`Split<"a.b.c", ".">` is `["a", "b", "c"]`. When the delimiter never occurs
the whole string is returned as a single-element tuple (`Split<"abc", ".">` is
`["abc"]`), so the result is never the empty tuple.

## Type Parameters

### S

`S` *extends* `string`

### D

`D` *extends* `string`
