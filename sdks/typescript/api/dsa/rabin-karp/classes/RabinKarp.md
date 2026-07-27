# Class: RabinKarp

Defined in: [rabin-karp.ts:124](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L124)

Rabin-Karp string matching algorithm implementation

Uses rolling hash for efficient pattern matching in text.
Particularly efficient for multiple pattern searches.

Time Complexity:
- Average case: O(n + m) where n = text length, m = pattern length
- Worst case: O(nm) with many hash collisions

Space Complexity: O(1) for single pattern, O(k) for k patterns

## Example

```ts
const matcher = new RabinKarp();

// Single pattern search
const matches = matcher.search('The quick brown fox', 'quick');
// Returns [{ index: 4, match: 'quick' }]

// Multiple patterns
const multiMatches = matcher.searchMultiple(
  'The quick brown fox jumps over the lazy dog',
  ['quick', 'fox', 'dog']
);
```

## Constructors

### Constructor

&gt; **new RabinKarp**(`options?`): `RabinKarp`

Defined in: [rabin-karp.ts:135](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L135)

Creates a new Rabin-Karp matcher.

#### Parameters

##### options?

[`RabinKarpOptions`](../interfaces/RabinKarpOptions) = `{}`

Configuration options.

#### Returns

`RabinKarp`

#### Throws

If options validation fails.

## Methods

### findRepeatedPatterns()

&gt; **findRepeatedPatterns**(`text`, `patternLength`, `minOccurrences?`): `Map`\<`string`, `number`\>

Defined in: [rabin-karp.ts:357](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L357)

Finds every fixed-length substring that repeats, useful for detecting
duplicate phrases in a document.

#### Parameters

##### text

`string`

The text to analyze.

##### patternLength

`number`

Length of the substrings to consider.

##### minOccurrences?

`number` = `2`

Minimum repeat count to include. Defaults to `2`.

#### Returns

`Map`\<`string`, `number`\>

A map from each repeated substring to its occurrence count.

***

### search()

&gt; **search**(`text`, `pattern`): [`PatternMatch`](../interfaces/PatternMatch)[]

Defined in: [rabin-karp.ts:155](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L155)

Searches for a single pattern in text using the Rabin-Karp algorithm.

#### Parameters

##### text

`string`

The text to search in.

##### pattern

`string`

The pattern to search for.

#### Returns

[`PatternMatch`](../interfaces/PatternMatch)[]

The matches found, capped at the `maxMatches` option.

***

### searchMultiple()

&gt; **searchMultiple**(`text`, `patterns`): `Map`\<`string`, [`PatternMatch`](../interfaces/PatternMatch)[]\>

Defined in: [rabin-karp.ts:229](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L229)

Searches for multiple patterns in a single pass, grouping them by length
so each length shares one rolling hash.

#### Parameters

##### text

`string`

The text to search in.

##### patterns

`string`[]

The patterns to search for.

#### Returns

`Map`\<`string`, [`PatternMatch`](../interfaces/PatternMatch)[]\>

A map from each pattern to its matches.

***

### searchWithStats()

&gt; **searchWithStats**(`text`, `pattern`): `object`

Defined in: [rabin-karp.ts:270](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/rabin-karp.ts#L270)

Searches for a pattern while recording performance statistics such as
hash collisions and elapsed time.

#### Parameters

##### text

`string`

The text to search in.

##### pattern

`string`

The pattern to search for.

#### Returns

`object`

The matches together with the collected [SearchStats](../interfaces/SearchStats).

##### matches

&gt; **matches**: [`PatternMatch`](../interfaces/PatternMatch)[]

##### stats

&gt; **stats**: [`SearchStats`](../interfaces/SearchStats)
