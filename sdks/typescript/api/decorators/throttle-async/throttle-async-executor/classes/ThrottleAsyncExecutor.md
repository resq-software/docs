# Class: ThrottleAsyncExecutor\<D\>

Defined in: [throttle-async/throttle-async-executor.ts:47](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/throttle-async/throttle-async-executor.ts#L47)

Manages the queue and execution of throttled async method calls.
Ensures that only a specified number of calls run concurrently,
queueing additional calls until slots become available.

 ThrottleAsyncExecutor

## Example

```typescript
const executor = new ThrottleAsyncExecutor(
  async (data) => await fetchData(data),
  3 // Max 3 concurrent calls
);

// Execute multiple calls
const promises = [
  executor.exec(this, ['arg1']),
  executor.exec(this, ['arg2']),
  executor.exec(this, ['arg3']),
  executor.exec(this, ['arg4']), // Queued
  executor.exec(this, ['arg5']), // Queued
];

const results = await Promise.all(promises);
```

## Type Parameters

### D

`D`

The resolved type of the async method

## Constructors

### Constructor

> **new ThrottleAsyncExecutor**\<`D`\>(`fun`, `parallelCalls`): `ThrottleAsyncExecutor`\<`D`\>

Defined in: [throttle-async/throttle-async-executor.ts:68](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/throttle-async/throttle-async-executor.ts#L68)

Creates a new ThrottleAsyncExecutor instance.

#### Parameters

##### fun

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>

The async method to throttle

##### parallelCalls

`number`

Maximum number of concurrent calls allowed

#### Returns

`ThrottleAsyncExecutor`\<`D`\>

## Methods

### exec()

> **exec**(`context`, `args`): `Promise`\<`D`\>

Defined in: [throttle-async/throttle-async-executor.ts:88](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/throttle-async/throttle-async-executor.ts#L88)

Queues a method call for execution.

#### Parameters

##### context

`unknown`

The `this` context for the method call

##### args

`unknown`[]

The arguments to pass to the method

#### Returns

`Promise`\<`D`\>

A promise that resolves with the method result

#### Example

```typescript
const executor = new ThrottleAsyncExecutor(myAsyncMethod, 2);

// Queue a call
const result = await executor.exec(this, ['arg1', 'arg2']);
```
