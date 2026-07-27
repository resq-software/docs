# Variable: TrieOptionsSchema

&gt; `const` **TrieOptionsSchema**: `Struct`\<\{ `caseInsensitive`: `optional`\<`Boolean`\>; `maxResults`: `optional`\<`Int`\>; \}\>

Defined in: [schemas.ts:36](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L36)

Construction options for Trie.

- `caseInsensitive` — fold case during insert and lookup.
- `maxResults`      — cap returned matches (positive integer).
