# Type Alias: RequireAtLeastOne\<T, K\>

&gt; **RequireAtLeastOne**\<`T`, `K`\> = `Omit`\<`T`, `K`\> & `{ [P in K]-?: Required<Pick<T, P>> & Partial<Pick<T, Exclude<K, P>>> }`\[`K`\]

Defined in: [object.ts:113](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L113)

Require **at least one** of the keys `K` of `T` (the rest stay optional).
Models "you must supply one of `apiKey` or `token`, and may supply both".

## Type Parameters

### T

`T`

### K

`K` *extends* keyof `T` = keyof `T`
