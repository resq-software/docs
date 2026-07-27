# Function: createApiResponseSchema()

&gt; **createApiResponseSchema**\<`T`\>(`dataSchema`): `Struct`\<\{ `data`: `Schema`\<`T`\>; `errors`: `optional`\<`$Array`\<`String`\>\>; `message`: `optional`\<`String`\>; `success`: `Boolean`; \}\>

Defined in: [packages/http/src/fetcher.ts:1092](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L1092)

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

`Struct`\<\{ `data`: `Schema`\<`T`\>; `errors`: `optional`\<`$Array`\<`String`\>\>; `message`: `optional`\<`String`\>; `success`: `Boolean`; \}\>
