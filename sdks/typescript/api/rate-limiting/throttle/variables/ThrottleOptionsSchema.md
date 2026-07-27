# Variable: ThrottleOptionsSchema

&gt; `const` **ThrottleOptionsSchema**: `Struct`\<\{ `leading`: `optional`\<`Boolean`\>; `trailing`: `optional`\<`Boolean`\>; \}\>

Defined in: [throttle.ts:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L37)

Effect Schema for [throttle](../functions/throttle) edge-behaviour options, exported so callers
can runtime-validate options that arrive as untyped JSON.
