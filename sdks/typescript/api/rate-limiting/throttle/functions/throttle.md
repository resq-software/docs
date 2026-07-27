# Function: throttle()

&gt; **throttle**\<`T`\>(`func`, `wait`, `options?`): (...`args`) =&gt; `ReturnType`\<`T`\> \| `undefined` & `object`

Defined in: [throttle.ts:143](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L143)

Throttle a function so it executes at most once per `wait` interval.

The returned wrapper is **stateful**: it closes over the last-fire
timestamp, the cached result, and a pending trailing-edge timer. Reads the
wall clock (`Date.now`) and schedules a `setTimeout` for the trailing call,
so it is neither pure nor deterministic — do not share one wrapper across
unrelated call streams that should throttle independently (reach for
[KeyedThrottle](../classes/KeyedThrottle)). `cancel()` clears any pending trailing call and
resets the window. `func` is invoked with the `this` and arguments of the
call that triggers it.

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Parameters

### func

`T`

Function to throttle.

### wait

`number`

Minimum interval between invocations, in milliseconds.

### options?

Leading/trailing edge behaviour.

#### leading?

`boolean` = `...`

Whether to invoke on the leading edge of the throttle window.

#### trailing?

`boolean` = `...`

Whether to invoke on the trailing edge of the throttle window.

## Returns

(...`args`) =&gt; `ReturnType`\<`T`\> \| `undefined` & `object`

The throttled wrapper, with a `cancel()` to clear any pending
  trailing call. Each call returns the most recent result — the value from
  the invocation just made, or the cached prior result, or `undefined`
  before `func` has ever run.

## Example

```ts
const fetchData = throttle(() => fetch('/api/data'), 1000);
fetchData(); // Executes immediately
fetchData(); // Ignored
fetchData(); // Ignored
// After 1000ms, next call will execute
```
