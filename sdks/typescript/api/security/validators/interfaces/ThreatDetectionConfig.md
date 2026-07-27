# Interface: ThreatDetectionConfig

Defined in: [validators.ts:419](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L419)

Per-detector toggles for [detectThreatPatterns](../functions/detectThreatPatterns).

Defaults: XSS, SQL, NoSQL, path-traversal, and homoglyph detectors
are **on**; command injection is **off** (false-positive prone).
Pass `false` to disable a detector or `true` to force-enable
`checkCommandInjection`.

## Properties

### checkCommandInjection?

&gt; `optional` **checkCommandInjection?**: `boolean`

Defined in: [validators.ts:427](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L427)

Default `false` — opt in only when input reaches a shell.

***

### checkHomoglyphs?

&gt; `optional` **checkHomoglyphs?**: `boolean`

Defined in: [validators.ts:431](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L431)

Default `true`.

***

### checkNoSQLInjection?

&gt; `optional` **checkNoSQLInjection?**: `boolean`

Defined in: [validators.ts:425](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L425)

Default `true`.

***

### checkPathTraversal?

&gt; `optional` **checkPathTraversal?**: `boolean`

Defined in: [validators.ts:429](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L429)

Default `true`.

***

### checkSQLInjection?

&gt; `optional` **checkSQLInjection?**: `boolean`

Defined in: [validators.ts:423](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L423)

Default `true`.

***

### checkXSS?

&gt; `optional` **checkXSS?**: `boolean`

Defined in: [validators.ts:421](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L421)

Default `true`.
