# Function: valueToAngle()

&gt; **valueToAngle**(`value`, `min`, `max`, `startAngle`, `sweep`): `number`

Defined in: [packages/ui/src/lib/instrument-dial.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/instrument-dial.ts#L59)

Map a scale `value` (clamped to `[min, max]`) to an angle, starting at
`startAngle` and covering `sweep` degrees. A zero-width range maps to
`startAngle`.

## Parameters

### value

`number`

### min

`number`

### max

`number`

### startAngle

`number`

### sweep

`number`

## Returns

`number`
