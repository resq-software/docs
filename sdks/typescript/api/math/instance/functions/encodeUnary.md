# Function: encodeUnary()

&gt; **encodeUnary**(`op`, `sort`): `number`

Defined in: [packages/math/src/instance.ts:106](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L106)

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
