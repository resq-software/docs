# Function: execTimeFn()

> **execTimeFn**\<`D`, `A`\>(`originalMethod`, `arg?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`void`, `A`\>

Defined in: [exec-time/exec-time.fn.ts:73](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/exec-time/exec-time.fn.ts#L73)

Wraps a method to measure and report its execution time.
Handles both synchronous and asynchronous methods.

## Type Parameters

### D

`D` = `any`

The return type of the original method

### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\> \| [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The method to wrap

### arg?

`string` \| [`ReportFunction`](../../exec-time.types/type-aliases/ReportFunction)

Optional reporter function or label

## Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`void`, `A`\>

The wrapped method

## Example

```typescript
class Calculator {
  fibonacci(n: number): number {
    if (n <= 1) return n;
    return this.fibonacci(n - 1) + this.fibonacci(n - 2);
  }
}

const calc = new Calculator();

// Wrap with default reporter
const timed = execTimeFn(calc.fibonacci.bind(calc));
await timed(40); // Logs: "Execution time: 450ms"

// Wrap with custom label
const labeled = execTimeFn(
  calc.fibonacci.bind(calc),
  'Fibonacci calculation'
);
await labeled(40); // Logs: "Fibonacci calculation execution time: 450ms"

// Wrap with custom reporter
const custom = execTimeFn(
  calc.fibonacci.bind(calc),
  (data) => {
    console.log(`Took ${data.execTime}ms for n=${data.args[0]}`);
  }
);
await custom(40); // Logs: "Took 450ms for n=40"
```
