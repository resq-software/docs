# Interface: QueueNode\<T\>

Defined in: [queue.ts:28](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/queue.ts#L28)

A cell in the queue's singly-linked chain. Exposed because [Queue](../classes/Queue)
fields reference it, but callers rarely construct one directly.

## Type Parameters

### T

`T`

## Properties

### next

&gt; **next**: `QueueNode`\<`T`\> \| `null`

Defined in: [queue.ts:30](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/queue.ts#L30)

The next node toward the back of the queue, or `null` at the tail.

***

### value

&gt; **value**: `T`

Defined in: [queue.ts:32](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/queue.ts#L32)

The stored element, held by reference.
