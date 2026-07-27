# Function: put()

Issue an HTTP PUT (full-resource replace). Convenience wrapper
around [fetcher](./fetcher).

## Call Signature

&gt; **put**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:908](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L908)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### url

`string`

#### body?

[`RequestBody`](../type-aliases/RequestBody)

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **put**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:915](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L915)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### url

`string`

#### body

[`RequestBody`](../type-aliases/RequestBody)

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>
