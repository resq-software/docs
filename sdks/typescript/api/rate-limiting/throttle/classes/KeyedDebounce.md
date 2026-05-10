# Class: KeyedDebounce\<T\>

Defined in: [throttle.ts:325](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L325)

Per-key debounce manager for debouncing by specific keys
Useful for debouncing per-endpoint or per-user

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Constructors

### Constructor

> **new KeyedDebounce**\<`T`\>(`func`, `wait`, `options?`): `KeyedDebounce`\<`T`\>

Defined in: [throttle.ts:334](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L334)

#### Parameters

##### func

`T`

##### wait

`number`

##### options?

###### leading?

`boolean`

###### maxWait?

`number`

#### Returns

`KeyedDebounce`\<`T`\>

## Methods

### cancel()

> **cancel**(`key`): `void`

Defined in: [throttle.ts:357](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L357)

Cancel debounce for specific key

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

> **cancelAll**(): `void`

Defined in: [throttle.ts:378](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L378)

Cancel all debounces

#### Returns

`void`

***

### execute()

> **execute**(`key`, ...`args`): `void`

Defined in: [throttle.ts:343](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L343)

Execute function with debouncing per key

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

Defined in: [throttle.ts:368](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L368)

Flush debounce for specific key (execute immediately)

#### Parameters

##### key

`string`

#### Returns

`void`

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:388](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L388)

Get stats

#### Returns

`object`

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]
