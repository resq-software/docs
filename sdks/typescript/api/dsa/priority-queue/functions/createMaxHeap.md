# Function: createMaxHeap()

&gt; **createMaxHeap**\<`T`\>(...`args`): [`PriorityQueue`](../classes/PriorityQueue)\<`T`\>

Defined in: [priority-queue.ts:514](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L514)

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
