# Variable: TrieOptionsSchema

> `const` **TrieOptionsSchema**: `Struct`\<\&#123; `caseInsensitive`: `optional`\<`Boolean`\>; `maxResults`: `optional`\<`Int`\>; \&#125;\>

Defined in: [schemas.ts:37](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L37)

Construction options for Trie.

- `caseInsensitive` — fold case during insert and lookup.
- `maxResults`      — cap returned matches (positive integer).
