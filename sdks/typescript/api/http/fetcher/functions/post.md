# Function: post()

Issue an HTTP POST with a JSON body (or text/form when overridden
via `options.bodyType`). Convenience wrapper around [fetcher](./fetcher).

## Example

```ts
const created = yield* post<User>("/api/users", { name: "Alice" });
```

## Call Signature

> **post**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:607](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L607)

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

> **post**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:614](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L614)

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
