# Interface: FetcherOptions\<T\>

Defined in: [packages/http/src/fetcher.ts:34](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L34)

Configuration options for the fetcher utility.

## Type Parameters

### T

`T` = `unknown`

## Properties

### bodyType?

> `optional` **bodyType?**: `"json"` \| `"text"` \| `"form"`

Defined in: [packages/http/src/fetcher.ts:50](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L50)

Body type - defaults to 'json', use 'text' for raw data, 'form' for FormData

***

### headers?

> `optional` **headers?**: `Record`\<`string`, `string`\>

Defined in: [packages/http/src/fetcher.ts:44](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L44)

Additional headers to include in the request

***

### onError?

> `optional` **onError?**: (`error`) => `void`

Defined in: [packages/http/src/fetcher.ts:40](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L40)

Optional callback invoked on error

#### Parameters

##### error

`unknown`

#### Returns

`void`

***

### retries?

> `optional` **retries?**: `number`

Defined in: [packages/http/src/fetcher.ts:36](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L36)

Number of times to retry the request on failure

***

### retryDelay?

> `optional` **retryDelay?**: `number`

Defined in: [packages/http/src/fetcher.ts:38](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L38)

Delay in milliseconds between retries

***

### schema?

> `optional` **schema?**: `SyncSchema`\<`T`\>

Defined in: [packages/http/src/fetcher.ts:46](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L46)

Effect/Schema for runtime validation of the response

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [packages/http/src/fetcher.ts:48](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L48)

Abortsignal

***

### timeout?

> `optional` **timeout?**: `number`

Defined in: [packages/http/src/fetcher.ts:42](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/http/src/fetcher.ts#L42)

Timeout in milliseconds for the request
