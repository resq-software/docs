# Type Alias: Zip\<T, U\>

&gt; **Zip**\<`T`, `U`\> = `T` *extends* readonly \[infer A, `...(infer RestT)`\] ? `U` *extends* readonly \[infer B, `...(infer RestU)`\] ? \[\[`A`, `B`\], `...Zip<RestT, RestU>`\] : \[\] : \[\]

Defined in: [collection.ts:159](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L159)

Pair up two tuples element-wise into a tuple of pairs, stopping at the
shorter length — `Zip<[1, 2], ["a", "b"]>` is `[[1, "a"], [2, "b"]]`.

## Type Parameters

### T

`T` *extends* readonly `unknown`[]

### U

`U` *extends* readonly `unknown`[]
