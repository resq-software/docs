# Function: normalizeUnicode()

> **normalizeUnicode**(`input`): `string`

Defined in: [validators.ts:422](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/validators.ts#L422)

Normalizes Unicode to prevent homoglyph attacks
Converts to NFC form and replaces common lookalikes with ASCII

## Parameters

### input

`string`

## Returns

`string`
