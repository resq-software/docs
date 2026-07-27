# Class: MemoryTransport

Defined in: [transports.ts:46](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L46)

Buffers log entries in memory for inspection or testing.

Optionally bounded: once `capacity` entries are held, the oldest are dropped
(a ring buffer), so it is safe to leave attached in long-running processes.

## Example

```ts
const mem = new MemoryTransport({ capacity: 100 });
const off = Logger.addTransport(mem);
logger.info("hi");
expect(mem.entries.at(-1)?.message).toBe("hi");
off();
```

## Implements

- [`LogTransport`](../../logger.types/interfaces/LogTransport)

## Constructors

### Constructor

&gt; **new MemoryTransport**(`options?`): `MemoryTransport`

Defined in: [transports.ts:55](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L55)

#### Parameters

##### options?

Optional transport `name` and buffer `capacity`; a
  non-positive or omitted capacity means unbounded.

###### capacity?

`number`

###### name?

`string`

#### Returns

`MemoryTransport`

## Properties

### name

&gt; `readonly` **name**: `string`

Defined in: [transports.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L47)

Transport name, used for identification and removal by name.

#### Implementation of

[`LogTransport`](../../logger.types/interfaces/LogTransport).[`name`](../../logger.types/interfaces/LogTransport#name)

## Accessors

### entries

#### Get Signature

&gt; **get** **entries**(): readonly [`LogEntry`](../../logger.types/interfaces/LogEntry)[]

Defined in: [transports.ts:76](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L76)

A snapshot of the buffered entries, oldest first.

##### Returns

readonly [`LogEntry`](../../logger.types/interfaces/LogEntry)[]

## Methods

### clear()

&gt; **clear**(): `void`

Defined in: [transports.ts:81](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L81)

Discard all buffered entries.

#### Returns

`void`

***

### write()

&gt; **write**(`entry`): `void`

Defined in: [transports.ts:68](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/transports.ts#L68)

Append an entry, evicting the oldest entries once `capacity` is exceeded.

#### Parameters

##### entry

[`LogEntry`](../../logger.types/interfaces/LogEntry)

The log entry to buffer.

#### Returns

`void`

#### Implementation of

[`LogTransport`](../../logger.types/interfaces/LogTransport).[`write`](../../logger.types/interfaces/LogTransport#write)
