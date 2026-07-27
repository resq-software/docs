# Function: registerUnary()

&gt; **registerUnary**(`key`, `impl`): `void`

Defined in: [packages/math/src/instance.ts:389](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/instance.ts#L389)

Register a custom unary operator instance.

Mutates the process-wide unary dispatch table, so every subsequent
[evaluate](../../evaluate) sees the change; registering an existing key (including a
built-in like `"neg:num"`) overwrites its instance. Not a pure function.

## Parameters

### key

`string`

A `"op:sort"` string (e.g. `"neg:num"`).

### impl

`UnaryImpl`

The implementation to invoke for that operator and sort.

## Returns

`void`

## Throws

If the key is malformed or names an unknown operator or sort.
