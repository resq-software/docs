# Function: decryptData()

> **decryptData**(`encryptedData`, `encryptionKey`): `Promise`\<`string`\>

Defined in: [crypto.ts:123](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L123)

Reverse [encryptData](./encryptData). Verifies the GCM authentication tag
before returning plaintext — tampered ciphertexts throw.

## Parameters

### encryptedData

`string`

Base64 string produced by [encryptData](./encryptData).

### encryptionKey

`string`

Same key/password used to encrypt. Wrong keys
  throw an "Unsupported state or unable to authenticate data" error
  from Node — the authenticated tag failure is indistinguishable from
  tampering, by design.

## Returns

`Promise`\<`string`\>

The original UTF-8 plaintext.

## Throws

Error if the tag does not verify (wrong key, modified
  ciphertext, truncated payload). Catch this and treat it as a
  security event, not a recoverable error.

## Example

```ts
const plaintext = await decryptData(stored, process.env.PII_KEY!);
```
