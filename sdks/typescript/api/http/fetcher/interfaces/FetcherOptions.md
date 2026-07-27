# Interface: FetcherOptions\<T\>

Defined in: [packages/http/src/fetcher.ts:73](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L73)

Configuration for a single [fetcher](../functions/fetcher) call (and the verb helpers built on
it). Every field is optional; the defaults listed per member apply when it is
omitted.

## Type Parameters

### T

`T` = `unknown`

The decoded response type. Bound to [schema](#schema) when one is
  supplied (the schema's output type), otherwise defaults to `unknown`.

## Properties

### allowedHosts?

&gt; `optional` **allowedHosts?**: readonly [`HostPattern`](../type-aliases/HostPattern)[]

Defined in: [packages/http/src/fetcher.ts:132](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L132)

Optional list of allowed hosts (e.g. `['api.example.com']` or `['*.example.com']`).
If provided, requests to other hosts fail with FetcherError.
NOTE: This offers basic hostname-based security filtering. It does not protect against
advanced DNS rebinding or IP-based bypasses (e.g., alternative IP encodings, IPv6 vs IPv4)
unless such filtering is enabled at the lower network transport or HttpClient layer.

***

### blockedHosts?

&gt; `optional` **blockedHosts?**: readonly [`HostPattern`](../type-aliases/HostPattern)[]

Defined in: [packages/http/src/fetcher.ts:140](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L140)

Optional list of blocked hosts (e.g. `['localhost', '127.0.0.1']`).
If provided, requests to these hosts fail with FetcherError.
NOTE: This offers basic hostname-based security filtering. It does not protect against
advanced DNS rebinding or IP-based bypasses (e.g., alternative IP encodings, IPv6 vs IPv4)
unless such filtering is enabled at the lower network transport or HttpClient layer.

***

### bodyType?

&gt; `optional` **bodyType?**: `"json"` \| `"text"` \| `"form"`

Defined in: [packages/http/src/fetcher.ts:124](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L124)

Encoding for a request body on `POST`/`PUT`/`PATCH`. `"json"` (default)
serialises via `bodyJson`; `"text"` sends `JSON.stringify` of objects or
`String(...)` of primitives; `"form"` **requires** a FormData body
and fails with [FetcherError](../classes/FetcherError) otherwise. A FormData body is
always sent as multipart regardless of this field.

***

### headers?

&gt; `optional` **headers?**: `Record`\<`string`, `string`\>

Defined in: [packages/http/src/fetcher.ts:103](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L103)

Extra request headers, merged onto the built request. Later duplicate keys win over defaults.

***

### onError?

&gt; `optional` **onError?**: (`error`) =&gt; `void`

Defined in: [packages/http/src/fetcher.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L95)

Callback fired with the failing error. May be invoked **more than once** for
a single call: once per rejected schema decode inside the retry cycle (see
[schema](#schema)) and once again when the effect ultimately fails. Runs
synchronously for its side effects; its return value is discarded and it is
never awaited. Throwing from it propagates out of the fetch.

#### Parameters

##### error

`unknown`

#### Returns

`void`

***

### retries?

&gt; `optional` **retries?**: `number`

Defined in: [packages/http/src/fetcher.ts:81](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L81)

Number of **additional** attempts after the first, per Effect's
`Schedule.recurs`; total attempts are `retries + 1`. Non-negative; defaults
to `0` (no retry). Retries are filtered: a `429` is always retried, other
`4xx` responses and [FetcherValidationError](../classes/FetcherValidationError) are never retried
regardless of this value.

***

### retryDelay?

&gt; `optional` **retryDelay?**: `number`

Defined in: [packages/http/src/fetcher.ts:87](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L87)

Base delay in **milliseconds** for the exponential backoff schedule
(`Schedule.exponential`) — the wait grows geometrically per attempt, not a
fixed gap. Defaults to `1000`. Ignored when [retries](#retries) is `0`.

***

### schema?

&gt; `optional` **schema?**: `SyncSchema`\<`T`\>

Defined in: [packages/http/src/fetcher.ts:110](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L110)

Effect Schema used to decode and validate the response body. When present,
the resolved value is the schema's output type and a decode failure fails
the effect with [FetcherValidationError](../classes/FetcherValidationError); when absent, the raw parsed
body is returned unchecked as `T`.

***

### signal?

&gt; `optional` **signal?**: `AbortSignal`

Defined in: [packages/http/src/fetcher.ts:116](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L116)

Reserved for request cancellation. **Currently accepted but not wired into
request execution** — the effect does not abort when this signal fires.
Cancel by interrupting the Effect fiber instead.

***

### timeout?

&gt; `optional` **timeout?**: `number`

Defined in: [packages/http/src/fetcher.ts:101](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L101)

Per-attempt timeout in **milliseconds** — applied to each retry attempt
independently, not to the call as a whole. Defaults to `10000`. Elapsing it
fails the attempt with a [FetcherError](../classes/FetcherError) (`status` absent).
