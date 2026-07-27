# Function: head()

Issue an HTTP HEAD (response headers only, no body). Convenience
wrapper around [fetcher](./fetcher).

Useful for cache validation, content-length probing, or existence
checks without the body transfer cost.

## Call Signature

&gt; **head**\<`T`\>(`url`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:1023](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L1023)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### url

`string`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

## Call Signature

&gt; **head**\<`S`\>(`url`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:1029](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L1029)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### url

`string`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>
