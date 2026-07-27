# Function: createDeadlineQueue()

&gt; **createDeadlineQueue**(): [`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

Defined in: [priority-queue.ts:479](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L479)

Creates a priority queue of [PriorityRequestItem](../interfaces/PriorityRequestItem)s ordered purely by
`deadline`, so the soonest deadline is dequeued first.

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

A deadline-ordered priority queue.
