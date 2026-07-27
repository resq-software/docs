# Variable: TrieOptionsSchema

&gt; `const` **TrieOptionsSchema**: `Struct`\<\{ `caseInsensitive`: `optional`\<`Boolean`\>; `maxResults`: `optional`\<`Int`\>; \}\>

Defined in: [schemas.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L36)

Construction options for Trie.

- `caseInsensitive` — fold case during insert and lookup.
- `maxResults`      — cap returned matches (positive integer).
