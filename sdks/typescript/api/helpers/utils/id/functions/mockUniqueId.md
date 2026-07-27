# Function: mockUniqueId()

&gt; **mockUniqueId**(`fn`): `void`

Defined in: [packages/helpers/src/utils/id.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/id.ts#L95)

**`Internal`**

Mock the unique ID generator with a custom implementation for testing.

Replaces the internal ID generation function with a custom one. This is useful
for testing scenarios where you need predictable or deterministic IDs.

Mutates module-global generator state: every subsequent [uniqueId](./uniqueId) call
process-wide routes through `fn` until [restoreUniqueId](./restoreUniqueId) is called. Not
scoped or nestable — a second `mockUniqueId` simply overwrites the first, so
restore in a test teardown to avoid leaking the mock into other tests.

## Parameters

### fn

(`size?`) =&gt; `string`

The mock function that should return a string ID. Takes optional size parameter.

## Returns

`void`

## Example

```ts
// Mock with predictable IDs for testing
mockUniqueId((size = 21) => 'test-id-' + size)
console.log(uniqueId()) // 'test-id-21'
console.log(uniqueId(10)) // 'test-id-10'

// Restore original implementation when done
restoreUniqueId()
```
