# ~~Type Alias: AsyncMemoizable\<T, D\>~~

&gt; **AsyncMemoizable**\<`T`, `D`\> = [`Memoizable`](../../../memoize/memoize.types/type-aliases/Memoizable)\<`T`, `Promise`\<`D`\>\>

Defined in: [memoize-async/memoize-async.types.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.types.ts#L41)

Legacy signature type for the `@memoizeAsync` decorator (async counterpart of
`Memoizable`).

## Type Parameters

### T

`T`

The class type that owns the decorated method.

### D

`D`

The resolved type of the async method.

## Deprecated

Use AsyncDecorator from `../types.js` instead — removed in
v1.0.0. This shape erases the decorated method's signature, which is not
assignable to a concrete async method's descriptor under strict
`strictFunctionTypes` (TS1241 / TS1270 at the decoration site). `memoizeAsync`
now returns AsyncDecorator, which preserves the signature. Migration:
replace `AsyncMemoizable<T, D>` annotations with `AsyncDecorator<T>` (drop the
`D` parameter); no runtime change.
