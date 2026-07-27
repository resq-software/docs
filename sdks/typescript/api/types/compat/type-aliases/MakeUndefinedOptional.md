# Type Alias: MakeUndefinedOptional\<T\>

&gt; **MakeUndefinedOptional**\<`T`\> = [`Simplify`](../../object/type-aliases/Simplify)\<`{ [K in keyof T as undefined extends T[K] ? never : K]: T[K] }` & `{ [K in keyof T as undefined extends T[K] ? K : never]?: T[K] }`\>

Defined in: [compat.ts:97](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/compat.ts#L97)

Rewrite `T` so that any property whose type includes `undefined` becomes
genuinely **optional** (`?`), while properties that cannot be `undefined` stay
required. Bridges the gap between "value may be `undefined`" and "key may be
omitted", which TypeScript otherwise treats as distinct.

The `extends object` bound is required because the mapping keys over `T`; pass
an object shape, not a primitive or union.

## Type Parameters

### T

`T` *extends* `object`

The object type to relax; must be an object shape.

## Example

```ts
type Raw = { id: string; note: string | undefined };
type Relaxed = MakeUndefinedOptional<Raw>;
//   ^? { id: string; note?: string | undefined }
```
