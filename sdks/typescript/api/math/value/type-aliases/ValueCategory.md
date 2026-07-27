# Type Alias: ValueCategory

&gt; **ValueCategory** = `"lvalue"` \| `"prvalue"`

Defined in: [packages/math/src/value.ts:38](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L38)

Value-category tag borrowed from C++ terminology: `prvalue` for freshly
computed results and `lvalue` for addressable operands. Purely advisory
metadata carried on [Value](./Value) — the evaluator never reads it, so it does
not affect any result. Every constructor here stamps `"prvalue"`.
