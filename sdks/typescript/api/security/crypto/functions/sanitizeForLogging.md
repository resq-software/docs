# Function: sanitizeForLogging()

> **sanitizeForLogging**\<`T`\>(`obj`, `sensitiveFields?`): `Partial`\<`T`\>

Defined in: [crypto.ts:138](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/crypto.ts#L138)

Sanitize object for logging (removes sensitive fields)

## Type Parameters

### T

`T` *extends* `Record`\<`string`, `unknown`\>

## Parameters

### obj

`T`

### sensitiveFields?

`string`[] = `...`

## Returns

`Partial`\<`T`\>
