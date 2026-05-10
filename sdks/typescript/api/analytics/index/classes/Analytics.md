# Class: Analytics

Defined in: [index.ts:111](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L111)

## Constructors

### Constructor

> **new Analytics**(): `Analytics`

#### Returns

`Analytics`

## Accessors

### config

#### Get Signature

> **get** **config**(): `Readonly`\<[`AnalyticsConfig`](../interfaces/AnalyticsConfig)\> \| `null`

Defined in: [index.ts:116](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L116)

##### Returns

`Readonly`\<[`AnalyticsConfig`](../interfaces/AnalyticsConfig)\> \| `null`

***

### posthog

#### Get Signature

> **get** **posthog**(): `PostHog` \| `null`

Defined in: [index.ts:120](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L120)

##### Returns

`PostHog` \| `null`

## Methods

### identify()

> **identify**(`userId`, `traits?`): `void`

Defined in: [index.ts:181](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L181)

#### Parameters

##### userId

`string`

##### traits?

`Record`\<`string`, `unknown`\>

#### Returns

`void`

***

### init()

> **init**(`config`): `Promise`\<`void`\>

Defined in: [index.ts:124](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L124)

#### Parameters

##### config

[`AnalyticsConfig`](../interfaces/AnalyticsConfig)

#### Returns

`Promise`\<`void`\>

***

### pageview()

> **pageview**(`url?`): `void`

Defined in: [index.ts:211](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L211)

Manually emit a pageview. Most consumers do **not** need to call this:
PostHog's `capture_pageview: "history_change"` (set in init) auto-captures
SPA navigation, and GA4's Enhanced Measurement (UI default) does the same
for gtag.js. Only call manually if you've disabled both auto-captures, or
for first-paint pageviews before init has resolved.

#### Parameters

##### url?

`string`

#### Returns

`void`

***

### reset()

> **reset**(): `void`

Defined in: [index.ts:194](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L194)

#### Returns

`void`

***

### track()

> **track**\<`E`\>(`event`, `properties?`): `void`

Defined in: [index.ts:166](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/index.ts#L166)

#### Type Parameters

##### E

`E` *extends* `EventName`

#### Parameters

##### event

`E`

##### properties?

`E` *extends* `string` \| `number` ? [`AnalyticsEvents`](../interfaces/AnalyticsEvents)\[`E`\] : `Record`\<`string`, `unknown`\>

#### Returns

`void`
