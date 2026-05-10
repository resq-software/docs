# Function: encryptData()

> **encryptData**(`plaintext`, `encryptionKey`): `Promise`\<`string`\>

Defined in: [crypto.ts:60](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/crypto.ts#L60)

Encrypts sensitive data using AES-256-GCM

## Parameters

### plaintext

`string`

Data to encrypt

### encryptionKey

`string`

Encryption key/password

## Returns

`Promise`\<`string`\>

Base64-encoded encrypted data (salt:iv:authTag:ciphertext)

## Compliance

NIST 800-53 SC-28 (Protection of Information at Rest)
