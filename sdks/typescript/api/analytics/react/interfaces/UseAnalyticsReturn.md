# Interface: UseAnalyticsReturn

Defined in: [react/index.ts:73](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L73)

## Properties

### analytics

> **analytics**: [`Analytics`](../../index/classes/Analytics)

Defined in: [react/index.ts:78](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L78)

***

### identify

> **identify**: (`userId`, `traits?`) => `void`

Defined in: [react/index.ts:75](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L75)

#### Parameters

##### userId

`string`

##### traits?

`Record`\<`string`, `unknown`\>

#### Returns

`void`

***

### pageview

> **pageview**: (`url?`) => `void`

Defined in: [react/index.ts:77](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L77)

#### Parameters

##### url?

`string`

#### Returns

`void`

***

### reset

> **reset**: () => `void`

Defined in: [react/index.ts:76](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L76)

#### Returns

`void`

***

### track

> **track**: \<`E`\>(`event`, `properties?`) => `void`

Defined in: [react/index.ts:74](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/react/index.ts#L74)

#### Type Parameters

##### E

`E` *extends* `EventName`

#### Parameters

##### event

`E`

##### properties?

`E` *extends* `string` \| `number` ? [`AnalyticsEvents`](../../index/interfaces/AnalyticsEvents)\[`E`\] : `Record`\<`string`, `unknown`\>

#### Returns

`void`
