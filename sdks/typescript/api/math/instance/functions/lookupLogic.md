# Function: lookupLogic()

&gt; **lookupLogic**(`key`): `LogicImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:374](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L374)

Look up a logic operator implementation.

## Parameters

### key

`number`

A key from [encodeLogic](./encodeLogic).

## Returns

`LogicImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
