# Interface: CLambdaExpr

Defined in: [packages/math/src/ast.ts:239](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L239)

Compiled lambda; the parameter name is erased in favor of a stack slot.

## Properties

### body

&gt; `readonly` **body**: [`CompiledExpr`](../type-aliases/CompiledExpr)

Defined in: [packages/math/src/ast.ts:242](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L242)

Compiled body evaluated with the argument pushed onto the stack.

***

### kind

&gt; `readonly` **kind**: `"lambda"`

Defined in: [packages/math/src/ast.ts:240](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L240)
