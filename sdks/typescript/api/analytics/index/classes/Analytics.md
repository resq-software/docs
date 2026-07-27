# Class: Analytics

Defined in: [index.ts:261](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L261)

Unified analytics facade over PostHog and GA4. A single shared instance
([analytics](../variables/analytics)) is initialised once via [Analytics.init](#init); every
method is a no-op until then and while `disabled`, so call sites never need
their own guards.

PostHog is imported lazily on init so non-analytics page loads pay nothing,
and every event fans out to whichever providers are configured.

## Example

```ts
const a = new Analytics();
await a.init({ posthog: { key: "phc_…" } });
a.track("cta_clicked", { id: "hero" });
```

## Constructors

### Constructor

&gt; **new Analytics**(): `Analytics`

#### Returns

`Analytics`

## Accessors

### config

#### Get Signature

&gt; **get** **config**(): `Readonly`\<[`AnalyticsConfig`](../interfaces/AnalyticsConfig)\> \| `null`

Defined in: [index.ts:267](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L267)

The active configuration, or `null` before init / after [reset](../functions/reset).

##### Returns

`Readonly`\<[`AnalyticsConfig`](../interfaces/AnalyticsConfig)\> \| `null`

***

### posthog

#### Get Signature

&gt; **get** **posthog**(): `PostHog` \| `null`

Defined in: [index.ts:276](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L276)

The lazily-loaded PostHog client, or `null` until PostHog init resolves.
Exposed for advanced features (feature flags, group identify) not on this
facade.

##### Returns

`PostHog` \| `null`

## Methods

### identify()

&gt; **identify**(`userId`, `traits?`): `void`

Defined in: [index.ts:384](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L384)

Bind a stable identity to the current session across both providers. Call
on sign-in; GA4 traits are flattened to primitives and the `user_id` is set
on the measurement config.

Effectful, never throws: a no-op before [init](#init) and while `disabled`
(a `debug` log still fires first). Otherwise calls `posthog.identify` and
emits gtag `set`/`config` commands on `window.dataLayer`.

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

### init()

&gt; **init**(`config`): `Promise`\<`void`\>

Defined in: [index.ts:300](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L300)

Initialise the client and lazily boot the configured providers.

Idempotent and not cancellable: the first call wins and every later call
returns the *same* cached promise — the second call's `config` is ignored,
so a double-mount never re-inits PostHog / GA4. Concurrent calls are safe
for this reason; there is no `AbortSignal`.

Effects (browser only, when not `disabled`): dynamically imports
`posthog-js`, calls `posthog.init`, injects the gtag.js `<script>` into
`document.head`, pushes commands onto `window.dataLayer`, and stores the
config and PostHog client on this instance. On the server or when
`config.disabled` is set it resolves immediately with no effects.

#### Parameters

##### config

[`AnalyticsConfig`](../interfaces/AnalyticsConfig)

PostHog/GA4 credentials plus cross-subdomain and debug flags.

#### Returns

`Promise`\<`void`\>

A promise that resolves once provider bootstrapping has settled.
  It **rejects** if the `posthog-js` dynamic import fails (e.g. a chunk
  load error) or `posthog.init` throws; because the promise is cached, a
  failed init is never retried — every later call re-returns the rejection.

***

### pageview()

&gt; **pageview**(`url?`): `void`

Defined in: [index.ts:430](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L430)

Manually emit a pageview. Most consumers do **not** need to call this:
PostHog's `capture_pageview: "history_change"` (set in init) auto-captures
SPA navigation, and GA4's Enhanced Measurement (UI default) does the same
for gtag.js. Only call manually if you've disabled both auto-captures, or
for first-paint pageviews before init has resolved.

Effectful, never throws: a no-op before [init](#init) and while `disabled`
(no `debug` log here, unlike `track`/`identify`). Otherwise emits a PostHog
`$pageview` and a gtag `page_view` event.

#### Parameters

##### url?

`string`

Explicit page URL; defaults to the current location.

#### Returns

`void`

***

### reset()

&gt; **reset**(): `void`

Defined in: [index.ts:407](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L407)

Clear the bound identity and tear down local state. Call on sign-out: it
clears GA4's `user_id`, resets PostHog, and drops the cached config so a
later [init](#init) can boot cleanly.

Effectful, never throws, and idempotent: it runs regardless of the
`disabled` flag, and mutates instance state (`config`, `posthog`, and the
cached init promise all reset to `null`). Calling it on an uninitialised
instance is a harmless no-op.

#### Returns

`void`

***

### track()

&gt; **track**\<`E`\>(`event`, ...`args`): `void`

Defined in: [index.ts:359](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L359)

Emit an event to every configured provider. Registered events (via
[AnalyticsEvents](../interfaces/AnalyticsEvents) augmentation) get a typed, sometimes-required
payload; ad-hoc names accept an optional free-form bag. GA4 params are
flattened to primitives by primitivesOnly before dispatch.

Effectful, never throws: a no-op before [init](#init) and while `disabled`
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

...[`TrackArgs`](../type-aliases/TrackArgs)\<`E`\>

The event payload, shaped by [TrackArgs](../type-aliases/TrackArgs).

#### Returns

`void`

#### Example

```ts
analytics.track("cta_clicked", { id: "hero" });
```
