# Function: toProbability()

&gt; **toProbability**(`value`): `number` & `Brand`\<`"Probability"`\>

Defined in: [schemas.ts:281](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L281)

Smart constructor for [Probability](../type-aliases/Probability). Decodes `value`, throwing a
schema error when it is non-finite or outside the open interval `(0, 1)`.

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Probability"`\>

## Throws

The Effect parse error when `value` is out of range.
