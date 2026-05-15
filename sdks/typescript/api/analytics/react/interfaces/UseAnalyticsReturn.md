# Interface: UseAnalyticsReturn

Defined in: [react/index.ts:134](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L134)

Return type of [useAnalytics](../functions/useAnalytics).

Bundles the public method surface of the singleton plus a direct
reference to it for advanced callers (e.g. component-level
`groupIdentify`, `featureFlags`).

## Properties

### analytics

> **analytics**: [`Analytics`](../../index/classes/Analytics)

Defined in: [react/index.ts:144](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L144)

Direct singleton reference for advanced PostHog/GA4 features not on this surface.

***

### identify

> **identify**: (`userId`, `traits?`) => `void`

Defined in: [react/index.ts:138](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L138)

Bind an identity to the current session. Use on sign-in.

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

Defined in: [react/index.ts:142](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L142)

Manually emit a pageview (rarely needed — auto-capture is on by default).

#### Parameters

##### url?

`string`

#### Returns

`void`

***

### reset

> **reset**: () => `void`

Defined in: [react/index.ts:140](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L140)

Clear identity + provider state. Use on sign-out.

#### Returns

`void`

***

### track

> **track**: \<`E`\>(`event`, `properties?`) => `void`

Defined in: [react/index.ts:136](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/analytics/src/react/index.ts#L136)

Type-safe `track(event, props)` — extend `AnalyticsEvents` for typed events.

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
