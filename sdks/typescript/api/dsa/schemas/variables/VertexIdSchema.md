# Variable: VertexIdSchema

&gt; `const` **VertexIdSchema**: `brand`\<`String`, `"VertexId"`\>

Defined in: [schemas.ts:149](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L149)

Schema for a graph vertex identifier: a non-empty string carrying a
nominal `VertexId` brand. A `VertexId` is assignable to `string`, but a
plain `string` is not assignable to `VertexId` without going through
validation — see isValidVertexId.
