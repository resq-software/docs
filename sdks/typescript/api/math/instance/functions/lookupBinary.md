# Function: lookupBinary()

&gt; **lookupBinary**(`key`): `BinaryImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:358](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L358)

Look up a binary operator implementation.

## Parameters

### key

`number`

A key from [encodeBinary](./encodeBinary).

## Returns

`BinaryImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
