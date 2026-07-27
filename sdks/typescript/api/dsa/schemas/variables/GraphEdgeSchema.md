# Variable: GraphEdgeSchema

&gt; `const` **GraphEdgeSchema**: `Struct`\<\{ `source`: `String`; `target`: `String`; `weight`: `optional`\<`Finite`\>; \}\>

Defined in: [schemas.ts:135](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L135)

Schema for an edge in a Graph: non-empty source and target,
optional finite numeric weight (NaN/Infinity rejected).
