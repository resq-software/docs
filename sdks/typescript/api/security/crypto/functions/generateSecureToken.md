# Function: generateSecureToken()

> **generateSecureToken**(`length?`): `string`

Defined in: [crypto.ts:180](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L180)

Generate a cryptographically random hex token suitable for session
IDs, password-reset tokens, CSRF tokens, and similar single-use
secrets.

## Parameters

### length?

`number` = `32`

Number of random *bytes* to draw (the returned hex
  string is twice as long). Default `32` ⇒ 64-char hex / 256 bits of
  entropy.

## Returns

`string`

Lowercase hex string of length `length * 2`.

## Example

```ts
generateSecureToken();    // 64-char hex (256-bit entropy)
generateSecureToken(16);  // 32-char hex (128-bit entropy)
```
