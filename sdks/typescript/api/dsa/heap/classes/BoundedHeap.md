# Class: BoundedHeap\<T\>

Defined in: [heap.ts:45](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L45)

Fixed-capacity max-heap that keeps the **N smallest** items by `distance`.

Designed for top-K nearest-neighbour use: insert `M` candidates, retrieve
the `N` closest in `O(M log N)` total time and `O(N)` memory regardless of
how many candidates are scanned.

Internally a max-heap on `distance`, so the *largest* distance among the
kept N sits at the root. New entries are accepted only when they are
strictly closer than the current worst.

## Example

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

> **new BoundedHeap**\<`T`\>(`limit`): `BoundedHeap`\<`T`\>

Defined in: [heap.ts:56](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L56)

#### Parameters

##### limit

`number`

Maximum number of items to retain. Once full, new
  inserts are accepted only when their `distance` is strictly less
  than the current worst-kept element's distance.

#### Returns

`BoundedHeap`\<`T`\>

## Properties

### limit

> `readonly` **limit**: `number`

Defined in: [heap.ts:49](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L49)

Maximum number of elements the heap will retain.

## Accessors

### size

#### Get Signature

> **get** **size**(): `number`

Defined in: [heap.ts:95](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L95)

Current number of retained elements (≤ `limit`).

##### Returns

`number`

## Methods

### insert()

> **insert**(`entry`): `void`

Defined in: [heap.ts:67](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L67)

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

> **peek**(): `T` \| `undefined`

Defined in: [heap.ts:82](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L82)

#### Returns

`T` \| `undefined`

The element with the **largest** retained distance, or
  `undefined` if the heap is empty. This is the entry that would be
  evicted next on a closer insert.

***

### toSorted()

> **toSorted**(): `T`[]

Defined in: [heap.ts:90](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/heap.ts#L90)

#### Returns

`T`[]

A new array of the retained entries sorted ascending by
  `distance` (nearest first). Does not mutate the heap.
