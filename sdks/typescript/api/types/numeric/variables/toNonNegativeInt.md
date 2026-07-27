# Variable: toNonNegativeInt

&gt; `const` **toNonNegativeInt**: (`n`) =&gt; [`NonNegativeInt`](../type-aliases/NonNegativeInt) = `nonNegativeInt.from`

Defined in: [numeric.ts:117](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L117)

Assert `n` is a [NonNegativeInt](../type-aliases/NonNegativeInt) and return it branded.

## Parameters

### n

`number`

## Returns

[`NonNegativeInt`](../type-aliases/NonNegativeInt)

## Throws

If `n` is not an integer greater than or equal to zero.
