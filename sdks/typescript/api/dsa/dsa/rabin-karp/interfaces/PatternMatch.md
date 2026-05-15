# Interface: PatternMatch

Defined in: [rabin-karp.ts:38](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L38)

Result of a pattern match

## Properties

### column?

> `optional` **column?**: `number`

Defined in: [rabin-karp.ts:46](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L46)

Column number within the line

***

### index

> **index**: `number`

Defined in: [rabin-karp.ts:40](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L40)

Starting index of the match in the text

***

### line?

> `optional` **line?**: `number`

Defined in: [rabin-karp.ts:44](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L44)

Line number (if text contains newlines)

***

### match

> **match**: `string`

Defined in: [rabin-karp.ts:42](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/rabin-karp.ts#L42)

The matched substring
