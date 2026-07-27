# Variable: GraphEdgeSchema

&gt; `const` **GraphEdgeSchema**: `Struct`\<\{ `source`: `String`; `target`: `String`; `weight`: `optional`\<`Finite`\>; \}\>

Defined in: [schemas.ts:135](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L135)

Schema for an edge in a Graph: non-empty source and target,
optional finite numeric weight (NaN/Infinity rejected).
