# Class: Distance

Defined in: [distance.ts:234](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L234)

Distance calculation utility class.

Provides multiple distance formulas for different use cases:
- **Geographic distances**: haversine, vincenty (for Earth coordinates)
- **Mathematical distances**: euclidean, manhattan, chebyshev, minkowski
- **Vector distances**: cosine, hamming
- **Set distances**: jaccard, sorensen-dice

## Constructors

### Constructor

&gt; **new Distance**(): `Distance`

#### Returns

`Distance`

## Methods

### calculate()

&gt; `static` **calculate**\<`F`\>(`formula`, `point1`, `point2`, `options?`): `number`

Defined in: [distance.ts:571](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L571)

Dispatch to the named distance formula. [PointFor](../type-aliases/PointFor) constrains the
point shape at the type level, so `"threed"` requires 3D points and every
other formula requires 2D points.

#### Type Parameters

##### F

`F` *extends* [`DistanceFormula`](../type-aliases/DistanceFormula)

The selected [DistanceFormula](../type-aliases/DistanceFormula).

#### Parameters

##### formula

`F`

Which distance formula to apply.

##### point1

[`PointFor`](../type-aliases/PointFor)\<`F`\>

First point, of the shape the formula requires.

##### point2

[`PointFor`](../type-aliases/PointFor)\<`F`\>

Second point, of the shape the formula requires.

##### options?

[`DistanceOptions`](../interfaces/DistanceOptions) = `{}`

Formula options; only `p` (Minkowski order) is consulted.

#### Returns

`number`

The computed distance in the formula's native units.

#### Throws

If the points are invalid for the formula.

#### See

