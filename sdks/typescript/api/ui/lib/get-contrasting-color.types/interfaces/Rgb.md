# Interface: Rgb

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L42)

A parsed, in-gamut RGB triple.

Fallibility is expressed at the boundary — parsers return `Rgb | null` — not
baked into this type. A value of type `Rgb` is therefore always a valid color,
so downstream code never has to re-check for `null`.

## Properties

### b

&gt; `readonly` **b**: `NumberRange`

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L45)

***

### g

&gt; `readonly` **g**: `NumberRange`

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L44)

***

### r

&gt; `readonly` **r**: `NumberRange`

Defined in: [packages/ui/src/lib/get-contrasting-color.types.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.types.ts#L43)
