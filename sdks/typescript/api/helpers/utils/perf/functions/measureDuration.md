# Function: measureDuration()

&gt; **measureDuration**(`_target`, `propertyKey`, `descriptor`): `PropertyDescriptor`

Defined in: [packages/helpers/src/utils/perf.ts:122](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/perf.ts#L122)

**`Internal`**

Decorator that measures and logs the execution time of class methods.
Wraps the decorated method to automatically log its execution duration.

Effects: mutates `descriptor` in place (replaces `descriptor.value` with the
wrapper) and returns the same descriptor; the wrapper logs one `console.debug`
line per invocation. Only the synchronous return of the method is timed — an
`async` method's awaited work is not included.

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

The same `descriptor`, with its `value` wrapped for timing

## Example

```ts
class DataProcessor {
  @measureDuration
  processData(data: unknown[]) {
    return data.map(item => transform(item))
  }
}
// When processData is called, logs: "Perf processData took: 15.2ms"
```
