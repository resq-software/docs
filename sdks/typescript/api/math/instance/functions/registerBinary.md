# Function: registerBinary()

&gt; **registerBinary**(`key`, `impl`): `void`

Defined in: [packages/math/src/instance.ts:409](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L409)

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
