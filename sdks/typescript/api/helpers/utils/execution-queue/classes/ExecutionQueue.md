# Class: ExecutionQueue

Defined in: [packages/helpers/src/utils/execution-queue.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/execution-queue.ts#L56)

**`Internal`**

A queue that executes tasks sequentially with optional delay between tasks.

ExecutionQueue ensures that tasks are executed one at a time in the order they were added,
with an optional timeout delay between each task execution. This is useful for rate limiting,
preventing race conditions, or controlling the flow of asynchronous operations.

## Example

```ts
// Create a queue with 100ms delay between tasks
const queue = new ExecutionQueue(100)

// Add tasks to the queue
const result1 = await queue.push(() => fetch('/api/data'))
const result2 = await queue.push(async () => {
  const data = await processData()
  return data
})

// Check if queue is empty
if (queue.isEmpty()) {
  console.log('All tasks completed')
}

// Clean up
queue.close()
```

## Constructors

### Constructor

&gt; **new ExecutionQueue**(`timeout?`): `ExecutionQueue`

Defined in: [packages/helpers/src/utils/execution-queue.ts:77](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/execution-queue.ts#L77)

Creates a new ExecutionQueue.

Creates a new execution queue that will process tasks sequentially.
If a timeout is provided, there will be a delay between each task execution,
which is useful for rate limiting or controlling execution flow.

#### Parameters

##### timeout?

`number`

Optional delay in milliseconds between task executions.

#### Returns

`ExecutionQueue`

#### Example

```ts
// Create queue without delay
const fastQueue = new ExecutionQueue()

// Create queue with 500ms delay between tasks
const slowQueue = new ExecutionQueue(500)
```

## Methods

### close()

&gt; **close**(): `void`

Defined in: [packages/helpers/src/utils/execution-queue.ts:190](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/execution-queue.ts#L190)

Clears all pending tasks from the queue.

Immediately removes all pending tasks from the queue. Any currently
running task will complete normally, but no additional tasks will be executed.
This method does not wait for the current task to finish.

Discarded tasks are dropped without settling: the promise returned by the
`push` that enqueued each cleared task never resolves nor rejects, so any
`await` on it hangs forever. Only call `close()` when those pending results
are known to be unawaited.

#### Returns

`void`

#### Example

```ts
const queue = new ExecutionQueue()

// Add several tasks
queue.push(() => console.log('task 1'))
queue.push(() => console.log('task 2'))
queue.push(() => console.log('task 3'))

// Clear all pending tasks
queue.close()
// Only 'task 1' will execute if it was already running
```

***

### isEmpty()

&gt; **isEmpty**(): `boolean`

Defined in: [packages/helpers/src/utils/execution-queue.ts:96](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/execution-queue.ts#L96)

Checks if the queue is empty and not currently running a task.

Determines whether the execution queue has completed all tasks and is idle.
Returns true only when there are no pending tasks in the queue AND no task is currently being executed.

#### Returns

`boolean`

True if the queue has no pending tasks and is not currently executing

#### Example

```ts
const queue = new ExecutionQueue()

console.log(queue.isEmpty()) // true - queue is empty

queue.push(() => console.log('task'))
console.log(queue.isEmpty()) // false - task is running/pending
```

***

### push()

&gt; **push**\<`T`\>(`task`): `Promise`\<`Awaited`\<`T`\>\>

Defined in: [packages/helpers/src/utils/execution-queue.ts:147](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/execution-queue.ts#L147)

Adds a task to the queue and returns a promise that resolves with the task's result.

Enqueues a task for sequential execution. The task will be executed after all
previously queued tasks have completed. If a timeout was specified in the constructor,
there will be a delay between this task and the next one.

A failing task never strands the queue: whether `task` throws synchronously
or its promise rejects, only that task's returned promise rejects (with the
thrown value) and the queue proceeds to the next task. Failure is surfaced as
a rejected promise, not a synchronous throw from `push`.

#### Type Parameters

##### T

`T`

#### Parameters

##### task

() =&gt; `T`

The function to execute (can be sync or async)

#### Returns

`Promise`\<`Awaited`\<`T`\>\>

Promise that resolves with the task's return value, or rejects with
  whatever `task` threw / rejected with.

#### Example

```ts
const queue = new ExecutionQueue(100)

// Add async task
const result = await queue.push(async () => {
  const response = await fetch('/api/data')
  return response.json()
})

// Add sync task
const number = await queue.push(() => 42)
```
