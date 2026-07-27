# Interface: PatternMatch

Defined in: [rabin-karp.ts:40](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L40)

A single pattern occurrence within the searched text.

`line` and `column` are populated together, and only when the matcher's
`includeLineInfo` option is enabled — both are absent otherwise.

## Properties

### column?

&gt; `optional` **column?**: `number`

Defined in: [rabin-karp.ts:48](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L48)

One-based column within [line](#line); absent when line info is disabled.

***

### index

&gt; **index**: `number`

Defined in: [rabin-karp.ts:42](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L42)

Zero-based character offset of the match's first character in the text.

***

### line?

&gt; `optional` **line?**: `number`

Defined in: [rabin-karp.ts:46](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L46)

One-based line number of the match; absent when line info is disabled.

***

### match

&gt; **match**: `string`

Defined in: [rabin-karp.ts:44](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/rabin-karp.ts#L44)

The matched substring, sliced from the original (case-preserved) text.
