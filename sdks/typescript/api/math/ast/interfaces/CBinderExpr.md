# Interface: CBinderExpr

Defined in: [packages/math/src/ast.ts:222](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/ast.ts#L222)

Compiled binder; the bound name is erased in favor of stack indices.

## Properties

### body

&gt; `readonly` **body**: [`CompiledExpr`](../type-aliases/CompiledExpr)

Defined in: [packages/math/src/ast.ts:227](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/ast.ts#L227)

Body where the bound name is replaced by index lookups.

***

### domain

&gt; `readonly` **domain**: [`CompiledExpr`](../type-aliases/CompiledExpr)

Defined in: [packages/math/src/ast.ts:225](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/ast.ts#L225)

***

### kind

&gt; `readonly` **kind**: `"binder"`

Defined in: [packages/math/src/ast.ts:223](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/ast.ts#L223)

***

### op

&gt; `readonly` **op**: [`BinderOp`](../type-aliases/BinderOp)

Defined in: [packages/math/src/ast.ts:224](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/ast.ts#L224)
