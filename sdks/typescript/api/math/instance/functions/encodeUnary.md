# Function: encodeUnary()

&gt; **encodeUnary**(`op`, `sort`): `number`

Defined in: [packages/math/src/instance.ts:106](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L106)

Encode unary operator and argument sort into a single integer key.

## Parameters

### op

[`UnaryOp`](../../ast/type-aliases/UnaryOp)

The unary operator.

### sort

`"num"` \| `"set"` \| `"bool"` \| `"func"` \| `"record"`

The argument sort.

## Returns

`number`

The packed dispatch key, or `0` if either id is unknown.
