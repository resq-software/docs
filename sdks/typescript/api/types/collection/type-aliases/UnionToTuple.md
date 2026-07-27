# Type Alias: UnionToTuple\<U\>

&gt; **UnionToTuple**\<`U`\> = [`LastInUnion`](./LastInUnion)\<`U`\> *extends* infer L ? \[`U`\] *extends* \[`never`\] ? \[\] : \[`...UnionToTuple<Exclude<U, L>>`, `L`\] : `never`

Defined in: [collection.ts:123](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L123)

Convert a union into a tuple of its members. Order follows the compiler's
internal union ordering, so treat the *set* of elements as meaningful and the
order as incidental. Useful for iterating a union at the type level.

`UnionToTuple<"a" | "b">` is `["a", "b"]` (or `["b", "a"]`, version-dependent).

## Type Parameters

### U

`U`
