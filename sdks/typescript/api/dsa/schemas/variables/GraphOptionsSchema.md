# Variable: GraphOptionsSchema

&gt; `const` **GraphOptionsSchema**: `Struct`\<\{ `directed`: `optional`\<`Boolean`\>; \}\>

Defined in: [schemas.ts:125](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L125)

Construction options for Graph. The schema leaves `directed`
optional (no schema-level default); Graph itself treats an omitted
value as `true` (directed).
