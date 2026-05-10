# Interface: PriorityRequestItem

Defined in: [priority-queue.ts:423](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L423)

Priority request item

## Properties

### deadline

> **deadline**: `Date`

Defined in: [priority-queue.ts:427](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L427)

Response deadline

***

### id

> **id**: `string`

Defined in: [priority-queue.ts:425](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L425)

Request ID

***

### metadata?

> `optional` **metadata?**: `Record`\<`string`, `unknown`\>

Defined in: [priority-queue.ts:433](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L433)

Additional metadata

***

### priority

> **priority**: `number`

Defined in: [priority-queue.ts:429](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L429)

Priority level (1 = highest)

***

### status

> **status**: `string`

Defined in: [priority-queue.ts:431](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L431)

Request status
