# Function: createMinHeap()

&gt; **createMinHeap**\<`T`\>(...`args`): [`PriorityQueue`](../classes/PriorityQueue)\<`T`\>

Defined in: [priority-queue.ts:536](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L536)

Creates a min-heap priority queue (lowest value = highest priority).

For Comparable elements no options are required; for non-comparable
elements a `compareFn` is required (see [PQArgs](../type-aliases/PQArgs)).

## Type Parameters

### T

`T`

## Parameters

### args

...[`PQArgs`](../type-aliases/PQArgs)\<`T`\>

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<`T`\>

Min-heap priority queue
