# Function: catchError()

&gt; **catchError**\<`Args`, `R`\>(`asyncFunction`, ...`args`): `Promise`\<`Result`\<`R`, `Error`\>\>

Defined in: [packages/helpers/src/helpers.ts:204](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L204)

Run an async function and convert thrown errors into a Failure
branch instead of rejecting the returned promise.

Logs a structured `error` line via `@resq-systems/logger` whenever the inner
function throws — useful for keeping rejected paths visible in
production telemetry without forcing every caller to wrap a try/catch.

Non-`Error` thrown values are coerced to `new Error(String(value))` so
the failure branch always carries a real `Error` instance with a stack.

The returned promise **always resolves** — the failure path is a resolved
`Failure`, never a rejection — so callers never need a surrounding
`try`/`catch` or `.catch()`. No `AbortSignal` handling is added here; pass one
through `args` if `asyncFunction` honours it.

## Type Parameters

### Args

`Args` *extends* readonly `unknown`[]

### R

`R`

## Parameters

### asyncFunction

(...`args`) =&gt; `Promise`\<`R`\>

The async function to invoke.

### args

...`Args`

Arguments forwarded to `asyncFunction`.

## Returns

`Promise`\<`Result`\<`R`, `Error`\>\>

A `Result<T, Error>` resolving to `success(returnValue)` on
  resolve, or `failure(err)` on throw / reject. Emits one structured `error`
  log per failure as a side effect.

## Example

```ts
const r = await catchError(fetch, "/api/users");
if (r.success) handleResponse(r.value);
else logger.warn("fetch failed", r.error);
```
