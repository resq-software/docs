# Variable: toUnitInterval

&gt; `const` **toUnitInterval**: (`n`) =&gt; [`UnitInterval`](../type-aliases/UnitInterval) = `unitInterval.from`

Defined in: [numeric.ts:150](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L150)

Assert `n` is a [UnitInterval](../type-aliases/UnitInterval) and return it branded.

## Parameters

### n

`number`

## Returns

[`UnitInterval`](../type-aliases/UnitInterval)

## Throws

If `n` is not a finite number within the closed range `[0, 1]`.
