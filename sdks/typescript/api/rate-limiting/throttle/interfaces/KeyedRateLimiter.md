# Interface: KeyedRateLimiter

Defined in: [throttle.ts:567](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L567)

A **per-key** rate limiter: one independent limit per string key (e.g. per
user or IP). The Strategy interface implemented by [SlidingWindowCounter](../classes/SlidingWindowCounter).
Unlike [RateLimiter](./RateLimiter) it is keyed and non-blocking — each [check](#check)
both records the request and returns a [RateLimitDecision](../../decision/type-aliases/RateLimitDecision).

## Methods

### check()

&gt; **check**(`key`): `ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>

Defined in: [throttle.ts:569](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L569)

Record a request for `key` and decide whether it is allowed.

#### Parameters

##### key

`string`

#### Returns

`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>

***

### getStats()

&gt; **getStats**(): [`KeyedStats`](../type-aliases/KeyedStats)

Defined in: [throttle.ts:573](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L573)

A snapshot of the currently-tracked keys.

#### Returns

[`KeyedStats`](../type-aliases/KeyedStats)

***

### reset()

&gt; **reset**(`key`): `void`

Defined in: [throttle.ts:571](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L571)

Forget all state for `key`; the next `check(key)` starts fresh.

#### Parameters

##### key

`string`

#### Returns

`void`
