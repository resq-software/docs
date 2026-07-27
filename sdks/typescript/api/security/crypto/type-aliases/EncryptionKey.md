# Type Alias: EncryptionKey

&gt; **EncryptionKey** = `Brand`\<`string`, `"EncryptionKey"`\>

Defined in: [crypto.ts:67](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L67)

A secret accepted by [encryptData](../functions/encryptData)/[decryptData](../functions/decryptData) as the
scrypt password. Mint one at the boundary where the secret enters the
process (typically from `process.env`) via [toEncryptionKey](../variables/toEncryptionKey).
