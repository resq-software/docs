# Type Alias: Join\<T, D\>

&gt; **Join**\<`T`, `D`\> = `T` *extends* readonly \[infer Head, `...(infer Rest extends string[])`\] ? `Rest` *extends* readonly \[\] ? `Head` : `` `${Head}${D}${Join<Rest, D>}` `` : `""`

Defined in: [string.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L56)

Join a tuple of string literals with a delimiter —
`Join<["a", "b", "c"], ".">` is `"a.b.c"`. The empty tuple joins to the empty
string, and a single-element tuple joins to that element with no delimiter.

## Type Parameters

### T

`T` *extends* readonly `string`[]

### D

`D` *extends* `string`
