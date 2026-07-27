# Class: SlidingWindowCounter

Defined in: [throttle.ts:917](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L917)

Sliding-window counter for per-key rate limiting.

Maintains a `current` and `previous` window count per key and
estimates the *weighted* request rate over the trailing
`windowMs` ms by interpolating between the two windows. This
provides smoother enforcement than a fixed-window counter (which
lets twice the limit through across a window boundary) without the
memory cost of a true sliding-window log.

Calls a periodic `cleanup` every `windowMs` ms to drop stale
entries — note that this means **the limiter holds a Node timer
for its entire lifetime**. Long-lived processes are fine; for
short-lived workers, manage instances explicitly or you'll keep
the event loop alive.

## Example

```ts
const counter = new SlidingWindowCounter(60_000, 100); // 100 req/min
const decision = counter.check(`user:${userId}`);
if (!decision.allowed) return new Response("Too many requests", { status: 429 });
```

## Implements

- [`KeyedRateLimiter`](../interfaces/KeyedRateLimiter)

## Constructors

### Constructor

&gt; **new SlidingWindowCounter**(`windowMs`, `maxRequests`): `SlidingWindowCounter`

Defined in: [throttle.ts:929](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L929)

#### Parameters

##### windowMs

`PositiveMillis`

Sliding-window length in milliseconds. Construct with
  `toPositiveMillis(...)` so non-positive windows are rejected at the
  boundary.

##### maxRequests

`PositiveInt`

Maximum allowed weighted count per window
  per key. Construct with `toPositiveInt(...)`.

#### Returns

`SlidingWindowCounter`

## Methods

### check()

&gt; **check**(`key`): `ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>

Defined in: [throttle.ts:951](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L951)

Atomically increment the counter for `key` and decide whether
to allow the request based on the trailing weighted count.

#### Parameters

##### key

`string`

#### Returns

`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>

A [RateLimitDecision](../../decision/type-aliases/RateLimitDecision) — the same discriminated union the
  store layer returns — where:
  - `allowed` — `true` if under the limit; `false` if rejected
    (counter is **not** incremented in this case).
  - `remaining` — best-effort lower bound on how many more
    requests fit in the current window for this key (`0` when rejected).
  - `limit` — the configured `maxRequests` for this counter.
  - `resetAt` — Unix epoch ms when the current fixed window
    boundary rolls over.

#### Implementation of

[`KeyedRateLimiter`](../interfaces/KeyedRateLimiter).[`check`](../interfaces/KeyedRateLimiter#check)

***

### getStats()

&gt; **getStats**(): [`KeyedStats`](../type-aliases/KeyedStats)

Defined in: [throttle.ts:1026](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L1026)

Snapshot of currently-tracked keys.

#### Returns

[`KeyedStats`](../type-aliases/KeyedStats)

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.

#### Implementation of

[`KeyedRateLimiter`](../interfaces/KeyedRateLimiter).[`getStats`](../interfaces/KeyedRateLimiter#getstats)

***

### reset()

&gt; **reset**(`key`): `void`

Defined in: [throttle.ts:1001](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L1001)

Forget all state for `key`. The next `check(key)` starts fresh.

Useful for admin/test reset paths and for clearing limits when
a user upgrades to a higher tier.

#### Parameters

##### key

`string`

#### Returns

`void`

#### Implementation of

[`KeyedRateLimiter`](../interfaces/KeyedRateLimiter).[`reset`](../interfaces/KeyedRateLimiter#reset)
