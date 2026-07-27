# Function: parse()

&gt; **parse**(`input`): [`Expr`](../../ast/type-aliases/Expr)

Defined in: [packages/math/src/parse.ts:357](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/parse.ts#L357)

Parse a math expression string into an [Expr](../../ast/type-aliases/Expr) AST.

Accepts both Unicode operators (`×`, `∪`, `∀`) and their ASCII equivalents
(`*`, `union`, `forall`).

## Parameters

### input

`string`

The source expression to parse.

## Returns

[`Expr`](../../ast/type-aliases/Expr)

The parsed named AST.

## Throws

On unexpected characters, tokens, or trailing input.

## Throws

When the expression nests deeper than the parser limit.

## Example

```ts
parse("sum(i in {1, 2, 3}, i * i)");
```
