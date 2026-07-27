# Class: TaskExec

Defined in: [\_utils.ts:156](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/_utils.ts#L156)

A minimal timer-backed scheduler that fires queued tasks in due-time order,
keeping a single active `setTimeout` for the nearest pending task.

## Constructors

### Constructor

&gt; **new TaskExec**(): `TaskExec`

#### Returns

`TaskExec`

## Methods

### exec()

&gt; **exec**(`func`, `ttl`): `void`

Defined in: [\_utils.ts:172](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/_utils.ts#L172)

Schedule `func` to run after `ttl` milliseconds.

Effectful: reads the wall clock (`Date.now`), pushes onto and re-sorts the
internal task list, and arms a single `setTimeout` for the nearest due task
(rescheduling the shared timer if this task is now the soonest). `ttl` is a
relative delay in milliseconds from the moment of the call, not an absolute
timestamp. Tasks fire in due-time order regardless of insertion order.

#### Parameters

##### func

(...`args`) =&gt; `unknown`

The callback to run once its delay elapses.

##### ttl

`number`

Delay before execution, in milliseconds from now.

#### Returns

`void`
