# Type Alias: ValueCategory

&gt; **ValueCategory** = `"lvalue"` \| `"prvalue"`

Defined in: [packages/math/src/value.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L38)

Value-category tag borrowed from C++ terminology: `prvalue` for freshly
computed results and `lvalue` for addressable operands. Purely advisory
metadata carried on [Value](./Value) — the evaluator never reads it, so it does
not affect any result. Every constructor here stamps `"prvalue"`.
