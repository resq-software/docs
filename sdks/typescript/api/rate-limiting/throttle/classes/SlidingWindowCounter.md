# Class: SlidingWindowCounter

Defined in: [throttle.ts:776](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L776)

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

## Constructors

### Constructor

> **new SlidingWindowCounter**(`windowMs`, `maxRequests`): `SlidingWindowCounter`

Defined in: [throttle.ts:786](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L786)

#### Parameters

##### windowMs

`number`

Sliding-window length in milliseconds.

##### maxRequests

`number`

Maximum allowed weighted count per window
  per key.

#### Returns

`SlidingWindowCounter`

## Methods

### check()

> **check**(`key`): `object`

Defined in: [throttle.ts:806](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L806)

Atomically increment the counter for `key` and decide whether
to allow the request based on the trailing weighted count.

#### Parameters

##### key

`string`

#### Returns

`object`

`{ allowed, remaining, resetAt }` where:
  - `allowed` — `true` if under the limit; `false` if rejected
    (counter is **not** incremented in this case).
  - `remaining` — best-effort lower bound on how many more
    requests fit in the current window for this key.
  - `resetAt` — Unix epoch ms when the current fixed window
    boundary rolls over.

##### allowed

> **allowed**: `boolean`

##### remaining

> **remaining**: `number`

##### resetAt

> **resetAt**: `number`

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:877](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L877)

Snapshot of currently-tracked keys.

#### Returns

`object`

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]

***

### reset()

> **reset**(`key`): `void`

Defined in: [throttle.ts:852](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L852)

Forget all state for `key`. The next `check(key)` starts fresh.

Useful for admin/test reset paths and for clearing limits when
a user upgrades to a higher tier.

#### Parameters

##### key

`string`

#### Returns

`void`
