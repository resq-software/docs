# Function: uniqueId()

&gt; **uniqueId**(`size?`): `string`

Defined in: [packages/helpers/src/utils/id.ts:152](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/id.ts#L152)

Generate a unique ID using a modified nanoid algorithm.

Generates a cryptographically secure random string ID using URL-safe characters.
The default size is 21 characters, which provides a good balance of uniqueness
and brevity. Uses the global crypto API for secure random number generation.

Draws from a shared, lazily-refilled random pool (module state), so output is
non-deterministic — the values shown below are illustrative, not reproducible.
Under a [mockUniqueId](./mockUniqueId) override this delegates to the mock instead.

## Parameters

### size?

`number`

Optional length of the generated ID (defaults to 21 characters)

## Returns

`string`

A unique string identifier

## Example

```ts
// Generate default 21-character ID
const id = uniqueId()
console.log(id) // e.g. 'V1StGXR8_Z5jdHi6B-myT'

// Generate shorter ID
const shortId = uniqueId(10)
console.log(shortId) // e.g. 'V1StGXR8_Z'

// Generate longer ID
const longId = uniqueId(32)
console.log(longId) // e.g. 'V1StGXR8_Z5jdHi6B-myTVKahvjdx...'
```
