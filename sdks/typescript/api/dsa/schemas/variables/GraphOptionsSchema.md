# Variable: GraphOptionsSchema

&gt; `const` **GraphOptionsSchema**: `Struct`\<\{ `directed`: `optional`\<`Boolean`\>; \}\>

Defined in: [schemas.ts:125](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L125)

Construction options for Graph. The schema leaves `directed`
optional (no schema-level default); Graph itself treats an omitted
value as `true` (directed).
