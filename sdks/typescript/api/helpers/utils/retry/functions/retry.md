# Function: retry()

&gt; **retry**\<`T`\>(`fn`, `options?`): `Promise`\<`T`\>

Defined in: [packages/helpers/src/utils/retry.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/retry.ts#L88)

**`Internal`**

Retries an async operation with configurable attempt count, wait duration, and error filtering.
Executes the provided async function repeatedly until it succeeds or the maximum number of attempts is reached.
Includes support for abort signals and custom error matching to determine which errors should trigger retries.

Cancellation is cooperative and coarse: `abortSignal` is polled only at the top
of each attempt, so aborting does not interrupt an in-flight `fn` or a wait in
progress — it takes effect before the next attempt. The inter-attempt wait runs
after every failure, including the final one, so a run that exhausts all
attempts still sleeps once more before rejecting. `fn` receives 0-based
`attempt`, `remaining` (`attempts - attempt`), and `total` (`attempts`).

## Type Parameters

### T

`T`

## Parameters

### fn

(`args`) =&gt; `Promise`\<`T`\>

The async function to retry on failure

### options?

Configuration options for retry behavior:
  - `attempts`: Maximum number of retry attempts (default: 3)
  - `waitDuration`: Milliseconds to wait between retry attempts (default: 1000)
  - `abortSignal`: Optional AbortSignal to cancel the retry operation
  - `matchError`: Optional function to determine if an error should trigger a retry

#### abortSignal?

`AbortSignal`

#### attempts?

`number` = `3`

#### waitDuration?

`number` = `1000`

#### matchError?

## Returns

`Promise`\<`T`\>

Promise that resolves with the function's return value on the first
  successful attempt.

## Throws

`"aborted"` if `abortSignal` is already aborted when an attempt
  is about to start.

## Throws

The last error thrown by `fn` once `attempts` is exhausted (re-thrown
  as-is, so it may be any value, not necessarily an `Error`).

## Throws

Immediately re-throws `fn`'s error, without retrying, when `matchError`
  is provided and returns `false` for it.

## Example

```ts
// Basic retry with default settings (3 attempts, 1 second wait)
const data = await retry(async () => {
  const response = await fetch('/api/data')
  if (!response.ok) throw new Error('Network error')
  return response.json()
})

// Custom retry configuration
const result = await retry(
  async () => unreliableApiCall(),
  {
    attempts: 5,
    waitDuration: 2000,
    matchError: (error) => error instanceof NetworkError
  }
)

// With abort signal for cancellation
const controller = new AbortController()
setTimeout(() => controller.abort(), 10000) // Cancel after 10 seconds

const data = await retry(
  async () => fetchData(),
  {
    attempts: 10,
    abortSignal: controller.signal
  }
)
```
