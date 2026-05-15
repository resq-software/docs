# Function: get()

Issue an HTTP GET. Convenience wrapper around [fetcher](./fetcher).

## Examples

```ts
const data = yield* get<User[]>("/api/users");
```

```ts
const users = yield* get("/api/users", { schema: UserListSchema });
```

## Call Signature

> **get**\<`T`\>(`url`, `options?`, `params?`): `Effect`\<`T`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:578](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L578)

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

> **get**\<`A`\>(`url`, `options`, `params?`): `Effect`\<`A`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:584](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L584)

### Type Parameters

#### A

`A`

### Parameters

#### url

`string`

#### options

[`FetcherOptions`](../interfaces/FetcherOptions)\<`A`\> & `object`

#### params?

### Returns

`Effect`\<`A`, [`FetcherValidationError`](../classes/FetcherValidationError) \| [`FetcherError`](../classes/FetcherError), `HttpClient`\>
