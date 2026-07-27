# Function: unsafeBrand()

&gt; **unsafeBrand**\<`B`, `T`\>(`value`): [`Brand`](../type-aliases/Brand)\<`T`, `B`\>

Defined in: [brand.ts:121](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/brand.ts#L121)

Assert-cast an already-validated base value into a brand **without a runtime
check**. This is the deliberate escape hatch: use it only at a boundary where
validation has already happened by other means (an Effect schema decode, a
regex you just tested, a value returned by a trusted crypto primitive).

Prefer [brandRefiner](./brandRefiner) when you have the predicate on hand — it ties the
cast to an actual runtime check.

Both type parameters must be supplied — the carrier `T` is **not** defaulted,
because TypeScript cannot infer it while `B` is given explicitly, and a
default of `unknown` would silently collapse `Brand<unknown, B>` to a bare
tag (losing the carrier). Prefer a [brandRefiner](./brandRefiner)'s `.unsafe` when you
already have a refiner for the brand.

## Type Parameters

### B

`B` *extends* `PropertyKey`

The brand name to apply.

### T

`T`

The carrier type of `value`.

## Parameters

### value

`T`

The already-validated base value.

## Returns

[`Brand`](../type-aliases/Brand)\<`T`, `B`\>

`value`, retyped as `Brand<T, B>`.

## Example

```ts
const token = unsafeBrand<"SecureToken", string>(crypto.randomUUID());
//    ^? Brand<string, "SecureToken">
```
