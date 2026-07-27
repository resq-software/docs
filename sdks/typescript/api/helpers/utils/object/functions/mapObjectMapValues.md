# Function: mapObjectMapValues()

&gt; **mapObjectMapValues**\<`Key`, `ValueBefore`, `ValueAfter`\>(`object`, `mapper`): `{ [K in string]: ValueAfter }`

Defined in: [packages/helpers/src/utils/object.ts:245](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/object.ts#L245)

**`Internal`**

Maps the values of an object to new values using a mapper function, preserving keys.
The mapper function receives both the key and value for each entry.

## Type Parameters

### Key

`Key` *extends* `string`

### ValueBefore

`ValueBefore`

### ValueAfter

`ValueAfter`

## Parameters

### object

`{ readonly [K in string]: ValueBefore }`

The object whose values to transform

### mapper

(`key`, `value`) =&gt; `ValueAfter`

Function that transforms each value (receives key and value)

## Returns

`{ [K in string]: ValueAfter }`

A new object with the same keys but transformed values

## Example

```ts
const prices = { apple: 1.50, banana: 0.75, orange: 2.00 }
const withTax = mapObjectMapValues(prices, (fruit, price) => price * 1.08)
// { apple: 1.62, banana: 0.81, orange: 2.16 }
```
