# Variable: toUnitInterval

&gt; `const` **toUnitInterval**: (`n`) =&gt; [`UnitInterval`](../type-aliases/UnitInterval) = `unitInterval.from`

Defined in: [numeric.ts:150](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L150)

Assert `n` is a [UnitInterval](../type-aliases/UnitInterval) and return it branded.

## Parameters

### n

`number`

## Returns

[`UnitInterval`](../type-aliases/UnitInterval)

## Throws

If `n` is not a finite number within the closed range `[0, 1]`.
