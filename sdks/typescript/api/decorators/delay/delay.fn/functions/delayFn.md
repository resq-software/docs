# Function: delayFn()

&gt; **delayFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [delay/delay.fn.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/delay/delay.fn.ts#L59)

Wraps a method to delay its execution by the specified time.

Effectful: each call schedules an **independent** `setTimeout` — unlike
debounceFn there is no dedup or timer reset, so N calls produce N
deferred executions. The wrapper returns `undefined` immediately; the original
method's return value is **discarded**, so it cannot wrap a method whose
result the caller needs. A throw from the method surfaces inside the timer
callback, not to the caller. No `AbortSignal` / cancellation.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to delay.

### delayMs

`number`

The delay time in milliseconds.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The delayed wrapper; it always returns `undefined` (`void`), never
  the wrapped method's value.

## Example

```typescript
class MessageService {
  send(message: string): void {
    console.log(`Sending: ${message}`);
  }
}

const service = new MessageService();
const delayedSend = delayFn(
  service.send.bind(service),
  2000
);

delayedSend('Hello'); // "Sending: Hello" appears after 2 seconds
```
