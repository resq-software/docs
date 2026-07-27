# Type Alias: SortContext

&gt; **SortContext** = `ReadonlyMap`\<`string`, [`Sort`](../../value/type-aliases/Sort)\>

Defined in: [packages/math/src/check.ts:42](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/check.ts#L42)

Maps names to their known [Sort](../../value/type-aliases/Sort) in the current scope. Keys are plain
variable names, plus synthetic dotted/call paths (`"obj.prop"`, `"f()"`) that
let the checker resolve member-access and call-return sorts statically — see
`getMemberPath`. A referenced name with no entry is reported as an unbound
`SortError` rather than assumed.
