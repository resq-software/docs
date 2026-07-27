# Function: getHashForString()

&gt; **getHashForString**(`string`): `string`

Defined in: [hash.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/hash.ts#L41)

Compute a deterministic non-cryptographic 32-bit hash of a string.

Uses the classic `hash * 31 + charCode` accumulation (expressed as
`(hash << 5) - hash`), yielding the same value for the same input across runs.
Intended for cache keys and change detection, not for security.

## Parameters

### string

`string`

The input to hash.

## Returns

`string`

The signed 32-bit hash rendered as a decimal string.

## Example

```ts
getHashForString("hello") === getHashForString("hello"); // → true
```
