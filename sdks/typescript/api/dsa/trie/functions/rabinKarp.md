# Function: rabinKarp()

&gt; **rabinKarp**(`text`, `pattern`): `number`[]

Defined in: [trie.ts:328](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L328)

Finds all occurrences of a pattern in text using the Rabin-Karp rolling hash
algorithm. Matching is exact and case-sensitive.

## Parameters

### text

`string`

The text to search in.

### pattern

`string`

The pattern to search for.

## Returns

`number`[]

The zero-based starting indices of every occurrence, in ascending
  order. Returns an empty array when `pattern` is empty or longer than
  `text` — the sentinel for "no matches".
