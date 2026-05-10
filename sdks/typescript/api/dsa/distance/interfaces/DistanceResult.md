# Interface: DistanceResult

Defined in: [distance.ts:116](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L116)

Result of a safe distance calculation.

## Properties

### distance

> **distance**: `number`

Defined in: [distance.ts:118](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L118)

Calculated distance (NaN if invalid)

***

### error?

> `optional` **error?**: `string`

Defined in: [distance.ts:124](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L124)

Error message if calculation failed

***

### formula

> **formula**: [`DistanceFormula`](../type-aliases/DistanceFormula.md)

Defined in: [distance.ts:120](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L120)

Formula used for calculation

***

### valid

> **valid**: `boolean`

Defined in: [distance.ts:122](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/distance.ts#L122)

Whether the calculation succeeded
