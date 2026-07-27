# Type Alias: GtagEventParams

&gt; **GtagEventParams** = `Readonly`\<`Record`\<`string`, `GtagParamValue`\>\>

Defined in: [index.ts:154](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L154)

Flat parameter bag for `gtag("event", …)` and `gtag("set", …)`. Values are
primitives only — primitivesOnly enforces this at runtime; the type
enforces it at the call site.
