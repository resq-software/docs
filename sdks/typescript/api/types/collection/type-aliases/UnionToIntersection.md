# Type Alias: UnionToIntersection\<U\>

&gt; **UnionToIntersection**\<`U`\> = `U` *extends* `unknown` ? (`k`) =&gt; `void` : `never` *extends* (`k`) =&gt; `void` ? `I` : `never`

Defined in: [collection.ts:89](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L89)

Convert a union into the intersection of its members —
`UnionToIntersection<{ a: 1 } | { b: 2 }>` is `{ a: 1 } & { b: 2 }`. Built on
the contravariant-parameter inference trick; the foundational primitive for
most union manipulation.

## Type Parameters

### U

`U`
