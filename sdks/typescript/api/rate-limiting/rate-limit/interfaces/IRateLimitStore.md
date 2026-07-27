# Interface: IRateLimitStore

Defined in: [rate-limit.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L83)

Pluggable backend for rate-limit state.

Implementations decide how counters are stored and how concurrency is
resolved (in-memory, Redis, distributed log, …). Stores are designed
to be reused across multiple `(windowMs, maxRequests)` configurations
keyed by the caller's `key` (typically `userId`, `ip`, or
`route + clientId`).

## Methods

### check()

&gt; **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

Defined in: [rate-limit.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L102)

Atomically increment the counter for `key` within a sliding window
of `windowMs` and decide whether to allow the request.

This is **not** a pure query: an allowed request is recorded (the
counter is advanced) as a side effect, so calling `check` twice
consumes two slots. Reads the wall clock to place the window.
Distributed implementations reach out to their backend and may
therefore reject; a rejected `Promise` signals an infrastructure
failure, distinct from a resolved `{ allowed: false }` decision.

#### Parameters

##### key

`string`

Caller-chosen identity key (e.g. `"user:42"`).

##### windowMs

`number`

Window length in milliseconds.

##### maxRequests

`number`

Maximum requests permitted in the window.

#### Returns

`Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

A [RateLimitDecision](../../decision/type-aliases/RateLimitDecision) describing the decision; a
  rejected `Promise` (implementation-dependent) signals that the
  decision could not be reached, not that the request was denied.

***

### reset()

&gt; **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:107](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L107)

Drop any state held for `key`. Useful for admin / unit-test reset
paths; not invoked by middleware itself.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>
