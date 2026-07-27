# Class: BoundedHeap\<T\>

Defined in: [heap.ts:52](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L52)

Fixed-capacity max-heap that keeps the **N smallest** items by `distance`.

Designed for top-K nearest-neighbour use: insert `M` candidates, retrieve
the `N` closest in `O(M log N)` total time and `O(N)` memory regardless of
how many candidates are scanned.

Internally a max-heap on `distance`, so the *largest* distance among the
kept N sits at the root. New entries are accepted only when they are
strictly closer than the current worst.

## Example

**Keep the 5 nearest survey points**

```ts
const top5 = new BoundedHeap<{ id: string; distance: number }>(5);
for (const p of points) top5.insert(p);
const nearest = top5.toSorted(); // ascending by distance
```

## Type Parameters

### T

`T` *extends* [`Distanced`](../interfaces/Distanced)

Element type; must expose a numeric `distance` field.

## Constructors

### Constructor

&gt; **new BoundedHeap**\<`T`\>(`limit`): `BoundedHeap`\<`T`\>

Defined in: [heap.ts:65](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L65)

#### Parameters

##### limit

`number`

Maximum number of items to retain. Once full, new
  inserts are accepted only when their `distance` is strictly less
  than the current worst-kept element's distance. A non-positive
  `limit` yields a heap that retains nothing — every [insert](#insert) is a
  no-op.

#### Returns

`BoundedHeap`\<`T`\>

## Properties

### limit

&gt; `readonly` **limit**: `number`

Defined in: [heap.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L56)

Maximum number of elements the heap will retain.

## Accessors

### size

#### Get Signature

&gt; **get** **size**(): `number`

Defined in: [heap.ts:104](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L104)

Current number of retained elements (≤ `limit`).

##### Returns

`number`

## Methods

### insert()

&gt; **insert**(`entry`): `void`

Defined in: [heap.ts:76](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L76)

Insert a candidate. If the heap is below capacity, the entry is added
unconditionally. Otherwise the entry replaces the current worst-kept
element if and only if `entry.distance < currentWorst.distance`.

Time complexity: `O(log limit)`.

#### Parameters

##### entry

`T`

#### Returns

`void`

***

### peek()

&gt; **peek**(): `T` \| `undefined`

Defined in: [heap.ts:91](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L91)

#### Returns

`T` \| `undefined`

The element with the **largest** retained distance, or
  `undefined` if the heap is empty. This is the entry that would be
  evicted next on a closer insert.

***

### toSorted()

&gt; **toSorted**(): `T`[]

Defined in: [heap.ts:99](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/heap.ts#L99)

#### Returns

`T`[]

A new array of the retained entries sorted ascending by
  `distance` (nearest first). Does not mutate the heap.
