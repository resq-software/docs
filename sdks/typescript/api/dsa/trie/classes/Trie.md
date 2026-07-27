# Class: Trie\<T\>

Defined in: [trie.ts:90](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L90)

Trie (Prefix Tree) for efficient prefix-based autocomplete

Time Complexity:
- insert: O(k) where k is word length
- search: O(k) for exact match
- startsWith: O(k + m) where m is number of results
- delete: O(k)

Space Complexity: O(ALPHABET_SIZE * k * n) where n is number of words

## Example

```ts
const trie = new Trie<{ id: string }>();
trie.insert('hello', { id: '1' });
const results = trie.searchByPrefix('hel');
```

## Type Parameters

### T

`T`

Type of data stored with each word

## Constructors

### Constructor

&gt; **new Trie**\<`T`\>(`options?`): `Trie`\<`T`\>

Defined in: [trie.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L102)

Creates a new Trie instance.

#### Parameters

##### options?

Configuration options.

###### caseInsensitive?

`boolean` = `...`

###### maxResults?

`number` = `...`

#### Returns

`Trie`\<`T`\>

#### Throws

If options validation fails.

## Accessors

### length

#### Get Signature

&gt; **get** **length**(): `number`

Defined in: [trie.ts:234](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L234)

Returns the number of words in the Trie.

##### Returns

`number`

## Methods

### clear()

&gt; **clear**(): `void`

Defined in: [trie.ts:241](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L241)

Clears all words from the Trie.

#### Returns

`void`

***

### delete()

&gt; **delete**(`word`): `boolean`

Defined in: [trie.ts:225](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L225)

Deletes a word from the Trie, pruning now-empty nodes.

#### Parameters

##### word

`string`

#### Returns

`boolean`

`true` if the word existed and was deleted.

***

### getAllWords()

&gt; **getAllWords**(): `object`[]

Defined in: [trie.ts:249](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L249)

Gets every word in the Trie with its associated data, unordered.

#### Returns

`object`[]

***

### has()

&gt; **has**(`word`): `boolean`

Defined in: [trie.ts:179](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L179)

Checks whether an exact word exists in the Trie.

#### Parameters

##### word

`string`

#### Returns

`boolean`

***

### insert()

&gt; **insert**(`word`, `data`): `this`

Defined in: [trie.ts:129](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L129)

Inserts a word with associated data into the Trie. Invalid (empty) words
are silently ignored rather than throwing.

#### Parameters

##### word

`string`

##### data

`T`

#### Returns

`this`

This Trie instance, for chaining.

***

### insertMany()

&gt; **insertMany**(`entries`): `this`

Defined in: [trie.ts:159](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L159)

Bulk-inserts multiple `[word, data]` entries.

#### Parameters

##### entries

\[`string`, `T`\][]

#### Returns

`this`

This Trie instance, for chaining.

***

### search()

&gt; **search**(`word`): `T` \| `null`

Defined in: [trie.ts:171](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L171)

Searches for an exact word match.

#### Parameters

##### word

`string`

#### Returns

`T` \| `null`

The associated data, or `null` if the word is not present.

***

### searchByPrefix()

&gt; **searchByPrefix**(`prefix`, `limit?`): [`TrieSearchResult`](../interfaces/TrieSearchResult)\<`T`\>[]

Defined in: [trie.ts:199](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L199)

Finds all words starting with the given prefix, ranked by frequency.

#### Parameters

##### prefix

`string`

The prefix to search for.

##### limit?

`number`

Maximum number of results. Defaults to the `maxResults`
  constructor option.

#### Returns

[`TrieSearchResult`](../interfaces/TrieSearchResult)\<`T`\>[]

Search results sorted by descending relevance score.

***

### startsWith()

&gt; **startsWith**(`prefix`): `boolean`

Defined in: [trie.ts:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/trie.ts#L187)

Checks whether any stored word starts with the given prefix.

#### Parameters

##### prefix

`string`

#### Returns

`boolean`
