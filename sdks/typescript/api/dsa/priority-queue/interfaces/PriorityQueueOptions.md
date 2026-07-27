# Interface: PriorityQueueOptions\<T\>

Defined in: [priority-queue.ts:43](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L43)

Options for priority-queue configuration.

## Type Parameters

### T

`T`

## Properties

### compareFn?

&gt; `optional` **compareFn?**: [`CompareFn`](../type-aliases/CompareFn)\<`T`\>

Defined in: [priority-queue.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L45)

Custom comparison function (default: min-heap with numeric comparison)

***

### initialCapacity?

&gt; `optional` **initialCapacity?**: `number`

Defined in: [priority-queue.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L47)

Initial capacity for the underlying array
