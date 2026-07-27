# Variable: toPositiveNumber

&gt; `const` **toPositiveNumber**: (`n`) =&gt; [`PositiveNumber`](../type-aliases/PositiveNumber) = `positiveNumber.from`

Defined in: [numeric.ts:139](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L139)

Assert `n` is a [PositiveNumber](../type-aliases/PositiveNumber) and return it branded.

## Parameters

### n

`number`

## Returns

[`PositiveNumber`](../type-aliases/PositiveNumber)

## Throws

If `n` is not a finite number strictly greater than zero.
