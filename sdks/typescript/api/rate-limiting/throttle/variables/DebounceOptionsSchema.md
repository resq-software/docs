# Variable: DebounceOptionsSchema

&gt; `const` **DebounceOptionsSchema**: `Struct`\<\{ `leading`: `optional`\<`Boolean`\>; `maxWait`: `optional`\<`Number`\>; \}\>

Defined in: [throttle.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L51)

Effect Schema for [debounce](../functions/debounce) options, exported so callers can
runtime-validate options that arrive as untyped JSON.
