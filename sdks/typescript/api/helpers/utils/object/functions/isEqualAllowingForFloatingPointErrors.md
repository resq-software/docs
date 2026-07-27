# Function: isEqualAllowingForFloatingPointErrors()

&gt; **isEqualAllowingForFloatingPointErrors**(`obj1`, `obj2`, `threshold?`): `boolean`

Defined in: [packages/helpers/src/utils/object.ts:405](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L405)

**`Internal`**

Deep equality comparison that allows for floating-point precision errors.
Numbers are considered equal if they differ by less than the threshold.
Uses lodash.isequalwith internally for the deep comparison logic.

Only the numeric leaves are tolerance-compared (`Math.abs(a - b) < threshold`,
a strict `<`); every other value falls back to lodash's deep structural
equality. Because the comparison is `NaN`-unaware, two `NaN` leaves are treated
as unequal.

## Parameters

### obj1

`object`

First object to compare

### obj2

`object`

Second object to compare

### threshold?

`number` = `0.000001`

Maximum absolute difference two numbers may have and still
  count as equal (default: `0.000001`). Must be non-negative; a `0` threshold
  makes numbers effectively exact (any difference fails).

## Returns

`boolean`

True if objects are deeply equal with floating-point tolerance

## Example

```ts
const a = { x: 0.1 + 0.2 } // 0.30000000000000004
const b = { x: 0.3 }
isEqualAllowingForFloatingPointErrors(a, b) // true

const c = { coords: [1.0000001, 2.0000001] }
const d = { coords: [1.0000002, 2.0000002] }
isEqualAllowingForFloatingPointErrors(c, d) // true
```
