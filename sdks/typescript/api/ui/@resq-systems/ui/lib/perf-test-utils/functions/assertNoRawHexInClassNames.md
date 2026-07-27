# Function: assertNoRawHexInClassNames()

&gt; **assertNoRawHexInClassNames**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:902](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L902)

Throw when a raw hex colour appears inside a `className` prop.
Hex colours bypass the design-token system; use semantic Tailwind
tokens (`bg-primary`, `text-foreground`, `border-destructive`, …)
instead. Chart files are exempt because Recharts' config takes
raw hex.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When a raw hex color appears inside a `className` prop in a
  non-chart `file`.
