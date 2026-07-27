# Function: print()

&gt; **print**(`expr`, `options?`): `string`

Defined in: [packages/math/src/print.ts:224](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/print.ts#L224)

Render an expression AST to readable mathematical notation.

## Parameters

### expr

[`Expr`](../../ast/type-aliases/Expr)

The expression tree to print.

### options?

[`PrintOptions`](../interfaces/PrintOptions)

Optional formatting configuration.

## Returns

`string`

A string representation with minimal parentheses.

## Throws

If the tree nests deeper than the internal limit (200).
