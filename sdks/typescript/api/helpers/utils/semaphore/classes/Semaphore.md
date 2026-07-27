# Class: Semaphore

Defined in: [packages/helpers/src/utils/semaphore.ts:57](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/semaphore.ts#L57)

An async counting semaphore that caps how many holders may proceed
concurrently. A caller `await`s [acquire](#acquire) before
entering the guarded section and must call [release](#release)
exactly once when finished — pair them with `try`/`finally`.

Waiters are released in FIFO order.

## Example

```ts
const gate = new Semaphore(2); // at most 2 concurrent fetches
await Promise.all(
  urls.map(async (url) => {
    await gate.acquire();
    try {
      return await fetch(url);
    } finally {
      gate.release();
    }
  }),
);
```

## Constructors

### Constructor

&gt; **new Semaphore**(`max`): `Semaphore`

Defined in: [packages/helpers/src/utils/semaphore.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/semaphore.ts#L66)

#### Parameters

##### max

`number`

Maximum number of holders allowed at once. Values `<= 0` block
  every acquirer until [setMax](#setmax) raises the limit.

#### Returns

`Semaphore`

## Methods

### acquire()

&gt; **acquire**(): `Promise`\<`void`\>

Defined in: [packages/helpers/src/utils/semaphore.ts:80](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/semaphore.ts#L80)

Acquire a slot; the returned promise resolves once one is available.

#### Returns

`Promise`\<`void`\>

***

### release()

&gt; **release**(): `void`

Defined in: [packages/helpers/src/utils/semaphore.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/semaphore.ts#L95)

Release a previously-acquired slot, letting the next waiter proceed.

Guarded against underflow: a stray release with no matching acquire is
ignored rather than driving the counter negative, which would silently
admit more than `max` concurrent holders. Ignoring (instead of throwing)
keeps `release()` safe to call from a `finally` block.

#### Returns

`void`

***

### setMax()

&gt; **setMax**(`max`): `void`

Defined in: [packages/helpers/src/utils/semaphore.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/semaphore.ts#L74)

Change the maximum concurrency. Raising it flushes any waiters that now
fit; lowering it only takes effect as in-flight holders release.

#### Parameters

##### max

`number`

#### Returns

`void`
