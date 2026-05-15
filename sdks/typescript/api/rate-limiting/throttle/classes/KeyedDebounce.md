# Class: KeyedDebounce\<T\>

Defined in: [throttle.ts:367](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L367)

Per-key debounce manager — wraps [debounce](../functions/debounce) with a `Map` keyed
by user-supplied identifiers so different keys debounce
independently.

Typical use: per-input search-as-you-type, per-form auto-save,
per-resource validation. Memory grows with the number of distinct
keys; call [cancel](#cancel), [flush](#flush), or [cancelAll](#cancelall) to
release resources.

## Example

```ts
const search = new KeyedDebounce(runSearch, 300);
search.execute("filter:name", "ali");   // debounced per key
search.execute("filter:tag",  "team");  // independent timer
```

## Type Parameters

### T

`T` *extends* `AnyFunction`

Function being debounced.

## Constructors

### Constructor

> **new KeyedDebounce**\<`T`\>(`func`, `wait`, `options?`): `KeyedDebounce`\<`T`\>

Defined in: [throttle.ts:383](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L383)

#### Parameters

##### func

`T`

Function to debounce. The same instance is used for
  every key.

##### wait

`number`

Quiet window in milliseconds before firing.

##### options?

Forwarded to [debounce](../functions/debounce) for each key's
  internal debounced wrapper.

###### leading?

`boolean`

###### maxWait?

`number`

#### Returns

`KeyedDebounce`\<`T`\>

## Methods

### cancel()

> **cancel**(`key`): `void`

Defined in: [throttle.ts:408](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L408)

Cancel any pending fire for `key` and drop the bucket from the map.
The next `execute(key, …)` will start fresh.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

> **cancelAll**(): `void`

Defined in: [throttle.ts:432](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L432)

Cancel and drop every bucket.

#### Returns

`void`

***

### execute()

> **execute**(`key`, ...`args`): `void`

Defined in: [throttle.ts:393](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L393)

Push a new call for `key`, lazily creating the debounce bucket on
first invocation. Resets the quiet timer for that key.

#### Parameters

##### key

`string`

##### args

...`Parameters`\<`T`\>

#### Returns

`void`

***

### flush()

> **flush**(`key`): `void`

Defined in: [throttle.ts:424](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L424)

Cancel any pending timer for `key` without firing it. The bucket
stays alive — future `execute(key, …)` calls are still debounced.

(The wrapped `debounce(...).flush()` from this implementation
cancels rather than forces — see the `debounce` source for
specifics.)

#### Parameters

##### key

`string`

#### Returns

`void`

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:445](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L445)

Snapshot of currently-tracked keys.

#### Returns

`object`

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]
