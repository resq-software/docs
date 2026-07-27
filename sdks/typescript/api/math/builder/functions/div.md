# Function: div()

&gt; **div**(`a`, `b`): [`Expr`](../../ast/type-aliases/Expr)

Defined in: [packages/math/src/builder.ts:111](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/builder.ts#L111)

Division: `a ÷ b`. The built node throws DomainError at evaluation when the divisor is `0`.

## Parameters

### a

[`Expr`](../../ast/type-aliases/Expr)

### b

[`Expr`](../../ast/type-aliases/Expr)

## Returns

[`Expr`](../../ast/type-aliases/Expr)
