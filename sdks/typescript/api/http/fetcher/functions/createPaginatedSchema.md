# Function: createPaginatedSchema()

&gt; **createPaginatedSchema**\<`T`\>(`itemSchema`): `Struct`\<\{ `data`: `$Array`\<`Schema`\<`T`\>\>; `pagination`: `Struct`\<\{ `page`: `Number`; `pageSize`: `Number`; `total`: `Number`; `totalPages`: `Number`; \}\>; \}\>

Defined in: [packages/http/src/fetcher.ts:1068](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L1068)

Build a paginated-list schema:

```
{ data: T[], pagination: { page, pageSize, total, totalPages } }
```

Pass to `options.schema` to validate paginated endpoints in a
single declarative call.

## Type Parameters

### T

`T`

Element type of the paginated list.

## Parameters

### itemSchema

`Schema`\<`T`\>

## Returns

`Struct`\<\{ `data`: `$Array`\<`Schema`\<`T`\>\>; `pagination`: `Struct`\<\{ `page`: `Number`; `pageSize`: `Number`; `total`: `Number`; `totalPages`: `Number`; \}\>; \}\>

## Example

```ts
const Page = createPaginatedSchema(UserSchema);
const page = yield* get("/api/users?page=1", { schema: Page });
```
