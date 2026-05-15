# Class: RabinKarp

Defined in: [rabin-karp.ts:122](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L122)

Rabin-Karp string matching algorithm implementation

Uses rolling hash for efficient pattern matching in text.
Particularly efficient for multiple pattern searches.

Time Complexity:
- Average case: O(n + m) where n = text length, m = pattern length
- Worst case: O(nm) with many hash collisions

Space Complexity: O(1) for single pattern, O(k) for k patterns

## Example

```typescript
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

> **new RabinKarp**(`options?`): `RabinKarp`

Defined in: [rabin-karp.ts:132](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L132)

Creates a new Rabin-Karp matcher

#### Parameters

##### options?

[`RabinKarpOptions`](../interfaces/RabinKarpOptions) = `{}`

Configuration options

#### Returns

`RabinKarp`

#### Throws

Error if options validation fails

## Methods

### findRepeatedPatterns()

> **findRepeatedPatterns**(`text`, `patternLength`, `minOccurrences?`): `Map`\<`string`, `number`\>

Defined in: [rabin-karp.ts:352](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L352)

Finds all unique patterns of a given length that appear more than once
Useful for finding duplicate phrases in documents

#### Parameters

##### text

`string`

The text to analyze

##### patternLength

`number`

Length of patterns to find

##### minOccurrences?

`number` = `2`

Minimum occurrences to include (default: 2)

#### Returns

`Map`\<`string`, `number`\>

Map of patterns to their occurrence count

***

### search()

> **search**(`text`, `pattern`): [`PatternMatch`](../interfaces/PatternMatch)[]

Defined in: [rabin-karp.ts:152](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L152)

Searches for a pattern in text using Rabin-Karp algorithm

#### Parameters

##### text

`string`

The text to search in

##### pattern

`string`

The pattern to search for

#### Returns

[`PatternMatch`](../interfaces/PatternMatch)[]

Array of matches found

***

### searchMultiple()

> **searchMultiple**(`text`, `patterns`): `Map`\<`string`, [`PatternMatch`](../interfaces/PatternMatch)[]\>

Defined in: [rabin-karp.ts:225](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L225)

Searches for multiple patterns simultaneously

#### Parameters

##### text

`string`

The text to search in

##### patterns

`string`[]

Array of patterns to search for

#### Returns

`Map`\<`string`, [`PatternMatch`](../interfaces/PatternMatch)[]\>

Map of pattern to matches

***

### searchWithStats()

> **searchWithStats**(`text`, `pattern`): `object`

Defined in: [rabin-karp.ts:265](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L265)

Searches with statistics for performance monitoring

#### Parameters

##### text

`string`

The text to search in

##### pattern

`string`

The pattern to search for

#### Returns

`object`

Object containing matches and statistics

##### matches

> **matches**: [`PatternMatch`](../interfaces/PatternMatch)[]

##### stats

> **stats**: [`SearchStats`](../interfaces/SearchStats)
