# Function: fetcher()

## Call Signature

> **fetcher**\<`T`\>(`input`, `method?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:366](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L366)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method?

`"GET"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:373](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L373)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### input

`string`

#### method

`"GET"`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`Type`\<`S`\>\> & `object`

#### params?

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`, `body?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:384](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L384)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method

`"POST"` \| `"PUT"` \| `"PATCH"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`T`\>

#### params?

#### body?

`any`

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **fetcher**\<`S`\>(`input`, `method`, `options`, `params?`, `body?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:392](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L392)

### Type Parameters

#### S

`S` *extends* `SyncSchema`\<`Type`\<`S`\>\>

### Parameters

#### input

`string`

#### method

`"POST"` \| `"PUT"` \| `"PATCH"`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`Type`\<`S`\>\> & `object`

#### params?

#### body?

`any`

### Returns

`Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

## Call Signature

> **fetcher**\<`T`\>(`input`, `method`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:404](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L404)

### Type Parameters

#### T

`T` = `unknown`

### Parameters

#### input

`string`

#### method

`"DELETE"` \| `"OPTIONS"` \| `"HEAD"`

#### options?

[`FetcherOptions`](../interfaces/FetcherOptions.md)\<`T`\>

#### params?

### Returns

`Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError.md) \| [`FetcherError`](../classes/FetcherError.md), `HttpClient`\>
