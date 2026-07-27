# Class: PriorityQueue\<T\>

Defined in: [priority-queue.ts:125](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L125)

Priority queue implemented as a binary heap.

By default this is a min-heap where the smallest element has highest
priority. Supply a custom `compareFn` for a max-heap or bespoke ordering.

Time Complexity:
- enqueue (insert): O(log n)
- dequeue (extractMin/Max): O(log n)
- peek: O(1)
- contains: O(n)
- updatePriority: O(n + log n)

Space Complexity: O(n)

## Example

```ts
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

&gt; **new PriorityQueue**\<`T`\>(...`args`): `PriorityQueue`\<`T`\>

Defined in: [priority-queue.ts:136](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L136)

Creates a new priority queue.

#### Parameters

##### args

...[`PQArgs`](../type-aliases/PQArgs)\<`T`\>

#### Returns

`PriorityQueue`\<`T`\>

#### Throws

If options validation fails.

## Accessors

### isEmpty

#### Get Signature

&gt; **get** **isEmpty**(): `boolean`

Defined in: [priority-queue.ts:174](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L174)

Whether the queue currently holds no elements.

##### Returns

`boolean`

***

### size

#### Get Signature

&gt; **get** **size**(): `number`

Defined in: [priority-queue.ts:167](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L167)

Returns the number of elements in the queue.

##### Returns

`number`

## Methods

### clear()

&gt; **clear**(): `void`

Defined in: [priority-queue.ts:324](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L324)

Removes all elements from the queue.

#### Returns

`void`

***

### contains()

&gt; **contains**(`element`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:278](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L278)

Checks whether an element exists in the queue. Linear scan, `O(n)`.

#### Parameters

##### element

`T`

Element to find.

##### equalsFn?

(`a`, `b`) =&gt; `boolean`

Equality predicate. Defaults to strict `===`.

#### Returns

`boolean`

`true` if a matching element exists.

***

### dequeue()

&gt; **dequeue**(): `T` \| `undefined`

Defined in: [priority-queue.ts:209](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L209)

Removes and returns the highest-priority element.

#### Returns

`T` \| `undefined`

The highest-priority element, or `undefined` if the queue is
  empty.

***

### drain()

&gt; **drain**(): `T`[]

Defined in: [priority-queue.ts:288](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L288)

Removes and returns all elements in priority order, emptying the queue.

#### Returns

`T`[]

The elements in priority order.

***

### enqueue()

&gt; **enqueue**(`element`): `this`

Defined in: [priority-queue.ts:184](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L184)

Adds an element to the queue, restoring the heap invariant.

#### Parameters

##### element

`T`

Element to add.

#### Returns

`this`

This queue, for chaining.

***

### enqueueAll()

&gt; **enqueueAll**(`elements`): `this`

Defined in: [priority-queue.ts:196](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L196)

Adds multiple elements to the queue.

#### Parameters

##### elements

`T`[]

Elements to add.

#### Returns

`this`

This queue, for chaining.

***

### getStats()

&gt; **getStats**(): [`PriorityQueueStats`](../interfaces/PriorityQueueStats)

Defined in: [priority-queue.ts:333](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L333)

Snapshot of queue statistics (size, capacity, emptiness).

#### Returns

[`PriorityQueueStats`](../interfaces/PriorityQueueStats)

The current [PriorityQueueStats](../interfaces/PriorityQueueStats).

***

### peek()

&gt; **peek**(): `T` \| `undefined`

Defined in: [priority-queue.ts:231](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L231)

Returns the highest-priority element without removing it.

#### Returns

`T` \| `undefined`

The highest-priority element, or `undefined` if the queue is
  empty.

***

### remove()

&gt; **remove**(`element`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:242](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L242)

Removes a specific element from the queue, wherever it sits in the heap.

#### Parameters

##### element

`T`

Element to remove.

##### equalsFn?

(`a`, `b`) =&gt; `boolean`

Equality predicate. Defaults to strict `===`.

#### Returns

`boolean`

`true` if the element was found and removed.

***

### toArray()

&gt; **toArray**(): `T`[]

Defined in: [priority-queue.ts:307](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L307)

Returns a shallow copy of the elements without draining the queue.

The order reflects internal heap layout and is **not** priority order —
use [PriorityQueue.toSortedArray](#tosortedarray) when order matters.

#### Returns

`T`[]

A copy of the internal array.

***

### toSortedArray()

&gt; **toSortedArray**(): `T`[]

Defined in: [priority-queue.ts:316](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L316)

Returns the elements in priority order without modifying the queue.

#### Returns

`T`[]

The elements in priority order.

***

### updatePriority()

&gt; **updatePriority**(`oldElement`, `newElement`, `equalsFn?`): `boolean`

Defined in: [priority-queue.ts:263](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L263)

Updates an element's priority by removing it and re-inserting its
replacement.

#### Parameters

##### oldElement

`T`

Element to replace.

##### newElement

`T`

New element carrying the updated priority.

##### equalsFn?

(`a`, `b`) =&gt; `boolean`

Equality predicate used to locate `oldElement`.

#### Returns

`boolean`

`true` if the old element was found and updated.

***

### from()

&gt; `static` **from**\<`T`\>(`elements`, ...`args`): `PriorityQueue`\<`T`\>

Defined in: [priority-queue.ts:349](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/priority-queue.ts#L349)

Creates a new priority queue pre-loaded with the given elements.

#### Type Parameters

##### T

`T`

#### Parameters

##### elements

`T`[]

Initial elements.

##### args

...[`PQArgs`](../type-aliases/PQArgs)\<`T`\>

Queue options (a `compareFn` is required for non-comparable
  element types; see [PQArgs](../type-aliases/PQArgs)).

#### Returns

`PriorityQueue`\<`T`\>

A new priority queue containing `elements`.
