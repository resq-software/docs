# Type Alias: CompiledExpr

&gt; **CompiledExpr** = [`CLitExpr`](../interfaces/CLitExpr) \| [`CFreeVarExpr`](../interfaces/CFreeVarExpr) \| [`CBoundVarExpr`](../interfaces/CBoundVarExpr) \| [`CUnaryExpr`](../interfaces/CUnaryExpr) \| [`CBinaryExpr`](../interfaces/CBinaryExpr) \| [`CRelExpr`](../interfaces/CRelExpr) \| [`CLogicExpr`](../interfaces/CLogicExpr) \| [`CBinderExpr`](../interfaces/CBinderExpr) \| [`CCondExpr`](../interfaces/CCondExpr) \| [`CLambdaExpr`](../interfaces/CLambdaExpr) \| [`CCallExpr`](../interfaces/CCallExpr) \| [`CMemberExpr`](../interfaces/CMemberExpr)

Defined in: [packages/math/src/ast.ts:266](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L266)

A scope-resolved expression ready for [evaluate](../../evaluate) — the output of
[compile](../../compile). Shares the `kind` discriminant with [Expr](./Expr), but variable
names are gone: [CBoundVarExpr](../interfaces/CBoundVarExpr) holds a De Bruijn index into the
evaluation stack, and [CFreeVarExpr](../interfaces/CFreeVarExpr) holds a name resolved from the
environment at evaluation. Deeply `readonly`.
