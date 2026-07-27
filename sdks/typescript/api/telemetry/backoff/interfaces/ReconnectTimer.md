# Interface: ReconnectTimer

Defined in: [backoff.ts:74](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L74)

## Methods

### cancel()

&gt; **cancel**(): `void`

Defined in: [backoff.ts:81](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L81)

Cancel a pending run; no-op when idle.

#### Returns

`void`

***

### pending()

&gt; **pending**(): `boolean`

Defined in: [backoff.ts:85](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L85)

Whether a run is currently armed.

#### Returns

`boolean`

***

### reset()

&gt; **reset**(): `void`

Defined in: [backoff.ts:83](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L83)

Reset the underlying backoff schedule — call on a successful open.

#### Returns

`void`

***

### schedule()

&gt; **schedule**(): `number`

Defined in: [backoff.ts:79](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L79)

Arm `task` after the next backoff delay (replacing any pending run).
Returns the delay used, mostly for logging / tests.

#### Returns

`number`
