# Function: toLatitude()

&gt; **toLatitude**(`value`): `number` & `Brand`\<`"Latitude"`\>

Defined in: [schemas.ts:291](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L291)

Smart constructor for [Latitude](../type-aliases/Latitude).

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Latitude"`\>

## Throws

The Effect parse error when `value` is non-finite or outside the
  closed interval `[-90, 90]`.
