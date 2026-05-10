# Function: delayFn()

> **delayFn**\<`D`, `A`\>(`originalMethod`, `delayMs`): [`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

Defined in: [delay/delay.fn.ts:45](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/delay/delay.fn.ts#L45)

Wraps a method to delay its execution by the specified time.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to delay

### delayMs

`number`

The delay time in milliseconds

## Returns

[`Method`](../../../types/type-aliases/Method)\<`void`, `A`\>

The delayed method

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
