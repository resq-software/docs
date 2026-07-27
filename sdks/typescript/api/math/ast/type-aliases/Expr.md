# Type Alias: Expr

&gt; **Expr** = [`LitExpr`](../interfaces/LitExpr) \| [`VarExpr`](../interfaces/VarExpr) \| [`UnaryExpr`](../interfaces/UnaryExpr) \| [`BinaryExpr`](../interfaces/BinaryExpr) \| [`RelExpr`](../interfaces/RelExpr) \| [`LogicExpr`](../interfaces/LogicExpr) \| [`BinderExpr`](../interfaces/BinderExpr) \| [`CondExpr`](../interfaces/CondExpr) \| [`LambdaExpr`](../interfaces/LambdaExpr) \| [`CallExpr`](../interfaces/CallExpr) \| [`MemberExpr`](../interfaces/MemberExpr)

Defined in: [packages/math/src/ast.ts:150](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L150)

A parsed or hand-built mathematical expression — the *named* representation
layer. Discriminated on the `kind` field, one variant per node interface
above. Variables and binders carry string names; [compile](../../compile) resolves
those into the index-based [CompiledExpr](./CompiledExpr). Trees are deeply `readonly`;
the constructors in `builder.ts` are the ergonomic way to build them (and
perform no validation — an ill-sorted tree is rejected only by `checkExpr` or
`evaluate`).
