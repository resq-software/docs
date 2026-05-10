# Interface: IRateLimitStore

Defined in: [rate-limit.ts:51](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L51)

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:52](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L52)

#### Parameters

##### key

`string`

##### windowMs

`number`

##### maxRequests

`number`

#### Returns

`Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

***

### reset()

> **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:53](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L53)

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>
