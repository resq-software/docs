# Class: Queue\<T\>

Defined in: [queue.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/queue.ts#L41)

A generic FIFO (First In, First Out) queue data structure.
Implements queue operations using a linked list for efficient O(1) enqueue and dequeue.

## Type Parameters

### T

`T`

The type of elements stored in the queue.

## Constructors

### Constructor

&gt; **new Queue**\<`T`\>(): `Queue`\<`T`\>

#### Returns

`Queue`\<`T`\>

## Methods

### dequeue()

&gt; **dequeue**(): `T` \| `null`

Defined in: [queue.ts:82](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/queue.ts#L82)

Remove and return the item at the front of the queue. O(1).

#### Returns

`T` \| `null`

The dequeued value, or `null` if the queue is empty.

***

### enqueue()

&gt; **enqueue**(`item`): `void`

Defined in: [queue.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/queue.ts#L61)

Append an item to the back of the queue. O(1).

#### Parameters

##### item

`T`

Value to store. The queue does not copy or freeze it.

#### Returns

`void`

***

### getSize()

&gt; **getSize**(): `number`

Defined in: [queue.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/queue.ts#L47)

#### Returns

`number`

The number of items currently in the queue.

***

### isEmpty()

&gt; **isEmpty**(): `boolean`

Defined in: [queue.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/queue.ts#L52)

#### Returns

`boolean`

`true` if the queue contains no items.
