# Type Alias: RateLimitConfig

&gt; **RateLimitConfig** = *typeof* `RateLimitConfigSchema.Type`

Defined in: [rate-limit.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L68)

TypeScript type inferred from [RateLimitConfigSchema](../variables/RateLimitConfigSchema).

The static type only guarantees `number`; the positive-integer bounds on
`windowMs`/`maxRequests` are enforced solely by decoding through the schema,
so trust these fields only after validation, not when hand-constructing the
object.
