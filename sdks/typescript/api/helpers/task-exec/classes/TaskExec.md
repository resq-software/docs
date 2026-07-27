# Class: TaskExec

Defined in: [packages/helpers/src/task-exec.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/task-exec.ts#L48)

Earliest-deadline-first task scheduler backed by a binary heap.

Add work via [\`exec(func, ttl)\`](#exec); the scheduler keeps a
single active `setTimeout` armed for the next-due task and re-arms
it after each fire. Tasks scheduled with shorter `ttl` than what is
currently armed pre-empt the current timer (the existing timer is
cleared and re-scheduled for the new earliest deadline).

Compared to manually calling `setTimeout` per task, this avoids
holding many concurrent timers and keeps wall-clock ordering
deterministic when many tasks queue at once.

## Example

```ts
const sched = new TaskExec();
sched.exec(() => flush(), 5_000);    // run in ~5s
sched.exec(() => log("now"), 0);     // runs immediately
sched.exec(() => report(), 60_000);  // run in ~60s
```

## Constructors

### Constructor

&gt; **new TaskExec**(): `TaskExec`

#### Returns

`TaskExec`

## Methods

### exec()

&gt; **exec**(`func`, `ttl`): `void`

Defined in: [packages/helpers/src/task-exec.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/task-exec.ts#L71)

Schedule a callback to run no sooner than `ttl` milliseconds from
now. Multiple tasks can be queued; each fires at its own deadline.

Mutates the internal heap and arms/re-arms a single `setTimeout`, so
this is an effectful call tied to the event loop and the clock.

#### Parameters

##### func

() =&gt; `unknown`

Callback to run; receives no arguments. Return value
  is ignored. A synchronous throw bubbles out of the timer callback
  (per `setTimeout` semantics) **before** the scheduler re-arms — so
  the timer is left un-armed and any still-queued tasks stay pending
  until the next `exec` call re-arms it. Keep task bodies
  self-guarding if later tasks must still fire.

##### ttl

`number`

Delay in milliseconds. Pass `0` for "run on the next
  tick". Negative values are clamped to `0`.

#### Returns

`void`
