# ~~Type Alias: RGB~~

&gt; **RGB** = [`Rgb`](../interfaces/Rgb) \| `null`

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:55](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L55)

## Deprecated

Use [Rgb](../interfaces/Rgb) for a definitely-valid color and express the
parse-failure state as `Rgb | null` at each boundary — removed in the next
major. Migration: replace `RGB` with `Rgb | null` (the `null` arm was already
folded into this alias), then drop the redundant null-checks on values the
parser has already narrowed to `Rgb`. Retained as an alias until then.
