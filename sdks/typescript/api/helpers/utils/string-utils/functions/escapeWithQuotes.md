# Function: escapeWithQuotes()

&gt; **escapeWithQuotes**(`text`, `char?`): `string`

Defined in: [packages/helpers/src/utils/string-utils.ts:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/string-utils.ts#L40)

Quote and escape `text` with the given quote character (`'`, `"`, or `` ` ``).

NOTE: this is not safe for building CSS/DOM selectors.

## Parameters

### text

`string`

### char?

`string` = `"'"`

## Returns

`string`

## Throws

If `char` is not one of `'`, `"`, `` ` ``.
