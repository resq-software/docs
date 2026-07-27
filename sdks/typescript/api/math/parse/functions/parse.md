# Function: parse()

&gt; **parse**(`input`): [`Expr`](../../ast/type-aliases/Expr)

Defined in: [packages/math/src/parse.ts:357](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/parse.ts#L357)

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
