# Class: SimpleRateLimitCounter

Defined in: [rate-limit/simple-rate-limit-counter.ts:48](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L48)

In-memory [RateLimitCounter](../../rate-limit.types/interfaces/RateLimitCounter) backed by a `Map` of per-key counts. This is
the default counter when a RateLimitConfigs supplies none.

## Example

```ts
const counter = new SimpleRateLimitCounter();

// Track API calls per user.
counter.inc("user-1");
counter.inc("user-1");
counter.inc("user-2");

counter.getCount("user-1"); // → 2
counter.getCount("user-2"); // → 1
counter.getCount("user-3"); // → 0

// After some time, decrement.
counter.dec("user-1");
counter.getCount("user-1"); // → 1
```

## Implements

- [`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter)

## Constructors

### Constructor

&gt; **new SimpleRateLimitCounter**(`counterMap?`): `SimpleRateLimitCounter`

Defined in: [rate-limit/simple-rate-limit-counter.ts:57](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L57)

Create a new counter, optionally seeded with an existing map of counts.

The map is retained by reference and mutated in place by `inc`/`dec`, so a
shared map lets several counters observe and update the same counts.

#### Parameters

##### counterMap?

`Map`\<`string`, `number`\> = `...`

Backing store for per-key counts; defaults to a new `Map`.

#### Returns

`SimpleRateLimitCounter`

## Methods

### dec()

&gt; **dec**(`key`): `void`

Defined in: [rate-limit/simple-rate-limit-counter.ts:111](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L111)

Decrement the count for a key, removing the key entirely when it reaches `0`.

#### Parameters

##### key

`string`

The key to decrement.

#### Returns

`void`

#### Example

```ts
const counter = new SimpleRateLimitCounter();
counter.inc("key");
counter.inc("key");
counter.dec("key");
counter.getCount("key"); // → 1
counter.dec("key");
counter.getCount("key"); // → 0 (key removed from the map)
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`dec`](../../rate-limit.types/interfaces/RateLimitCounter#dec)

***

### getCount()

&gt; **getCount**(`key`): `number`

Defined in: [rate-limit/simple-rate-limit-counter.ts:72](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L72)

Get the current count for a key.

#### Parameters

##### key

`string`

The key to read.

#### Returns

`number`

The current count, or `0` when the key is absent.

#### Example

```ts
const counter = new SimpleRateLimitCounter();
counter.getCount("key"); // → 0
counter.inc("key");
counter.getCount("key"); // → 1
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`getCount`](../../rate-limit.types/interfaces/RateLimitCounter#getcount)

***

### inc()

&gt; **inc**(`key`): `void`

Defined in: [rate-limit/simple-rate-limit-counter.ts:88](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L88)

Increment the count for a key.

#### Parameters

##### key

`string`

The key to increment.

#### Returns

`void`

#### Example

```ts
const counter = new SimpleRateLimitCounter();
counter.inc("user-123");
counter.inc("user-123");
counter.getCount("user-123"); // → 2
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`inc`](../../rate-limit.types/interfaces/RateLimitCounter#inc)
