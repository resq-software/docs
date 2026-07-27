# Function: fetcher()

Effect-based HTTP client with retry, timeout, schema validation,
and structured error handling.

Resolves the URL by prepending the runtime-detected base URL
(Vite/Next env, fallback to `http://localhost:5173` server-side; no
prefix in the browser). Encodes `params` into a query string,
picks the body encoding (`json` / `text` / `form`) per
`options.bodyType`, and runs the request through `HttpClient` with
`Schedule.exponential` retry on failure.

On 4xx/5xx, timeout, transport, or body-parse failure: fails with
[FetcherError](../classes/FetcherError). When `options.schema` is supplied and the
response body decodes against it: returns the typed value;
otherwise: fails with [FetcherValidationError](../classes/FetcherValidationError).

Prefer the verb-specific helpers ([get](./get), [post](./post),
[put](./put), [patch](./patch), [del](./del), [options](./options),
[head](./head)) — they have nicer overloads and avoid you specifying
the method string by hand. Reach for `fetcher` directly only when
the method is dynamic.

Failure is signalled through the `Effect` error channel (a failed
effect), never a resolved error-shaped value. The returned effect is
a cold description: building it performs no I/O, and each `runFork`/
`runPromise` executes an independent request, so the same effect
value may be run concurrently. Cancellation follows Effect fiber
interruption; `options.signal` is **not** honoured (see
[FetcherOptions.signal](../interfaces/FetcherOptions#signal)). The `timeout` applies per attempt, so
a retried call can outlive a single `timeout` window. As side
effects, the call performs network I/O, reads the runtime environment
and base-URL globals (getBaseURL), and invokes
`options.onError` — possibly more than once (see
[FetcherOptions.onError](../interfaces/FetcherOptions#onerror)).

## Type Param

**T**

Response shape inferred from `options.schema` when
  provided, otherwise `unknown`.

## Param

**input**

URL or path. Absolute (`http(s)://…`) is used
  verbatim; relative paths are joined to the resolved base URL.

## Param

**method**

HTTP verb. Defaults to `"GET"`.

## Param

**options**

[FetcherOptions](../interfaces/FetcherOptions) (retries, timeout, headers,
  schema, abort signal, …).

## Param

**params**

Optional query parameters. Array values are
  serialised as repeated keys.

## Param

**body**

Optional request body for POST/PUT/PATCH. Encoded
  per `options.bodyType` (default `"json"`).

## Call Signature

&gt; **fetcher**\<`T`\>(`input`, `method?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:535](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L535)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method?

`"GET"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:542](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L542)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### input

`string`

#### method

`"GET"`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`, `body?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:553](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L553)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method

`"POST"` \| `"PUT"` \| `"PATCH"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

#### body?

[`RequestBody`](../type-aliases/RequestBody)

### Returns

`Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`, `body?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:561](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L561)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### input

`string`

#### method

`"POST"` \| `"PUT"` \| `"PATCH"`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`Type`\<`S`\>\> & `object`

#### params?

#### body?

[`RequestBody`](../type-aliases/RequestBody)

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:573](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L573)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method

`"DELETE"` \| `"OPTIONS"` \| `"HEAD"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>
