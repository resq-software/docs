# Class: SimpleRateLimitCounter

Defined in: [rate-limit/simple-rate-limit-counter.ts:44](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L44)

Simple in-memory implementation of RateLimitCounter.
Uses a Map to store counts for each key.

 SimpleRateLimitCounter

## Implements

## Example

```typescript
const counter = new SimpleRateLimitCounter();

// Track API calls per user
counter.inc('user-1');
counter.inc('user-1');
counter.inc('user-2');

console.log(counter.getCount('user-1')); // 2
console.log(counter.getCount('user-2')); // 1
console.log(counter.getCount('user-3')); // 0

// After some time, decrement
counter.dec('user-1');
console.log(counter.getCount('user-1')); // 1
```

## Implements

- [`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter)

## Constructors

### Constructor

> **new SimpleRateLimitCounter**(`counterMap?`): `SimpleRateLimitCounter`

Defined in: [rate-limit/simple-rate-limit-counter.ts:50](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L50)

Creates a new SimpleRateLimitCounter instance.

#### Parameters

##### counterMap?

`Map`\<`string`, `number`\> = `...`

Optional existing Map to use for storage

#### Returns

`SimpleRateLimitCounter`

## Methods

### dec()

> **dec**(`key`): `void`

Defined in: [rate-limit/simple-rate-limit-counter.ts:110](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L110)

Decrements the count for a key.
Removes the key from the map if count reaches 0.

#### Parameters

##### key

`string`

The key to decrement

#### Returns

`void`

#### Example

```typescript
const counter = new SimpleRateLimitCounter();
counter.inc('key');
counter.inc('key');
counter.dec('key');
console.log(counter.getCount('key')); // 1
counter.dec('key');
console.log(counter.getCount('key')); // 0 (key removed from map)
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`dec`](../../rate-limit.types/interfaces/RateLimitCounter#dec)

***

### getCount()

> **getCount**(`key`): `number`

Defined in: [rate-limit/simple-rate-limit-counter.ts:66](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L66)

Gets the current count for a key.

#### Parameters

##### key

`string`

The key to get count for

#### Returns

`number`

The current count (0 if key doesn't exist)

#### Example

```typescript
const counter = new SimpleRateLimitCounter();
console.log(counter.getCount('key')); // 0
counter.inc('key');
console.log(counter.getCount('key')); // 1
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`getCount`](../../rate-limit.types/interfaces/RateLimitCounter#getcount)

***

### inc()

> **inc**(`key`): `void`

Defined in: [rate-limit/simple-rate-limit-counter.ts:84](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/simple-rate-limit-counter.ts#L84)

Increments the count for a key.

#### Parameters

##### key

`string`

The key to increment

#### Returns

`void`

#### Example

```typescript
const counter = new SimpleRateLimitCounter();
counter.inc('user-123');
counter.inc('user-123');
console.log(counter.getCount('user-123')); // 2
```

#### Implementation of

[`RateLimitCounter`](../../rate-limit.types/interfaces/RateLimitCounter).[`inc`](../../rate-limit.types/interfaces/RateLimitCounter#inc)
