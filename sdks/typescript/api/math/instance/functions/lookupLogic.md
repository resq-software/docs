# Function: lookupLogic()

&gt; **lookupLogic**(`key`): `LogicImpl` \| `undefined`

Defined in: [packages/math/src/instance.ts:374](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L374)

Look up a logic operator implementation.

## Parameters

### key

`number`

A key from [encodeLogic](./encodeLogic).

## Returns

`LogicImpl` \| `undefined`

The implementation, or `undefined` when no instance is registered.
