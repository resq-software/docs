# Function: rabinKarp()

> **rabinKarp**(`text`, `pattern`): `number`[]

Defined in: [trie.ts:321](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L321)

Finds all occurrences of a pattern in text using the Rabin-Karp rolling hash algorithm.

## Parameters

### text

`string`

The text to search in

### pattern

`string`

The pattern to search for

## Returns

`number`[]

Array of starting indices where the pattern is found
