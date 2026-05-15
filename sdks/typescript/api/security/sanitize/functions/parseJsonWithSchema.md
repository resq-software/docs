# Function: parseJsonWithSchema()

> **parseJsonWithSchema**\<`A`\>(`jsonString`, `schema`): `Option`\<`A`\>

Defined in: [sanitize.ts:340](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L340)

Safely parses JSON with Effect Schema validation and prototype pollution protection.

## Type Parameters

### A

`A`

The expected schema type

## Parameters

### jsonString

`string`

The JSON string to parse.

### schema

`SyncSchema`\<`A`\>

Effect Schema to validate against.

## Returns

`Option`\<`A`\>

Option containing the parsed and validated object.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const UserSchema = S.Struct({ name: S.String, age: S.Number });
const result = parseJsonWithSchema('{"name":"John","age":30}', UserSchema);
// Option.some({ name: 'John', age: 30 })
```
