# Variable: ProbabilitySchema

&gt; `const` **ProbabilitySchema**: `brand`\<`Finite`, `"Probability"`\>

Defined in: [schemas.ts:246](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L246)

A probability / unit-interval value in the OPEN interval `(0, 1)`.

Carries a nominal `Probability` brand: a `Probability` is assignable to
`number`, but a plain `number` is not assignable to `Probability` without
going through [toProbability](../functions/toProbability) (or a deliberate cast for untrusted
input). Used at the public boundary of `BloomFilter` (`errorRate`) and
`CountMinSketch` (`epsilon`, `delta`) so an out-of-range rate is
unrepresentable at the type level.
