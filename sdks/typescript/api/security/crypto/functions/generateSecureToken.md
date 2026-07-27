# Function: generateSecureToken()

&gt; **generateSecureToken**(`length?`): `Brand`

Defined in: [crypto.ts:278](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L278)

Generate a cryptographically random hex token suitable for session
IDs, password-reset tokens, CSRF tokens, and similar single-use
secrets.

## Parameters

### length?

`PositiveInt` = `...`

Number of random *bytes* to draw as a PositiveInt
  (the returned hex string is twice as long). Default `32` ⇒ 64-char hex
  / 256 bits of entropy. Construct non-default lengths with `toPositiveInt`
  so zero-byte and negative lengths are unrepresentable.

## Returns

`Brand`

A [SecureToken](../type-aliases/SecureToken): lowercase hex string of length `length * 2`.

## Example

```ts
import { toPositiveInt } from "@resq-systems/types";
generateSecureToken();                 // 64-char hex (256-bit entropy)
generateSecureToken(toPositiveInt(16)); // 32-char hex (128-bit entropy)
```
