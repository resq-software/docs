# Function: lookupUnary()

&gt; **lookupUnary**(`key`): `UnaryImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:350](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L350)

Look up a unary operator implementation.

## Parameters

### key

`number`

A key from [encodeUnary](./encodeUnary).

## Returns

`UnaryImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
