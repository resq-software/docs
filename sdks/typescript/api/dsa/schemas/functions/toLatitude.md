# Function: toLatitude()

&gt; **toLatitude**(`value`): `number` & `Brand`\<`"Latitude"`\>

Defined in: [schemas.ts:291](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L291)

Smart constructor for [Latitude](../type-aliases/Latitude).

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Latitude"`\>

## Throws

The Effect parse error when `value` is non-finite or outside the
  closed interval `[-90, 90]`.
