# Class: JsonTransport

Defined in: [transports.ts:94](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/transports.ts#L94)

Serializes each entry to a single JSON line and hands it to a sink
(`console.log` by default) — the shape most log aggregators ingest.

Serialization is defensive: an entry whose `data` cannot be stringified
(circular references, BigInt, …) is emitted with `data` replaced by a marker
rather than throwing.

## Implements

- [`LogTransport`](../../logger.types/interfaces/LogTransport)

## Constructors

### Constructor

&gt; **new JsonTransport**(`options?`): `JsonTransport`

Defined in: [transports.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/transports.ts#L102)

#### Parameters

##### options?

Optional transport `name` and a `sink` for each JSON line
  (defaults to `console.log`).

###### name?

`string`

###### sink?

(`line`) =&gt; `void`

#### Returns

`JsonTransport`

## Properties

### name

&gt; `readonly` **name**: `string`

Defined in: [transports.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/transports.ts#L95)

Transport name, used for identification and removal by name.

#### Implementation of

[`LogTransport`](../../logger.types/interfaces/LogTransport).[`name`](../../logger.types/interfaces/LogTransport#name)

## Methods

### write()

&gt; **write**(`entry`): `void`

Defined in: [transports.ts:117](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/transports.ts#L117)

Serialize the entry to one JSON line and hand it to the sink, substituting
a marker for `data` that cannot be stringified rather than throwing.

#### Parameters

##### entry

[`LogEntry`](../../logger.types/interfaces/LogEntry)

The log entry to serialize.

#### Returns

`void`

#### Implementation of

[`LogTransport`](../../logger.types/interfaces/LogTransport).[`write`](../../logger.types/interfaces/LogTransport#write)
