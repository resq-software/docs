# Function: createApiResponseSchema()

> **createApiResponseSchema**\<`T`\>(`dataSchema`): `Struct`\<\&#123; `data`: `Schema`\<`T`\>; `errors`: `optional`\<`$Array`\<`String`\>\>; `message`: `optional`\<`String`\>; `success`: `Boolean`; \&#125;\>

Defined in: [packages/http/src/fetcher.ts:827](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L827)

Build an envelope schema:

```
{ success: boolean, data: T, message?: string, errors?: string[] }
```

Use as the response schema for endpoints that wrap their payload
in a uniform success/error envelope.

## Type Parameters

### T

`T`

Inner data shape on success.

## Parameters

### dataSchema

`Schema`\<`T`\>

## Returns

`Struct`\<\&#123; `data`: `Schema`\<`T`\>; `errors`: `optional`\<`$Array`\<`String`\>\>; `message`: `optional`\<`String`\>; `success`: `Boolean`; \&#125;\>
