# Class: Queue\<T\>

Defined in: [queue.ts:32](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/queue.ts#L32)

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

Defined in: [queue.ts:61](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/queue.ts#L61)

#### Returns

`T` \| `null`

***

### enqueue()

> **enqueue**(`item`): `void`

Defined in: [queue.ts:45](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/queue.ts#L45)

#### Parameters

##### item

`T`

#### Returns

`void`

***

### getSize()

> **getSize**(): `number`

Defined in: [queue.ts:37](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/queue.ts#L37)

#### Returns

`number`

***

### isEmpty()

> **isEmpty**(): `boolean`

Defined in: [queue.ts:41](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/queue.ts#L41)

#### Returns

`boolean`
