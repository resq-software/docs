# Function: registerBinary()

&gt; **registerBinary**(`key`, `impl`): `void`

Defined in: [packages/math/src/instance.ts:409](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L409)

Register a custom binary operator instance.

Mutates the process-wide binary dispatch table, so every subsequent
[evaluate](../../evaluate) sees the change; registering an existing key (including a
built-in like `"+:num:num"`) overwrites its instance. Not a pure function.

## Parameters

### key

`string`

An `"op:leftSort:rightSort"` string (e.g. `"+:num:num"`).

### impl

`BinaryImpl`

The implementation to invoke for that operator and sort pair.

## Returns

`void`

## Throws

If the key is malformed or names an unknown operator or sort.
