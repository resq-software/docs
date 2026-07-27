# Function: restoreUniqueId()

&gt; **restoreUniqueId**(): `void`

Defined in: [packages/helpers/src/utils/id.ts:119](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/id.ts#L119)

**`Internal`**

Restore the original unique ID generator after mocking.

Resets the ID generation function back to the original nanoid implementation.
This should be called after testing to restore normal ID generation behavior.

Mutates module-global generator state, undoing any [mockUniqueId](./mockUniqueId). Safe
to call when no mock is active — it just reasserts the default generator.

## Returns

`void`

## Example

```ts
// After mocking for tests
mockUniqueId(() => 'mock-id')

// Restore original behavior
restoreUniqueId()
console.log(uniqueId()) // Now generates real random IDs again
```
