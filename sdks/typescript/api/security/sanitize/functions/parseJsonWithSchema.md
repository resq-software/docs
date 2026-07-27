# Function: parseJsonWithSchema()

&gt; **parseJsonWithSchema**\<`A`\>(`jsonString`, `schema`): `Option`\<`A`\>

Defined in: [sanitize.ts:529](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L529)

Safely parses JSON with Effect Schema validation and prototype pollution protection.

Never throws: malformed JSON, a non-string argument, and schema-validation
failure all resolve to Option.none rather than a thrown error, so the
failure channel is the `Option` itself. As a side effect the parsed value is
stripped of prototype-pollution keys in place before validation (the value is
freshly created by `JSON.parse`, so no caller state is mutated).

## Type Parameters

### A

`A`

The decoded value type the `schema` produces on success; the
  returned `Option` carries this type.

## Parameters

### jsonString

`string`

The JSON string to parse.

### schema

`SyncSchema`\<`A`\>

Effect Schema to validate against; its decode must require no
  services (SyncSchema) so parsing stays synchronous.

## Returns

`Option`\<`A`\>

Option.some with the parsed, validated value, or
  Option.none on any parse or validation failure.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const UserSchema = S.Struct({ name: S.String, age: S.Number });
const result = parseJsonWithSchema('{"name":"John","age":30}', UserSchema);
// Option.some({ name: 'John', age: 30 })
```
