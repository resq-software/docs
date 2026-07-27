# Interface: BinderExpr

Defined in: [packages/math/src/ast.ts:97](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L97)

Binder (sum, product, or quantifier) that binds `bound` over `domain`.

## Properties

### body

&gt; `readonly` **body**: [`Expr`](../type-aliases/Expr)

Defined in: [packages/math/src/ast.ts:109](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L109)

Evaluated once per domain element with `bound` in scope.

***

### bound

&gt; `readonly` **bound**: `string`

Defined in: [packages/math/src/ast.ts:105](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L105)

Name introduced into scope for `body` only — it is *not* visible in
`domain`. The evaluator iterates the domain set, binding each element to
this name in turn.

***

### domain

&gt; `readonly` **domain**: [`Expr`](../type-aliases/Expr)

Defined in: [packages/math/src/ast.ts:107](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L107)

The set to iterate. Must evaluate to a `set`-sorted value, or evaluation throws.

***

### kind

&gt; `readonly` **kind**: `"binder"`

Defined in: [packages/math/src/ast.ts:98](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L98)

***

### op

&gt; `readonly` **op**: [`BinderOp`](../type-aliases/BinderOp)

Defined in: [packages/math/src/ast.ts:99](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L99)
