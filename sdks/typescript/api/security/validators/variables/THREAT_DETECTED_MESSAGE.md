# Variable: THREAT\_DETECTED\_MESSAGE

> `const` **THREAT\_DETECTED\_MESSAGE**: `"Input contains potentially unsafe content"` = `"Input contains potentially unsafe content"`

Defined in: [validators.ts:577](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L577)

Generic user-facing fallback message. Render this verbatim when a
detector fires but you don't want to expose which one. Prefer
[getThreatErrorMessage](../functions/getThreatErrorMessage) for category-specific messages.
