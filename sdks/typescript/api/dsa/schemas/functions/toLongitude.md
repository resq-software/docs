# Function: toLongitude()

&gt; **toLongitude**(`value`): `number` & `Brand`\<`"Longitude"`\>

Defined in: [schemas.ts:301](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L301)

Smart constructor for [Longitude](../type-aliases/Longitude).

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Longitude"`\>

## Throws

The Effect parse error when `value` is non-finite or outside the
  closed interval `[-180, 180]`.
