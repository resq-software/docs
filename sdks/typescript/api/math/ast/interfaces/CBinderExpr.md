# Interface: CBinderExpr

Defined in: [packages/math/src/ast.ts:222](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L222)

Compiled binder; the bound name is erased in favor of stack indices.

## Properties

### body

&gt; `readonly` **body**: [`CompiledExpr`](../type-aliases/CompiledExpr)

Defined in: [packages/math/src/ast.ts:227](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L227)

Body where the bound name is replaced by index lookups.

***

### domain

&gt; `readonly` **domain**: [`CompiledExpr`](../type-aliases/CompiledExpr)

Defined in: [packages/math/src/ast.ts:225](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L225)

***

### kind

&gt; `readonly` **kind**: `"binder"`

Defined in: [packages/math/src/ast.ts:223](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L223)

***

### op

&gt; `readonly` **op**: [`BinderOp`](../type-aliases/BinderOp)

Defined in: [packages/math/src/ast.ts:224](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L224)
