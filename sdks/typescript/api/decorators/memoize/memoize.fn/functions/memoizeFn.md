# Function: memoizeFn()

## Call Signature

&gt; **memoizeFn**\<`D`, `A`\>(`originalMethod`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:85](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.fn.ts#L85)

Wrap a method so its results are cached by argument key (function form of
[memoize](../..)).

The second argument selects the caching policy: omit it to cache forever, pass
a number for a TTL in milliseconds, or pass a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a
custom cache, key resolver, and/or expiry.

Each call to `memoizeFn` owns its own cache (closed over by the returned
function), so binding the method per instance yields independent caches. A
stored `null`/`undefined` is a genuine hit — presence is checked with the
cache's `has`, not by inspecting the value — so falsy results are cached
correctly. When `expirationTimeMs` is set, each written entry schedules a timer
that deletes it after the delay (a clock/timer effect); the entry is not
refreshed on read, so the TTL runs from insertion.

### Type Parameters

#### D

`D` = `unknown`

The return type of the original method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method whose results are cached.

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method, sharing one cache across all its invocations.

### Throws

When no `keyResolver` is configured and the arguments
contain a circular reference — the default key is `JSON.stringify(args)`, which
throws on circular input.

### Example

```ts
class ExpensiveOperations {
  calculatePrimes(max: number): number[] {
    const primes = [];
    for (let i = 2; i <= max; i++) {
      if (this.isPrime(i)) primes.push(i);
    }
    return primes;
  }
}

const ops = new ExpensiveOperations();

// Basic memoization.
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes.
const primes2 = memoized(1000); // Returns the cached result.

// With a TTL of 60 seconds.
const withTTL = memoizeFn(ops.calculatePrimes.bind(ops), 60000);

// With a custom config.
const withConfig = memoizeFn(ops.calculatePrimes.bind(ops), {
  cache: new Map(),
  keyResolver: (max) => `primes-${max}`,
  expirationTimeMs: 300000,
});
```

## Call Signature

&gt; **memoizeFn**\<`T`, `D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.fn.ts#L88)

Wrap a method so its results are cached by argument key (function form of
[memoize](../..)).

The second argument selects the caching policy: omit it to cache forever, pass
a number for a TTL in milliseconds, or pass a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a
custom cache, key resolver, and/or expiry.

Each call to `memoizeFn` owns its own cache (closed over by the returned
function), so binding the method per instance yields independent caches. A
stored `null`/`undefined` is a genuine hit — presence is checked with the
cache's `has`, not by inspecting the value — so falsy results are cached
correctly. When `expirationTimeMs` is set, each written entry schedules a timer
that deletes it after the delay (a clock/timer effect); the entry is not
refreshed on read, so the TTL runs from insertion.

### Type Parameters

#### T

`T` = `unknown`

The class type a `keyof T` key resolver resolves against.

#### D

`D` = `unknown`

The return type of the original method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method whose results are cached.

#### config

[`MemoizeConfig`](../../memoize.types/interfaces/MemoizeConfig)\<`T`, `D`\>

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method, sharing one cache across all its invocations.

### Throws

When no `keyResolver` is configured and the arguments
contain a circular reference — the default key is `JSON.stringify(args)`, which
throws on circular input.

### Example

```ts
class ExpensiveOperations {
  calculatePrimes(max: number): number[] {
    const primes = [];
    for (let i = 2; i <= max; i++) {
      if (this.isPrime(i)) primes.push(i);
    }
    return primes;
  }
}

const ops = new ExpensiveOperations();

// Basic memoization.
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes.
const primes2 = memoized(1000); // Returns the cached result.

// With a TTL of 60 seconds.
const withTTL = memoizeFn(ops.calculatePrimes.bind(ops), 60000);

// With a custom config.
const withConfig = memoizeFn(ops.calculatePrimes.bind(ops), {
  cache: new Map(),
  keyResolver: (max) => `primes-${max}`,
  expirationTimeMs: 300000,
});
```

## Call Signature

&gt; **memoizeFn**\<`D`, `A`\>(`originalMethod`, `expirationTimeMs`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.fn.ts#L92)

Wrap a method so its results are cached by argument key (function form of
[memoize](../..)).

The second argument selects the caching policy: omit it to cache forever, pass
a number for a TTL in milliseconds, or pass a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a
custom cache, key resolver, and/or expiry.

Each call to `memoizeFn` owns its own cache (closed over by the returned
function), so binding the method per instance yields independent caches. A
stored `null`/`undefined` is a genuine hit — presence is checked with the
cache's `has`, not by inspecting the value — so falsy results are cached
correctly. When `expirationTimeMs` is set, each written entry schedules a timer
that deletes it after the delay (a clock/timer effect); the entry is not
refreshed on read, so the TTL runs from insertion.

### Type Parameters

#### D

`D` = `unknown`

The return type of the original method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method whose results are cached.

#### expirationTimeMs

`number`

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method, sharing one cache across all its invocations.

### Throws

When no `keyResolver` is configured and the arguments
contain a circular reference — the default key is `JSON.stringify(args)`, which
throws on circular input.

### Example

```ts
class ExpensiveOperations {
  calculatePrimes(max: number): number[] {
    const primes = [];
    for (let i = 2; i <= max; i++) {
      if (this.isPrime(i)) primes.push(i);
    }
    return primes;
  }
}

const ops = new ExpensiveOperations();

// Basic memoization.
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes.
const primes2 = memoized(1000); // Returns the cached result.

// With a TTL of 60 seconds.
const withTTL = memoizeFn(ops.calculatePrimes.bind(ops), 60000);

// With a custom config.
const withConfig = memoizeFn(ops.calculatePrimes.bind(ops), {
  cache: new Map(),
  keyResolver: (max) => `primes-${max}`,
  expirationTimeMs: 300000,
});
```
