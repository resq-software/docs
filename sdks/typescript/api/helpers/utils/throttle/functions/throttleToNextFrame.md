# Function: throttleToNextFrame()

&gt; **throttleToNextFrame**(`fn`): () =&gt; `void`

Defined in: [packages/helpers/src/utils/throttle.ts:271](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L271)

**`Internal`**

Schedules a function to execute on the next animation frame, targeting 120fps.
If the same function is passed multiple times before the frame executes,
it will only be called once, effectively batching multiple calls.

Uses the default throttle instance for UI operations.

Delegates to a shared module-level [FpsScheduler](../classes/FpsScheduler) (120fps). In a test
environment `fn` runs synchronously and the returned cancel is a no-op — see
[FpsScheduler.throttleToNextFrame](../classes/FpsScheduler#throttletonextframe).

## Parameters

### fn

() =&gt; `void`

The function to execute on the next frame

## Returns

A cancel function that can prevent execution if called before the next frame

() =&gt; `void`

## Example

```ts
const updateUI = throttleToNextFrame(() => {
  // Batches multiple calls into the next animation frame
  updateStatusBar()
  refreshToolbar()
})

// Multiple calls within the same frame are batched
updateUI() // Will execute
updateUI() // Ignored (same function already queued)
updateUI() // Ignored (same function already queued)

// Get cancel function to prevent execution
const cancel = updateUI()
cancel() // Prevents execution if called before next frame
```
