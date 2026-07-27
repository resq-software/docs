# Interface: CBoundVarExpr

Defined in: [packages/math/src/ast.ts:180](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L180)

Bound variable addressed by its De Bruijn index into the value stack.

## Properties

### index

&gt; `readonly` **index**: `number`

Defined in: [packages/math/src/ast.ts:187](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L187)

Stack offset from the top; index 0 is the innermost binding. Must be less
than the live stack depth at evaluation — an out-of-range index (a sign of
a malformed tree) raises a `StackError`.

***

### kind

&gt; `readonly` **kind**: `"bound_var"`

Defined in: [packages/math/src/ast.ts:181](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/ast.ts#L181)
