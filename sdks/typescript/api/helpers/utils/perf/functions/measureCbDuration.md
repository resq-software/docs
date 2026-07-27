# Function: measureCbDuration()

&gt; **measureCbDuration**\<`T`\>(`name`, `cb`): `T`

Defined in: [packages/helpers/src/utils/perf.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/perf.ts#L71)

**`Internal`**

Measures and logs the execution time of a callback function.
Executes the provided callback and logs the duration to the console with styled output.

Side effect: writes one styled line to the console (`console.debug`) on every
call. Timing is synchronous wall-clock (`performance.now()`); if `cb` returns a
promise the measured span covers only the synchronous portion, not the awaited
work. Any error thrown by `cb` propagates and no line is logged.

## Type Parameters

### T

`T`

## Parameters

### name

`string`

Descriptive name for the operation being measured

### cb

() =&gt; `T`

Callback function to execute and measure

## Returns

`T`

The return value of the callback function

## Example

```ts
const result = measureCbDuration('data processing', () => {
  return processLargeDataSet(data)
})
// Console output: "Perf data processing took 42.5ms"
```
