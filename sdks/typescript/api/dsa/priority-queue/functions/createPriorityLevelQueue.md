# Function: createPriorityLevelQueue()

&gt; **createPriorityLevelQueue**(): [`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

Defined in: [priority-queue.ts:492](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L492)

Creates a priority queue of [PriorityRequestItem](../interfaces/PriorityRequestItem)s ordered by
`priority` level (lower number = higher priority), breaking ties by earliest
`deadline`.

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

A priority-then-deadline ordered priority queue.
