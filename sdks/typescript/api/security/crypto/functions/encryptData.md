# Function: encryptData()

&gt; **encryptData**(`plaintext`, `encryptionKey`): `Promise`\<`Brand`\<`string`, `"Ciphertext"`\>\>

Defined in: [crypto.ts:177](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L177)

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

`Brand`

Caller-supplied secret. Treated as a password
  and stretched into a 256-bit AES key via scrypt; can be any length,
  though a high-entropy secret (≥ 32 bytes) is strongly preferred.

## Returns

`Promise`\<`Brand`\<`string`, `"Ciphertext"`\>\>

A self-contained base64 string. Store or transmit verbatim;
  the salt/IV are recovered on decryption.

## Throws

From the underlying Node crypto primitives if `encryptionKey`
  is empty or scrypt fails. Failure surfaces as a rejected `Promise`,
  never a resolved error value.

Draws from the platform CSPRNG (`randomBytes`) each call, so it is not
a pure function and its output is non-deterministic. There is no
`AbortSignal` hook — once awaited the scrypt work runs to completion.
Independent calls share no state and are safe to run concurrently.

## Compliance

NIST 800-53 SC-28 (Protection of Information at Rest),
  SC-13 (Cryptographic Protection).

## Example

```ts
const ct = await encryptData("user@example.com", process.env.PII_KEY!);
await db.users.update(id, { email: ct });
```
