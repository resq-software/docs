# Function: lookupRel()

&gt; **lookupRel**(`key`): `RelImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:366](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L366)

Look up a relational operator implementation.

## Parameters

### key

`number`

A key from [encodeRel](./encodeRel).

## Returns

`RelImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
