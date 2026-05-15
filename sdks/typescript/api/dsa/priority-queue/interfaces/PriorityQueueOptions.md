# Interface: PriorityQueueOptions\<T\>

Defined in: [priority-queue.ts:43](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/priority-queue.ts#L43)

Options for priority queue configuration

## Type Parameters

### T

`T`

## Properties

### compareFn?

> `optional` **compareFn?**: [`CompareFn`](../type-aliases/CompareFn)\<`T`\>

Defined in: [priority-queue.ts:45](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/priority-queue.ts#L45)

Custom comparison function (default: min-heap with numeric comparison)

***

### initialCapacity?

> `optional` **initialCapacity?**: `number`

Defined in: [priority-queue.ts:47](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/priority-queue.ts#L47)

Initial capacity for the underlying array
