# Class: KeyedDebounce\<T\>

Defined in: [throttle.ts:419](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L419)

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

&gt; **new KeyedDebounce**\<`T`\>(`func`, `wait`, `options?`): `KeyedDebounce`\<`T`\>

Defined in: [throttle.ts:435](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L435)

#### Parameters

##### func

`T`

Function to debounce. The same instance is used for
  every key.

##### wait

`number`

Quiet window in milliseconds before firing.

##### options?

`object` & `object` = `{}`

Forwarded to [debounce](../functions/debounce) for each key's
  internal debounced wrapper. Supports `maxKeys` configuration.

#### Returns

`KeyedDebounce`\<`T`\>

## Methods

### cancel()

&gt; **cancel**(`key`): `void`

Defined in: [throttle.ts:467](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L467)

Cancel any pending fire for `key` and drop the bucket from the map.
The next `execute(key, …)` will start fresh.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

&gt; **cancelAll**(): `void`

Defined in: [throttle.ts:491](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L491)

Cancel and drop every bucket.

#### Returns

`void`

***

### execute()

&gt; **execute**(`key`, ...`args`): `void`

Defined in: [throttle.ts:452](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L452)

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

&gt; **flush**(`key`): `void`

Defined in: [throttle.ts:483](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L483)

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

&gt; **getStats**(): [`KeyedStats`](../type-aliases/KeyedStats)

Defined in: [throttle.ts:504](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L504)

Snapshot of currently-tracked keys.

#### Returns

[`KeyedStats`](../type-aliases/KeyedStats)

`{ activeKeys, keys }`. The `keys` array is a one-shot
  copy and not kept in sync with future mutations.
