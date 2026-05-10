# Class: Distance

Defined in: [distance.ts:209](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L209)

Distance calculation utility class.

Provides multiple distance formulas for different use cases:
- **Geographic distances**: haversine, vincenty (for Earth coordinates)
- **Mathematical distances**: euclidean, manhattan, chebyshev, minkowski
- **Vector distances**: cosine, hamming
- **Set distances**: jaccard, sorensen-dice

## Constructors

### Constructor

> **new Distance**(): `Distance`

#### Returns

`Distance`

## Methods

### calculate()

> `static` **calculate**(`formula`, `point1`, `point2`, `options?`): `number`

Defined in: [distance.ts:419](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L419)

#### Parameters

##### formula

[`DistanceFormula`](../type-aliases/DistanceFormula.md)

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md) \| [`Coordinates3D`](../interfaces/Coordinates3D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md) \| [`Coordinates3D`](../interfaces/Coordinates3D.md)

##### options?

[`DistanceOptions`](../interfaces/DistanceOptions.md) = `{}`

#### Returns

`number`

***

### calculateSafe()

> `static` **calculateSafe**(`formula`, `point1`, `point2`, `options?`): [`DistanceResult`](../interfaces/DistanceResult.md)

Defined in: [distance.ts:455](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L455)

#### Parameters

##### formula

[`DistanceFormula`](../type-aliases/DistanceFormula.md)

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md) \| [`Coordinates3D`](../interfaces/Coordinates3D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md) \| [`Coordinates3D`](../interfaces/Coordinates3D.md)

##### options?

[`DistanceOptions`](../interfaces/DistanceOptions.md) = `{}`

#### Returns

[`DistanceResult`](../interfaces/DistanceResult.md)

***

### chebyshev()

> `static` **chebyshev**(`point1`, `point2`): `number`

Defined in: [distance.ts:327](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L327)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### cosine()

> `static` **cosine**(`point1`, `point2`): `number`

Defined in: [distance.ts:359](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L359)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### euclidean()

> `static` **euclidean**(`point1`, `point2`): `number`

Defined in: [distance.ts:210](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L210)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### hamming()

> `static` **hamming**(`point1`, `point2`): `number`

Defined in: [distance.ts:377](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L377)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### haversine()

> `static` **haversine**(`point1`, `point2`): `number`

Defined in: [distance.ts:219](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L219)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### haversineMeters()

> `static` **haversineMeters**(`point1`, `point2`): `number`

Defined in: [distance.ts:236](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L236)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### jaccard()

> `static` **jaccard**(`point1`, `point2`): `number`

Defined in: [distance.ts:389](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L389)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### manhattan()

> `static` **manhattan**(`point1`, `point2`): `number`

Defined in: [distance.ts:320](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L320)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### minkowski()

> `static` **minkowski**(`point1`, `point2`, `p?`): `number`

Defined in: [distance.ts:334](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L334)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### p?

`number` = `2`

#### Returns

`number`

***

### recommendGeoFormula()

> `static` **recommendGeoFormula**(`maxDistanceKm?`): [`DistanceFormula`](../type-aliases/DistanceFormula.md)

Defined in: [distance.ts:478](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L478)

#### Parameters

##### maxDistanceKm?

`number`

#### Returns

[`DistanceFormula`](../type-aliases/DistanceFormula.md)

***

### sorensenDice()

> `static` **sorensenDice**(`point1`, `point2`): `number`

Defined in: [distance.ts:404](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L404)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`

***

### threed()

> `static` **threed**(`point1`, `point2`): `number`

Defined in: [distance.ts:352](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L352)

#### Parameters

##### point1

[`Coordinates3D`](../interfaces/Coordinates3D.md)

##### point2

[`Coordinates3D`](../interfaces/Coordinates3D.md)

#### Returns

`number`

***

### vincenty()

> `static` **vincenty**(`point1`, `point2`): `number`

Defined in: [distance.ts:240](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L240)

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D.md)

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D.md)

#### Returns

`number`
