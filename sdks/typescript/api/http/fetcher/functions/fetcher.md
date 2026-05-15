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

## Type Param

Response shape inferred from `options.schema` when
  provided, otherwise `unknown`.

## Param

URL or path. Absolute (`http(s)://…`) is used
  verbatim; relative paths are joined to the resolved base URL.

## Param

HTTP verb. Defaults to `"GET"`.

## Param

[FetcherOptions](../interfaces/FetcherOptions) (retries, timeout, headers,
  schema, abort signal, …).

## Param

Optional query parameters. Array values are
  serialised as repeated keys.

## Param

Optional request body for POST/PUT/PATCH. Encoded
  per `options.bodyType` (default `"json"`).

## Call Signature

> **fetcher**\<`T`\>(`input`, `method?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:390](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L390)

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

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:397](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L397)

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

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`, `body?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:408](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L408)

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

`any`

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`, `body?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:416](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L416)

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

`any`

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:428](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L428)

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

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>
