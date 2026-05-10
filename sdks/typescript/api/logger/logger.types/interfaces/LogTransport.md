# Interface: LogTransport

Defined in: [logger.types.ts:99](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L99)

Interface for custom log transports

## Properties

### name

> **name**: `string`

Defined in: [logger.types.ts:101](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L101)

Transport name for identification

## Methods

### write()

> **write**(`entry`): `void` \| `Promise`\<`void`\>

Defined in: [logger.types.ts:103](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L103)

Method to write a log entry

#### Parameters

##### entry

[`LogEntry`](./LogEntry)

#### Returns

`void` \| `Promise`\<`void`\>
