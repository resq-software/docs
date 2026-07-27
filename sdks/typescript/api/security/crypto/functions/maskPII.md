# Function: maskPII()

&gt; **maskPII**(`data`): `Brand`

Defined in: [crypto.ts:296](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L296)

Mask an arbitrary PII string for safe logging — keeps the first two
and last two characters and replaces everything in between with
asterisks. Strings of length ≤ 4 are fully masked as `"****"`.

## Parameters

### data

`string`

Raw PII string.

## Returns

`Brand`

Masked representation safe for logs.

## Example

```ts
maskPII("4242424242424242"); // → "42************42"
maskPII("AB12");              // → "****"
```
