# Interface: RateLimitCounter

Defined in: [rate-limit/rate-limit.types.ts:100](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L100)

Synchronous counter contract used to track call counts within time windows.

`getCount` must return `0` (never negative or `undefined`) for a key that was
never incremented or has been fully decremented. `rateLimitFn` increments on an
admitted call and schedules a matching `dec` after the window, so `inc` and
`dec` must be balanced for the count to reflect the live in-window total.

## Example

```ts
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

&gt; **dec**: (`key`) =&gt; `void`

Defined in: [rate-limit/rate-limit.types.ts:104](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L104)

Decrement the count for a key.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### getCount

&gt; **getCount**: (`key`) =&gt; `number`

Defined in: [rate-limit/rate-limit.types.ts:106](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L106)

Get the current count for a key.

#### Parameters

##### key

`string`

#### Returns

`number`

***

### inc

&gt; **inc**: (`key`) =&gt; `void`

Defined in: [rate-limit/rate-limit.types.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L102)

Increment the count for a key.

#### Parameters

##### key

`string`

#### Returns

`void`
