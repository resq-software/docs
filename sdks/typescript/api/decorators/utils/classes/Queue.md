# Class: Queue\<T\>

Defined in: [\_utils.ts:85](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L85)

A minimal linked-list FIFO queue with O(1) enqueue and dequeue.

## Type Parameters

### T

`T`

## Constructors

### Constructor

&gt; **new Queue**\<`T`\>(): `Queue`\<`T`\>

#### Returns

`Queue`\<`T`\>

## Methods

### dequeue()

&gt; **dequeue**(): `T` \| `null`

Defined in: [\_utils.ts:132](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L132)

Remove and return the item at the head of the queue.

Mutates the queue in place: unlinks the head node and decrements the size.
Signals emptiness by returning the sentinel `null` rather than throwing, so
a stored `null` value is indistinguishable from "empty" — do not enqueue
`null` if you rely on the return to detect drain.

#### Returns

`T` \| `null`

The dequeued item, or `null` when the queue is empty.

***

### enqueue()

&gt; **enqueue**(`item`): `void`

Defined in: [\_utils.ts:108](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L108)

Append an item to the tail of the queue.

Mutates the queue in place: links a new node at the tail and increments the
size. Not idempotent — each call adds a distinct entry, duplicates included.

#### Parameters

##### item

`T`

The value to enqueue.

#### Returns

`void`

***

### getSize()

&gt; **getSize**(): `number`

Defined in: [\_utils.ts:91](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L91)

Return the number of queued items.

#### Returns

`number`

***

### isEmpty()

&gt; **isEmpty**(): `boolean`

Defined in: [\_utils.ts:96](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/_utils.ts#L96)

Return `true` when the queue holds no items.

#### Returns

`boolean`
