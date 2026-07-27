# Function: print()

&gt; **print**(`expr`, `options?`): `string`

Defined in: [packages/math/src/print.ts:224](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/print.ts#L224)

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
