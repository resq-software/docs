# Interface: UseAnalyticsReturn

Defined in: [react/index.ts:145](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L145)

Return type of [useAnalytics](../functions/useAnalytics).

Bundles the public method surface of the singleton plus a direct
reference to it for advanced callers (e.g. component-level
`groupIdentify`, `featureFlags`).

## Properties

### analytics

&gt; **analytics**: [`Analytics`](../../index/classes/Analytics)

Defined in: [react/index.ts:155](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L155)

Direct singleton reference for advanced PostHog/GA4 features not on this surface.

***

### identify

&gt; **identify**: (`userId`, `traits?`) =&gt; `void`

Defined in: [react/index.ts:149](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L149)

Bind an identity to the current session. Use on sign-in.

Bind an identity on the shared [analytics](../../index/variables/analytics) singleton. Convenience
wrapper over [Analytics.identify](../../index/classes/Analytics#identify).

#### Parameters

##### userId

`string`

The stable user identifier.

##### traits?

`Record`\<`string`, `unknown`\>

Optional user properties / person profile fields.

#### Returns

`void`

***

### pageview

&gt; **pageview**: (`url?`) =&gt; `void`

Defined in: [react/index.ts:153](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L153)

Manually emit a pageview (rarely needed — auto-capture is on by default).

Emit a manual pageview through the shared [analytics](../../index/variables/analytics) singleton.
Convenience wrapper over [Analytics.pageview](../../index/classes/Analytics#pageview).

#### Parameters

##### url?

`string`

Explicit page URL; defaults to the current location.

#### Returns

`void`

***

### reset

&gt; **reset**: () =&gt; `void`

Defined in: [react/index.ts:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L151)

Clear identity + provider state. Use on sign-out.

Clear identity and state on the shared [analytics](../../index/variables/analytics) singleton.
Convenience wrapper over [Analytics.reset](../../index/classes/Analytics#reset).

#### Returns

`void`

***

### track

&gt; **track**: \<`E`\>(`event`, ...`args`) =&gt; `void`

Defined in: [react/index.ts:147](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/react/index.ts#L147)

Type-safe `track(event, props)` — extend `AnalyticsEvents` for typed events.

Emit an event to every configured provider. Registered events (via
[AnalyticsEvents](../../index/interfaces/AnalyticsEvents) augmentation) get a typed, sometimes-required
payload; ad-hoc names accept an optional free-form bag. GA4 params are
flattened to primitives by primitivesOnly before dispatch.

Effectful, never throws: a no-op before [init](../../index/classes/Analytics#init) and while `disabled`
(a `debug` log still fires first). Otherwise forwards to `posthog.capture`
and pushes a gtag `event` command onto `window.dataLayer`.

#### Type Parameters

##### E

`E` *extends* `string`

The event name, narrowed to a registered key when one exists.

#### Parameters

##### event

`E`

The event name.

##### args

...[`TrackArgs`](../../index/type-aliases/TrackArgs)\<`E`\>

The event payload, shaped by [TrackArgs](../../index/type-aliases/TrackArgs).

#### Returns

`void`

#### Example

```ts
analytics.track("cta_clicked", { id: "hero" });
```
