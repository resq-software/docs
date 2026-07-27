# Type Alias: QueryParams

&gt; **QueryParams** = `Schema.Schema.Type`\<*typeof* `QueryParams`\>

Defined in: [packages/http/src/fetcher.ts:158](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L158)

Query parameters as a flat string-keyed map. Each value is a scalar
(`string | number | boolean`), `null`/`undefined`, or an array of scalars.

Serialisation invariants (buildQueryString): `null`/`undefined` values
— and `null`/`undefined` array elements — are dropped entirely (no empty
`key=`); an array emits one repeated `key=value` pair per surviving element;
scalars are stringified via `String(...)`.
