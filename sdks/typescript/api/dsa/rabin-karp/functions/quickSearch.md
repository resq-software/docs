# Function: quickSearch()

&gt; **quickSearch**(`text`, `pattern`, `caseInsensitive?`): `number`[]

Defined in: [rabin-karp.ts:572](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L572)

Convenience wrapper around [RabinKarp.search](../classes/RabinKarp#search) for simple one-off
lookups that only need match positions.

## Parameters

### text

`string`

Text to search in.

### pattern

`string`

Pattern to find.

### caseInsensitive?

`boolean` = `true`

Whether to ignore case. Defaults to `true`.

## Returns

`number`[]

The starting indices of each match.
