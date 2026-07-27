# Function: lookupBinary()

&gt; **lookupBinary**(`key`): `BinaryImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:358](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L358)

Look up a binary operator implementation.

## Parameters

### key

`number`

A key from [encodeBinary](./encodeBinary).

## Returns

`BinaryImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
