# Function: debounce()

&gt; **debounce**\<`T`\>(`func`, `wait`, `options?`): (...`args`) =&gt; `void` & `object`

Defined in: [throttle.ts:222](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L222)

Debounce a function so it executes only after `wait` ms have elapsed with no
further calls.

The returned wrapper is **stateful**: it closes over the last-call and
last-invoke timestamps plus a live `setTimeout`. Reads the wall clock and
(re)arms a timer on every call, so it is effectful and non-deterministic.
`func`'s return value is discarded — the wrapper returns `void`. `cancel()`
drops any pending fire; `flush()` clears the pending timer **without**
invoking `func` (it cancels rather than forces — see the body).

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Parameters

### func

`T`

Function to debounce.

### wait

`number`

Quiet interval, in milliseconds, that must pass before firing.

### options?

Leading-edge behaviour and optional `maxWait` ceiling.

#### leading?

`boolean` = `...`

Whether to invoke on the leading edge of the debounce window.

#### maxWait?

`number` = `...`

Upper bound, in milliseconds, on how long invocation may be deferred.

## Returns

(...`args`) =&gt; `void` & `object`

The debounced wrapper, with `cancel()` and `flush()` controls.

## Example

```ts
const search = debounce((query) => fetchSearchResults(query), 300);
search('a'); // Waiting...
search('ab'); // Waiting...
search('abc'); // Executes after 300ms of no calls
```
