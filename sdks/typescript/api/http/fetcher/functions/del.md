# Function: del()

Issue an HTTP DELETE. Named `del` because `delete` is a reserved
keyword. Convenience wrapper around [fetcher](./fetcher).

## Call Signature

> **del**\<`T`\>(`url`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:705](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L705)

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

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

## Call Signature

> **del**\<`S`\>(`url`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:711](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L711)

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

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>
