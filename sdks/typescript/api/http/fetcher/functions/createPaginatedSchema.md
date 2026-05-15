# Function: createPaginatedSchema()

> **createPaginatedSchema**\<`T`\>(`itemSchema`): `Struct`\<\&#123; `data`: `$Array`\<`Schema`\<`T`\>\>; `pagination`: `Struct`\<\&#123; `page`: `Number`; `pageSize`: `Number`; `total`: `Number`; `totalPages`: `Number`; \&#125;\>; \&#125;\>

Defined in: [packages/http/src/fetcher.ts:803](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/fetcher.ts#L803)

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

`Struct`\<\&#123; `data`: `$Array`\<`Schema`\<`T`\>\>; `pagination`: `Struct`\<\&#123; `page`: `Number`; `pageSize`: `Number`; `total`: `Number`; `totalPages`: `Number`; \&#125;\>; \&#125;\>

## Example

```ts
const Page = createPaginatedSchema(UserSchema);
const page = yield* get("/api/users?page=1", { schema: Page });
```
