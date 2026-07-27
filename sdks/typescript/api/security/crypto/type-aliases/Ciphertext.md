# Type Alias: Ciphertext

&gt; **Ciphertext** = `Brand`\<`string`, `"Ciphertext"`\>

Defined in: [crypto.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L60)

Base64 AES-256-GCM payload produced by [encryptData](../functions/encryptData) — the
`salt | iv | authTag | ciphertext` envelope. Only [decryptData](../functions/decryptData)
should consume a value of this type; read one back from storage through
[toCiphertext](../variables/toCiphertext).
