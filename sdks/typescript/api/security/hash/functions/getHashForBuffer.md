# Function: getHashForBuffer()

&gt; **getHashForBuffer**(`buffer`): `string`

Defined in: [hash.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/hash.ts#L75)

Compute a deterministic non-cryptographic 32-bit hash of an `ArrayBuffer`.

Applies the same accumulation as [getHashForString](./getHashForString) over each byte.

## Parameters

### buffer

`ArrayBuffer`

The bytes to hash.

## Returns

`string`

The signed 32-bit hash rendered as a decimal string.
