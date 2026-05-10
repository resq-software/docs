# Class: PriorityQueue\<T\>

Defined in: [priority-queue.ts:97](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L97)

Priority Queue implemented as a Binary Heap

By default, this is a min-heap where the smallest element has highest priority.
Use a custom compareFn for max-heap or custom ordering.

Time Complexity:
- enqueue (insert): O(log n)
- dequeue (extractMin/Max): O(log n)
- peek: O(1)
- contains: O(n)
- updatePriority: O(n + log n)

Space Complexity: O(n)

## Example

```typescript
// Min-heap by deadline
const requestQueue = new PriorityQueue<Request>({
  compareFn: (a, b) => a.deadline.getTime() - b.deadline.getTime()
});

requestQueue.enqueue({ id: '1', deadline: new Date('2025-01-15') });
requestQueue.enqueue({ id: '2', deadline: new Date('2025-01-10') });

const mostUrgent = requestQueue.dequeue();
// Returns request with deadline 2025-01-10
```

## Type Parameters

### T

`T`

Type of elements in the queue

## Constructors

### Constructor

> **new PriorityQueue**\<`T`\>(`options?`): `PriorityQueue`\<`T`\>

Defined in: [priority-queue.ts:106](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L106)

Creates a new Priority Queue

#### Parameters

##### options?

[`PriorityQueueOptions`](../interfaces/PriorityQueueOptions.md)\<`T`\> = `{}`

Configuration options

#### Returns

`PriorityQueue`\<`T`\>

#### Throws

Error if options validation fails

## Accessors

### isEmpty

#### Get Signature

> **get** **isEmpty**(): `boolean`

Defined in: [priority-queue.ts:142](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L142)

Checks if the queue is empty

##### Returns

`boolean`

***

### size

#### Get Signature

> **get** **size**(): `number`

Defined in: [priority-queue.ts:135](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L135)

Returns the number of elements in the queue

##### Returns

`number`

## Methods

### clear()

> **clear**(): `void`

Defined in: [priority-queue.ts:287](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L287)

Clears all elements from the queue

#### Returns

`void`

***

### contains()

> **contains**(`element`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:243](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L243)

Checks if an element exists in the queue

#### Parameters

##### element

`T`

Element to find

##### equalsFn?

(`a`, `b`) => `boolean`

Optional equality function

#### Returns

`boolean`

True if the element exists

***

### dequeue()

> **dequeue**(): `T` \| `undefined`

Defined in: [priority-queue.ts:176](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L176)

Removes and returns the highest priority element

#### Returns

`T` \| `undefined`

The highest priority element or undefined if empty

***

### drain()

> **drain**(): `T`[]

Defined in: [priority-queue.ts:253](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L253)

Returns all elements in priority order (drains the queue)

#### Returns

`T`[]

Array of elements in priority order

***

### enqueue()

> **enqueue**(`element`): `this`

Defined in: [priority-queue.ts:152](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L152)

Adds an element to the queue

#### Parameters

##### element

`T`

Element to add

#### Returns

`this`

This queue for chaining

***

### enqueueAll()

> **enqueueAll**(`elements`): `this`

Defined in: [priority-queue.ts:164](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L164)

Adds multiple elements to the queue

#### Parameters

##### elements

`T`[]

Elements to add

#### Returns

`this`

This queue for chaining

***

### getStats()

> **getStats**(): [`PriorityQueueStats`](../interfaces/PriorityQueueStats.md)

Defined in: [priority-queue.ts:296](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L296)

Gets queue statistics

#### Returns

[`PriorityQueueStats`](../interfaces/PriorityQueueStats.md)

Queue statistics

***

### peek()

> **peek**(): `T` \| `undefined`

Defined in: [priority-queue.ts:197](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L197)

Returns the highest priority element without removing it

#### Returns

`T` \| `undefined`

The highest priority element or undefined if empty

***

### remove()

> **remove**(`element`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:208](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L208)

Removes a specific element from the queue

#### Parameters

##### element

`T`

Element to remove

##### equalsFn?

(`a`, `b`) => `boolean`

Optional equality function (default: strict equality)

#### Returns

`boolean`

True if the element was found and removed

***

### toArray()

> **toArray**(): `T`[]

Defined in: [priority-queue.ts:270](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L270)

Returns all elements as an array (does not drain)
Note: Order is not guaranteed to be in priority order

#### Returns

`T`[]

Copy of internal array

***

### toSortedArray()

> **toSortedArray**(): `T`[]

Defined in: [priority-queue.ts:279](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L279)

Returns elements in priority order without modifying the queue

#### Returns

`T`[]

Array of elements in priority order

***

### updatePriority()

> **updatePriority**(`oldElement`, `newElement`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:228](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L228)

Updates an element's priority by removing and re-adding it

#### Parameters

##### oldElement

`T`

Element to update

##### newElement

`T`

New element with updated priority

##### equalsFn?

(`a`, `b`) => `boolean`

Optional equality function

#### Returns

`boolean`

True if the element was found and updated

***

### from()

> `static` **from**\<`T`\>(`elements`, `options?`): `PriorityQueue`\<`T`\>

Defined in: [priority-queue.ts:311](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/priority-queue.ts#L311)

Creates a new priority queue from an array

#### Type Parameters

##### T

`T`

#### Parameters

##### elements

`T`[]

Elements to add

##### options?

[`PriorityQueueOptions`](../interfaces/PriorityQueueOptions.md)\<`T`\> = `{}`

Queue options

#### Returns

`PriorityQueue`\<`T`\>

New priority queue with elements
