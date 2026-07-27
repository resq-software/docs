# Function: decryptData()

&gt; **decryptData**(`encryptedData`, `encryptionKey`): `Promise`\<`string`\>

Defined in: [crypto.ts:216](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L216)

Reverse [encryptData](./encryptData). Verifies the GCM authentication tag
before returning plaintext — tampered ciphertexts throw.

## Parameters

### encryptedData

`Brand`

Base64 string produced by [encryptData](./encryptData).

### encryptionKey

`Brand`

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
  security event, not a recoverable error. The rejection comes back
  as a rejected `Promise`. No `AbortSignal` is honoured; concurrent
  calls are independent and share no state.

## Example

```ts
const plaintext = await decryptData(stored, process.env.PII_KEY!);
```
