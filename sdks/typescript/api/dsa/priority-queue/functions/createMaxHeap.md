# Function: createMaxHeap()

&gt; **createMaxHeap**\<`T`\>(...`args`): [`PriorityQueue`](../classes/PriorityQueue)\<`T`\>

Defined in: [priority-queue.ts:514](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L514)

Creates a max-heap priority queue (highest value = highest priority).

For Comparable elements the ordering is derived automatically. For
non-comparable elements a `compareFn` is required (min-ordering semantics);
it is wrapped so the largest element sits at the head.

## Type Parameters

### T

`T`

## Parameters

### args

...[`PQArgs`](../type-aliases/PQArgs)\<`T`\>

## Returns

[`PriorityQueue`](../classes/PriorityQueue)\<`T`\>

Max-heap priority queue
