# Type Alias: Join\<T, D\>

&gt; **Join**\<`T`, `D`\> = `T` *extends* readonly \[infer Head, `...(infer Rest extends string[])`\] ? `Rest` *extends* readonly \[\] ? `Head` : `` `${Head}${D}${Join<Rest, D>}` `` : `""`

Defined in: [string.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L56)

Join a tuple of string literals with a delimiter —
`Join<["a", "b", "c"], ".">` is `"a.b.c"`. The empty tuple joins to the empty
string, and a single-element tuple joins to that element with no delimiter.

## Type Parameters

### T

`T` *extends* readonly `string`[]

### D

`D` *extends* `string`
