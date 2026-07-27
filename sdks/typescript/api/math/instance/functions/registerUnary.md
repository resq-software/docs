# Function: registerUnary()

&gt; **registerUnary**(`key`, `impl`): `void`

Defined in: [packages/math/src/instance.ts:389](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/instance.ts#L389)

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
