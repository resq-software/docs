# Interface: WebSocketLike

Defined in: [types.ts:33](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L33)

The minimal WebSocket surface the client relies on. Both the browser
`WebSocket` and the Node `ws` package satisfy this structurally, so the
transport stays environment-agnostic and free of a DOM dependency.

## Properties

### onclose

&gt; **onclose**: ((`event`) =&gt; `void`) \| `null`

Defined in: [types.ts:39](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L39)

***

### onerror

&gt; **onerror**: ((`event`) =&gt; `void`) \| `null`

Defined in: [types.ts:40](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L40)

***

### onmessage

&gt; **onmessage**: ((`event`) =&gt; `void`) \| `null`

Defined in: [types.ts:38](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L38)

***

### onopen

&gt; **onopen**: ((`event`) =&gt; `void`) \| `null`

Defined in: [types.ts:37](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L37)

***

### readyState

&gt; `readonly` **readyState**: `number`

Defined in: [types.ts:34](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L34)

## Methods

### close()

&gt; **close**(`code?`, `reason?`): `void`

Defined in: [types.ts:36](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L36)

#### Parameters

##### code?

`number`

##### reason?

`string`

#### Returns

`void`

***

### send()

&gt; **send**(`data`): `void`

Defined in: [types.ts:35](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/types.ts#L35)

#### Parameters

##### data

`string`

#### Returns

`void`
