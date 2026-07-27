# Class: ThrottleAsyncExecutor\<D\>

Defined in: [throttle-async/throttle-async-executor.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle-async/throttle-async-executor.ts#L56)

Manages the queue and execution of throttled async calls, ensuring at most a
fixed number run concurrently and queuing the rest until a slot frees up.

Queued calls dispatch in FIFO order; each slot is released once its call settles
(resolve or reject), which drives the next dispatch. `parallelCalls` must be
`>= 1` — the constructor does not validate it, and a value below `1` leaves
`tryCall` unable to ever dispatch, so every queued call hangs.

## Example

```ts
const executor = new ThrottleAsyncExecutor(
  async (data) => await fetchData(data),
  3, // At most three concurrent calls.
);

// Execute multiple calls.
const promises = [
  executor.exec(this, ["arg1"]),
  executor.exec(this, ["arg2"]),
  executor.exec(this, ["arg3"]),
  executor.exec(this, ["arg4"]), // Queued.
  executor.exec(this, ["arg5"]), // Queued.
];

const results = await Promise.all(promises);
```

## Type Parameters

### D

`D`

The resolved type of the async method.

## Constructors

### Constructor

&gt; **new ThrottleAsyncExecutor**\<`D`\>(`fun`, `parallelCalls`): `ThrottleAsyncExecutor`\<`D`\>

Defined in: [throttle-async/throttle-async-executor.ts:69](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle-async/throttle-async-executor.ts#L69)

Create a new executor.

#### Parameters

##### fun

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>

The async method to throttle.

##### parallelCalls

`number`

Maximum number of concurrent calls allowed.

#### Returns

`ThrottleAsyncExecutor`\<`D`\>

## Methods

### exec()

&gt; **exec**(`context`, `args`): `Promise`\<`D`\>

Defined in: [throttle-async/throttle-async-executor.ts:93](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle-async/throttle-async-executor.ts#L93)

Queue a method call, executing it immediately if a slot is free or deferring
it until one opens.

Appends to the internal queue and may synchronously start the call; queued
calls preserve FIFO order. The returned promise mirrors the method outcome —
a thrown/rejected method rejects it with the same reason.

#### Parameters

##### context

`unknown`

The `this` context for the method call.

##### args

`unknown`[]

The arguments to pass to the method.

#### Returns

`Promise`\<`D`\>

A promise that resolves (or rejects) with the method's result.

#### Example

```ts
const executor = new ThrottleAsyncExecutor(myAsyncMethod, 2);

// Queue a call.
const result = await executor.exec(this, ["arg1", "arg2"]);
```
