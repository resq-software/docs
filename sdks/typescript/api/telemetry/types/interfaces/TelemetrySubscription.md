# Interface: TelemetrySubscription

Defined in: [types.ts:50](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/types.ts#L50)

A consumer attached to the shared socket. Every callback is optional so a
consumer subscribes only to what it needs (raw frames, lifecycle, or both).

## Methods

### onClose()?

&gt; `optional` **onClose**(): `void`

Defined in: [types.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/types.ts#L60)

Fired when the underlying socket closes (before any reconnect).

#### Returns

`void`

***

### onMessage()?

&gt; `optional` **onMessage**(`data`): `void`

Defined in: [types.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/types.ts#L52)

Every raw text frame from the socket.

#### Parameters

##### data

`string`

#### Returns

`void`

***

### onOpen()?

&gt; `optional` **onOpen**(): `void`

Defined in: [types.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/types.ts#L58)

Fired on every open — including immediately at subscribe time when the
socket is already connected — so late subscribers can (re)send channel
handshakes across reconnects.

#### Returns

`void`

***

### onStateChange()?

&gt; `optional` **onStateChange**(`state`): `void`

Defined in: [types.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/types.ts#L62)

Fired whenever the connection state changes.

#### Parameters

##### state

[`ConnectionState`](../type-aliases/ConnectionState)

#### Returns

`void`
