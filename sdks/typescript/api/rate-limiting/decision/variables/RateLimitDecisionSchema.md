# Variable: RateLimitDecisionSchema

&gt; `const` **RateLimitDecisionSchema**: `Union`\<readonly \[`Struct`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}\>, `Struct`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}\>\]\>

Defined in: [decision.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/decision.ts#L45)

Effect Schema for a [RateLimitDecision](../type-aliases/RateLimitDecision). A discriminated union keyed
on `allowed`: a permitted request carries the requests still available,
while a rejected request pins `remaining` to `0`. Useful when serialising
decisions to inter-service queues or persisting them for audit.

Invariant the union encodes: the rejected variant's `remaining` is the
literal `0`, so a `remaining > 0` value can only appear on `allowed: true`.

## Example

```ts
import { Schema } from "effect";
// Throws a ParseError if `input` doesn't match either variant.
const decision = Schema.decodeUnknownSync(RateLimitDecisionSchema)(input);
if (decision.allowed) { ... } // narrowed to the permitted variant
```
