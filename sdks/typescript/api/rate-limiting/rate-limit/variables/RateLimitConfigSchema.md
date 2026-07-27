# Variable: RateLimitConfigSchema

&gt; `const` **RateLimitConfigSchema**: `Struct`\<\{ `headers`: `optional`\<`Boolean`\>; `maxRequests`: `Int`; `windowMs`: `Int`; \}\>

Defined in: [rate-limit.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L51)

Effect Schema for runtime-validating a rate-limit configuration —
useful at framework boundaries where the config arrives as untyped
JSON (env-var parsing, admin endpoints, feature-flag payloads).

Invariant the type can't state: `windowMs` and `maxRequests` are both
strictly-positive **integers** (`0` and negatives are rejected), and
`headers` absent is treated the same as `false` by middleware. Decoding
a value that violates these throws — see the example.

## Example

```ts
import { Schema } from "effect";
// Throws a ParseError if `input` is missing a field or has a non-positive value.
const config = Schema.decodeUnknownSync(RateLimitConfigSchema)(input);
```
