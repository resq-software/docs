# Interface: TelemetrySocketOptions

Defined in: [socket.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/socket.ts#L45)

## Extended by

- [`TelemetryProviderProps`](../../react/telemetry-provider/interfaces/TelemetryProviderProps)

## Properties

### backoff?

&gt; `optional` **backoff?**: [`BackoffOptions`](../../backoff/interfaces/BackoffOptions)

Defined in: [socket.ts:54](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/socket.ts#L54)

Reconnect backoff tuning.

***

### connect?

&gt; `optional` **connect?**: [`WebSocketFactory`](../../types/type-aliases/WebSocketFactory)

Defined in: [socket.ts:52](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/socket.ts#L52)

WebSocket implementation factory. Defaults to the global `WebSocket`;
inject one to run under Node (`ws`) or in tests.

***

### url

&gt; **url**: `string`

Defined in: [socket.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/socket.ts#L47)

WebSocket URL to connect to (e.g. `wss://host/fleet/ws`).
