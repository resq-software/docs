# Type Alias: Required\<T, K\>

&gt; **Required**\<`T`, `K`\> = [`Simplify`](../../object/type-aliases/Simplify)\<`Omit`\<`T`, `K`\> & `{ [P in K]-?: T[P] }`\>

Defined in: [compat.ts:77](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/compat.ts#L77)

Make the keys `K` of `T` required while leaving the rest untouched — the
partial-application counterpart of the global `Required`, which has no
key-selecting overload.

This intentionally **shadows** the global `Required<T>` within any module that
imports it: the second `K` parameter is required, so a bare `Required<T>` will
no longer type-check where this alias is in scope. Import it deliberately.

## Type Parameters

### T

`T`

The source object type.

### K

`K` *extends* keyof `T`

The subset of `T`'s keys to force required.

## Example

```ts
type Config = { host?: string; port?: number; tls?: boolean };
type Connectable = Required<Config, "host" | "port">;
//   ^? { host: string; port: number; tls?: boolean }
```
