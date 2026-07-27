# Function: encodeLogic()

&gt; **encodeLogic**(`op`, `sortL`, `sortR`): `number`

Defined in: [packages/math/src/instance.ts:153](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L153)

Encode logical operator and left/right sorts into a single integer key.

## Parameters

### op

[`LogicOp`](../../ast/type-aliases/LogicOp)

The logical operator.

### sortL

`"num"` \| `"set"` \| `"bool"` \| `"func"` \| `"record"`

The left operand sort.

### sortR

`"num"` \| `"set"` \| `"bool"` \| `"func"` \| `"record"`

The right operand sort.

## Returns

`number`

The packed dispatch key, or `0` if any id is unknown.
