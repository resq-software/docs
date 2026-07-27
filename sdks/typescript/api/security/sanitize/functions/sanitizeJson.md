# Function: sanitizeJson()

&gt; **sanitizeJson**(`jsonString`): `unknown`

Defined in: [sanitize.ts:574](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L574)

Sanitizes and safely parses a JSON string, removing suspicious syntax elements that could
potentially result in JSON polyglot exploits or prototype pollution.

The result is returned as `unknown` — this function performs **no** schema
validation, so it cannot honestly promise any concrete shape for
attacker-controlled input. Narrow the result yourself, or prefer
[parseJsonWithSchema](./parseJsonWithSchema), which validates against an Effect Schema and
returns a typed `Option`.

## Parameters

### jsonString

`string`

The JSON string to sanitize and parse.

## Returns

`unknown`

The parsed value (as `unknown`) if valid, or `null` if invalid.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const obj = sanitizeJson('{"foo":"bar"}');
// obj: unknown — narrow before use, or use parseJsonWithSchema
```
