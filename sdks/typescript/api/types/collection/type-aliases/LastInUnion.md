# Type Alias: LastInUnion\<U\>

&gt; **LastInUnion**\<`U`\> = [`UnionToIntersection`](./UnionToIntersection)\<`U` *extends* `unknown` ? (`x`) =&gt; `void` : `never`\> *extends* (`x`) =&gt; `void` ? `L` : `never`

Defined in: [collection.ts:111](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L111)

The "last" member of a union, per the compiler's internal ordering.

## Type Parameters

### U

`U`
