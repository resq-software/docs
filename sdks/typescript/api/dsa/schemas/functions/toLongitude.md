# Function: toLongitude()

&gt; **toLongitude**(`value`): `number` & `Brand`\<`"Longitude"`\>

Defined in: [schemas.ts:301](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L301)

Smart constructor for [Longitude](../type-aliases/Longitude).

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Longitude"`\>

## Throws

The Effect parse error when `value` is non-finite or outside the
  closed interval `[-180, 180]`.
