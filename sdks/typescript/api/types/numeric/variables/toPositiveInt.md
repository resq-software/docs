# Variable: toPositiveInt

&gt; `const` **toPositiveInt**: (`n`) =&gt; [`PositiveInt`](../type-aliases/PositiveInt) = `positiveInt.from`

Defined in: [numeric.ts:106](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L106)

Assert `n` is a [PositiveInt](../type-aliases/PositiveInt) and return it branded.

## Parameters

### n

`number`

## Returns

[`PositiveInt`](../type-aliases/PositiveInt)

## Throws

If `n` is not an integer strictly greater than zero.
