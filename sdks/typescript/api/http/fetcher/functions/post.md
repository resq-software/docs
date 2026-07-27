# Function: post()

Issue an HTTP POST with a JSON body (or text/form when overridden
via `options.bodyType`). Convenience wrapper around [fetcher](./fetcher).

## Example

```ts
const created = yield* post<User>("/api/users", { name: "Alice" });
```

## Call Signature

&gt; **post**\<`T`\>(`url`, `body?`, `options?`, `params?`): `Effect`\<`T`, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:872](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L872)

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

&gt; **post**\<`S`\>(`url`, `body`, `options`, `params?`): `Effect`\<`Type`\<`S`\>, [`FetcherError`](../classes/FetcherError) \| [`FetcherValidationError`](../classes/FetcherValidationError), `HttpClient`\>

Defined in: [packages/http/src/fetcher.ts:879](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L879)

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
