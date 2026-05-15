# Function: hashData()

> **hashData**(`data`): `string`

Defined in: [crypto.ts:160](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L160)

Compute a SHA-256 digest of a UTF-8 string and return it as lowercase
hex.

**Not for password storage.** SHA-256 is fast by design — use a
deliberately slow KDF (`bcrypt`, `argon2`, or `scrypt`) for
password-equivalent material. This helper is intended for
non-reversible identifiers, content hashes, and idempotency keys.

## Parameters

### data

`string`

UTF-8 input.

## Returns

`string`

64-character lowercase hex digest.

## Example

```ts
hashData("hello"); // → "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```
