# Type Alias: Awaitable\<T\>

&gt; **Awaitable**\<`T`\> = `T` \| `PromiseLike`\<`T`\>

Defined in: [compat.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/compat.ts#L56)

A value that may be delivered synchronously or asynchronously: `T` itself, or
anything `await`-able that resolves to `T`. Use it to type a parameter or
return that a caller is free to make either sync or `async` — `await`-ing an
`Awaitable<T>` always yields `T`.

## Type Parameters

### T

`T`

The resolved value type.
