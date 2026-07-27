# Class: MemoryRateLimitStore

Defined in: [rate-limit.ts:215](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L215)

[IRateLimitStore](../interfaces/IRateLimitStore) that keeps counters in a process-local `Map`.

Suitable for **single-process** deployments only — a multi-instance
deployment will under-count because each instance sees only its own
traffic. Use [RedisRateLimitStore](./RedisRateLimitStore) (or another distributed
backend) in production when more than one node serves traffic.

Counters are reset *implicitly* once the window expires — the next
`check()` past `resetAt` starts a fresh window. There is no
background sweeper, so memory grows with the number of distinct keys
over the lifetime of the process; pair with periodic `reset()` for
long-lived processes that see unbounded key cardinality.

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore)

## Constructors

### Constructor

&gt; **new MemoryRateLimitStore**(`options?`): `MemoryRateLimitStore`

Defined in: [rate-limit.ts:221](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L221)

#### Parameters

##### options?

###### maxSize?

`number`

#### Returns

`MemoryRateLimitStore`

## Methods

### check()

&gt; **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

Defined in: [rate-limit.ts:235](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L235)

#### Parameters

##### key

`string`

##### windowMs

`number`

##### maxRequests

`number`

#### Returns

`Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

#### Inherit Doc

**Purely**

process-local: reads the wall clock, mutates the backing LRU
entry for `key` in place, and always **resolves** — there is no I/O to
fail on, so it never rejects. The `async` signature exists only to
satisfy [IRateLimitStore](../interfaces/IRateLimitStore). Concurrent calls are safe within a
single JS event loop, but two processes each keep independent counters
(hence the single-process caveat on the class).

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`check`](../interfaces/IRateLimitStore#check)

***

### reset()

&gt; **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:281](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L281)

Drop any state held for `key`. Useful for admin / unit-test reset
paths; not invoked by middleware itself.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`reset`](../interfaces/IRateLimitStore#reset)
