# Class: Queue\<T\>

Defined in: [queue.ts:32](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/queue.ts#L32)

A generic FIFO (First In, First Out) queue data structure.
Implements queue operations using a linked list for efficient O(1) enqueue and dequeue.

 Queue

## Type Parameters

### T

`T`

The type of elements stored in the queue

## Constructors

### Constructor

> **new Queue**\<`T`\>(): `Queue`\<`T`\>

#### Returns

`Queue`\<`T`\>

## Methods

### dequeue()

> **dequeue**(): `T` \| `null`

Defined in: [queue.ts:73](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/queue.ts#L73)

Remove and return the item at the front of the queue. O(1).

#### Returns

`T` \| `null`

The dequeued value, or `null` if the queue is empty.

***

### enqueue()

> **enqueue**(`item`): `void`

Defined in: [queue.ts:52](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/queue.ts#L52)

Append an item to the back of the queue. O(1).

#### Parameters

##### item

`T`

Value to store. The queue does not copy or freeze it.

#### Returns

`void`

***

### getSize()

> **getSize**(): `number`

Defined in: [queue.ts:38](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/queue.ts#L38)

#### Returns

`number`

The number of items currently in the queue.

***

### isEmpty()

> **isEmpty**(): `boolean`

Defined in: [queue.ts:43](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/queue.ts#L43)

#### Returns

`boolean`

`true` if the queue contains no items.
