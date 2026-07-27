# Function: throttleAsync()

&gt; **throttleAsync**\<`T`\>(`parallelCalls?`): [`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

Defined in: [throttle-async/throttle-async.ts:64](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle-async/throttle-async.ts#L64)

Limit an async method to `parallelCalls` concurrent executions; excess calls
queue and run in FIFO order as slots free up.

The queue/executor is created once, at decoration time, so the concurrency limit
spans every instance of the class, not each instance separately. A call's promise
settles with its own method result — a rejection rejects only that promise and
frees its slot so the queue keeps draining. The queue is unbounded and there is
no cancellation (`AbortSignal` is not honoured). `parallelCalls` must be at least
`1`; a value below `1` never dispatches and calls queue forever. Mutates the
supplied property descriptor in place.

## Type Parameters

### T

`T` = `unknown`

The class type that owns the decorated method.

## Parameters

### parallelCalls?

`number`

Maximum number of concurrent calls; defaults to `1`. Must
be `>= 1`.

## Returns

[`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

The async method decorator.

## Throws

If applied to a member without a `value` descriptor (an accessor
or plain property rather than a method).

## Example

```ts
class BatchProcessor {
  // Process up to five items concurrently.
  @throttleAsync(5)
  async processItem(item: Item): Promise<Result> {
    return await this.performHeavyProcessing(item);
  }
}

const processor = new BatchProcessor();
const items = Array.from({ length: 100 }, (_, i) => ({ id: i }));

// Process 100 items, five at a time.
const results = await Promise.all(items.map((item) => processor.processItem(item)));
```

## See

[throttleAsyncFn](../../throttle-async.fn/functions/throttleAsyncFn) for the function form.
