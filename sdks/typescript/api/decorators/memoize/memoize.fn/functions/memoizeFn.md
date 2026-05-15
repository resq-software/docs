# Function: memoizeFn()

## Call Signature

> **memoizeFn**\<`D`, `A`\>(`originalMethod`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.fn.ts#L80)

Wraps a method to cache its results based on arguments.

### Type Parameters

#### D

`D` = `any`

The return type of the original method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to memoize

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method

### Example

```typescript
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

// Basic memoization
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes
const primes2 = memoized(1000); // Returns cached result

// With TTL
const withTTL = memoizeFn(
  ops.calculatePrimes.bind(ops),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeFn(
  ops.calculatePrimes.bind(ops),
  {
    cache: new Map(),
    keyResolver: (max) => `primes-${max}`,
    expirationTimeMs: 300000
  }
);
```

## Call Signature

> **memoizeFn**\<`D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:83](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.fn.ts#L83)

Wraps a method to cache its results based on arguments.

### Type Parameters

#### D

`D` = `any`

The return type of the original method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to memoize

#### config

[`MemoizeConfig`](../../memoize.types/interfaces/MemoizeConfig)\<`any`, `D`\>

Configuration for memoization

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method

### Example

```typescript
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

// Basic memoization
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes
const primes2 = memoized(1000); // Returns cached result

// With TTL
const withTTL = memoizeFn(
  ops.calculatePrimes.bind(ops),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeFn(
  ops.calculatePrimes.bind(ops),
  {
    cache: new Map(),
    keyResolver: (max) => `primes-${max}`,
    expirationTimeMs: 300000
  }
);
```

## Call Signature

> **memoizeFn**\<`D`, `A`\>(`originalMethod`, `expirationTimeMs`): [`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

Defined in: [memoize/memoize.fn.ts:87](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.fn.ts#L87)

Wraps a method to cache its results based on arguments.

### Type Parameters

#### D

`D` = `any`

The return type of the original method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to memoize

#### expirationTimeMs

`number`

Cache expiration time in milliseconds

### Returns

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The memoized method

### Example

```typescript
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

// Basic memoization
const memoized = memoizeFn(ops.calculatePrimes.bind(ops));
const primes1 = memoized(1000); // Computes
const primes2 = memoized(1000); // Returns cached result

// With TTL
const withTTL = memoizeFn(
  ops.calculatePrimes.bind(ops),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeFn(
  ops.calculatePrimes.bind(ops),
  {
    cache: new Map(),
    keyResolver: (max) => `primes-${max}`,
    expirationTimeMs: 300000
  }
);
```
