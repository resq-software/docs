# Type Alias: Channel

&gt; **Channel** = `NumberRange`\<`0`, `255`\>

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L33)

A single 8-bit color channel: an integer in the **inclusive** range `0–255`.

Modeled with NumberRange so the compiler rejects out-of-gamut literals
(`{ r: 256 }` is a type error), while any parsed value is normalized through
a channel constructor at the boundary.
