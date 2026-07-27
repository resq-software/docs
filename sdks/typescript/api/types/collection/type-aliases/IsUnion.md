# Type Alias: IsUnion\<T, U\>

&gt; **IsUnion**\<`T`, `U`\> = \[`T`\] *extends* \[`never`\] ? `false` : `T` *extends* `unknown` ? \[`U`\] *extends* \[`T`\] ? `false` : `true` : `never`

Defined in: [collection.ts:102](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L102)

`true` when `T` is a union of two or more distinct members. `boolean` counts —
it is `true | false` internally, so `IsUnion<boolean>` is `true`. `never` is
not a union (`IsUnion<never>` is `false`). The `U` parameter is an internal
accumulator that preserves the original union while `T` distributes; do not
pass it.

## Type Parameters

### T

`T`

### U

`U` = `T`
