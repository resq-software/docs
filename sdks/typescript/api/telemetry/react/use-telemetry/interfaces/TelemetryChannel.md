# Interface: TelemetryChannel

Defined in: [react/use-telemetry.ts:41](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/react/use-telemetry.ts#L41)

## Properties

### connected

&gt; **connected**: `boolean`

Defined in: [react/use-telemetry.ts:43](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/react/use-telemetry.ts#L43)

Whether the shared socket is currently open.

## Methods

### send()

&gt; **send**(`message`): `boolean`

Defined in: [react/use-telemetry.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/react/use-telemetry.ts#L45)

Send a frame on the shared socket; `false` when not open.

#### Parameters

##### message

`string`

#### Returns

`boolean`