[Distance.calculateSafe](#calculatesafe) for a non-throwing variant.

***

### calculateSafe()

&gt; `static` **calculateSafe**\<`F`\>(`formula`, `point1`, `point2`, `options?`): [`DistanceResult`](../interfaces/DistanceResult)

Defined in: [distance.ts:622](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L622)

Non-throwing wrapper around [Distance.calculate](#calculate): catches validation
failures and reports them in the returned [DistanceResult](../interfaces/DistanceResult) instead
of throwing, so callers can branch on `valid`.

#### Type Parameters

##### F

`F` *extends* [`DistanceFormula`](../type-aliases/DistanceFormula)

The selected [DistanceFormula](../type-aliases/DistanceFormula).

#### Parameters

##### formula

`F`

Which distance formula to apply.

##### point1

[`PointFor`](../type-aliases/PointFor)\<`F`\>

First point, of the shape the formula requires.

##### point2

[`PointFor`](../type-aliases/PointFor)\<`F`\>

Second point, of the shape the formula requires.

##### options?

[`DistanceOptions`](../interfaces/DistanceOptions) = `{}`

Formula options; only `p` (Minkowski order) is consulted.

#### Returns

[`DistanceResult`](../interfaces/DistanceResult)

A result with the distance (or `NaN`), the formula, a `valid`
  flag, and an `error` message on failure.

***

### chebyshev()

&gt; `static` **chebyshev**(`point1`, `point2`): `number`

Defined in: [distance.ts:407](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L407)

Chessboard (L∞) distance: the largest single-axis coordinate difference.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second point.

#### Returns

`number`

The Chebyshev distance in coordinate units.

#### Throws

If either point has non-finite coordinates.

***

### cosine()

&gt; `static` **cosine**(`point1`, `point2`): `number`

Defined in: [distance.ts:470](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L470)

Cosine distance (`1 - cosine similarity`) between the two coordinates read
as 2D vectors from the origin. Ranges from `0` (identical direction) to
`2` (opposite direction).

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First vector.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second vector.

#### Returns

`number`

The cosine distance in `[0, 2]`.

#### Throws

If a point is non-finite or is the zero vector.

***

### euclidean()

&gt; `static` **euclidean**(`point1`, `point2`): `number`

Defined in: [distance.ts:244](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L244)

Straight-line (L2) distance between two points, treating `lat`/`lng` as
plain planar coordinates rather than geographic ones.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second point.

#### Returns

`number`

The Euclidean distance in coordinate units.

#### Throws

If either point has non-finite coordinates.

***

### hamming()

&gt; `static` **hamming**(`point1`, `point2`): `number`

Defined in: [distance.ts:497](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L497)

Hamming distance: the count of coordinate positions whose values differ.
Intended for discrete/binary vectors encoded as `lat`/`lng`.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First vector.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second vector.

#### Returns

`number`

The number of differing positions (`0`, `1`, or `2`).

#### Throws

If either point has non-finite coordinates.

***

### haversine()

&gt; `static` **haversine**(`point1`, `point2`): `number`

Defined in: [distance.ts:263](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L263)

Great-circle distance between two geographic points on a spherical Earth.
Fast and accurate to ~0.5% — prefer [Distance.vincenty](#vincenty) when
ellipsoidal precision matters.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First geographic point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second geographic point.

#### Returns

`number`

The distance in kilometres.

#### Throws

If either point is outside valid lat/lng ranges.

***

### haversineMeters()

&gt; `static` **haversineMeters**(`point1`, `point2`): `number`

Defined in: [distance.ts:289](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L289)

Convenience wrapper around [Distance.haversine](#haversine) returning metres
instead of kilometres.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First geographic point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second geographic point.

#### Returns

`number`

The great-circle distance in metres.

#### Throws

If either point is outside valid lat/lng ranges.

***

### jaccard()

&gt; `static` **jaccard**(`point1`, `point2`): `number`

Defined in: [distance.ts:518](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L518)

Jaccard distance (`1 - |A ∩ B| / |A ∪ B|`) between the two coordinates
read as sets of their `lat`/`lng` values.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First set of values.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second set of values.

#### Returns

`number`

The Jaccard distance in `[0, 1]`.

#### Throws

If either point has non-finite coordinates.

***

### manhattan()

&gt; `static` **manhattan**(`point1`, `point2`): `number`

Defined in: [distance.ts:392](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L392)

Taxicab (L1) distance: the sum of the absolute coordinate differences.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second point.

#### Returns

`number`

The Manhattan distance in coordinate units.

#### Throws

If either point has non-finite coordinates.

***

### minkowski()

&gt; `static` **minkowski**(`point1`, `point2`, `p?`): `number`

Defined in: [distance.ts:425](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L425)

Generalised Lp distance. Reduces to Manhattan at `p = 1`, Euclidean at
`p = 2`, and Chebyshev at `p = Infinity`.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second point.

##### p?

`number` = `2`

Order of the norm; must be a positive finite number (or
  `Infinity`). Defaults to `2` (Euclidean).

#### Returns

`number`

The Minkowski distance in coordinate units.

#### Throws

If a point is non-finite or `p <= 0`.

***

### recommendGeoFormula()

&gt; `static` **recommendGeoFormula**(`maxDistanceKm?`): [`DistanceFormula`](../type-aliases/DistanceFormula)

Defined in: [distance.ts:654](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L654)

Recommend a geographic formula for an expected distance range, trading
speed for accuracy: `"haversine"` for short hops, `"vincenty"` once
ellipsoidal error starts to matter.

#### Parameters

##### maxDistanceKm?

`number`

Expected upper bound of the distances to compute,
  in kilometres. Omit to assume a short range.

#### Returns

[`DistanceFormula`](../type-aliases/DistanceFormula)

`"haversine"` below 1000 km, otherwise `"vincenty"`.

***

### sorensenDice()

&gt; `static` **sorensenDice**(`point1`, `point2`): `number`

Defined in: [distance.ts:542](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L542)

Sørensen–Dice distance (`1 - 2|A ∩ B| / (|A| + |B|)`) between the two
coordinates read as sets of their `lat`/`lng` values.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First set of values.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second set of values.

#### Returns

`number`

The Sørensen–Dice distance in `[0, 1]`.

#### Throws

If either point has non-finite coordinates.

***

### threed()

&gt; `static` **threed**(`point1`, `point2`): `number`

Defined in: [distance.ts:453](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L453)

Euclidean distance in 3D, treating `alt` as the third axis alongside
`lat`/`lng`.

#### Parameters

##### point1

[`Coordinates3D`](../interfaces/Coordinates3D)

First 3D point.

##### point2

[`Coordinates3D`](../interfaces/Coordinates3D)

Second 3D point.

#### Returns

`number`

The 3D Euclidean distance in coordinate units.

#### Throws

If either point lacks a finite `alt` or has
  non-finite coordinates.

***

### vincenty()

&gt; `static` **vincenty**(`point1`, `point2`): `number`

Defined in: [distance.ts:304](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/distance.ts#L304)

Ellipsoidal geodesic distance on the WGS-84 spheroid via Vincenty's
inverse formula. More accurate than [Distance.haversine](#haversine) but
iterative, and it may fail to converge for near-antipodal points.

#### Parameters

##### point1

[`Coordinates2D`](../interfaces/Coordinates2D)

First geographic point.

##### point2

[`Coordinates2D`](../interfaces/Coordinates2D)

Second geographic point.

#### Returns

`number`

The geodesic distance in kilometres.

#### Throws

If either point is out of range, or if the
  iteration fails to converge (near-antipodal points).
