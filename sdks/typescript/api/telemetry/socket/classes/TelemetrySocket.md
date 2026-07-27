# Class: TelemetrySocket

Defined in: [socket.ts:79](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L79)

A reconnecting WebSocket shared by many consumers.

## Example

```ts
const socket = new TelemetrySocket({ url: "wss://host/fleet/ws" });
const off = socket.subscribe({ onMessage: (raw) => handle(JSON.parse(raw)) });
socket.connect();
socket.send("subscribe:ops");
// later: off(); socket.close();
```

## Constructors

### Constructor

&gt; **new TelemetrySocket**(`options`): `TelemetrySocket`

Defined in: [socket.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L88)

#### Parameters

##### options

`Readonly`\<[`TelemetrySocketOptions`](../interfaces/TelemetrySocketOptions)\>

#### Returns

`TelemetrySocket`

## Accessors

### connected

#### Get Signature

&gt; **get** **connected**(): `boolean`

Defined in: [socket.ts:100](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L100)

Whether the socket is currently open.

##### Returns

`boolean`

***

### state

#### Get Signature

&gt; **get** **state**(): [`ConnectionState`](../../types/type-aliases/ConnectionState)

Defined in: [socket.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L95)

Current connection state.

##### Returns

[`ConnectionState`](../../types/type-aliases/ConnectionState)

## Methods

### close()

&gt; **close**(): `void`

Defined in: [socket.ts:114](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L114)

Close intentionally and stop reconnecting.

#### Returns

`void`

***

### connect()

&gt; **connect**(): `this`

Defined in: [socket.ts:105](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L105)

Open the connection (idempotent while already connecting/open).

#### Returns

`this`

***

### send()

&gt; **send**(`message`): `boolean`

Defined in: [socket.ts:126](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L126)

Send a frame; returns `false` (no-op) when not open.

#### Parameters

##### message

`string`

#### Returns

`boolean`

***

### subscribe()

&gt; **subscribe**(`subscription`): () =&gt; `void`

Defined in: [socket.ts:136](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/socket.ts#L136)

Attach a consumer. Returns an unsubscribe function.

#### Parameters

##### subscription

[`TelemetrySubscription`](../../types/interfaces/TelemetrySubscription)

#### Returns

() =&gt; `void`
