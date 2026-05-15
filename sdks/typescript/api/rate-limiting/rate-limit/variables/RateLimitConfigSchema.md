# Variable: RateLimitConfigSchema

> `const` **RateLimitConfigSchema**: `Struct`\<\&#123; `headers`: `optional`\<`Boolean`\>; `maxRequests`: `Number`; `windowMs`: `Number`; \&#125;\>

Defined in: [rate-limit.ts:41](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L41)

Effect Schema for runtime-validating a rate-limit configuration —
useful at framework boundaries where the config arrives as untyped
JSON (env-var parsing, admin endpoints, feature-flag payloads).

## Example

```ts
import { Schema } from "effect";
const config = Schema.decodeUnknownSync(RateLimitConfigSchema)(input);
```
