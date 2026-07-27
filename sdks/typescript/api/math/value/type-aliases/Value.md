# Type Alias: Value

&gt; **Value** = \{ `sort`: `"num"`; `value`: `number`; \} \| \{ `sort`: `"set"`; `value`: `ReadonlySet`\<`number`\>; \} \| \{ `sort`: `"bool"`; `value`: `boolean`; \} \| \{ `body`: [`CompiledExpr`](../../ast/type-aliases/CompiledExpr); `closure`: readonly `Value`[]; `sort`: `"func"`; \} \| \{ `sort`: `"record"`; `value`: `Readonly`\<`Record`\<`string`, `Value`\>\>; \} & `object`

Defined in: [packages/math/src/value.ts:55](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L55)

A tagged runtime value, the output of evaluation. `sort` is the discriminant:
it selects which remaining fields are present and which operator instances the
evaluator dispatches to.

- `"num"`, `"bool"`, and `"record"` carry a matching `value` payload; `"set"`
  carries a `ReadonlySet<number>` (finite integer sets only).
- `"func"` is the exception — it has no `value`. It carries a compiled `body`
  plus the `closure` (the lexical value stack captured where the lambda was
  evaluated); the two together *are* the function. See [func](../functions/func) and
  [asFunc](../functions/asFunc).

All payloads are deeply `readonly`; `category` is optional advisory metadata
(see [ValueCategory](./ValueCategory)).

## Type Declaration

### category?

&gt; `readonly` `optional` **category?**: [`ValueCategory`](./ValueCategory)
