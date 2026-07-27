# Function: toProbability()

&gt; **toProbability**(`value`): `number` & `Brand`\<`"Probability"`\>

Defined in: [schemas.ts:281](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L281)

Smart constructor for [Probability](../type-aliases/Probability). Decodes `value`, throwing a
schema error when it is non-finite or outside the open interval `(0, 1)`.

## Parameters

### value

`number`

## Returns

`number` & `Brand`\<`"Probability"`\>

## Throws

The Effect parse error when `value` is out of range.
