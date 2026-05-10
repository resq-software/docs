# Function: sanitizeJson()

> **sanitizeJson**\<`T`\>(`jsonString`): `T`

Defined in: [sanitize.ts:387](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L387)

Sanitizes and safely parses a JSON string, removing suspicious syntax elements that could
potentially result in JSON polyglot exploits or prototype pollution.

## Type Parameters

### T

`T`

The expected type of the parsed object

## Parameters

### jsonString

`string`

The JSON string to sanitize and parse.

## Returns

`T`

The parsed JavaScript object if valid, or `null` if invalid.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const obj = sanitizeJson<{ foo: string }>('{"foo":"bar"}');
// obj = { foo: 'bar' }
```
