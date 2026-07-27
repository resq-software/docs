# ~~Type Alias: Memoizable\<T, D\>~~

&gt; **Memoizable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) =&gt; `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

Defined in: [memoize/memoize.types.ts:127](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.types.ts#L127)

Type for the `@memoize` decorator function.

## Type Parameters

### T

`T`

The class type that owns the decorated method.

### D

`D`

The return type of the decorated method.

## Parameters

### target

`T`

The class prototype.

### propertyName

keyof `T`

The name of the method being decorated.

### descriptor

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

The property descriptor.

## Returns

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

The modified descriptor.

## Deprecated

Use Decorator from `../types.js` instead — removed in
v1.0.0. This shape erases the decorated method's signature to `Method<D>`,
which is not assignable to a concrete method's descriptor under strict
`strictFunctionTypes` (TS1241 / TS1270 at the decoration site). `memoize` now
returns Decorator, which preserves the signature end-to-end. Migration:
replace `Memoizable<T, D>` annotations with `Decorator<T>` (drop the `D`
parameter); no runtime change.
