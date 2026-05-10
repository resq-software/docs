# Class: BoundedHeap\<T\>

Defined in: [heap.ts:21](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L21)

## Type Parameters

### T

`T` *extends* [`Distanced`](../interfaces/Distanced.md)

## Constructors

### Constructor

> **new BoundedHeap**\<`T`\>(`limit`): `BoundedHeap`\<`T`\>

Defined in: [heap.ts:25](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L25)

#### Parameters

##### limit

`number`

#### Returns

`BoundedHeap`\<`T`\>

## Properties

### limit

> `readonly` **limit**: `number`

Defined in: [heap.ts:23](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L23)

## Accessors

### size

#### Get Signature

> **get** **size**(): `number`

Defined in: [heap.ts:47](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L47)

##### Returns

`number`

## Methods

### insert()

> **insert**(`entry`): `void`

Defined in: [heap.ts:29](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L29)

#### Parameters

##### entry

`T`

#### Returns

`void`

***

### peek()

> **peek**(): `T` \| `undefined`

Defined in: [heap.ts:39](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L39)

#### Returns

`T` \| `undefined`

***

### toSorted()

> **toSorted**(): `T`[]

Defined in: [heap.ts:43](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/heap.ts#L43)

#### Returns

`T`[]
