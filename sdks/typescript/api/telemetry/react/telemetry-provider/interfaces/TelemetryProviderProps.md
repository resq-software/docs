# Interface: TelemetryProviderProps

Defined in: [react/telemetry-provider.tsx:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/react/telemetry-provider.tsx#L44)

## Extends

- [`TelemetrySocketOptions`](../../../socket/interfaces/TelemetrySocketOptions)

## Properties

### backoff?

&gt; `optional` **backoff?**: [`BackoffOptions`](../../../backoff/interfaces/BackoffOptions)

Defined in: [socket.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L54)

Reconnect backoff tuning.

#### Inherited from

[`TelemetrySocketOptions`](../../../socket/interfaces/TelemetrySocketOptions).[`backoff`](../../../socket/interfaces/TelemetrySocketOptions#backoff)

***

### children

&gt; **children**: `ReactNode`

Defined in: [react/telemetry-provider.tsx:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/react/telemetry-provider.tsx#L45)

***

### connect?

&gt; `optional` **connect?**: [`WebSocketFactory`](../../../types/type-aliases/WebSocketFactory)

Defined in: [socket.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L52)

WebSocket implementation factory. Defaults to the global `WebSocket`;
inject one to run under Node (`ws`) or in tests.

#### Inherited from

[`TelemetrySocketOptions`](../../../socket/interfaces/TelemetrySocketOptions).[`connect`](../../../socket/interfaces/TelemetrySocketOptions#connect)

***

### url

&gt; **url**: `string`

Defined in: [socket.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L47)

WebSocket URL to connect to (e.g. `wss://host/fleet/ws`).

#### Inherited from

[`TelemetrySocketOptions`](../../../socket/interfaces/TelemetrySocketOptions).[`url`](../../../socket/interfaces/TelemetrySocketOptions#url)
