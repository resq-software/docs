# Function: createReconnectTimer()

&gt; **createReconnectTimer**(`task`, `backoff?`): [`ReconnectTimer`](../interfaces/ReconnectTimer)

Defined in: [backoff.ts:94](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L94)

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
