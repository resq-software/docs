# Class: KeyedThrottle\<T\>

Defined in: [throttle.ts:314](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L314)

Per-key throttle manager — wraps [throttle](../functions/throttle) with a `Map` keyed
by user-supplied identifiers so different keys throttle independently.

Use cases: per-endpoint throttles, per-user click handlers,
per-document save buffers. Memory grows with the number of distinct
keys; call [cancel](#cancel) or [cancelAll](#cancelall) to free resources.

## Example

```ts
const saveDoc = new KeyedThrottle(saveToServer, 1000);
saveDoc.execute("doc:42", payload);
saveDoc.execute("doc:43", payload);   // independent timer
```

## Type Parameters

### T

`T` *extends* `AnyFunction`

Function being throttled.

## Constructors

### Constructor

&gt; **new KeyedThrottle**\<`T`\>(`func`, `wait`, `options?`): `KeyedThrottle`\<`T`\>

Defined in: [throttle.ts:330](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L330)

#### Parameters

##### func

`T`

Function to throttle. The same instance is used for
  every key.

##### wait

`number`

Throttle window in milliseconds.

##### options?

`object` & `object` = `{}`

Forwarded to [throttle](../functions/throttle) for each key's
  internal throttled wrapper. Supports `maxKeys` configuration.

#### Returns

`KeyedThrottle`\<`T`\>

## Methods

### cancel()

&gt; **cancel**(`key`): `void`

Defined in: [throttle.ts:366](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L366)

Cancel any pending trailing-edge call for `key` and drop the
bucket from the map. The next `execute(key, …)` will start fresh.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

&gt; **cancelAll**(): `void`

Defined in: [throttle.ts:375](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L375)

Cancel and drop every bucket.

#### Returns

`void`

***

### execute()

&gt; **execute**(`key`, ...`args`): `ReturnType`\<`T`\> \| `undefined`

Defined in: [throttle.ts:351](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L351)

Invoke `func` under the throttle bucket associated with `key`,
lazily creating that bucket on first call.

#### Parameters

##### key

`string`

##### args

...`Parameters`\<`T`\>

#### Returns

`ReturnType`\<`T`\> \| `undefined`

Whatever the throttled call returns this tick — either
  the freshly-computed result, the cached previous result, or
  `undefined` if neither has fired yet.

***

### getStats()

&gt; **getStats**(): [`KeyedStats`](../type-aliases/KeyedStats)

Defined in: [throttle.ts:388](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L388)

Snapshot of currently-tracked keys.

#### Returns

[`KeyedStats`](../type-aliases/KeyedStats)

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.
