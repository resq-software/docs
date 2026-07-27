# Function: compile()

&gt; **compile**(`expr`, `scope?`): [`CompiledExpr`](../../ast/type-aliases/CompiledExpr)

Defined in: [packages/math/src/compile.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/compile.ts#L45)

Compile a named mathematical expression AST into an index-based executable AST.

Pure: returns a fresh tree and does not mutate `expr` or `scope`. It never
fails on unknown variables — a name not bound by an enclosing binder or lambda
becomes a CFreeVarExpr, deferred to [evaluate](../../evaluate) to resolve (or
reject) against the environment.

## Parameters

### expr

[`Expr`](../../ast/type-aliases/Expr)

The named AST node to compile.

### scope?

readonly `string`[] = `[]`

The stack of active lexical variable names (innermost binder at the end).

## Returns

[`CompiledExpr`](../../ast/type-aliases/CompiledExpr)

The compiled expression node.

## Throws

When the expression nests deeper than the internal limit (200).
