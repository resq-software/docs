# Function: patch()

Issue an HTTP PATCH (partial update). Convenience wrapper around
[fetcher](./fetcher).

## Call Signature

&gt; **patch**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:939](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L939)

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

&gt; **patch**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:946](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L946)

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
