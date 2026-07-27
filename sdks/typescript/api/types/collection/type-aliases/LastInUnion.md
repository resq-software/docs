# Type Alias: LastInUnion\<U\>

&gt; **LastInUnion**\<`U`\> = [`UnionToIntersection`](./UnionToIntersection)\<`U` *extends* `unknown` ? (`x`) =&gt; `void` : `never`\> *extends* (`x`) =&gt; `void` ? `L` : `never`

Defined in: [collection.ts:111](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L111)

The "last" member of a union, per the compiler's internal ordering.

## Type Parameters

### U

`U`
