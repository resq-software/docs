# Function: execTimeFn()

## Call Signature

&gt; **execTimeFn**\<`D`, `A`\>(`originalMethod`, `arg?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [exec-time/exec-time.fn.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.fn.ts#L93)

Wraps a method to measure and report its execution time.
Handles both synchronous and asynchronous methods.

Effectful only through timing and reporting: it reads the clock (`Date.now`)
and invokes the reporter (which logs or records metrics); it does not touch the
arguments or the return value. Timing preserves async-ness — a sync method is
measured and reported synchronously, a promise-returning method is measured
until it resolves and the resolved value is forwarded unchanged. Because the
async path attaches only a fulfillment handler, a **rejected** method is *not*
reported and the rejection propagates untouched. When `arg` is a string that
names a method on the receiver, that method is used as the reporter (bound to
the instance); otherwise the string is a label prefix on the default logger,
and a detached call (`this` nullish) falls back to that label logger. Each call
is independent; concurrent calls are safe.

### Type Parameters

#### D

`D`

The return type of the original method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The method to wrap.

#### arg?

`string` \| [`ReportFunction`](../../exec-time.types/type-aliases/ReportFunction)

Optional reporter function or label.

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The wrapped method. Preserves the original return value and stays
  synchronous for synchronous methods — it only awaits when the wrapped method
  itself returns a promise.

### Example

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

## Call Signature

&gt; **execTimeFn**\<`D`, `A`\>(`originalMethod`, `arg?`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [exec-time/exec-time.fn.ts:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.fn.ts#L97)

Wraps a method to measure and report its execution time.
Handles both synchronous and asynchronous methods.

Effectful only through timing and reporting: it reads the clock (`Date.now`)
and invokes the reporter (which logs or records metrics); it does not touch the
arguments or the return value. Timing preserves async-ness — a sync method is
measured and reported synchronously, a promise-returning method is measured
until it resolves and the resolved value is forwarded unchanged. Because the
async path attaches only a fulfillment handler, a **rejected** method is *not*
reported and the rejection propagates untouched. When `arg` is a string that
names a method on the receiver, that method is used as the reporter (bound to
the instance); otherwise the string is a label prefix on the default logger,
and a detached call (`this` nullish) falls back to that label logger. Each call
is independent; concurrent calls are safe.

### Type Parameters

#### D

`D`

The return type of the original method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method.

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to wrap.

#### arg?

`string` \| [`ReportFunction`](../../exec-time.types/type-aliases/ReportFunction)

Optional reporter function or label.

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The wrapped method. Preserves the original return value and stays
  synchronous for synchronous methods — it only awaits when the wrapped method
  itself returns a promise.

### Example

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
