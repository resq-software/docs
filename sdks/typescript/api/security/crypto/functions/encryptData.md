# Function: encryptData()

> **encryptData**(`plaintext`, `encryptionKey`): `Promise`\<`string`\>

Defined in: [crypto.ts:89](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L89)

Encrypt a UTF-8 string with AES-256-GCM authenticated encryption.

Each call generates a fresh random salt and IV — the same plaintext
encrypted twice with the same `encryptionKey` produces different
ciphertexts, which is the property you want for at-rest encryption.

Output layout (base64-encoded): `salt(32) | iv(16) | authTag(16) | ciphertext(*)`.
The companion [decryptData](./decryptData) understands this layout.

## Parameters

### plaintext

`string`

UTF-8 string to encrypt.

### encryptionKey

`string`

Caller-supplied secret. Treated as a password
  and stretched into a 256-bit AES key via scrypt; can be any length,
  though a high-entropy secret (≥ 32 bytes) is strongly preferred.

## Returns

`Promise`\<`string`\>

A self-contained base64 string. Store or transmit verbatim;
  the salt/IV are recovered on decryption.

## Throws

From the underlying Node crypto primitives if `encryptionKey`
  is empty or scrypt fails.

## Compliance

NIST 800-53 SC-28 (Protection of Information at Rest),
  SC-13 (Cryptographic Protection).

## Example

```ts
const ct = await encryptData("user@example.com", process.env.PII_KEY!);
await db.users.update(id, { email: ct });
```
