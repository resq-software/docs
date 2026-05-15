# Variable: GraphEdgeSchema

> `const` **GraphEdgeSchema**: `Struct`\<\&#123; `source`: `String`; `target`: `String`; `weight`: `optional`\<`Finite`\>; \&#125;\>

Defined in: [schemas.ts:132](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L132)

Schema for an edge in a Graph: non-empty source and target,
optional finite numeric weight (NaN/Infinity rejected).
