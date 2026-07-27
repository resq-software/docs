# Function: assertFontCompliance()

&gt; **assertFontCompliance**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:866](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L866)

Enforce typography rules from `STYLE_GUIDE.md`. Walks the
built-in `FONT_RULES` map and, when the file path matches a rule,
verifies the source contains every required class
(`font-mono uppercase` for buttons/badges/labels, `font-display`
for titles).

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

Naming the first required class missing from a file that
  matches a FONT\_RULES entry.
