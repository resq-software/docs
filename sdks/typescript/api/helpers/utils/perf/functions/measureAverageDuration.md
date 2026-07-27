# Function: measureAverageDuration()

&gt; **measureAverageDuration**(`_target`, `propertyKey`, `descriptor`): `PropertyDescriptor`

Defined in: [packages/helpers/src/utils/perf.ts:173](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/perf.ts#L173)

**`Internal`**

Decorator that measures method execution time and tracks running averages.
Wraps the decorated method to log both current execution time and running average.
Maintains a running total and count for each decorated method to calculate averages.

Effects: mutates `descriptor` in place and keeps per-method totals in a
module-global `Map` keyed by the wrapper function — so the running average
accumulates for the lifetime of the process and is never reset. Invocations
whose measured duration rounds to exactly `0`ms are skipped (neither logged nor
counted). Logs one `console.debug` line per counted invocation.

## Parameters

### \_target

`unknown`

The class prototype (unused)

### propertyKey

`string`

Name of the method being decorated

### descriptor

`PropertyDescriptor`

Property descriptor of the method (mutated in place)

## Returns

`PropertyDescriptor`

The same `descriptor`, with its `value` wrapped for timing and averaging

## Example

```ts
class RenderEngine {
  @measureAverageDuration
  renderFrame() {
    // Rendering logic here
  }
}
// After multiple calls, logs: "Perf renderFrame took 16.67ms | average 15.83ms"
```
