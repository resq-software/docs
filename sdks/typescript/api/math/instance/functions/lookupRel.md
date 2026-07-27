# Function: lookupRel()

&gt; **lookupRel**(`key`): `RelImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:366](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L366)

Look up a relational operator implementation.

## Parameters

### key

`number`

A key from [encodeRel](./encodeRel).

## Returns

`RelImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
