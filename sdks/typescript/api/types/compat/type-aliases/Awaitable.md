# Type Alias: Awaitable\<T\>

&gt; **Awaitable**\<`T`\> = `T` \| `PromiseLike`\<`T`\>

Defined in: [compat.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/compat.ts#L56)

A value that may be delivered synchronously or asynchronously: `T` itself, or
anything `await`-able that resolves to `T`. Use it to type a parameter or
return that a caller is free to make either sync or `async` — `await`-ing an
`Awaitable<T>` always yields `T`.

## Type Parameters

### T

`T`

The resolved value type.
