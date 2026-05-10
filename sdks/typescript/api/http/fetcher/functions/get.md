# Function: get()

## Call Signature

> **get**\<`T`\>(`url`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:514](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L514)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### url

`string`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **get**\<`A`\>(`url`, `options`, `params?`): `Effect`\<`A`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:520](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L520)

### Type Parameters

#### A

`A`

### Parameters

#### url

`string`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`A`\> & `object`

#### params?

### Returns

`Effect`\<`A`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>
