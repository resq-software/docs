# Class: Trie\<T\>

Defined in: [trie.ts:91](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L91)

Trie (Prefix Tree) for efficient prefix-based autocomplete

Time Complexity:
- insert: O(k) where k is word length
- search: O(k) for exact match
- startsWith: O(k + m) where m is number of results
- delete: O(k)

Space Complexity: O(ALPHABET_SIZE * k * n) where n is number of words

## Example

```typescript
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

> **new Trie**\<`T`\>(`options?`): `Trie`\<`T`\>

Defined in: [trie.ts:102](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L102)

Creates a new Trie instance

#### Parameters

##### options?

Configuration options

###### caseInsensitive?

`boolean`

###### maxResults?

`number`

#### Returns

`Trie`\<`T`\>

#### Throws

Error if options validation fails

## Accessors

### length

#### Get Signature

> **get** **length**(): `number`

Defined in: [trie.ts:228](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L228)

Returns the number of words in the Trie

##### Returns

`number`

## Methods

### clear()

> **clear**(): `void`

Defined in: [trie.ts:235](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L235)

Clears all words from the Trie

#### Returns

`void`

***

### delete()

> **delete**(`word`): `boolean`

Defined in: [trie.ts:219](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L219)

Deletes a word from the Trie

#### Parameters

##### word

`string`

#### Returns

`boolean`

True if the word was deleted

***

### getAllWords()

> **getAllWords**(): `object`[]

Defined in: [trie.ts:243](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L243)

Gets all words in the Trie

#### Returns

`object`[]

***

### has()

> **has**(`word`): `boolean`

Defined in: [trie.ts:175](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L175)

Checks if a word exists in the Trie

#### Parameters

##### word

`string`

#### Returns

`boolean`

***

### insert()

> **insert**(`word`, `data`): `this`

Defined in: [trie.ts:127](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L127)

Inserts a word with associated data into the Trie

#### Parameters

##### word

`string`

##### data

`T`

#### Returns

`this`

This Trie instance for chaining

***

### insertMany()

> **insertMany**(`entries`): `this`

Defined in: [trie.ts:156](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L156)

Bulk insert multiple words with data

#### Parameters

##### entries

\[`string`, `T`\][]

#### Returns

`this`

This Trie instance for chaining

***

### search()

> **search**(`word`): `T` \| `null`

Defined in: [trie.ts:167](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L167)

Searches for an exact word match

#### Parameters

##### word

`string`

#### Returns

`T` \| `null`

The associated data or null if not found

***

### searchByPrefix()

> **searchByPrefix**(`prefix`, `limit?`): [`TrieSearchResult`](../interfaces/TrieSearchResult)\<`T`\>[]

Defined in: [trie.ts:194](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L194)

Finds all words starting with the given prefix

#### Parameters

##### prefix

`string`

The prefix to search for

##### limit?

`number`

Maximum number of results (defaults to maxResults option)

#### Returns

[`TrieSearchResult`](../interfaces/TrieSearchResult)\<`T`\>[]

Array of search results sorted by relevance

***

### startsWith()

> **startsWith**(`prefix`): `boolean`

Defined in: [trie.ts:183](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/trie.ts#L183)

Checks if any word starts with the given prefix

#### Parameters

##### prefix

`string`

#### Returns

`boolean`
