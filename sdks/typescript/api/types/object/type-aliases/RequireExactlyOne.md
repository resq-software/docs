# Type Alias: RequireExactlyOne\<T, K\>

&gt; **RequireExactlyOne**\<`T`, `K`\> = `Omit`\<`T`, `K`\> & `{ [P in K]-?: Required<Pick<T, P>> & { [Q in Exclude<K, P>]?: never } }`\[`K`\]

Defined in: [object.ts:121](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L121)

Require **exactly one** of the keys `K` of `T` (the others become forbidden).
Models mutually-exclusive discriminated config, e.g. a rate limiter that
takes either a sync counter or an async counter but never both.

## Type Parameters

### T

`T`

### K

`K` *extends* keyof `T` = keyof `T`
