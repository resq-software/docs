# Variable: VertexIdSchema

&gt; `const` **VertexIdSchema**: `brand`\<`String`, `"VertexId"`\>

Defined in: [schemas.ts:149](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L149)

Schema for a graph vertex identifier: a non-empty string carrying a
nominal `VertexId` brand. A `VertexId` is assignable to `string`, but a
plain `string` is not assignable to `VertexId` without going through
validation — see isValidVertexId.
