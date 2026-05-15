# Variable: RateLimitCheckResultSchema

> `const` **RateLimitCheckResultSchema**: `Struct`\<\&#123; `limited`: `Boolean`; `remaining`: `Number`; `resetTime`: `Number`; `total`: `Number`; \&#125;\>

Defined in: [rate-limit.ts:58](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L58)

Effect Schema for the structured result of an [IRateLimitStore](../interfaces/IRateLimitStore)
`check()`. Useful when serialising decisions to inter-service queues
or persisting them for audit.
