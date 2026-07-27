# Function: div()

&gt; **div**(`a`, `b`): [`Expr`](../../ast/type-aliases/Expr)

Defined in: [packages/math/src/builder.ts:111](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/builder.ts#L111)

Division: `a ÷ b`. The built node throws DomainError at evaluation when the divisor is `0`.

## Parameters

### a

[`Expr`](../../ast/type-aliases/Expr)

### b

[`Expr`](../../ast/type-aliases/Expr)

## Returns

[`Expr`](../../ast/type-aliases/Expr)
