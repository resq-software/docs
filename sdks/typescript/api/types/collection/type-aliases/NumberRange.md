# Type Alias: NumberRange\<Low, High\>

&gt; **NumberRange**\<`Low`, `High`\> = `Exclude`\<[`Enumerate`](./Enumerate)\<`High`\>, [`Enumerate`](./Enumerate)\<`Low`\>\> \| `High`

Defined in: [collection.ts:193](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/collection.ts#L193)

The union of integer literals in the **inclusive** range `[Low, High]` —
`NumberRange<2, 5>` is `2 | 3 | 4 | 5`. Turns a bounded numeric domain (an RGB
channel `0..255`, an HTTP status `100..599`, a percentage `0..100`) into an
exact literal type the compiler checks at call sites.

The bounds are materialized as tuples, so keep `High` below ~1000 (the
TypeScript instantiation-depth limit); past that, reach for a branded numeric
instead.

## Type Parameters

### Low

`Low` *extends* `number`

### High

`High` *extends* `number`
