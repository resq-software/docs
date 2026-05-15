# Variable: PriorityItemSchema

> `const` **PriorityItemSchema**: `Struct`\<\&#123; `dueDate`: `String`; `id`: `String`; `priority`: `withDecodingDefault`\<`optional`\<`Int`\>\>; \&#125;\>

Defined in: [schemas.ts:78](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L78)

Schema for an item enqueued into the deadline-aware priority queue.

`priority` defaults to `3` (mid-range) when omitted — encoded as a
decoding default rather than a TypeScript default so server-side
decoding produces the same shape regardless of how the JSON was
serialised.
