# Type Alias: DistributiveOmit\<T, K\>

&gt; **DistributiveOmit**\<`T`, `K`\> = `T` *extends* `unknown` ? `Omit`\<`T`, `K`\> : `never`

Defined in: [packages/ui/src/components/picture/types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/picture/types.ts#L44)

Like `Omit<T, K>`, but distributes over a union so each member is stripped
independently — `Omit` on a union would collapse to the shared keys and lose
per-variant properties.

## Type Parameters

### T

`T`

The (possibly union) shape to omit from.

### K

`K` *extends* `PropertyKey`

The property key(s) to remove from every union member.
