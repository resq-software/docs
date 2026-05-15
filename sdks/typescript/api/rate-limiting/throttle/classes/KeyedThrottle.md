# Class: KeyedThrottle\<T\>

Defined in: [throttle.ts:269](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L269)

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

> **new KeyedThrottle**\<`T`\>(`func`, `wait`, `options?`): `KeyedThrottle`\<`T`\>

Defined in: [throttle.ts:285](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L285)

#### Parameters

##### func

`T`

Function to throttle. The same instance is used for
  every key.

##### wait

`number`

Throttle window in milliseconds.

##### options?

Forwarded to [throttle](../functions/throttle) for each key's
  internal throttled wrapper.

###### leading?

`boolean`

###### trailing?

`boolean`

#### Returns

`KeyedThrottle`\<`T`\>

## Methods

### cancel()

> **cancel**(`key`): `void`

Defined in: [throttle.ts:314](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L314)

Cancel any pending trailing-edge call for `key` and drop the
bucket from the map. The next `execute(key, …)` will start fresh.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

> **cancelAll**(): `void`

Defined in: [throttle.ts:323](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L323)

Cancel and drop every bucket.

#### Returns

`void`

***

### execute()

> **execute**(`key`, ...`args`): `ReturnType`\<`T`\> \| `undefined`

Defined in: [throttle.ts:299](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L299)

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

> **getStats**(): `object`

Defined in: [throttle.ts:336](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L336)

Snapshot of currently-tracked keys.

#### Returns

`object`

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]
