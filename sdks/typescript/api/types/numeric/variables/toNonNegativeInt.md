# Variable: toNonNegativeInt

&gt; `const` **toNonNegativeInt**: (`n`) =&gt; [`NonNegativeInt`](../type-aliases/NonNegativeInt) = `nonNegativeInt.from`

Defined in: [numeric.ts:117](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L117)

Assert `n` is a [NonNegativeInt](../type-aliases/NonNegativeInt) and return it branded.

## Parameters

### n

`number`

## Returns

[`NonNegativeInt`](../type-aliases/NonNegativeInt)

## Throws

If `n` is not an integer greater than or equal to zero.
