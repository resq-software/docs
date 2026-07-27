# Function: createReconnectTimer()

&gt; **createReconnectTimer**(`task`, `backoff?`): [`ReconnectTimer`](../interfaces/ReconnectTimer)

Defined in: [backoff.ts:94](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/telemetry/src/backoff.ts#L94)

Bind a backoff schedule to a single pending `setTimeout`.

## Parameters

### task

() =&gt; `void`

Reconnect callback (e.g. the socket's `connect()` closure).

### backoff?

[`Backoff`](../interfaces/Backoff) = `...`

Schedule to consume; defaults to `createBackoff()`.

## Returns

[`ReconnectTimer`](../interfaces/ReconnectTimer)
