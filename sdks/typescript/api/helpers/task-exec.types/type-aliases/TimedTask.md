# Type Alias: TimedTask

&gt; **TimedTask** = `object`

Defined in: [packages/helpers/src/task-exec.types.ts:30](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/task-exec.types.ts#L30)

A unit of deferred work tracked by TaskExec.

Tasks are ordered by `execTime` (a Unix epoch millisecond) — the
earliest-due task is always at the head of the priority queue.

## Properties

### execTime

&gt; **execTime**: `number`

Defined in: [packages/helpers/src/task-exec.types.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/task-exec.types.ts#L34)

Earliest time (epoch ms) at which `func` should run.

***

### func

&gt; **func**: () =&gt; `unknown`

Defined in: [packages/helpers/src/task-exec.types.ts:32](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/task-exec.types.ts#L32)

Callback to invoke when the task fires. Invoked with no arguments; return value is ignored.

#### Returns

`unknown`
