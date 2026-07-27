# Function: createDeadlineQueue()

&gt; **createDeadlineQueue**(): [`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

Defined in: [priority-queue.ts:479](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L479)

Creates a priority queue of [PriorityRequestItem](../interfaces/PriorityRequestItem)s ordered purely by
`deadline`, so the soonest deadline is dequeued first.

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<[`PriorityRequestItem`](../interfaces/PriorityRequestItem)\>

A deadline-ordered priority queue.
