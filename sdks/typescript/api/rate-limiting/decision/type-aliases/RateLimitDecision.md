# Type Alias: RateLimitDecision

&gt; **RateLimitDecision** = *typeof* `RateLimitDecisionSchema.Type`

Defined in: [decision.ts:90](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/decision.ts#L90)

The outcome of a rate-limit check.

A discriminated union on `allowed`:
- `{ allowed: true, remaining, limit, resetAt }` — under the limit; the
  request was counted.
- `{ allowed: false, remaining: 0, limit, resetAt }` — over the limit; the
  request was **not** counted.

Callers narrow with a single check:

## Example

```ts
const decision = await store.check("user:42", 60_000, 100);
if (!decision.allowed) {
  return new Response("Too many requests", {
    status: 429,
    headers: { "RateLimit-Reset": String(decision.resetAt) },
  });
}
```
