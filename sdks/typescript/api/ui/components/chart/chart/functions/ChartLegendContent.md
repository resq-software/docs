# Function: ChartLegendContent()

&gt; **ChartLegendContent**(`__namedParameters`): `Element` \| `null`

Defined in: [packages/ui/src/components/chart/chart.tsx:390](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L390)

Themed legend content that resolves labels, icons, and colors from the chart
`config`.

Renders nothing (returns `null`) when `payload` is empty, so it is safe to
mount unconditionally as a Recharts legend content component.

## Parameters

### \_\_namedParameters

`Partial`\<`Pick`\<`Props`, `"verticalAlign"` \| `"payload"`\>\> & `ClassAttributes`\<`HTMLDivElement`\> & `HTMLAttributes`\<`HTMLDivElement`\> & `object`

## Returns

`Element` \| `null`

## Throws

If rendered outside a [ChartContainer](./ChartContainer) — it reads the
chart config from context via `useChart`.
