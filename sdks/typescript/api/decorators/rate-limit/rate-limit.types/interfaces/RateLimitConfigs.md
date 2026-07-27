# Interface: RateLimitConfigs\<T\>

Defined in: [rate-limit/rate-limit.types.ts:49](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L49)

Configuration for the `@rateLimit` decorator and rateLimitFn.

`timeSpanMs` and `allowedCalls` are required; supply at most one counter — when
both `rateLimitCounter` and `rateLimitAsyncCounter` are set, the async one wins
and the call becomes promise-returning. With no counter, an in-memory
[RateLimitCounter](./RateLimitCounter) is used. With no `keyResolver`, all calls share a single
`"default"` bucket.

## Example

```ts
const config: RateLimitConfigs<ApiService> = {
  timeSpanMs: 60000, // One minute.
  allowedCalls: 100, // 100 calls per minute.
  keyResolver: (userId) => `user-${userId}`,
  exceedHandler: () => {
    throw new Error("Rate limit exceeded");
  },
};
```

## Type Parameters

### T

`T` = `unknown`

The class type a `keyof T` key resolver resolves against.

## Properties

### allowedCalls

&gt; **allowedCalls**: `number`

Defined in: [rate-limit/rate-limit.types.ts:53](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L53)

Maximum admitted calls per key within the window.

***

### exceedHandler?

&gt; `optional` **exceedHandler?**: () =&gt; `void`

Defined in: [rate-limit/rate-limit.types.ts:65](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L65)

Invoked (for its side effects) when a call is dropped; a throw here propagates to the caller.

#### Returns

`void`

***

### keyResolver?

&gt; `optional` **keyResolver?**: ((...`args`) =&gt; `string`) \| keyof `T`

Defined in: [rate-limit/rate-limit.types.ts:59](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L59)

How the rate-limit bucket key is derived. A function is called with the
arguments; a `keyof T` names an instance method invoked with the arguments.
When omitted, all calls share the `"default"` bucket.

***

### rateLimitAsyncCounter?

&gt; `optional` **rateLimitAsyncCounter?**: [`RateLimitAsyncCounter`](./RateLimitAsyncCounter)

Defined in: [rate-limit/rate-limit.types.ts:63](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L63)

Async counter for distributed limiting; takes precedence over `rateLimitCounter`.

***

### rateLimitCounter?

&gt; `optional` **rateLimitCounter?**: [`RateLimitCounter`](./RateLimitCounter)

Defined in: [rate-limit/rate-limit.types.ts:61](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L61)

Custom synchronous counter; ignored when `rateLimitAsyncCounter` is set.

***

### timeSpanMs

&gt; **timeSpanMs**: `number`

Defined in: [rate-limit/rate-limit.types.ts:51](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.types.ts#L51)

Rolling window length in milliseconds; each admitted call is charged for this long.
