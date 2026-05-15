# Interface: RateLimitCounter

Defined in: [rate-limit/rate-limit.types.ts:114](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.types.ts#L114)

Interface for rate limit counter implementations.
Used to track call counts within time windows.

 RateLimitCounter

## Example

```typescript
class InMemoryCounter implements RateLimitCounter {
  private counts = new Map<string, number>();

  inc(key: string): void {
    this.counts.set(key, (this.counts.get(key) ?? 0) + 1);
  }

  dec(key: string): void {
    const count = this.counts.get(key) ?? 0;
    if (count <= 1) {
      this.counts.delete(key);
    } else {
      this.counts.set(key, count - 1);
    }
  }

  getCount(key: string): number {
    return this.counts.get(key) ?? 0;
  }
}
```

## Properties

### dec

> **dec**: (`key`) => `void`

Defined in: [rate-limit/rate-limit.types.ts:118](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.types.ts#L118)

Decrement the count for a key

#### Parameters

##### key

`string`

#### Returns

`void`

***

### getCount

> **getCount**: (`key`) => `number`

Defined in: [rate-limit/rate-limit.types.ts:120](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.types.ts#L120)

Get the current count for a key

#### Parameters

##### key

`string`

#### Returns

`number`

***

### inc

> **inc**: (`key`) => `void`

Defined in: [rate-limit/rate-limit.types.ts:116](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.types.ts#L116)

Increment the count for a key

#### Parameters

##### key

`string`

#### Returns

`void`
