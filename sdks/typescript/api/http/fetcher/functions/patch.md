# Function: patch()

## Call Signature

> **patch**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:584](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L584)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### url

`string`

#### body?

`any`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **patch**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:591](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L591)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### url

`string`

#### body

`any`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>
