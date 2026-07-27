# Type Alias: SortContext

&gt; **SortContext** = `ReadonlyMap`\<`string`, [`Sort`](../../value/type-aliases/Sort)\>

Defined in: [packages/math/src/check.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/check.ts#L42)

Maps names to their known [Sort](../../value/type-aliases/Sort) in the current scope. Keys are plain
variable names, plus synthetic dotted/call paths (`"obj.prop"`, `"f()"`) that
let the checker resolve member-access and call-return sorts statically — see
`getMemberPath`. A referenced name with no entry is reported as an unbound
`SortError` rather than assumed.
