# Function: registerLogic()

&gt; **registerLogic**(`key`, `impl`): `void`

Defined in: [packages/math/src/instance.ts:453](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L453)

Register a custom logic operator instance.

Mutates the process-wide logic dispatch table, so every subsequent
[evaluate](../../evaluate) sees the change; registering an existing key (including a
built-in like `"∧:bool:bool"`) overwrites its instance. Not a pure function.

## Parameters

### key

`string`

An `"op:leftSort:rightSort"` string (e.g. `"∧:bool:bool"`).

### impl

`LogicImpl`

The implementation to invoke for that operator and sort pair.

## Returns

`void`

## Throws

If the key is malformed or names an unknown operator or sort.
