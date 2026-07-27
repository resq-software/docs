# Type Alias: Brand\<T, B\>

&gt; **Brand**\<`T`, `B`\> = `T` & [`Tag`](../interfaces/Tag)\<`B`\>

Defined in: [brand.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/brand.ts#L83)

A nominal type: the base type `T` intersected with a compile-time-only brand
`B`. Assignable *to* `T` (a branded value is still a `T`), but a plain `T` is
**not** assignable *to* `Brand<T, B>` — construction must go through a
validated boundary ([brandRefiner](../functions/brandRefiner)) or an explicit [unsafeBrand](../functions/unsafeBrand).

## Type Parameters

### T

`T`

The underlying (carrier) type, e.g. `string` or `number`.

### B

`B` *extends* `PropertyKey`

The brand name, a string/symbol literal, e.g. `"Ciphertext"`.

## Example

```ts
type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

declare const u: UserId;
const s: string = u; // ✓ UserId is a string
const o: OrderId = u; // ✗ a UserId is not an OrderId
```
