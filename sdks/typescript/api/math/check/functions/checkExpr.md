# Function: checkExpr()

&gt; **checkExpr**(`expr`, `ctx?`, `depth?`): [`CheckResult`](../type-aliases/CheckResult)

Defined in: [packages/math/src/check.ts:127](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/check.ts#L127)

Infer the sort of `expr` under the given variable context, collecting
**all** sort errors encountered during the recursive walk.

## Parameters

### expr

[`Expr`](../../ast/type-aliases/Expr)

The expression AST node to check.

### ctx?

[`SortContext`](../type-aliases/SortContext) = `...`

An optional mapping from variable names to their sorts.
Defaults to an empty context.

### depth?

`number` = `0`

Current recursion depth; used internally to bound the walk.

## Returns

[`CheckResult`](../type-aliases/CheckResult)

A [CheckResult](../type-aliases/CheckResult) — either the inferred sort or an array of
every [SortError](../../error/classes/SortError) discovered.

## Throws

If the expression nests deeper than the internal limit.
