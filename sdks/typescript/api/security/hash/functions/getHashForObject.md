# Function: getHashForObject()

&gt; **getHashForObject**(`obj`): `string`

Defined in: [hash.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/hash.ts#L63)

Hash an arbitrary value by serializing it to JSON and hashing the result.

Key ordering follows `JSON.stringify`, so two structurally equal objects with
differently ordered keys can hash differently.

## Parameters

### obj

`unknown`

Any JSON-serializable value.

## Returns

`string`

The 32-bit hash of the serialized form, as a decimal string.

## Throws

When `obj` cannot be serialized: a circular
  reference or a `BigInt` makes `JSON.stringify` throw, and a value
  that stringifies to `undefined` (a bare function, `symbol`, or
  `undefined`) makes the downstream `.length` access throw.
