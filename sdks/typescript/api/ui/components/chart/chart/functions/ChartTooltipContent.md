# Function: ChartTooltipContent()

&gt; **ChartTooltipContent**(`__namedParameters`): `Element` \| `null`

Defined in: [packages/ui/src/components/chart/chart.tsx:216](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/components/chart/chart.tsx#L216)

Themed tooltip surface that resolves labels and colors from the chart `config`.

Renders nothing (returns `null`) while the tooltip is inactive or its `payload`
is empty, so it is safe to mount unconditionally as a Recharts tooltip content
component.

## Parameters

### \_\_namedParameters

`ClassAttributes`\<`HTMLDivElement`\> & `HTMLAttributes`\<`HTMLDivElement`\> & `Partial`\<`TooltipContentProps`\> & `object`

## Returns

`Element` \| `null`

## Throws

If rendered outside a [ChartContainer](./ChartContainer) — it reads the
chart config from context via `useChart`.
