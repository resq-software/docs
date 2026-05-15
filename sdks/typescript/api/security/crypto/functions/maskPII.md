# Function: maskPII()

> **maskPII**(`data`): `string`

Defined in: [crypto.ts:198](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L198)

Mask an arbitrary PII string for safe logging — keeps the first two
and last two characters and replaces everything in between with
asterisks. Strings of length ≤ 4 are fully masked as `"****"`.

## Parameters

### data

`string`

Raw PII string.

## Returns

`string`

Masked representation safe for logs.

## Example

```ts
maskPII("4242424242424242"); // → "42************42"
maskPII("AB12");              // → "****"
```
