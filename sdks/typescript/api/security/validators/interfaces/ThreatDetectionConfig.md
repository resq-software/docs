# Interface: ThreatDetectionConfig

Defined in: [validators.ts:410](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L410)

Per-detector toggles for [detectThreatPatterns](../functions/detectThreatPatterns).

Defaults: XSS, SQL, NoSQL, path-traversal, and homoglyph detectors
are **on**; command injection is **off** (false-positive prone).
Pass `false` to disable a detector or `true` to force-enable
`checkCommandInjection`.

## Properties

### checkCommandInjection?

> `optional` **checkCommandInjection?**: `boolean`

Defined in: [validators.ts:418](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L418)

Default `false` — opt in only when input reaches a shell.

***

### checkHomoglyphs?

> `optional` **checkHomoglyphs?**: `boolean`

Defined in: [validators.ts:422](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L422)

Default `true`.

***

### checkNoSQLInjection?

> `optional` **checkNoSQLInjection?**: `boolean`

Defined in: [validators.ts:416](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L416)

Default `true`.

***

### checkPathTraversal?

> `optional` **checkPathTraversal?**: `boolean`

Defined in: [validators.ts:420](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L420)

Default `true`.

***

### checkSQLInjection?

> `optional` **checkSQLInjection?**: `boolean`

Defined in: [validators.ts:414](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L414)

Default `true`.

***

### checkXSS?

> `optional` **checkXSS?**: `boolean`

Defined in: [validators.ts:412](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L412)

Default `true`.
