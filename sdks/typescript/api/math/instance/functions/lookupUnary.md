# Function: lookupUnary()

&gt; **lookupUnary**(`key`): `UnaryImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:350](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L350)

Look up a unary operator implementation.

## Parameters

### key

`number`

A key from [encodeUnary](./encodeUnary).

## Returns

`UnaryImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
