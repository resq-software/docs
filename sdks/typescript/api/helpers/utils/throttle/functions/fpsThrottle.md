# Function: fpsThrottle()

&gt; **fpsThrottle**(`fn`): \{(): `void`; `cancel?`: `void`; \}

Defined in: [packages/helpers/src/utils/throttle.ts:230](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/throttle.ts#L230)

**`Internal`**

Creates a throttled version of a function that executes at most once per frame.
The default target frame rate is 120fps, but can be customized per function.
Subsequent calls within the same frame are ignored, ensuring smooth performance
for high-frequency events like mouse movements or scroll events.

Uses the default throttle instance for UI operations. If you need a separate
throttling queue (e.g., for network operations), create your own Throttle instance.

Delegates to a shared module-level [FpsScheduler](../classes/FpsScheduler) (120fps), so every caller
of this function competes for the same frame queue. In a test environment it
returns `fn` unchanged (no throttling) — see [FpsScheduler.fpsThrottle](../classes/FpsScheduler#fpsthrottle).

## Parameters

### fn

\{(): `void`; `cancel?`: `void`; \}

The function to throttle, optionally with a cancel method

#### cancel?

## Returns

A throttled function with an optional cancel method to remove pending calls

\{(): `void`; `cancel?`: `void`; \}

### cancel()?

&gt; `optional` **cancel**(): `void`

#### Returns

`void`

## Example

```ts
// Default 120fps throttling
const updateCanvas = fpsThrottle(() => {
  // This will run at most once per frame (~8.33ms)
  redrawCanvas()
})

// Call as often as you want - automatically throttled to 120fps
document.addEventListener('mousemove', updateCanvas)

// Cancel pending calls if needed
updateCanvas.cancel?.()
```
