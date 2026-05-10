# Class: KeyedThrottle\<T\>

Defined in: [throttle.ts:256](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L256)

Per-key throttle manager for throttling by specific keys
Useful for throttling per-endpoint or per-user

## Type Parameters

### T

`T` *extends* `AnyFunction`

## Constructors

### Constructor

> **new KeyedThrottle**\<`T`\>(`func`, `wait`, `options?`): `KeyedThrottle`\<`T`\>

Defined in: [throttle.ts:265](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L265)

#### Parameters

##### func

`T`

##### wait

`number`

##### options?

###### leading?

`boolean`

###### trailing?

`boolean`

#### Returns

`KeyedThrottle`\<`T`\>

## Methods

### cancel()

> **cancel**(`key`): `void`

Defined in: [throttle.ts:288](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L288)

Cancel throttle for specific key

#### Parameters

##### key

`string`

#### Returns

`void`

***

### cancelAll()

> **cancelAll**(): `void`

Defined in: [throttle.ts:299](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L299)

Cancel all throttles

#### Returns

`void`

***

### execute()

> **execute**(`key`, ...`args`): `ReturnType`\<`T`\> \| `undefined`

Defined in: [throttle.ts:274](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L274)

Execute function with throttling per key

#### Parameters

##### key

`string`

##### args

...`Parameters`\<`T`\>

#### Returns

`ReturnType`\<`T`\> \| `undefined`

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:309](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L309)

Get stats

#### Returns

`object`

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]
