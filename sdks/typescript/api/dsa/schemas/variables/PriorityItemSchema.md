# Variable: PriorityItemSchema

&gt; `const` **PriorityItemSchema**: `Struct`\<\{ `dueDate`: `String`; `id`: `String`; `priority`: `withDecodingDefault`\<`optional`\<`Int`\>, `never`\>; \}\>

Defined in: [schemas.ts:77](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L77)

Schema for an item enqueued into the deadline-aware priority queue.

`priority` defaults to `3` (mid-range) when omitted — encoded as a
decoding default rather than a TypeScript default so server-side
decoding produces the same shape regardless of how the JSON was
serialised.
