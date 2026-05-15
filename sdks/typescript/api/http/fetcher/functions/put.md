# Function: put()

Issue an HTTP PUT (full-resource replace). Convenience wrapper
around [fetcher](./fetcher).

## Call Signature

> **put**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:643](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L643)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### url

`string`

#### body?

`any`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **put**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:650](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L650)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### url

`string`

#### body

`any`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>
