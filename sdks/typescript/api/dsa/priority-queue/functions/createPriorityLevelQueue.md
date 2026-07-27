# Function: createPriorityLevelQueue()

&gt; **createPriorityLevelQueue**(): [`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

Defined in: [priority-queue.ts:492](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L492)

Creates a priority queue of [PriorityRequestItem](../interfaces/PriorityRequestItem)s ordered by
`priority` level (lower number = higher priority), breaking ties by earliest
`deadline`.

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

A priority-then-deadline ordered priority queue.
