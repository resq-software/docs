# Interface: LogTransport

Defined in: [logger.types.ts:140](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L140)

Contract for a custom log transport that receives structured [LogEntry](./LogEntry)
values (see [Logger.addTransport](../../logger/classes/Logger#addtransport)).

A transport's [LogTransport.write](#write) runs inside the emitting log call.
Errors are isolated by [Logger](../../logger/classes/Logger): a synchronous throw is caught and a
rejected promise is swallowed, so a failing transport never breaks the log
call or sibling transports — but it also means write failures are silent, so a
transport that needs delivery guarantees must handle its own errors.

## Properties

### name

&gt; **name**: `string`

Defined in: [logger.types.ts:142](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L142)

Transport name, used for identification and removal by name.

## Methods

### write()

&gt; **write**(`entry`): `void` \| `Promise`\<`void`\>

Defined in: [logger.types.ts:148](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L148)

Write a single entry. May run synchronously or return a promise; the
returned promise is not awaited by the logger, only guarded against
rejection, so ordering across async transports is not guaranteed.

#### Parameters

##### entry

[`LogEntry`](./LogEntry)

#### Returns

`void` \| `Promise`\<`void`\>
